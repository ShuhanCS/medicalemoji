/**
 * Recapture the Google Search and Google Video Search evidence screenshots for
 * one concept, together with the `elephant` comparator, and refuse to save a
 * screenshot whose result count cannot be confirmed.
 *
 * Why this exists: the v1.18.0 white-blood-cell Search capture recorded "About
 * 125 results" for a term that independently measures ~880,000,000. Google
 * occasionally prints a collapsed estimate on a single page load. The original
 * capture script screenshotted whatever number was on screen, so the bad read
 * reached the submitted PDF.
 *
 * The guard here is agreement across independent loads: each query is loaded
 * CONFIRMATIONS times, and the count must land in the same order of magnitude
 * every time before anything is written to disk. A collapsed estimate does not
 * survive that, because reloading returns the ordinary figure.
 *
 * The script never attempts to bypass or solve a CAPTCHA. If Google presents a
 * challenge, the operator completes it in the visible browser and the script
 * detects clearance automatically.
 *
 * Usage:
 *   node scripts/recapture_google_search_evidence.mjs \
 *     --slug=white-blood-cell --release=v1.18.0 --term=white-blood-cell
 */

import { homedir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { mkdir, writeFile } from "node:fs/promises";

import { firefox } from "playwright";


const ROOT = resolve(import.meta.dirname, "..");
const VIEWPORT = { width: 1440, height: 1100 };
const PROFILE = join(homedir(), ".medicalemoji-google-evidence-firefox");
const COMPARATOR = "elephant";
const CONFIRMATIONS = 3;


function parseArgs(argv) {
  const values = {
    slug: null,
    release: null,
    term: null,
    date: new Date().toISOString().slice(0, 10),
  };
  for (const argument of argv) {
    const [key, ...parts] = argument.replace(/^--/, "").split("=");
    if (key in values && parts.length) values[key] = parts.join("=");
  }
  for (const required of ["slug", "release", "term"]) {
    if (!values[required]) throw new Error(`Missing --${required}.`);
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


async function revealGoogleTools(page) {
  const toggle = page.locator("#hdtb-tls, [role='button'][aria-controls]").filter({ hasText: /^Tools$/i });
  for (const attempt of [{ force: false }, { force: true }]) {
    if (!(await toggle.first().isVisible().catch(() => false))) break;
    const clicked = await toggle
      .first()
      .click({ timeout: 8000, ...attempt })
      .then(() => true)
      .catch(() => false);
    if (clicked) {
      await page.waitForTimeout(1500);
      return true;
    }
  }
  return false;
}


async function readCount(page) {
  const stats = await page
    .locator("#result-stats")
    .first()
    .textContent({ timeout: 5000 })
    .catch(() => null);
  const raw = stats?.trim()
    ? stats.replace(/\s+/g, " ").trim()
    : (await pageText(page)).match(/(?:About\s+)?[\d,.]+\+?\s+results?(?:\s|$)/i)?.[0]?.trim() ?? null;
  const digits = raw?.match(/([\d,.]+)\s+results?/i)?.[1];
  const count = digits ? Number(digits.replace(/[,.]/g, "")) : null;
  return { raw, count: Number.isFinite(count) ? count : null };
}


function searchUrl(query, video) {
  const params = new URLSearchParams({ q: query, hl: "en", num: "10", pws: "0" });
  if (video) params.set("tbm", "vid");
  return `https://www.google.com/search?${params}`;
}


function magnitude(value) {
  return Math.floor(Math.log10(value));
}


/**
 * Load the query CONFIRMATIONS times and require every reading to sit in the
 * same order of magnitude. Returns the final page state, left loaded and with
 * the Tools panel open, ready to screenshot.
 */
async function confirmCount(page, query, video, label) {
  const readings = [];
  for (let load = 1; load <= CONFIRMATIONS; load += 1) {
    await page.goto(searchUrl(query, video), { waitUntil: "domcontentloaded", timeout: 60_000 });
    await ensureGoogleAccess(page, `${label} load ${load}`);
    await revealGoogleTools(page);

    let reading = await readCount(page);
    for (let retry = 1; retry <= 12 && reading.count === null; retry += 1) {
      await page.waitForTimeout(4000);
      await revealGoogleTools(page);
      reading = await readCount(page);
    }
    if (reading.count === null) {
      throw new Error(`${label}: no result count was visible on load ${load}.`);
    }

    readings.push(reading);
    console.log(`  ${label} load ${load}: ${reading.raw}`);
    if (load < CONFIRMATIONS) await page.waitForTimeout(6000);
  }

  const magnitudes = new Set(readings.map((r) => magnitude(r.count)));
  if (magnitudes.size > 1) {
    const seen = readings.map((r) => r.count).join(", ");
    throw new Error(
      `${label}: result count was unstable across ${CONFIRMATIONS} loads (${seen}). ` +
      "Refusing to save. Re-run; if it stays unstable, capture manually and record why."
    );
  }

  return readings;
}


/**
 * The count lives in the Tools panel. readCount() can pull it from the DOM
 * while the panel is collapsed, which is fine for confirming the value but
 * useless as evidence: the screenshot has to show the number on screen.
 */
async function exposeCountOnScreen(page, label) {
  const stats = page.locator("#result-stats").first();
  for (let attempt = 1; attempt <= 6; attempt += 1) {
    if (await stats.isVisible().catch(() => false)) return;
    await revealGoogleTools(page);
    await page.waitForTimeout(1200);
  }
  throw new Error(`${label}: the result count never became visible on screen. Refusing to save.`);
}


async function captureQuery(page, { query, video, label, destination }) {
  const readings = await confirmCount(page, query, video, label);
  await page.evaluate(() => window.scrollTo(0, 0));
  await exposeCountOnScreen(page, label);
  await page.screenshot({ path: destination, fullPage: false });
  return {
    label,
    query,
    kind: video ? "Google Video Search" : "Google Search",
    url: searchUrl(query, video),
    result: readings.at(-1).raw,
    count: readings.at(-1).count,
    confirmations: readings.map((r) => r.count),
    file: destination,
    capturedAt: new Date().toISOString(),
  };
}


async function main() {
  const args = parseArgs(process.argv.slice(2));
  const outputDir = join(ROOT, "submissions", args.release, args.slug, "evidence", "frequency");
  await mkdir(outputDir, { recursive: true });
  await mkdir(dirname(PROFILE), { recursive: true });

  const jobs = [
    {
      query: args.term,
      video: false,
      label: `${args.slug} Google Search`,
      destination: join(outputDir, `${args.slug}_google_search_${args.date}_SUBMIT.png`),
    },
    {
      query: COMPARATOR,
      video: false,
      label: `${COMPARATOR} Google Search`,
      destination: join(outputDir, `${args.slug}_google_search_elephant_${args.date}_SUBMIT.png`),
    },
    {
      query: args.term,
      video: true,
      label: `${args.slug} Google Video Search`,
      destination: join(outputDir, `${args.slug}_google_video_search_${args.date}_SUBMIT.png`),
    },
    {
      query: COMPARATOR,
      video: true,
      label: `${COMPARATOR} Google Video Search`,
      destination: join(outputDir, `${args.slug}_google_video_search_elephant_${args.date}_SUBMIT.png`),
    },
  ];

  const context = await firefox.launchPersistentContext(PROFILE, {
    headless: false,
    viewport: VIEWPORT,
    locale: "en-US",
    colorScheme: "light",
    slowMo: 75,
  });
  const page = context.pages()[0] ?? await context.newPage();

  const records = [];
  try {
    for (const job of jobs) {
      console.log(`\nConfirming ${job.label}...`);
      records.push(await captureQuery(page, job));
      await page.waitForTimeout(7000);
    }
  } finally {
    await context.close();
  }

  const logPath = join(outputDir, `${args.slug}_google_recapture_log_${args.date}.json`);
  await writeFile(
    logPath,
    `${JSON.stringify({ viewport: VIEWPORT, comparator: COMPARATOR, confirmations: CONFIRMATIONS, records }, null, 2)}\n`,
    "utf8"
  );

  console.log("\nConfirmed counts:");
  for (const record of records) console.log(`  ${record.label.padEnd(38)} ${record.result}`);
  console.log(`\nWrote ${logPath}`);
}


main().catch((error) => {
  console.error(`\nRecapture failed: ${error.message}`);
  process.exitCode = 1;
});
