/* eslint-disable @typescript-eslint/no-require-imports */
const pptxgen = require("pptxgenjs");
const path = require("path");

const pptx = new pptxgen();
pptx.layout = "LAYOUT_WIDE";
pptx.author = "Shuhan He";
pptx.company = "Medical Emoji Project";
pptx.subject = "Microsoft internal review of the 2026 Medical Emoji proposal strategy";
pptx.title = "Medical Emoji: Microsoft Internal Review";
pptx.lang = "en-US";
pptx.theme = {
  headFontFace: "Segoe UI Semibold",
  bodyFontFace: "Segoe UI",
  lang: "en-US",
};
pptx.defineLayout({ name: "LAYOUT_WIDE", width: 13.333, height: 7.5 });

const C = {
  navy: "0B1739",
  blue: "2563EB",
  cyan: "0E7490",
  teal: "0F8A7B",
  green: "159A72",
  amber: "D99A2B",
  red: "C85A54",
  ink: "172033",
  muted: "667085",
  line: "D8DEE9",
  pale: "F4F7FB",
  white: "FFFFFF",
  bluePale: "EAF1FF",
  tealPale: "E8F7F4",
  amberPale: "FFF4DB",
  redPale: "FCEAE8",
};

const ROOT = path.resolve(__dirname, "../../..");
const RELEASE = path.join(ROOT, "submissions", "v1.7.0");
const OUT = path.join(__dirname, "Emoji-2026-Brief-v6.pptx");

const assets = {
  kidney: {
    c72: path.join(RELEASE, "kidney", "images", "kidney_color_72x72_SUBMIT.png"),
    c18: path.join(RELEASE, "kidney", "images", "kidney_color_18x18_SUBMIT.png"),
    b72: path.join(RELEASE, "kidney", "images", "kidney_bw_72x72_SUBMIT.png"),
    b18: path.join(RELEASE, "kidney", "images", "kidney_bw_18x18_SUBMIT.png"),
  },
  stomach: {
    c72: path.join(RELEASE, "stomach", "images", "stomach_color_72x72_SUBMIT.png"),
    c18: path.join(RELEASE, "stomach", "images", "stomach_color_18x18_SUBMIT.png"),
    b72: path.join(RELEASE, "stomach", "images", "stomach_bw_72x72_SUBMIT.png"),
    b18: path.join(RELEASE, "stomach", "images", "stomach_bw_18x18_SUBMIT.png"),
  },
  liver: {
    c72: path.join(RELEASE, "liver", "images", "liver_color_72x72_SUBMIT.png"),
    c18: path.join(RELEASE, "liver", "images", "liver_color_18x18_SUBMIT.png"),
    b72: path.join(RELEASE, "liver", "images", "liver_bw_72x72_SUBMIT.png"),
    b18: path.join(RELEASE, "liver", "images", "liver_bw_18x18_SUBMIT.png"),
  },
};

function shadow() {
  return { type: "outer", color: "000000", blur: 3, offset: 1, angle: 135, opacity: 0.1 };
}

function addHeader(slide, title, kicker) {
  slide.background = { color: C.pale };
  slide.addText(kicker.toUpperCase(), {
    x: 0.65, y: 0.34, w: 4.6, h: 0.25, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 10, charSpacing: 1.5, color: C.blue,
  });
  slide.addText(title, {
    x: 0.65, y: 0.68, w: 12.0, h: 0.55, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 28, color: C.ink,
  });
}

function addFooter(slide, index, source) {
  slide.addText(source, {
    x: 0.65, y: 7.02, w: 11.65, h: 0.22, margin: 0,
    fontFace: "Segoe UI", fontSize: 9, color: C.muted, breakLine: false,
  });
  slide.addText(String(index), {
    x: 12.45, y: 7.02, w: 0.28, h: 0.22, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 9, color: C.muted, align: "right",
  });
}

