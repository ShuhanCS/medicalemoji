/* eslint-disable @typescript-eslint/no-require-imports */
const pptxgen = require("pptxgenjs");
const path = require("path");

const pptx = new pptxgen();
pptx.layout = "LAYOUT_WIDE";
pptx.author = "Shuhan He";
pptx.company = "Medical Emoji Project";
pptx.subject = "Independent materials for Microsoft review of 2026 Medical Emoji proposals";
pptx.title = "Medical Emoji proposals for Microsoft review";
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
  green: "16866F",
  amber: "C98412",
  red: "B95049",
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
const R13 = path.join(ROOT, "submissions", "v1.3.0");
const R15 = path.join(ROOT, "submissions", "v1.5.0");
const R17 = path.join(ROOT, "submissions", "v1.7.0");
const OUT = path.join(__dirname, "Emoji-2026-External-Review-v7.pptx");

const assets = {
  ct: path.join(R13, "ct-scan", "images", "ct-scan_color_72x72_SUBMIT.png"),
  blood: path.join(R13, "blood-bag", "images", "blood-bag_color_72x72_SUBMIT.png"),
  pillbox: path.join(R13, "pill-box", "images", "pill-box_color_72x72_SUBMIT.png"),
  pillpack: path.join(R13, "pill-pack", "images", "pill-pack_color_72x72_SUBMIT.png"),
  weight: path.join(R13, "weight-scale", "images", "weight-scale_color_72x72_SUBMIT.png"),
  whitecell: path.join(R13, "white-blood-cell", "images", "white-blood-cell_color_72x72_SUBMIT.png"),
  inhaler: path.join(R13, "inhaler", "images", "inhaler_color_72x72_SUBMIT.png"),
  iv: path.join(R13, "iv-bag", "images", "iv-bag_color_72x72_SUBMIT.png"),
  cast: path.join(R13, "leg-cast", "images", "leg-cast_color_72x72_SUBMIT.png"),
  ultrasound: path.join(R15, "ultrasound", "images", "ultrasound_color_72x72_SUBMIT.png"),
  maze: path.join(R15, "maze", "images", "maze_color_72x72_SUBMIT.png"),
  firstaid: path.join(R15, "first-aid-kit", "images", "first-aid-kit_color_72x72_SUBMIT.png"),
  kidney: path.join(R17, "kidney", "images", "kidney_color_72x72_SUBMIT.png"),
  stomach: path.join(R17, "stomach", "images", "stomach_color_72x72_SUBMIT.png"),
  liver: path.join(R17, "liver", "images", "liver_color_72x72_SUBMIT.png"),
};

function shadow() {
  return { type: "outer", color: "000000", blur: 3, offset: 1, angle: 135, opacity: 0.1 };
}

function addHeader(slide, title, kicker) {
  slide.background = { color: C.pale };
  slide.addText(kicker.toUpperCase(), {
    x: 0.65, y: 0.34, w: 5.5, h: 0.24, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 10, charSpacing: 1.35, color: C.blue,
  });
  slide.addText(title, {
    x: 0.65, y: 0.68, w: 12.0, h: 0.58, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 28, color: C.ink, fit: "shrink",
  });
}

function addFooter(slide, index, source) {
  slide.addText(source, {
    x: 0.65, y: 7.02, w: 11.72, h: 0.22, margin: 0,
    fontFace: "Segoe UI", fontSize: 8.5, color: C.muted, fit: "shrink",
  });
  slide.addText(String(index), {
    x: 12.45, y: 7.02, w: 0.28, h: 0.22, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 9, color: C.muted, align: "right",
  });
}

function panel(slide, x, y, w, h, fill = C.white, line = C.line) {
  slide.addShape(pptx.ShapeType.roundRect, {
    x, y, w, h, rectRadius: 0.06,
    fill: { color: fill }, line: { color: line, width: 0.8 }, shadow: shadow(),
  });
}

