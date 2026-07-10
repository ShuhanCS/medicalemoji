/**
 * Capture a conservative Bing evidence supplement for use only when Google is
 * inaccessible. Unicode permits other search engines that display real data
 * in that circumstance, provided the substitution is reproducible and
 * comparable in quality.
 *
 * These files supplement rather than silently replace the five Google
 * categories. The proposal stays DRAFT until the submitter chooses and
 * explains the official fallback or obtains the Google captures.
 *
 * Usage:
 *   npm run evidence:capture:alternate -- --concept=ultrasound --release=v1.5.0
 */

import { resolve, join } from "node:path";
import { mkdir, writeFile } from "node:fs/promises";

import { firefox } from "playwright";


const ROOT = resolve(import.meta.dirname, "..");
const VIEWPORT = { width: 1440, height: 1100 };
const CAPTURE_DATE = new Date().toISOString().slice(0, 10);

const CONCEPTS = {
  maze: { slug: "maze", term: "maze", webTerm: "maze" },
  ultrasound: { slug: "ultrasound", term: "ultrasound", webTerm: "ultrasound" },
  "first-aid-kit": { slug: "first-aid-kit", term: "first aid kit", webTerm: '"first aid kit"' },
};


function parseArgs(argv) {
  const values = { concept: "all", release: "v1.5.0" };
  for (const argument of argv) {
    const [key, ...parts] = argument.replace(/^--/, "").split("=");
    if (key in values && parts.length) values[key] = parts.join("=");
  }
  if (values.concept !== "all" && !(values.concept in CONCEPTS)) {
    throw new Error(`Unknown concept '${values.concept}'. Use maze, ultrasound, first-aid-kit, or all.`);
  }
  return values;
}


async function pageText(page) {
  return (await page.locator("body").innerText({ timeout: 20_000 })).replace(/\s+/g, " ");
}


async function fetchBingHtml(url, label) {
  const response = await fetch(url, {
    headers: {
      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
      "accept-language": "en-US,en;q=0.9",
    },
  });
  const html = await response.text();
  if (!response.ok) {
    throw new Error(`${label}: Bing HTTP request returned ${response.status}.`);
  }
  const text = html.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ");
  if (/captcha|unusual traffic|verify you are human|our systems have detected/i.test(text)) {
    throw new Error(`${label}: Bing returned a challenge page; no evidence was saved.`);
  }
  return html;
}


async function renderStaticBingResponse(page, html) {
  const staticHtml = html
    .replace(/<script\b[^>]*>[\s\S]*?<\/script>/gi, "")
    .replace(/<meta\b[^>]*http-equiv=["']?refresh["']?[^>]*>/gi, "")
    .replace(/<head([^>]*)>/i, '<head$1><base href="https://www.bing.com/">');
  await page.setContent(staticHtml, { waitUntil: "domcontentloaded", timeout: 60_000 });
  await page.waitForTimeout(2500);
}


async function captureBingWeb(page, concept, outputDir) {
  const query = concept.webTerm;
  const params = new URLSearchParams({ q: query, setlang: "en-us", cc: "us" });
  const url = `https://www.bing.com/search?${params.toString()}`;
  const label = "Bing Web Search";

  const html = await fetchBingHtml(url, `${concept.slug} ${label}`);
  await renderStaticBingResponse(page, html);

  const countLocator = page.locator(".sb_count").first();
  const count = (await countLocator.isVisible().catch(() => false))
    ? (await countLocator.innerText()).trim()
    : null;
  if (!count || !/\d/.test(count)) {
    throw new Error(`${concept.slug} ${label}: refusing to save without Bing's visible result count.`);
  }

  const filename = `${concept.slug}_bing_web_search_${CAPTURE_DATE}_SUPPLEMENT.png`;
  await page.screenshot({ path: join(outputDir, filename), fullPage: false });
  return { kind: label, result: count, query, url, filename, capturedAt: new Date().toISOString() };
}


async function captureBingVertical(page, concept, outputDir, vertical) {
  const params = new URLSearchParams({ q: concept.term, setlang: "en-us", cc: "us" });
  const url = `https://www.bing.com/${vertical}/search?${params.toString()}`;
  const label = vertical === "videos" ? "Bing Video Search" : "Bing Image Search";

  const html = await fetchBingHtml(url, `${concept.slug} ${label}`);
  await renderStaticBingResponse(page, html);
  const text = await pageText(page);
  const hasResults = vertical === "videos"
    ? (await page.locator("a[href*='/videos/']").count()) > 1 || /video/i.test(text)
    : (await page.locator("img").count()) > 5;
  if (!hasResults) {
    throw new Error(`${concept.slug} ${label}: no recognizable result set was present.`);
  }

  const suffix = vertical === "videos" ? "bing_video_search" : "bing_image_search";
  const filename = `${concept.slug}_${suffix}_${CAPTURE_DATE}_SUPPLEMENT.png`;
  await page.screenshot({ path: join(outputDir, filename), fullPage: false });
  return {
    kind: label,
    result: "Visible result set; Bing does not expose a vertical-result total on this page",
    query: concept.term,
    url,
    filename,
    capturedAt: new Date().toISOString(),
  };
}


async function captureConcept(browser, release, concept) {
  const context = await browser.newContext({
    viewport: VIEWPORT,
    locale: "en-US",
    colorScheme: "light",
  });
  const page = await context.newPage();
  const outputDir = join(
    ROOT,
    "submissions",
    release,
    concept.slug,
    "evidence",
    "frequency",
    "alternative"
  );
  await mkdir(outputDir, { recursive: true });

  try {
    const records = [];
    records.push(await captureBingWeb(page, concept, outputDir));
    records.push(await captureBingVertical(page, concept, outputDir, "videos"));
    records.push(await captureBingVertical(page, concept, outputDir, "images"));

    const logPath = join(outputDir, `${concept.slug}_bing_capture_log_${CAPTURE_DATE}.json`);
    await writeFile(
      logPath,
      `${JSON.stringify({
        concept: concept.slug,
        provider: "Microsoft Bing",
        purpose: "Unicode Google-inaccessibility supplement",
        captureMethod: "Bing HTTPS response rendered locally without response scripts",
        viewport: VIEWPORT,
        records,
      }, null, 2)}\n`,
      "utf8"
    );
    return logPath;
  } finally {
    await context.close();
  }
}


async function main() {
  const args = parseArgs(process.argv.slice(2));
  const concepts = args.concept === "all" ? Object.values(CONCEPTS) : [CONCEPTS[args.concept]];
  const browser = await firefox.launch({ headless: true });
  try {
    for (const concept of concepts) {
      console.log(`Capturing Bing supplement for ${concept.slug}...`);
      console.log(`Completed: ${await captureConcept(browser, args.release, concept)}`);
    }
  } finally {
    await browser.close();
  }
}


main().catch((error) => {
  console.error(`Alternative evidence capture failed: ${error.message}`);
  process.exitCode = 1;
});