function card(slide, x, y, w, h, options) {
  slide.addShape(pptx.ShapeType.roundRect, {
    x, y, w, h,
    rectRadius: 0.06,
    fill: { color: options.fill || C.white },
    line: { color: options.line || C.line, width: 0.8 },
    shadow: shadow(),
  });
  if (options.accent) {
    slide.addShape(pptx.ShapeType.rect, {
      x, y, w: 0.1, h,
      fill: { color: options.accent }, line: { color: options.accent, transparency: 100 },
    });
  }
  if (options.label) {
    slide.addText(options.label.toUpperCase(), {
      x: x + 0.28, y: y + 0.2, w: w - 0.55, h: 0.22, margin: 0,
      fontFace: "Segoe UI Semibold", fontSize: 9.5, charSpacing: 1.1,
      color: options.accent || C.blue,
    });
  }
  if (options.title) {
    slide.addText(options.title, {
      x: x + 0.28, y: y + 0.54, w: w - 0.55, h: 0.38, margin: 0,
      fontFace: "Segoe UI Semibold", fontSize: options.titleSize || 20, color: C.ink,
    });
  }
  if (options.body) {
    slide.addText(options.body, {
      x: x + 0.28, y: y + 1.02, w: w - 0.55, h: h - 1.18, margin: 0,
      fontFace: "Segoe UI", fontSize: options.bodySize || 12.5, color: C.muted,
      breakLine: false, valign: "top", fit: "shrink",
    });
  }
}

function statusPill(slide, text, x, y, w, fill, color) {
  slide.addShape(pptx.ShapeType.roundRect, {
    x, y, w, h: 0.34, rectRadius: 0.06,
    fill: { color: fill }, line: { color: fill, transparency: 100 },
  });
  slide.addText(text, {
    x, y: y + 0.02, w, h: 0.22, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 9.5, color, align: "center",
  });
}

// Slide 1: title
{
  const slide = pptx.addSlide();
  slide.background = { color: C.navy };
  slide.addShape(pptx.ShapeType.arc, {
    x: 8.8, y: -1.1, w: 5.8, h: 5.8, adjustPoint: 0.28,
    rotate: 28, fill: { color: C.blue, transparency: 68 },
    line: { color: C.blue, transparency: 100 },
  });
  slide.addShape(pptx.ShapeType.arc, {
    x: 9.7, y: 3.4, w: 4.2, h: 4.2, adjustPoint: 0.28,
    rotate: 206, fill: { color: C.cyan, transparency: 58 },
    line: { color: C.cyan, transparency: 100 },
  });
  slide.addText("MICROSOFT INTERNAL REVIEW", {
    x: 0.85, y: 0.78, w: 4.8, h: 0.28, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 11, charSpacing: 1.6, color: "8FC5FF",
  });
  slide.addText("Medical Emoji", {
    x: 0.85, y: 1.45, w: 7.7, h: 0.9, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 42, color: C.white,
  });
  slide.addText("A focused 2026 filing decision and a defensible Unicode review path", {
    x: 0.85, y: 2.55, w: 7.7, h: 0.74, margin: 0,
    fontFace: "Segoe UI", fontSize: 22, color: "D7E4F7", fit: "shrink",
  });
  slide.addShape(pptx.ShapeType.rect, {
    x: 0.85, y: 3.78, w: 5.9, h: 1.18,
    fill: { color: "132653", transparency: 0 }, line: { color: "2B4C83", width: 1 },
  });
  slide.addText("Decision needed by July 17", {
    x: 1.15, y: 4.06, w: 3.1, h: 0.34, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 18, color: C.white,
  });
  slide.addText("One conditional lead. One fallback. No 2026 organ filing.", {
    x: 1.15, y: 4.49, w: 5.15, h: 0.26, margin: 0,
    fontFace: "Segoe UI", fontSize: 12.5, color: "AFC7EA",
  });
  slide.addText("Prepared by Shuhan He  |  July 12, 2026", {
    x: 0.85, y: 6.72, w: 5.7, h: 0.28, margin: 0,
    fontFace: "Segoe UI", fontSize: 11.5, color: "AFC7EA",
  });
}

