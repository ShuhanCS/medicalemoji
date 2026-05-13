# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.8.0] - 2026-05-13

### Added
- Added kidney emoji packet `v0.6.0` with frequency screenshot attempts, evidence-status review, and 18x18 visual-review evidence.

## [0.7.0] - 2026-05-13

### Added
- Added kidney emoji packet `v0.5.0` aligned to the reusable approval rubric, including packet-specific score, must-pass gate status, and circulation/submission criteria.

## [0.6.0] - 2026-05-13

### Added
- Added a reusable emoji proposal approval rubric covering must-pass gates, scoring, Unicode requirements, review criteria, and packet controls.

## [0.5.0] - 2026-05-13

### Added
- Added kidney emoji packet `v0.4.0` with owned artwork, Alla Shamanska / ConductScience credit, draft image sizes, and stronger global/universal framing.

## [0.4.0] - 2026-05-13

### Added
- Added kidney emoji packet `v0.3.0` with the first full narrative proposal draft for review and circulation.

## [0.3.0] - 2026-05-13

### Added
- Added kidney emoji packet `v0.2.0` with a 100 percent submission-readiness checklist, scoring gates, and execution log.

## [0.2.9] - 2026-05-13

### Added
- Created the first synchronized preliminary kidney emoji submission packet under `submissions/v0.1.0`.

## [0.2.8] - 2026-05-13

### Added
- Documented synchronized submission packet semantic versioning and required packet manifests in the README.

## [0.2.7] - 2026-05-13

### Added
- Linked current supporter cards to recovered old WordPress support letters and article references.
- Converted image-only kidney support letters to PDF files for stable current-site document links.

## [0.2.6] - 2026-05-13

### Fixed
- Rebuilt the site favicon from the anatomical-heart logo image used in the header.
- Updated press cards to link directly to the supplied article URLs.
- Replaced the personal Gmail `mailto:` contact flow with a captcha-protected server contact form that defaults to `info@conductscience.com`.
- Added the EbVAS JAMA citation and Google Scholar citing-articles link to the Visual Analogue Scale page.

## [0.2.5] - 2026-05-13

### Added
- Recovered old WordPress kidney support-letter assets from the legacy GliaServer/InMotion copy of `medicalemoji.org`.
- Added old WordPress recovery notes, support-letter inventory, prior proposal review, and an expanded kidney emoji working proposal draft.

## [0.2.4] - 2026-05-13

### Changed
- Replaced the template README with a Medical Emoji submission tracker covering current Unicode submission links, candidate status, reeligibility planning dates, and next steps.

## [0.2.3] - 2026-05-13

### Added
- Kidney emoji decline-date and submission update with current Unicode submission URLs, template requirements, and detailed coordination email draft.

## [0.2.2] - 2026-05-13

### Added
- Kidney emoji 2026 submission project with updated Unicode timeline, guidelines, fact base, evidence checklist, and proposal outline.

## [0.2.1] - 2026-05-13

### Added
- Kidney emoji Unicode resubmission audit and recommended email reply.

## [0.2.0] - 2026-03-28

### Added
- Multi-platform AI agent support: Claude Code, Codex CLI, OpenCode, GitHub Copilot, Cursor, Windsurf, Gemini CLI, Cline/Roo Code, Continue, Amazon Q, Augment Code, Aider
- Platform-specific instruction files and `/clone-website` skill for each supported agent
- `scripts/sync-agent-rules.sh` to regenerate platform instruction files from AGENTS.md
- `scripts/sync-skills.mjs` to regenerate `/clone-website` skill across all platforms
- GEMINI.md for Gemini CLI configuration
- Supported Platforms table in README
- "Updating for Other Platforms" documentation section in README

### Changed
- README now describes the project as multi-agent (Claude Code recommended, not required)
- AGENTS.md updated with sync script reminders

## [0.1.1] - 2026-03-28

### Added
- Bug report and feature request issue templates
- Pull request template with checklist
- CHANGELOG.md following Keep a Changelog format
- Package.json metadata (description, repository, homepage, keywords, engines)

### Fixed
- LICENSE copyright holder now attributed to JCodesMore

## [0.1.0] - 2026-03-28

### Added
- Initial template scaffold for website reverse-engineering with Claude Code
- `/clone-website` skill for full-site cloning pipeline
- `/build-from-spec` and `/customize` skills
- Parallel builder agents with git worktree isolation
- Chrome MCP integration for design token extraction
- Comprehensive inspection guide and project structure documentation
- Next.js 16 + shadcn/ui + Tailwind CSS v4 base scaffold
- MIT license
- README with badges, demo section, quick start, and star history