function status(slide, text, x, y, w, fill, color) {
  slide.addShape(pptx.ShapeType.roundRect, {
    x, y, w, h: 0.32, rectRadius: 0.05,
    fill: { color: fill }, line: { color: fill, transparency: 100 },
  });
  slide.addText(text, {
    x, y: y + 0.025, w, h: 0.2, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 9, color, align: "center", fit: "shrink",
  });
}

function questionBar(slide, text, x, y, w, fill, color) {
  slide.addShape(pptx.ShapeType.roundRect, {
    x, y, w, h: 0.48, rectRadius: 0.05,
    fill: { color: fill }, line: { color: fill, transparency: 100 },
  });
  slide.addText(text, {
    x: x + 0.18, y: y + 0.09, w: w - 0.36, h: 0.26, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 10.2, color, align: "center", fit: "shrink",
  });
}

function iconLabel(slide, x, y, w, image, name, note, noteColor = C.muted) {
  panel(slide, x, y, w, 0.9);
  const compact = w < 2.0;
  const imageX = compact ? x + 0.10 : x + 0.16;
  const imageY = compact ? y + 0.2 : y + 0.14;
  const imageSize = compact ? 0.46 : 0.58;
  const textX = compact ? x + 0.66 : x + 0.86;
  const textWidth = w - (compact ? 0.75 : 1.02);
  slide.addImage({ path: image, x: imageX, y: imageY, w: imageSize, h: imageSize, altText: name });
  slide.addText(name, {
    x: textX, y: y + 0.14, w: textWidth, h: 0.32, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: compact ? 10.5 : 12, color: C.ink, fit: "shrink",
  });
  slide.addText(note, {
    x: textX, y: y + 0.5, w: textWidth, h: 0.23, margin: 0,
    fontFace: "Segoe UI", fontSize: compact ? 8.7 : 9.5, color: noteColor, fit: "shrink",
  });
}

function conceptCard(slide, x, y, w, h, image, name, label, body, accent, fill) {
  panel(slide, x, y, w, h, fill);
  slide.addShape(pptx.ShapeType.ellipse, {
    x: x + 0.28, y: y + 0.3, w: 1.12, h: 1.12,
    fill: { color: C.white }, line: { color: accent, width: 1.2 },
  });
  slide.addImage({ path: image, x: x + 0.48, y: y + 0.5, w: 0.72, h: 0.72, altText: name });
  slide.addText(label.toUpperCase(), {
    x: x + 1.65, y: y + 0.3, w: w - 1.95, h: 0.2, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 9.5, charSpacing: 1.0, color: accent,
  });
  slide.addText(name, {
    x: x + 1.65, y: y + 0.62, w: w - 1.95, h: 0.34, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 20, color: C.ink,
  });
  slide.addText(body, {
    x: x + 0.34, y: y + 1.68, w: w - 0.68, h: h - 1.96, margin: 0,
    fontFace: "Segoe UI", fontSize: 13.2, color: C.muted, valign: "top", fit: "shrink",
  });
}