// Slide 2: decision
{
  const slide = pptx.addSlide();
  addHeader(slide, "The decision is narrow", "Recommendation");
  card(slide, 0.65, 1.55, 3.85, 4.25, {
    label: "Conditional lead", title: "Ultrasound", accent: C.green, fill: C.tealPale,
    body: "Advance only after the four missing Google captures are embedded and the monitor-plus-probe image passes an 18 × 18 px recognition review.",
  });
  statusPill(slide, "EVIDENCE + DESIGN GATE", 1.0, 5.16, 3.05, C.white, C.green);
  card(slide, 4.75, 1.55, 3.85, 4.25, {
    label: "Fallback", title: "CT Scan", accent: C.blue, fill: C.bluePale,
    body: "Use only if its 2020 evidence, current factor labels, and the submitter’s explicit ownership warranty are refreshed. It is a fallback packet, not filing-ready today.",
  });
  statusPill(slide, "CURRENT-FORMAT REFRESH", 5.1, 5.16, 3.05, C.white, C.blue);
  card(slide, 8.85, 1.55, 3.85, 4.25, {
    label: "Hold", title: "Kidney · Stomach · Liver", accent: C.red, fill: C.redPale,
    body: "Keep the redesigned v1.7 organ packets as future-cycle assets. Their November 2022 declines remain inside Unicode's four-year re-review bar during the July 2026 intake.",
    titleSize: 16.5,
  });
  statusPill(slide, "ELIGIBILITY GATE", 9.2, 5.16, 3.05, C.white, C.red);
  addFooter(slide, 2, "Source: https://www.unicode.org/emoji/proposals.html");
}

// Slide 3: requirements
{
  const slide = pptx.addSlide();
  addHeader(slide, "Four non-negotiable submission checks", "Submission bar");
  const items = [
    ["01", "Public PDF", "One publicly accessible PDF link submitted through the official form; individual submitter names, title, and revision date."],
    ["02", "Four example images", "Color and true black-and-white artwork at 18 × 18 px and 72 × 72 px, all at the top of page 1."],
    ["03", "Five usage screenshots", "Google Search, Google Video Search, Google Trends (Web and Image), and Google Books Ngram embedded in the PDF; use elephant as the comparator where required."],
    ["04", "Rights + factors", "Explicit IP-rights warranty, current inclusion and exclusion factors, reproducible data, and no reliance on petitions or logos."],
  ];
  items.forEach((item, i) => {
    const x = 0.65 + (i % 2) * 6.15;
    const y = 1.55 + Math.floor(i / 2) * 2.45;
    slide.addShape(pptx.ShapeType.roundRect, {
      x, y, w: 5.9, h: 2.05, rectRadius: 0.05,
      fill: { color: C.white }, line: { color: C.line, width: 0.8 }, shadow: shadow(),
    });
    slide.addText(item[0], {
      x: x + 0.28, y: y + 0.32, w: 0.72, h: 0.54, margin: 0,
      fontFace: "Segoe UI Semibold", fontSize: 30, color: i === 2 ? C.teal : C.blue,
    });
    slide.addText(item[1], {
      x: x + 1.15, y: y + 0.3, w: 4.3, h: 0.38, margin: 0,
      fontFace: "Segoe UI Semibold", fontSize: 18, color: C.ink,
    });
    slide.addText(item[2], {
      x: x + 1.15, y: y + 0.82, w: 4.35, h: 0.9, margin: 0,
      fontFace: "Segoe UI", fontSize: 11.5, color: C.muted, fit: "shrink",
    });
  });
  addFooter(slide, 3, "Guidance: https://www.unicode.org/emoji/proposals.html");
}

