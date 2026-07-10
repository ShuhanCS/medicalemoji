/**
 * Capture Unicode's required Google frequency screenshots in a persistent,
 * headed Playwright Firefox session.
 *
 * The script never attempts to bypass or solve a CAPTCHA. If Google presents a
 * challenge, the operator completes it in the visible browser. The script
 * detects clearance automatically. The same profile is reused for later captures.
 *
 * Usage:
 *   npm run evidence:capture -- --concept=ultrasound --release=v1.5.0
 *   npm run evidence:capture -- --concept=all --release=v1.5.0
 */

import { homedir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { mkdir, writeFile } from "node:fs/promises";

import { chromium, firefox } from "playwright";


const ROOT = resolve(import.meta.dirname, "..");
const VIEWPORT = { width: 1440, height: 1100 };
const CAPTURE_DATE = new Date().toISOString().slice(0, 10);
const DEFAULT_FIREFOX_PROFILE = join(homedir(), ".medicalemoji-google-evidence-firefox");
const DEFAULT_CHROME_PROFILE = join(homedir(), ".medicalemoji-google-evidence-chrome");

const CONCEPTS = {
  maze: {
    slug: "maze",
    term: "maze",
    searchTerm: "maze",
  },
  ultrasound: {
    slug: "ultrasound",
    term: "ultrasound",
    searchTerm: "ultrasound",
  },
  "first-aid-kit": {
    slug: "first-aid-kit",
    term: "first aid kit",
    searchTerm: "first-aid-kit",
  },
};


function parseArgs(argv) {
  const values = {
    concept: "all",
    release: "v1.5.0",
    browser: "firefox",
    profile: null,
  };
  for (const argument of argv) {
    const [key, ...parts] = argument.replace(/^--/, "").split("=");
    if (key in values && parts.length) values[key] = parts.join("=");
  }
  if (values.concept !== "all" && !(values.concept in CONCEPTS)) {
    throw new Error(`Unknown concept '${values.concept}'. Use maze, ultrasound, first-aid-kit, or all.`);
  }
  if (!(["firefox", "chrome"].includes(values.browser))) {
    throw new Error(`Unknown browser '${values.browser}'. Use firefox or chrome.`);
  }
  values.profile ??= values.browser === "chrome" ? DEFAULT_CHROME_PROFILE : DEFAULT_FIREFOX_PROFILE;
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


async function captureSearch(page, concept, outputDir, video) {
  const kind = video ? "Google Video Search" : "Google Search";
  const params = new URLSearchParams({
    q: concept.searchTerm,
    hl: "en",
    num: "10",
    pws: "0",
  });
  if (video) params.set("tbm", "vid");
  const url = `https://www.google.com/search?${params.toString()}`;

  await page.goto(url, { waitUntil: "domcontentloaded", timeout: 60_000 });
  await ensureGoogleAccess(page, `${concept.slug} ${kind}`);
  await revealGoogleTools(page);

  let resultCount = await findVisibleResultCount(page);
  if (!resultCount) {
    console.log(
      `\n${concept.slug} ${kind}: no result count is visible. ` +
      "Open Tools in Firefox if needed; the script will continue when it detects the count."
    );
    for (let attempt = 1; attempt <= 120 && !resultCount; attempt += 1) {
      await page.waitForTimeout(5000);
      await ensureGoogleAccess(page, `${concept.slug} ${kind}`);
      resultCount = await findVisibleResultCount(page);
    }
  }
  if (!resultCount) {
    throw new Error(`${concept.slug} ${kind}: refusing to save a screenshot without a visible result count.`);
  }

  const suffix = video ? "google_video_search" : "google_search";
  const filename = `${concept.slug}_${suffix}_${CAPTURE_DATE}_SUBMIT.png`;
  const destination = join(outputDir, filename);
  await page.screenshot({ path: destination, fullPage: false });
  return { kind, result: resultCount, url, filename, capturedAt: new Date().toISOString() };
}


async function captureTrends(page, concept, outputDir, imageSearch) {
  const kind = imageSearch ? "Google Trends Image Search" : "Google Trends Web Search";
  const params = new URLSearchParams({
    date: imageSearch ? "all_2008" : "all",
    q: `elephant,${concept.term}`,
  });
  if (imageSearch) params.set("gprop", "images");
  const url = `https://trends.google.com/trends/explore?${params.toString()}`;

  await page.goto(url, { waitUntil: "domcontentloaded", timeout: 60_000 });
  await ensureGoogleAccess(page, `${concept.slug} ${kind}`);
  await page.waitForTimeout(10_000);

  let text = await pageText(page);
  if (/oops! something went wrong|too many requests|429\.? that's an error/i.test(text)) {
    console.log(
      `\n${concept.slug} ${kind}: Trends did not load. ` +
      "Wait and reload once in Firefox. The script will continue when the chart is complete."
    );
    for (let attempt = 1; attempt <= 120; attempt += 1) {
      await page.waitForTimeout(5000);
      await ensureGoogleAccess(page, `${concept.slug} ${kind}`);
      text = await pageText(page);
      if (/Interest over time/i.test(text) && !/Oops! Something went wrong/i.test(text)) break;
    }
  }

  if (!/Interest over time/i.test(text) || /Oops! Something went wrong/i.test(text)) {
    throw new Error(`${concept.slug} ${kind}: refusing to save an incomplete or error-state Trends page.`);
  }
  if (!/Worldwide/i.test(text) || !/elephant/i.test(text)) {
    throw new Error(`${concept.slug} ${kind}: expected Worldwide and elephant controls were not visible.`);
  }

  await page.evaluate(() => window.scrollTo(0, 0));
  const suffix = imageSearch ? "google_trends_image" : "google_trends_web";
  const filename = `${concept.slug}_${suffix}_${CAPTURE_DATE}_SUBMIT.png`;
  const destination = join(outputDir, filename);
  await page.screenshot({ path: destination, fullPage: false });
  return {
    kind,
    result: imageSearch ? "Worldwide, 2008-present, Image Search" : "Worldwide, 2004-present, Web Search",
    url,
    filename,
    capturedAt: new Date().toISOString(),
  };
}


async function captureConcept(page, release, concept) {
  const outputDir = join(ROOT, "submissions", release, concept.slug, "evidence", "frequency");
  await mkdir(outputDir, { recursive: true });
  const records = [];

  records.push(await captureSearch(page, concept, outputDir, false));
  await page.waitForTimeout(7000);
  records.push(await captureSearch(page, concept, outputDir, true));
  await page.waitForTimeout(7000);
  records.push(await captureTrends(page, concept, outputDir, false));
  await page.waitForTimeout(7000);
  records.push(await captureTrends(page, concept, outputDir, true));

  const logPath = join(outputDir, `${concept.slug}_google_capture_log_${CAPTURE_DATE}.json`);
  await writeFile(
    logPath,
    `${JSON.stringify({ concept: concept.slug, viewport: VIEWPORT, records }, null, 2)}\n`,
    "utf8"
  );
  return { concept: concept.slug, logPath, records };
}


async function main() {
  const args = parseArgs(process.argv.slice(2));
  const concepts = args.concept === "all" ? Object.values(CONCEPTS) : [CONCEPTS[args.concept]];
  await mkdir(dirname(args.profile), { recursive: true });

  const browserType = args.browser === "chrome" ? chromium : firefox;
  const context = await browserType.launchPersistentContext(args.profile, {
    headless: false,
    ...(args.browser === "chrome" ? { channel: "chrome" } : {}),
    viewport: VIEWPORT,
    locale: "en-US",
    colorScheme: "light",
    slowMo: 75,
  });
  const page = context.pages()[0] ?? await context.newPage();

  try {
    for (const concept of concepts) {
      console.log(`\nCapturing ${concept.slug} into submissions/${args.release}/...`);
      const result = await captureConcept(page, args.release, concept);
      console.log(`Completed ${result.concept}: ${result.logPath}`);
      await page.waitForTimeout(10_000);
    }
  } finally {
    await context.close();
  }
}


main().catch((error) => {
  console.error(`\nEvidence capture failed: ${error.message}`);
  process.exitCode = 1;
});