// Slide 1: title
{
  const slide = pptx.addSlide();
  slide.background = { color: C.navy };
  slide.addShape(pptx.ShapeType.arc, {
    x: 8.65, y: -1.25, w: 5.9, h: 5.9, adjustPoint: 0.28, rotate: 28,
    fill: { color: C.blue, transparency: 70 }, line: { color: C.blue, transparency: 100 },
  });
  slide.addShape(pptx.ShapeType.arc, {
    x: 9.55, y: 3.4, w: 4.35, h: 4.35, adjustPoint: 0.28, rotate: 206,
    fill: { color: C.teal, transparency: 58 }, line: { color: C.teal, transparency: 100 },
  });
  slide.addText("MATERIALS FOR MICROSOFT REVIEW", {
    x: 0.85, y: 0.76, w: 5.5, h: 0.28, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 11, charSpacing: 1.55, color: "8FC5FF",
  });
  slide.addText("Medical Emoji proposals", {
    x: 0.85, y: 1.42, w: 8.2, h: 0.92, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 40, color: C.white, fit: "shrink",
  });
  slide.addText("A 2026 filing plan, two Unicode process questions, and the history behind them", {
    x: 0.85, y: 2.52, w: 7.65, h: 0.86, margin: 0,
    fontFace: "Segoe UI", fontSize: 21, color: "D7E4F7", fit: "shrink",
  });
  slide.addShape(pptx.ShapeType.roundRect, {
    x: 0.85, y: 4.0, w: 6.0, h: 1.3, rectRadius: 0.06,
    fill: { color: "132653" }, line: { color: "2B4C83", width: 1 },
  });
  const titleIcons = [assets.ct, assets.blood, assets.pillbox];
  titleIcons.forEach((image, index) => {
    slide.addShape(pptx.ShapeType.ellipse, {
      x: 1.18 + index * 1.05, y: 4.23, w: 0.82, h: 0.82,
      fill: { color: C.white }, line: { color: "88A5D6", width: 1 },
    });
    slide.addImage({ path: image, x: 1.32 + index * 1.05, y: 4.37, w: 0.54, h: 0.54 });
  });
  slide.addText("CT Scan and Blood Bag planned\nPill Box retained as the first alternate", {
    x: 4.42, y: 4.23, w: 2.05, h: 0.72, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 13, color: C.white, valign: "middle", fit: "shrink",
  });
  slide.addText("Prepared independently by Shuhan He  |  July 13, 2026", {
    x: 0.85, y: 6.73, w: 6.8, h: 0.26, margin: 0,
    fontFace: "Segoe UI", fontSize: 11.5, color: "AFC7EA",
  });
}

// Slide 2: plan and asks
{
  const slide = pptx.addSlide();
  addHeader(slide, "Current filing plan", "2026 intake");
  conceptCard(slide, 0.65, 1.5, 3.8, 3.5, assets.ct, "CT Scan", "Planned", "Strongest developed packet. Refresh 2020 evidence, confirm image ownership, and test the 18-pixel design against X-Ray and MRI.", C.blue, C.bluePale);
  conceptCard(slide, 4.77, 1.5, 3.8, 3.5, assets.blood, "Blood Bag", "Planned", "Complete evidence categories and a clear donation and transfusion use case. Refresh the evidence and test it beside IV Bag in black and white.", C.teal, C.tealPale);
  conceptCard(slide, 8.89, 1.5, 3.8, 3.5, assets.pillbox, "Pill Box", "First alternate", "The clearest weekly medication option in the portfolio. Its usage signal is weak, so reviewers may still favor the existing Pill emoji.", C.amber, C.amberPale);

  panel(slide, 0.65, 5.28, 12.04, 1.25, C.white);
  slide.addText("Two questions for Microsoft", {
    x: 0.95, y: 5.55, w: 2.45, h: 0.28, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 16, color: C.ink,
  });
  slide.addText("After submission, would Microsoft's Unicode representatives ask ESR to consider adding the proposals to an upcoming agenda through its normal review process?", {
    x: 3.65, y: 5.42, w: 4.05, h: 0.64, margin: 0,
    fontFace: "Segoe UI", fontSize: 12, color: C.muted, valign: "middle", fit: "shrink",
  });
  slide.addText("Would Microsoft's standards team review the paper and, if it merits UTC discussion, help revise it for submission?", {
    x: 8.02, y: 5.42, w: 4.28, h: 0.64, margin: 0,
    fontFace: "Segoe UI", fontSize: 12, color: C.muted, valign: "middle", fit: "shrink",
  });
  addFooter(slide, 2, "Filing window: https://www.unicode.org/emoji/proposals.html");
}