// Slide 4: readiness map
{
  const slide = pptx.addSlide();
  addHeader(slide, "Submission readiness determines the 2026 order", "Portfolio");
  const rows = [
    ["Ultrasound", "Conditional lead", "Google Books Ngram is documented; four current Google screenshots and an 18 × 18 px recognition sign-off are still missing", C.green, C.tealPale],
    ["CT Scan", "Fallback", "All five evidence categories are present, but the 2020 captures, factor labels, and ownership language need a current-format refresh", C.blue, C.bluePale],
    ["Kidney · Stomach · Liver", "Future-cycle assets", "The v1.7 artwork and PDFs are reviewable, but their November 2022 declines remain within Unicode’s four-year re-review window", C.red, C.redPale],
  ];
  rows.forEach((row, i) => {
    const y = 1.55 + i * 1.63;
    slide.addShape(pptx.ShapeType.roundRect, {
      x: 0.75, y, w: 11.85, h: 1.3, rectRadius: 0.05,
      fill: { color: row[4] }, line: { color: row[3], transparency: 70, width: 1 },
    });
    slide.addShape(pptx.ShapeType.ellipse, {
      x: 1.05, y: y + 0.35, w: 0.58, h: 0.58,
      fill: { color: row[3] }, line: { color: row[3], transparency: 100 },
    });
    slide.addText(String(i + 1), {
      x: 1.05, y: y + 0.43, w: 0.58, h: 0.25, margin: 0,
      fontFace: "Segoe UI Semibold", fontSize: 12, color: C.white, align: "center",
    });
    slide.addText(row[0], {
      x: 1.88, y: y + 0.22, w: 3.2, h: 0.36, margin: 0,
      fontFace: "Segoe UI Semibold", fontSize: 18, color: C.ink,
    });
    slide.addText(row[1], {
      x: 1.88, y: y + 0.73, w: 2.7, h: 0.28, margin: 0,
      fontFace: "Segoe UI Semibold", fontSize: 11, color: row[3],
    });
    slide.addText(row[2], {
      x: 5.02, y: y + 0.35, w: 6.95, h: 0.58, margin: 0,
      fontFace: "Segoe UI", fontSize: 12.5, color: C.muted, valign: "mid", fit: "shrink",
    });
  });
  slide.addText("Do not label a concept filing-ready until its evidence, rights, formatting, and eligibility gates are all closed.", {
    x: 1.25, y: 6.52, w: 10.9, h: 0.28, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 13, color: C.ink, align: "center",
  });
  addFooter(slide, 4, "Proposal workspace: https://github.com/ShuhanCS/medicalemoji/tree/codex/eligible-2026-slate/submissions");
}

// Slide 5: artwork board
{
  const slide = pptx.addSlide();
  addHeader(slide, "Organ art was rebuilt for small-size review", "Future-cycle assets");
  const organs = [
    ["Kidney", assets.kidney],
    ["Stomach", assets.stomach],
    ["Liver", assets.liver],
  ];
  const labels = ["72 px color", "18 px color", "72 px B&W", "18 px B&W"];
  organs.forEach((entry, row) => {
    const y = 1.55 + row * 1.58;
    slide.addShape(pptx.ShapeType.roundRect, {
      x: 0.7, y, w: 11.95, h: 1.34, rectRadius: 0.05,
      fill: { color: C.white }, line: { color: C.line, width: 0.8 }, shadow: shadow(),
    });
    slide.addText(entry[0], {
      x: 1.0, y: y + 0.46, w: 1.4, h: 0.34, margin: 0,
      fontFace: "Segoe UI Semibold", fontSize: 18, color: C.ink,
    });
    const imgs = [entry[1].c72, entry[1].c18, entry[1].b72, entry[1].b18];
    imgs.forEach((img, i) => {
      const bx = 2.65 + i * 1.53;
      slide.addShape(pptx.ShapeType.rect, {
        x: bx, y: y + 0.18, w: 1.18, h: 0.86,
        fill: { color: C.pale }, line: { color: C.line, width: 0.6 },
      });
      if (i % 2 === 0) {
        slide.addImage({
          path: img,
          x: bx + 0.23, y: y + 0.26, w: 0.72, h: 0.72,
          altText: `${entry[0]} ${labels[i]} proposal artwork`,
        });
      } else {
        slide.addImage({
          path: img,
          x: bx + 0.09, y: y + 0.51, w: 0.19, h: 0.19,
          altText: `${entry[0]} ${labels[i]} artwork at approximately native presentation size`,
        });
        slide.addImage({
          path: img,
          x: bx + 0.42, y: y + 0.28, w: 0.62, h: 0.62,
          altText: `${entry[0]} ${labels[i]} artwork enlarged for inspection`,
        });
      }
      slide.addText(labels[i], {
        x: bx, y: y + 1.03, w: 1.18, h: 0.16, margin: 0,
        fontFace: "Segoe UI", fontSize: 8.7, color: C.muted, align: "center",
      });
      if (i % 2 === 1) {
        slide.addText("native  |  enlarged", {
          x: bx, y: y + 1.18, w: 1.18, h: 0.13, margin: 0,
          fontFace: "Segoe UI", fontSize: 6.8, color: C.muted, align: "center",
        });
      }
    });
    slide.addText(row === 0 ? "One specimen; hilum + ureter" : row === 1 ? "Joined J silhouette" : "Full wedge; tucked gallbladder", {
      x: 9.15, y: y + 0.49, w: 2.9, h: 0.3, margin: 0,
      fontFace: "Segoe UI Semibold", fontSize: 12, color: C.blue,
    });
  });
  slide.addText("The 18 px variants are shown near native size and enlarged for inspection; proposal files remain textless and strict black-and-white where required.", {
    x: 1.1, y: 6.5, w: 11.1, h: 0.3, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 12.5, color: C.ink, align: "center",
  });
  addFooter(slide, 5, "Artwork release: https://github.com/ShuhanCS/medicalemoji/tree/codex/eligible-2026-slate/submissions/v1.7.0");
}

