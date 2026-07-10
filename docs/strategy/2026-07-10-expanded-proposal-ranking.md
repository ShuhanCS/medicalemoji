# 2026 Medical Emoji expanded slate: decision brief

Date: 2026-07-10
Audience: Shuhan He and Microsoft internal reviewers
Decision: Choose one lead concept for the 2026-07-31 Unicode intake and retain one operational fallback.

## Recommendation

**Run an immediate evidence and design sprint on Ultrasound. If its four missing Google screenshots confirm
the strong Google Books signal, make it the Microsoft lead. Keep CT Scan as the filing-ready fallback.**

Ultrasound is the highest-upside addition because it appears novel in the public Unicode request record, has
a recent Google Books signal approximately 1.70 times Unicode's `elephant` comparator, supports broad
personal and clinical communication, and has a clear monitor-plus-probe form. CT Scan remains the safer
operational choice because its packet already includes all five evidence categories.

Do not file the full slate. A focused product decision is easier to support, reduces open-ended-category risk,
and gives Microsoft's design and legal owners one concrete paradigm to assess.

## Ranked slate

| Rank | Concept | Public-record type | Packet readiness | Main strength | Main risk | Call |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Ultrasound | No matching public row | Four Google captures missing | Novel public-sheet concept; recent Ngram approximately 1.70x `elephant`; distinct monitor and probe | Must prove Search/Video/Trends usage and avoid pregnancy-only depiction | Evidence sprint; lead if passed |
| 2 | CT Scan | Re-eligible resubmission | Complete | Strong complete packet; clear appointment, procedure, and results uses | Must distinguish from X-Ray; resubmission baggage | Filing-ready fallback |
| 3 | Weight Scale | Re-eligible resubmission | Trends incomplete | Broad health, fitness, luggage, shipping, and veterinary use | Missing compliant Trends; Balance Scale neighbor | Hold behind lead/fallback |
| 4 | Maze | Re-eligible; declined twice | Four Google captures missing | Broad puzzle, path, complexity, and navigation meanings; iconic form | Two prior declines; current Ngram approximately 0.67x `elephant` | Evidence reserve |
| 5 | Blood Bag | Re-eligible resubmission | Complete | Donation, transfusion, supply, and blood-bank meanings | Drop of Blood is a plausible substitute | Complete reserve |
| 6 | First Aid Kit | No matching public row | Four Google captures missing | Novel public-sheet concept; immediately recognizable preparedness object | Low books signal; Bandage, Medical Symbol, and Toolbox substitute argument | Hold pending unusually strong current data |
| 7 | White Blood Cell | Re-eligible resubmission | Trends incomplete | Immunity, laboratory, research, and education uses | Can read as Microbe or a generic cell | Hold |
| 8 | Inhaler | Re-eligible resubmission | Video and Trends incomplete | Distinct routine, rescue, reminder, travel, and refill uses | 2018 recognition concern; incomplete global evidence | Hold |
| 9 | Pill Box | Re-eligible resubmission | Complete | Recurring medication organization and reminder uses | Pill substitute; overlaps Pill Pack; weak Ngram and Trends | Hold |
| 10 | IV Bag | Re-eligible resubmission | Trends incomplete | Infusion, fluids, hydration, and treatment meanings | Similar to Blood Bag; Syringe and Droplet cover part of the space | Hold |
| 11 | Leg Cast | Re-eligible resubmission | Trends incomplete | Familiar injury and recovery state | Leg plus Bandage substitute; modifier complexity | Hold |
| 12 | Pill Pack | Re-eligible resubmission | Trends incomplete | Finite course, remaining supply, and sealed doses | Overlaps Pill and Pill Box; weak independent case | Do not file this round |

## The lead/fallback test

Ultrasound becomes the lead only if all four conditions are satisfied:

1. Fresh Google Search and Video screenshots show a large, relevant result set.
2. Worldwide Web and Image Trends against `elephant` show sustained use rather than a narrow event spike.
3. Microsoft design reviewers agree that the probe remains recognizable at 18x18 and the monitor does not
   read as a generic computer.
4. Microsoft Legal accepts the original CC0 artwork route and any anticipated-implementation language.

If one of those conditions fails or cannot be completed in time, advance CT Scan. Do not wait past a defined
internal cutoff and lose the filing window.

## Portfolio conflicts

- **Ultrasound versus CT Scan:** file one lead imaging proposal unless Microsoft expressly decides that the
  evidence and implementation case for both is independently compelling.
- **Maze:** lead with puzzles, paths, navigation, choice, complexity, and escape. Neuroscience is a secondary
  sequence, not a cause argument.
- **First Aid Kit:** keep the generic white cross on green. Do not use a protected red cross or red crescent
  emblem, and do not characterize the case as signage.
- **Blood Bag versus IV Bag:** file no more than one unless independent recognition testing resolves their
  related monochrome silhouettes.
- **Pill Box versus Pill Pack:** do not file both; their medication-management uses overlap.

## What to ask Microsoft for

1. A Windows/Segoe UI Emoji product-owner decision on Ultrasound as the conditional lead and CT Scan as the
   fallback.
2. A Fluent Emoji or Windows design review of both paradigms at 18x18 and in black-and-white.
3. Legal clearance for the CC0 artwork route and narrowly written anticipated-implementation language.
4. Routing through Microsoft's Unicode standards owner without asking for a preferred Unicode review
   outcome.

The Kidney, Stomach, and Liver proposals declined on 2022-11-04 remain ineligible for the intake closing
2026-07-31. They should remain future assets and should not consume the Monday decision window.

## Source record

Unicode proposal guidance:

https://www.unicode.org/emoji/proposals.html

Unicode Emoji Proposals Status:

https://www.unicode.org/emoji/emoji-proposals-status.html

Three-concept public-status audit:

https://github.com/ShuhanCS/medicalemoji/blob/codex/eligible-2026-slate/docs/research/2026-07-10-maze-ultrasound-first-aid-status.md

Proposal releases:

https://github.com/ShuhanCS/medicalemoji/tree/codex/eligible-2026-slate/submissions/v1.3.0

https://github.com/ShuhanCS/medicalemoji/tree/codex/eligible-2026-slate/submissions/v1.4.0