// Slide 3: full portfolio
{
  const slide = pptx.addSlide();
  addHeader(slide, "Full proposal portfolio", "Current status");

  slide.addText("CURRENT PLAN", { x: 0.68, y: 1.42, w: 2.8, h: 0.22, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 10, color: C.blue, charSpacing: 1.1 });
  iconLabel(slide, 0.65, 1.75, 3.08, assets.ct, "CT Scan", "planned after revision", C.blue);
  iconLabel(slide, 0.65, 2.82, 3.08, assets.blood, "Blood Bag", "planned after revision", C.teal);
  iconLabel(slide, 0.65, 3.89, 3.08, assets.pillbox, "Pill Box", "first alternate", C.amber);

  slide.addText("MORE EVIDENCE OR A STRONGER CASE NEEDED", { x: 4.02, y: 1.42, w: 5.65, h: 0.22, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 10, color: C.amber, charSpacing: 1.0 });
  const middle = [
    [assets.ultrasound, "Ultrasound", "4 exhibits missing"],
    [assets.weight, "Weight Scale", "2 Trends missing"],
    [assets.whitecell, "White Blood Cell", "2 Trends missing"],
    [assets.inhaler, "Inhaler", "Video + Trends missing"],
    [assets.iv, "IV Bag", "2 Trends missing"],
    [assets.cast, "Leg Cast", "comparators + design"],
    [assets.pillpack, "Pill Pack", "Trends + overlap"],
    [assets.maze, "Maze", "4 exhibits; 2 declines"],
    [assets.firstaid, "First Aid Kit", "4 exhibits missing"],
  ];
  middle.forEach((item, index) => {
    const col = index % 3;
    const row = Math.floor(index / 3);
    iconLabel(slide, 4.0 + col * 2.02, 1.75 + row * 1.07, 1.82, item[0], item[1], item[2], C.amber);
  });

  slide.addText("LATER-CYCLE CANDIDATES", { x: 10.18, y: 1.42, w: 2.5, h: 0.22, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 9.5, color: C.red, charSpacing: 0.8, fit: "shrink" });
  iconLabel(slide, 10.05, 1.75, 2.64, assets.kidney, "Kidney", "2022 decline", C.red);
  iconLabel(slide, 10.05, 2.82, 2.64, assets.stomach, "Stomach", "2022 decline", C.red);
  iconLabel(slide, 10.05, 3.89, 2.64, assets.liver, "Liver", "2022 decline", C.red);

  panel(slide, 0.65, 5.28, 12.04, 1.13, C.white);
  slide.addText("The portfolio includes 15 concepts at different stages. The notes identify the work remaining before each could be considered for filing.", {
    x: 0.95, y: 5.62, w: 11.42, h: 0.42, margin: 0,
    fontFace: "Segoe UI", fontSize: 13, color: C.ink, align: "center", fit: "shrink",
  });
  addFooter(slide, 3, "Proposal releases: https://github.com/ShuhanCS/medicalemoji/tree/codex/eligible-2026-slate/submissions");
}

// Slide 4: why the planned filings lead
{
  const slide = pptx.addSlide();
  addHeader(slide, "Why CT Scan and Blood Bag lead today", "Evidence and distinctiveness");
  conceptCard(slide, 0.65, 1.55, 5.78, 3.6, assets.ct, "CT Scan", "Best developed case", "The machine and procedure support appointment, preparation, results, and care-sequence uses that X-Ray does not fully express.", C.blue, C.bluePale);
  conceptCard(slide, 6.9, 1.55, 5.78, 3.6, assets.blood, "Blood Bag", "Strongest transfusion case", "Donation, transfusion, blood supply, and patient-care uses are more specific than Drop of Blood.", C.teal, C.tealPale);
  panel(slide, 0.65, 5.42, 12.04, 1.02, C.white);
  slide.addText("Before filing", { x: 0.95, y: 5.74, w: 1.35, h: 0.28, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 16, color: C.ink });
  slide.addText("Evidence\nRecapture the 2020 exhibits", { x: 2.65, y: 5.62, w: 2.55, h: 0.48, margin: 0, fontFace: "Segoe UI", fontSize: 11.5, color: C.muted, align: "center", fit: "shrink" });
  slide.addText("Rights\nState the ownership chain clearly", { x: 5.45, y: 5.62, w: 2.55, h: 0.48, margin: 0, fontFace: "Segoe UI", fontSize: 11.5, color: C.muted, align: "center", fit: "shrink" });
  slide.addText("Design\nTest the closest visual substitutes", { x: 8.25, y: 5.62, w: 3.15, h: 0.48, margin: 0, fontFace: "Segoe UI", fontSize: 11.5, color: C.muted, align: "center", fit: "shrink" });
  addFooter(slide, 4, "Requirements: https://www.unicode.org/emoji/proposals.html");
}