// Slide 6: role
{
  const slide = pptx.addSlide();
  addHeader(slide, "Microsoft’s role is technical review, not outcome-seeking", "Legitimate role");
  const roles = [
    ["Standards", "Confirm the correct Unicode venue and carry a bounded discussion only if Microsoft approves the review path."],
    ["Product + design", "Test the actual 18 × 18 px paradigms for recognition, accessibility, and plausible Segoe UI Emoji implementation."],
    ["Legal", "Clear the image-rights route and any statement about possible implementation before it appears in a submission."],
    ["Medical leadership", "Validate broad communication needs and keep the slate focused on general-purpose use."],
  ];
  roles.forEach((role, i) => {
    const x = 0.75 + i * 3.12;
    slide.addShape(pptx.ShapeType.roundRect, {
      x, y: 1.65, w: 2.86, h: 4.2, rectRadius: 0.05,
      fill: { color: i % 2 === 0 ? C.bluePale : C.tealPale },
      line: { color: i % 2 === 0 ? C.blue : C.teal, transparency: 72, width: 1 },
    });
    slide.addShape(pptx.ShapeType.ellipse, {
      x: x + 0.25, y: 1.98, w: 0.62, h: 0.62,
      fill: { color: i % 2 === 0 ? C.blue : C.teal }, line: { transparency: 100 },
    });
    slide.addText(String(i + 1), {
      x: x + 0.25, y: 2.1, w: 0.62, h: 0.22, margin: 0,
      fontFace: "Segoe UI Semibold", fontSize: 12, color: C.white, align: "center",
    });
    slide.addText(role[0], {
      x: x + 0.25, y: 2.76, w: 2.35, h: 0.43, margin: 0,
      fontFace: "Segoe UI Semibold", fontSize: 17, color: C.ink,
    });
    slide.addText(role[1], {
      x: x + 0.25, y: 3.28, w: 2.35, h: 1.8, margin: 0,
      fontFace: "Segoe UI", fontSize: 12.2, color: C.muted, fit: "shrink",
    });
  });
  slide.addText("Guardrail: request ordinary technical review. Do not imply Microsoft endorsement, implementation, or preferred treatment before approval.", {
    x: 1.0, y: 6.18, w: 11.3, h: 0.42, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 13, color: C.red, align: "center", fit: "shrink",
  });
  addFooter(slide, 6, "Unicode document guidance: https://www.unicode.org/pending/docsubmit.html");
}

