/**
 * Capture Google Search and Google Video Search result counts for the term
 * `elephant`, which Unicode names as the required comparative search term.
 *
 * The stomach proposal already carries the elephant comparison on both Trends
 * exhibits and on Ngram. This script supplies the missing Search and Video
 * baselines so all five required sources show the comparison.
 *
 * Same rules as scripts/capture_unicode_evidence.mjs: headed browser, shared
 * persistent profile, never bypasses a challenge, and refuses to save a
 * screenshot unless a result count is actually visible on the page.
 *
 * Usage:
 *   node scripts/capture_elephant_baseline.mjs --out=<absolute output dir>
 */

import { homedir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { mkdir, writeFile } from "node:fs/promises";

import { firefox } from "playwright";

const ROOT = resolve(import.meta.dirname, "..");
const VIEWPORT = { width: 1440, height: 1100 };
const CAPTURE_DATE = new Date().toISOString().slice(0, 10);
const DEFAULT_PROFILE = join(homedir(), ".medicalemoji-google-evidence-firefox");
const TERM = "elephant";

function parseArgs(argv) {
  const values = {
    out: join(ROOT, "docs/proposals/stomach-emoji-2026/candidate-v1.13/evidence/frequency"),
    profile: DEFAULT_PROFILE,
  };
  for (const argument of argv) {
    const [key, ...parts] = argument.replace(/^--/, "").split("=");
    if (key in values && parts.length) values[key] = parts.join("=");
  }
  return values;
}

async function pageText(page) {
  return (await page.locator("body").innerText({ timeout: 15_000 })).replace(/\s+/g, " ");
}

async function ensureGoogleAccess(page, label) {
  for (let attempt = 1; attempt <= 120; attempt += 1) {
    await page.waitForLoadState("domcontentloaded").catch(() => {});
    await page.waitForTimeout(attempt === 1 ? 2500 : 5000);
    const text = await pageText(page).catch(() => "");
    const challenged =
      page.url().includes("/sorry/") ||
      /unusual traffic|i'm not a robot|recaptcha|429\.? that's an error|too many requests/i.test(text);
    if (!challenged) return;
    if (attempt === 1) {
      console.log(
        `\n${label}: Google presented a CAPTCHA or rate-limit page. ` +
        "Complete the challenge in the visible Firefox window. The script will detect clearance automatically."
      );
    }
  }
  throw new Error(`${label}: Google access was still blocked after ten minutes.`);
}

async function findVisibleResultCount(page) {
  const resultStats = page.locator("#result-stats");
  if (await resultStats.isVisible().catch(() => false)) {
    return (await resultStats.innerText()).trim();
  }
  const text = await pageText(page);
  const matches = text.match(/(?:About\s+)?[\d,.]+\+?\s+results?(?:\s|$)/i);
  return matches?.[0]?.trim() ?? null;
}

async function revealGoogleTools(page) {
  const candidates = [
    page.getByRole("button", { name: /^Tools$/i }),
    page.getByText(/^Tools$/i, { exact: true }),
  ];
  for (const candidate of candidates) {
    if (await candidate.first().isVisible().catch(() => false)) {
      await candidate.first().click();
      await page.waitForTimeout(1200);
      return true;
    }
  }
  return false;
}

async function captureSearch(page, outputDir, video) {
  const kind = video ? "Google Video Search" : "Google Search";
  const params = new URLSearchParams({ q: TERM, hl: "en", num: "10", pws: "0" });
  if (video) params.set("tbm", "vid");
  const url = `https://www.google.com/search?${params.toString()}`;

  await page.goto(url, { waitUntil: "domcontentloaded", timeout: 60_000 });
  await ensureGoogleAccess(page, `${TERM} ${kind}`);
  await revealGoogleTools(page);

  let resultCount = await findVisibleResultCount(page);
  if (!resultCount) {
    console.log(
      `\n${TERM} ${kind}: no result count is visible. ` +
      "Open Tools in Firefox if needed; the script will continue when it detects the count."
    );
    for (let attempt = 1; attempt <= 120 && !resultCount; attempt += 1) {
      await page.waitForTimeout(5000);
      await ensureGoogleAccess(page, `${TERM} ${kind}`);
      resultCount = await findVisibleResultCount(page);
    }
  }
  if (!resultCount) {
    throw new Error(`${TERM} ${kind}: refusing to save a screenshot without a visible result count.`);
  }

  const suffix = video ? "google_video_search" : "google_search";
  const filename = `elephant_${suffix}_${CAPTURE_DATE}_CANDIDATE.png`;
  await page.screenshot({ path: join(outputDir, filename), fullPage: false });
  console.log(`  ${kind}: ${resultCount} -> ${filename}`);
  return { kind, result: resultCount, url, filename, capturedAt: new Date().toISOString() };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  await mkdir(args.out, { recursive: true });
  await mkdir(dirname(args.profile), { recursive: true });

  const context = await firefox.launchPersistentContext(args.profile, {
    headless: false,
    viewport: VIEWPORT,
    locale: "en-US",
    colorScheme: "light",
    slowMo: 75,
  });
  const page = context.pages()[0] ?? await context.newPage();

  try {
    console.log(`Capturing elephant baselines into ${args.out}`);
    const records = [];
    records.push(await captureSearch(page, args.out, false));
    await page.waitForTimeout(7000);
    records.push(await captureSearch(page, args.out, true));

    const logPath = join(args.out, `elephant_google_capture_log_${CAPTURE_DATE}.json`);
    await writeFile(
      logPath,
      `${JSON.stringify({ term: TERM, viewport: VIEWPORT, records }, null, 2)}\n`,
      "utf8"
    );
    console.log(`\nCompleted. Log: ${logPath}`);
  } finally {
    await context.close();
  }
}

await main();
