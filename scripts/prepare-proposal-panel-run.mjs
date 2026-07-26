import { createHash } from "node:crypto";
import { mkdir, readFile, writeFile } from "node:fs/promises";
import { basename, dirname, relative, resolve } from "node:path";
import { execFileSync } from "node:child_process";

const args = new Map();
for (let index = 2; index < process.argv.length; index += 1) {
  const token = process.argv[index];
  if (!token.startsWith("--")) continue;
  const value = process.argv[index + 1];
  if (!value || value.startsWith("--")) {
    throw new Error(`Missing value for ${token}`);
  }
  args.set(token.slice(2), value);
  index += 1;
}

const proposal = args.get("proposal");
const artifactArg = args.get("artifact");
const packageVersion = args.get("package") ?? "unversioned";
const guidelineDate = args.get("guideline-date");

if (!proposal || !artifactArg || !guidelineDate) {
  throw new Error(
    "Usage: npm run panel:prepare -- --proposal <name> --artifact <path> --guideline-date YYYY-MM-DD [--package <version>] [--output <path>]",
  );
}

const repositoryRoot = resolve(import.meta.dirname, "..");
const artifact = resolve(repositoryRoot, artifactArg);
const templatePath = resolve(repositoryRoot, "docs/proposals/review-panel/REVIEW-TEMPLATE.md");
const relativeArtifact = relative(repositoryRoot, artifact).replaceAll("\\", "/");

if (relativeArtifact.startsWith("../") || relativeArtifact === "..") {
  throw new Error("Artifact must be inside the repository");
}

if (!artifact.toLowerCase().endsWith(".pdf")) {
  throw new Error("Panel artifact must be the reviewer-facing PDF");
}

const dirtyStatus = execFileSync("git", ["status", "--porcelain"], {
  cwd: repositoryRoot,
  encoding: "utf8",
}).trim();
if (dirtyStatus) {
  throw new Error("Commit or clean the worktree before freezing a panel run");
}

const artifactBytes = await readFile(artifact);
const sha256 = createHash("sha256").update(artifactBytes).digest("hex");
const generatedUtc = new Date().toISOString();
const safeProposal = proposal.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
const timestamp = generatedUtc.replace(/[:.]/g, "-");
const defaultOutput = resolve(
  repositoryRoot,
  `docs/proposals/review-panel/runs/${timestamp}-${safeProposal}.md`,
);
const output = resolve(repositoryRoot, args.get("output") ?? defaultOutput);
const gitCommit = execFileSync("git", ["rev-parse", "HEAD"], {
  cwd: repositoryRoot,
  encoding: "utf8",
}).trim();

const replacements = new Map([
  ["{{PROPOSAL}}", proposal],
  ["{{RUN_ID}}", `${safeProposal}-${sha256.slice(0, 12)}`],
  ["{{ARTIFACT}}", relativeArtifact],
  ["{{SHA256}}", sha256],
  ["{{BYTES}}", String(artifactBytes.byteLength)],
  ["{{PACKAGE}}", packageVersion],
  ["{{GIT_COMMIT}}", gitCommit],
  ["{{GENERATED_UTC}}", generatedUtc],
  ["{{GUIDELINE_DATE}}", guidelineDate],
]);

let review = await readFile(templatePath, "utf8");
for (const [placeholder, value] of replacements) {
  review = review.replaceAll(placeholder, value);
}

await mkdir(dirname(output), { recursive: true });
await writeFile(output, review, { encoding: "utf8", flag: "wx" });

console.log(`Prepared ${relative(repositoryRoot, output).replaceAll("\\", "/")}`);
console.log(`Artifact ${basename(artifact)} SHA-256 ${sha256}`);