// Slide 7: gate
{
  const slide = pptx.addSlide();
  addHeader(slide, "Run a 48-hour evidence and design gate", "Execution");
  const steps = [
    ["0–12h", "Route", "Name the Microsoft standards owner and confirm the individual-submission route."],
    ["13–36h", "Evidence", "Capture the four missing Ultrasound Google categories in a manual session on an approved network."],
    ["37–48h", "Design", "Cold-test the 18 × 18 px monitor-plus-probe paradigm and obtain product and legal clearance."],
  ];
  steps.forEach((s, i) => {
    const x = 0.85 + i * 4.14;
    slide.addShape(pptx.ShapeType.roundRect, {
      x, y: 1.8, w: 3.65, h: 3.15, rectRadius: 0.05,
      fill: { color: C.white }, line: { color: C.line, width: 0.8 }, shadow: shadow(),
    });
    statusPill(slide, s[0], x + 0.3, 2.15, 1.0, i === 0 ? C.bluePale : i === 1 ? C.amberPale : C.tealPale, i === 0 ? C.blue : i === 1 ? C.amber : C.teal);
    slide.addText(s[1], {
      x: x + 0.3, y: 2.85, w: 2.9, h: 0.42, margin: 0,
      fontFace: "Segoe UI Semibold", fontSize: 21, color: C.ink,
    });
    slide.addText(s[2], {
      x: x + 0.3, y: 3.52, w: 3.0, h: 1.25, margin: 0,
      fontFace: "Segoe UI", fontSize: 12.5, color: C.muted, fit: "shrink",
    });
  });
  slide.addShape(pptx.ShapeType.roundRect, {
    x: 1.35, y: 5.42, w: 10.6, h: 1.05, rectRadius: 0.05,
    fill: { color: C.redPale }, line: { color: C.red, transparency: 55, width: 0.8 },
  });
  slide.addText("Evidence capture is blocked on this network: Google Trends returns HTTP 429 and Google Search presents a CAPTCHA. Use a manual session on an approved network.", {
    x: 1.72, y: 5.7, w: 9.86, h: 0.5, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 12.5, color: C.red, align: "center", fit: "shrink",
  });
  addFooter(slide, 7, "Evidence requirements: https://www.unicode.org/emoji/proposals.html#evidence_of_frequency");
}

// Slide 8: request
{
  const slide = pptx.addSlide();
  slide.background = { color: C.navy };
  slide.addText("THREE DECISIONS", {
    x: 0.82, y: 0.65, w: 3.0, h: 0.28, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 11, charSpacing: 1.7, color: "8FC5FF",
  });
  slide.addText("What we need from Microsoft", {
    x: 0.82, y: 1.08, w: 7.7, h: 0.72, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 34, color: C.white,
  });
  const asks = [
    "Name one standards owner and one Windows/Segoe UI Emoji design owner.",
    "Confirm whether Ultrasound should proceed through the evidence gate, with CT Scan retained as the fallback.",
    "Authorize technical review only; keep authorship, endorsement, and implementation language pending explicit approval.",
  ];
  asks.forEach((a, i) => {
    const y = 2.2 + i * 1.15;
    slide.addShape(pptx.ShapeType.ellipse, {
      x: 0.9, y, w: 0.56, h: 0.56,
      fill: { color: C.blue }, line: { transparency: 100 },
    });
    slide.addText(String(i + 1), {
      x: 0.9, y: y + 0.1, w: 0.56, h: 0.22, margin: 0,
      fontFace: "Segoe UI Semibold", fontSize: 12, color: C.white, align: "center",
    });
    slide.addText(a, {
      x: 1.72, y: y - 0.02, w: 7.2, h: 0.64, margin: 0,
      fontFace: "Segoe UI", fontSize: 17, color: "E6EEF9", fit: "shrink",
    });
  });
  slide.addShape(pptx.ShapeType.roundRect, {
    x: 9.45, y: 1.28, w: 3.05, h: 4.95, rectRadius: 0.06,
    fill: { color: "132653" }, line: { color: "2B4C83", width: 1 },
  });
  slide.addText("REVIEW PACKET", {
    x: 9.82, y: 1.7, w: 2.3, h: 0.25, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 10, charSpacing: 1.3, color: "8FC5FF",
  });
  const packet = [
    "One-page decision brief",
    "Product/legal clearance sheet",
    "Artwork readiness board",
    "Selected proposal after gate",
    "Draft standards document marked for review",
  ];
  packet.forEach((item, i) => {
    slide.addText(item, {
      x: 9.82, y: 2.28 + i * 0.56, w: 2.28, h: 0.36, margin: 0,
      fontFace: "Segoe UI", fontSize: 12.2, color: C.white,
      bullet: { indent: 13 }, hanging: 3, fit: "shrink",
    });
  });
  slide.addText("Prepared for David Rhew and Microsoft internal review", {
    x: 0.82, y: 6.75, w: 5.6, h: 0.26, margin: 0,
    fontFace: "Segoe UI", fontSize: 11, color: "AFC7EA",
  });
}

pptx.writeFile({ fileName: OUT }).catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