// Slide 5: direct pair comparisons
{
  const slide = pptx.addSlide();
  addHeader(slide, "Related concepts need direct comparison", "Two portfolio choices");

  panel(slide, 0.65, 1.55, 12.04, 2.18, C.white);
  slide.addText("Medication", { x: 0.95, y: 1.82, w: 1.35, h: 0.28, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 16, color: C.ink });
  slide.addImage({ path: assets.pillbox, x: 2.45, y: 1.85, w: 0.78, h: 0.78, altText: "Pill Box" });
  slide.addText("Pill Box", { x: 3.4, y: 1.82, w: 1.3, h: 0.26, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 15, color: C.green });
  slide.addText("Five evidence categories are present. The weekly organization and caregiver use are clearer, although Pill remains a strong substitute.", { x: 3.4, y: 2.18, w: 3.1, h: 0.82, margin: 0, fontFace: "Segoe UI", fontSize: 11.5, color: C.muted, fit: "shrink" });
  slide.addImage({ path: assets.pillpack, x: 6.95, y: 1.85, w: 0.78, h: 0.78, altText: "Pill Pack" });
  slide.addText("Pill Pack", { x: 7.9, y: 1.82, w: 1.4, h: 0.26, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 15, color: C.ink });
  slide.addText("Web Trends is missing, Image Trends uses the wrong comparator, and the 18-pixel image can resemble a keypad. Blister Pack may be the safer future name.", { x: 7.9, y: 2.18, w: 3.95, h: 0.82, margin: 0, fontFace: "Segoe UI", fontSize: 11.5, color: C.muted, fit: "shrink" });
  status(slide, "PILL BOX IS THE CURRENT ALTERNATE", 4.3, 3.2, 4.7, C.tealPale, C.green);

  panel(slide, 0.65, 4.02, 12.04, 2.18, C.white);
  slide.addText("Infusion", { x: 0.95, y: 4.29, w: 1.35, h: 0.28, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 16, color: C.ink });
  slide.addImage({ path: assets.blood, x: 2.45, y: 4.32, w: 0.78, h: 0.78, altText: "Blood Bag" });
  slide.addText("Blood Bag", { x: 3.4, y: 4.29, w: 1.5, h: 0.26, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 15, color: C.green });
  slide.addText("Five evidence categories are present, and donation and transfusion supply a specific public meaning.", { x: 3.4, y: 4.65, w: 3.1, h: 0.66, margin: 0, fontFace: "Segoe UI", fontSize: 11.5, color: C.muted, fit: "shrink" });
  slide.addImage({ path: assets.iv, x: 6.95, y: 4.32, w: 0.78, h: 0.78, altText: "IV Bag" });
  slide.addText("IV Bag", { x: 7.9, y: 4.29, w: 1.4, h: 0.26, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 15, color: C.ink });
  slide.addText("Both Trends exhibits are missing, and its black-and-white silhouette is difficult to distinguish from Blood Bag.", { x: 7.9, y: 4.65, w: 3.95, h: 0.66, margin: 0, fontFace: "Segoe UI", fontSize: 11.5, color: C.muted, fit: "shrink" });
  status(slide, "BLOOD BAG IS THE CURRENT FILING CHOICE", 4.3, 5.67, 4.7, C.tealPale, C.green);
  addFooter(slide, 5, "Full slate: https://github.com/ShuhanCS/medicalemoji/tree/codex/eligible-2026-slate/submissions");
}

