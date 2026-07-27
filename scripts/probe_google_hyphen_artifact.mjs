/**
 * Probe whether Google's result-count estimate collapses for hyphen-grouped
 * multiword queries.
 *
 * Unicode's proposal instructions require multiword terms to be grouped with
 * hyphens ("when searching for black swan, use [black-swan]"). For some terms
 * the hyphenated form returns a result-count estimate several orders of
 * magnitude below the same words unhyphenated, while Google still returns
 * ordinary topical results and an AI Overview for the concept.
 *
 * This script measures that gap directly. It runs each term in both forms and
 * records whatever Google prints as its result count. It also runs Unicode's
 * own documentation example (black swan) as a control, so the finding does not
 * depend on the proposed term.
 *
 * The script never attempts to bypass or solve a CAPTCHA. If Google presents a
 * challenge, the operator completes it in the visible browser and the script
 * detects clearance automatically. It reuses the same persistent evidence
 * profile as scripts/capture_unicode_evidence.mjs.
 *
 * Usage:
 *   node scripts/probe_google_hyphen_artifact.mjs
 *   node scripts/probe_google_hyphen_artifact.mjs --out=path/to/probe.json
 */

import { homedir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { mkdir, writeFile } from "node:fs/promises";

import { firefox } from "playwright";


const ROOT = resolve(import.meta.dirname, "..");
const VIEWPORT = { width: 1440, height: 1100 };
const PROFILE = join(homedir(), ".medicalemoji-google-evidence-firefox");
const DEFAULT_OUT = join(
  ROOT,
  "submissions",
  "v1.19.0",
  "white-blood-cell",
  "evidence",
  "frequency",
  "google_hyphen_artifact_probe.json"
);

/**
 * Each pair is the same concept in both query forms. `elephant` is a
 * single word and acts as a null case: it has no hyphenated variant, so it
 * should show no gap. `black-swan` is the example Unicode prints in its own
 * instructions.
 */
const PAIRS = [
  { concept: "white blood cell", grouped: "white-blood-cell", plain: "white blood cell" },
  { concept: "black swan", grouped: "black-swan", plain: "black swan" },
  { concept: "first aid kit", grouped: "first-aid-kit", plain: "first aid kit" },
  { concept: "elephant", grouped: "elephant", plain: "elephant" },
];


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
  // Google renders the count inside the Tools panel. The panel toggle is a div
  // with role=button that intermittently swallows a normal click, so fall back
  // to a forced click and then to reading the node directly.
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


async function findVisibleResultCount(page) {
  // textContent rather than innerText: #result-stats is present in the DOM even
  // while the Tools panel that displays it is collapsed.
  const stats = await page
    .locator("#result-stats")
    .first()
    .textContent({ timeout: 5000 })
    .catch(() => null);
  if (stats?.trim()) return stats.replace(/\s+/g, " ").trim();

  const text = await pageText(page);
  return text.match(/(?:About\s+)?[\d,.]+\+?\s+results?(?:\s|$)/i)?.[0]?.trim() ?? null;
}


/** "About 125 results (0.24s)" -> 125 */
function parseCount(raw) {
  const digits = raw?.match(/([\d,.]+)\s+results?/i)?.[1];
  if (!digits) return null;
  const value = Number(digits.replace(/[,.]/g, ""));
  return Number.isFinite(value) ? value : null;
}


async function measure(page, query, label) {
  const url = `https://www.google.com/search?${new URLSearchParams({
    q: query,
    hl: "en",
    num: "10",
    pws: "0",
  })}`;

  await page.goto(url, { waitUntil: "domcontentloaded", timeout: 60_000 });
  await ensureGoogleAccess(page, label);
  await revealGoogleTools(page);

  let raw = await findVisibleResultCount(page);
  for (let attempt = 1; attempt <= 24 && !raw; attempt += 1) {
    await page.waitForTimeout(5000);
    await ensureGoogleAccess(page, label);
    raw = await findVisibleResultCount(page);
  }

  const body = await pageText(page);
  return {
    query,
    url,
    raw,
    count: parseCount(raw),
    // Evidence that Google understood the concept even when the count collapses.
    hasAiOverview: /AI Overview/i.test(body),
    capturedAt: new Date().toISOString(),
  };
}


async function main() {
  const outArg = process.argv.slice(2).find((a) => a.startsWith("--out="));
  const outPath = outArg ? resolve(outArg.slice("--out=".length)) : DEFAULT_OUT;

  await mkdir(dirname(PROFILE), { recursive: true });
  const context = await firefox.launchPersistentContext(PROFILE, {
    headless: false,
    viewport: VIEWPORT,
    locale: "en-US",
    colorScheme: "light",
    slowMo: 75,
  });
  const page = context.pages()[0] ?? await context.newPage();

  const results = [];
  try {
    for (const pair of PAIRS) {
      const grouped = await measure(page, pair.grouped, `${pair.concept} grouped`);
      await page.waitForTimeout(7000);
      const plain = pair.plain === pair.grouped
        ? grouped
        : await measure(page, pair.plain, `${pair.concept} plain`);
      await page.waitForTimeout(7000);

      const ratio = grouped.count && plain.count ? plain.count / grouped.count : null;
      results.push({ concept: pair.concept, grouped, plain, plainOverGrouped: ratio });
      console.log(
        `${pair.concept.padEnd(18)} grouped=${String(grouped.count).padStart(12)} ` +
        `plain=${String(plain.count).padStart(12)} ratio=${ratio ? ratio.toExponential(2) : "n/a"}`
      );
    }
  } finally {
    await context.close();
  }

  await mkdir(dirname(outPath), { recursive: true });
  await writeFile(outPath, `${JSON.stringify({ viewport: VIEWPORT, results }, null, 2)}\n`, "utf8");
  console.log(`\nWrote ${outPath}`);
}


main().catch((error) => {
  console.error(`\nProbe failed: ${error.message}`);
  process.exitCode = 1;
});
