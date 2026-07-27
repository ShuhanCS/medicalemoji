/**
 * Capture the two supplementary Google Books Ngram exhibits for the Stomach
 * proposal.
 *
 * 1. Idiom exhibit  - shows the metaphorical phrases in published English.
 * 2. Verb exhibit   - uses Ngram part-of-speech tagging to show that the verb
 *                     sense belongs to `stomach` and not to other organ words.
 *                     This is the evidence behind the Open-ended answer.
 *
 * Ngram is not rate-limited the way Google Search is, so this runs headless.
 * The script refuses to save a chart that did not actually render.
 *
 * Usage:
 *   node scripts/capture_stomach_idiom_ngrams.mjs --out=<absolute output dir>
 */

import { join, resolve } from "node:path";
import { mkdir, writeFile } from "node:fs/promises";

import { firefox } from "playwright";

const ROOT = resolve(import.meta.dirname, "..");
const VIEWPORT = { width: 1440, height: 900 };
const CAPTURE_DATE = new Date().toISOString().slice(0, 10);

const EXHIBITS = [
  {
    slug: "stomach_ngram_idioms",
    content: "butterflies in my stomach,a strong stomach,turn my stomach",
    label: "Stomach idioms in published books",
  },
  {
    // Deliberately a single series. A `stomach_VERB,liver_VERB,kidney_VERB`
    // comparison was tried and rejected: Ngram's part-of-speech tagger
    // mis-tags archaic text and reports implausible `liver_VERB` volume from
    // roughly 1550 to 1950, so that chart cannot be honestly explained.
    slug: "stomach_ngram_verb_sense",
    content: "stomach_VERB",
    label: "Verb sense of stomach",
  },
];

function buildUrl(content) {
  const params = new URLSearchParams({
    content,
    year_start: "1500",
    year_end: "2022",
    corpus: "en",
    smoothing: "3",
  });
  return `https://books.google.com/ngrams/graph?${params.toString()}`;
}

function parseArgs(argv) {
  const values = {
    out: join(ROOT, "docs/proposals/stomach-emoji-2026/candidate-v1.13/evidence/frequency"),
  };
  for (const argument of argv) {
    const [key, ...parts] = argument.replace(/^--/, "").split("=");
    if (key in values && parts.length) values[key] = parts.join("=");
  }
  return values;
}

async function capture(page, exhibit, outputDir) {
  const url = buildUrl(exhibit.content);
  await page.goto(url, { waitUntil: "networkidle", timeout: 90_000 });
  await page.waitForSelector("#chart svg", { timeout: 60_000 });
  await page.waitForTimeout(3500);

  // Refuse an empty chart: there must be at least one plotted series path.
  const seriesCount = await page.evaluate(() => {
    const paths = document.querySelectorAll("#chart svg path.ngram-line, #chart svg path");
    return Array.from(paths).filter((p) => (p.getAttribute("d") || "").length > 40).length;
  });
  if (seriesCount === 0) {
    throw new Error(`${exhibit.slug}: chart rendered no data series; refusing to save.`);
  }

  // Screenshot the SVG rather than the #chart wrapper. The wrapper carries a
  // tall empty margin above the plot, which forces the exhibit to render small
  // inside a fixed max-height in the PDF and leaves the axis labels unreadable.
  const chart = page.locator("#chart svg").first();
  const filename = `${exhibit.slug}_${CAPTURE_DATE}_CANDIDATE.png`;
  await chart.screenshot({ path: join(outputDir, filename) });
  console.log(`  ${exhibit.label}: ${seriesCount} series -> ${filename}`);
  return { ...exhibit, url, filename, seriesCount, capturedAt: new Date().toISOString() };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  await mkdir(args.out, { recursive: true });

  const browser = await firefox.launch({ headless: true });
  const context = await browser.newContext({ viewport: VIEWPORT, locale: "en-US" });
  const page = await context.newPage();

  try {
    const records = [];
    for (const exhibit of EXHIBITS) {
      records.push(await capture(page, exhibit, args.out));
    }
    const logPath = join(args.out, `stomach_ngram_supplementary_log_${CAPTURE_DATE}.json`);
    await writeFile(logPath, `${JSON.stringify({ records }, null, 2)}\n`, "utf8");
    console.log(`\nCompleted. Log: ${logPath}`);
  } finally {
    await browser.close();
  }
}

await main();