// Slide 6: promising alternatives
{
  const slide = pptx.addSlide();
  addHeader(slide, "Additional candidates could move forward after evidence work", "Alternatives for review");
  conceptCard(slide, 0.65, 1.55, 3.8, 3.8, assets.ultrasound, "Ultrasound", "Promising", "The strongest recent Books signal in the portfolio, with broad clinical and personal uses. Four Google exhibits and an 18-pixel probe test remain.", C.green, C.tealPale);
  conceptCard(slide, 4.77, 1.55, 3.8, 3.8, assets.weight, "Weight Scale", "Promising", "Broad medical and everyday uses, with a strong small-size image. Web and Image Trends remain outstanding.", C.blue, C.bluePale);
  conceptCard(slide, 8.89, 1.55, 3.8, 3.8, assets.inhaler, "Inhaler", "Worth another look", "A distinct medication route with familiar carry, refill, and rescue uses. Video, Trends, and global recognition remain open questions.", C.amber, C.amberPale);
  panel(slide, 0.65, 5.62, 12.04, 0.82, C.white);
  slide.addText("Microsoft's review can help determine whether one of these should replace a planned filing. Each would first require the evidence and design work shown above.", {
    x: 1.2, y: 5.88, w: 10.9, h: 0.28, margin: 0,
    fontFace: "Segoe UI Semibold", fontSize: 12.5, color: C.ink, align: "center", fit: "shrink",
  });
  addFooter(slide, 6, "Requirements: https://www.unicode.org/emoji/proposals.html");
}

// Slide 7: routes
{
  const slide = pptx.addSlide();
  addHeader(slide, "Two Unicode routes serve different purposes", "Process");

  panel(slide, 0.65, 1.55, 12.04, 2.15, C.bluePale, "B9CCF4");
  slide.addText("INDIVIDUAL EMOJI", { x: 0.95, y: 1.84, w: 1.62, h: 0.22, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 10, color: C.blue, charSpacing: 1.0 });
  const route1 = [
    ["CT Scan / Blood Bag", "Revise before filing"],
    ["Emoji Submission Form", "Required 2026 route"],
    ["ESR review", "Unicode controls timing"],
  ];
  route1.forEach((item, index) => {
    const x = 2.75 + index * 3.05;
    panel(slide, x, 1.83, 2.42, 1.15, C.white, "B9CCF4");
    slide.addText(item[0], { x: x + 0.18, y: 2.08, w: 2.06, h: 0.26, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 13, color: C.ink, align: "center", fit: "shrink" });
    slide.addText(item[1], { x: x + 0.18, y: 2.45, w: 2.06, h: 0.22, margin: 0, fontFace: "Segoe UI", fontSize: 9.5, color: C.muted, align: "center", fit: "shrink" });
    if (index < route1.length - 1) {
      slide.addShape(pptx.ShapeType.chevron, { x: x + 2.54, y: 2.18, w: 0.32, h: 0.42, fill: { color: C.blue }, line: { color: C.blue, transparency: 100 } });
    }
  });
  questionBar(slide, "Would Microsoft ask ESR to consider an upcoming agenda discussion through its normal review process?", 2.9, 3.03, 7.8, C.white, C.blue);

  panel(slide, 0.65, 4.05, 12.04, 2.15, C.tealPale, "B5DED5");
  slide.addText("TECHNICAL DISCUSSION", { x: 0.95, y: 4.34, w: 1.72, h: 0.22, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 10, color: C.teal, charSpacing: 0.9 });
  const route2 = [
    ["Revised discussion paper", "Microsoft determines its position"],
    ["Unicode document submission", "If Microsoft chooses"],
    ["L2 number if accepted", "UTC may discuss or refer"],
  ];
  route2.forEach((item, index) => {
    const x = 2.75 + index * 3.05;
    panel(slide, x, 4.33, 2.42, 1.15, C.white, "B5DED5");
    slide.addText(item[0], { x: x + 0.18, y: 4.58, w: 2.06, h: 0.26, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 13, color: C.ink, align: "center", fit: "shrink" });
    slide.addText(item[1], { x: x + 0.18, y: 4.95, w: 2.06, h: 0.22, margin: 0, fontFace: "Segoe UI", fontSize: 9.5, color: C.muted, align: "center", fit: "shrink" });
    if (index < route2.length - 1) {
      slide.addShape(pptx.ShapeType.chevron, { x: x + 2.54, y: 4.68, w: 0.32, h: 0.42, fill: { color: C.teal }, line: { color: C.teal, transparency: 100 } });
    }
  });
  questionBar(slide, "Would Microsoft review the paper and, if it merits UTC discussion, help revise it for submission?", 2.9, 5.53, 7.8, C.white, C.teal);
  addFooter(slide, 7, "Routes: https://www.unicode.org/emoji/proposals.html  |  https://www.unicode.org/pending/docsubmit.html");
}

// Slide 8: history
{
  const slide = pptx.addSlide();
  addHeader(slide, "Apple, Anatomical Heart, and Lungs", "Relevant history");
  panel(slide, 0.65, 1.55, 3.85, 4.9, C.white);
  slide.addText("9", { x: 0.98, y: 1.8, w: 1.05, h: 0.78, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 48, color: C.blue, align: "center" });
  slide.addText("accessibility emoji", { x: 2.05, y: 1.96, w: 1.92, h: 0.3, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 17, color: C.ink, fit: "shrink" });
  slide.addText("Apple L2/18-080  |  March 2018", { x: 1.0, y: 2.68, w: 3.12, h: 0.25, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 11.5, color: C.muted, align: "center" });
  const appleAreas = ["Blind / Low Vision", "Deaf / Hard of Hearing", "Physical Motor", "Hidden Disabilities"];
  appleAreas.forEach((area, index) => {
    const y = 3.18 + index * 0.58;
    slide.addShape(pptx.ShapeType.roundRect, { x: 1.0, y, w: 3.12, h: 0.42, rectRadius: 0.05, fill: { color: index % 2 === 0 ? C.bluePale : C.tealPale }, line: { color: C.line, width: 0.6 } });
    slide.addText(area, { x: 1.18, y: y + 0.11, w: 2.76, h: 0.18, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 10.5, color: C.ink, align: "center", fit: "shrink" });
  });
  slide.addText("Apple presented a finite starting set and addressed Unicode's selection factors. It used the emoji-proposal process available in 2018.", { x: 1.0, y: 5.7, w: 3.12, h: 0.48, margin: 0, fontFace: "Segoe UI", fontSize: 10.8, color: C.muted, align: "center", fit: "shrink" });

  const events = [
    ["2018", "Apple accessibility proposal", "Nine related concepts, organized as a finite set and argued under the selection factors used at that time."],
    ["2019", "Anatomical Heart and Lungs", "Christian Kamkoff, Shuhan He, and Melissa Thermidor submitted separate proposals. Unicode later encoded both characters."],
    ["2026", "Current process", "Emoji candidates use the official form. A separate discussion paper can raise a coverage and guidance question."],
  ];
  events.forEach((event, index) => {
    const y = 1.62 + index * 1.58;
    slide.addShape(pptx.ShapeType.ellipse, { x: 5.02, y: y + 0.16, w: 0.72, h: 0.72, fill: { color: index === 2 ? C.teal : C.blue }, line: { color: C.white, width: 2 } });
    slide.addText(event[0], { x: 5.02, y: y + 0.37, w: 0.72, h: 0.18, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 9.5, color: C.white, align: "center" });
    if (index < events.length - 1) {
      slide.addShape(pptx.ShapeType.line, { x: 5.38, y: y + 0.9, w: 0, h: 0.72, line: { color: "AAB5C5", width: 2 } });
    }
    slide.addText(event[1], { x: 6.08, y: y + 0.08, w: 3.0, h: 0.32, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 17, color: C.ink, fit: "shrink" });
    slide.addText(event[2], { x: 6.08, y: y + 0.55, w: 6.0, h: 0.6, margin: 0, fontFace: "Segoe UI", fontSize: 11.5, color: C.muted, fit: "shrink" });
  });
  panel(slide, 4.82, 6.16, 7.86, 0.46, C.amberPale, "E9D39D");
  slide.addText("For 2026, the individual proposals and the discussion paper follow separate submission routes.", { x: 5.1, y: 6.28, w: 7.3, h: 0.2, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 11.5, color: C.ink, align: "center", fit: "shrink" });
  addFooter(slide, 8, "Sources: https://www.unicode.org/L2/L2018/18080-accessibility-emoji.pdf  |  https://www.unicode.org/L2/L2019/19149-lung-emoji.pdf  |  https://www.unicode.org/L2/L2019/19150-heart-emoji.pdf");
}

// Slide 9: questions and packet
{
  const slide = pptx.addSlide();
  slide.background = { color: C.navy };
  slide.addText("QUESTIONS FOR MICROSOFT REVIEWERS", { x: 0.82, y: 0.66, w: 5.6, h: 0.26, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 11, charSpacing: 1.45, color: "8FC5FF" });
  slide.addText("Questions for Microsoft", { x: 0.82, y: 1.18, w: 7.2, h: 0.62, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 32, color: C.white });
  const asks = [
    "Are CT Scan and Blood Bag the right filing choices, or should Pill Box replace one?",
    "Do the images remain clear at 18 pixels and in black and white?",
    "After submission, would Microsoft ask ESR to consider an upcoming agenda discussion through its normal review process?",
    "Would Microsoft review the discussion paper and, if it merits UTC discussion, help revise it for submission?",
  ];
  asks.forEach((ask, index) => {
    const y = 2.14 + index * 0.91;
    slide.addShape(pptx.ShapeType.ellipse, { x: 0.92, y, w: 0.48, h: 0.48, fill: { color: index < 2 ? C.blue : C.teal }, line: { color: C.white, transparency: 100 } });
    slide.addText(String(index + 1), { x: 0.92, y: y + 0.14, w: 0.48, h: 0.16, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 10, color: C.white, align: "center" });
    slide.addText(ask, { x: 1.65, y: y - 0.02, w: 6.65, h: 0.52, margin: 0, fontFace: "Segoe UI", fontSize: 15, color: "E4EBF7", valign: "middle", fit: "shrink" });
  });

  slide.addShape(pptx.ShapeType.roundRect, { x: 8.65, y: 1.22, w: 3.75, h: 4.8, rectRadius: 0.06, fill: { color: "132653" }, line: { color: "2B4C83", width: 1 } });
  slide.addText("ATTACHED MATERIALS", { x: 9.0, y: 1.58, w: 3.05, h: 0.22, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 10, charSpacing: 1.15, color: "8FC5FF" });
  const packet = [
    "External review deck",
    "Proposal review brief",
    "Technical and rights questions",
    "Health-coverage discussion draft",
    "CT Scan working proposal",
    "Blood Bag working proposal",
    "Pill Box working proposal",
  ];
  packet.forEach((item, index) => {
    slide.addShape(pptx.ShapeType.ellipse, { x: 9.03, y: 2.1 + index * 0.48, w: 0.16, h: 0.16, fill: { color: C.teal }, line: { color: C.white, transparency: 100 } });
    slide.addText(item, { x: 9.35, y: 2.04 + index * 0.48, w: 2.55, h: 0.24, margin: 0, fontFace: "Segoe UI", fontSize: 12, color: C.white, fit: "shrink" });
  });
  slide.addText("Prepared independently by Shuhan He\nMicrosoft participation requires its own review and approval.", { x: 9.0, y: 5.42, w: 3.05, h: 0.5, margin: 0, fontFace: "Segoe UI", fontSize: 10.5, color: "C6D5EC", align: "center", fit: "shrink" });
  slide.addText("Unicode guidance: https://www.unicode.org/emoji/proposals.html", { x: 0.82, y: 6.81, w: 7.2, h: 0.22, margin: 0, fontFace: "Segoe UI", fontSize: 9.5, color: "AFC7EA" });
  slide.addText("9", { x: 12.05, y: 6.81, w: 0.28, h: 0.22, margin: 0, fontFace: "Segoe UI Semibold", fontSize: 9, color: "AFC7EA", align: "right" });
}

pptx.writeFile({ fileName: OUT }).catch((error) => {
  console.error(error);
  process.exit(1);
});
