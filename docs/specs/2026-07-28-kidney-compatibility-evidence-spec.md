# Kidney Emoji Compatibility Evidence Spec

Status: evidence acquisition spec; no positive Compatibility claim has been approved

## Outcome

Turn Compatibility into a positive 2026 selection factor only if the team can document an existing kidney
pictograph on a popular system, show that people already use it frequently, and show that the absence of a
standard Unicode character causes an interoperability problem. Until all three points are documented, the
proposal should keep Compatibility as `Not applicable`.

The controlling Unicode guidance is:

https://www.unicode.org/emoji/proposals.html

## Why the current evidence is not enough

The verified CLDR annotation connects the English search keyword `kidney` to U+1FAD8 BEANS. That proves a search
and representation mismatch, and it belongs under Breaks new ground and Already representable. It does not by
itself show that a popular non-Unicode system already has a kidney emoji in high-frequency use, which is the
2026 test for formal Compatibility.

A screenshot showing that Windows or Teams search returns Beans would strengthen the search-failure case, but it
would still not satisfy Compatibility without an existing kidney pictograph and usage evidence.

## Qualifying evidence gates

All gates are required before changing Section G from `Not applicable`.

### Gate 1: Existing implementation

Document a kidney pictograph that already exists on a popular deployed system, such as Microsoft Teams custom
emoji, a shipping Microsoft product, or another major communication platform. The evidence must show:

- the system and released product surface;
- the kidney image and its exact searchable name or shortcode;
- whether it is a built-in, tenant-wide, or custom character;
- the date it became available; and
- who owns the image and whether it may be reproduced in the public proposal.

Microsoft Teams is a plausible evidence source because it supports tenant-wide custom emoji, makes them searchable
with standard emoji, and permits them in chats, channels, meetings, replies, reactions, and cross-tenant messages.
Product documentation:

https://learn.microsoft.com/en-us/microsoftteams/teams-custom-emojis

https://support.microsoft.com/en-us/teams/chat/use-custom-emoji-in-microsoft-teams

### Gate 2: High-frequency use

Provide reproducible usage evidence for that exact kidney pictograph. Preferred evidence, in order:

1. Product telemetry with a defined date range, total uses, distinct users or tenants, and an appropriate
   denominator.
2. An administrator export or audited message sample showing repeated organic use over time.
3. A public corpus of messages using the exact custom emoji or shortcode, with the collection method and date
   range disclosed.

Do not use endorsements, petitions, a newly organized usage campaign, or a screenshot of a single use as the
frequency evidence. Aggregated or de-identified counts are sufficient; no private message content should be
included.

### Gate 3: Interoperability failure

Show what happens when the existing pictograph crosses a boundary where a Unicode character would survive:

- sender and recipient use different tenants, products, operating systems, or export formats;
- the recipient sees a missing image, a tenant-only asset, plain text, an inaccessible shortcode, or a different
  character; and
- the same message would remain semantically intact if a Unicode Kidney character existed.

Capture both endpoints, product versions, date, and a short test protocol. Microsoft documents that Teams custom
emoji can be viewed in cross-tenant or federated scenarios but are not added to the recipient tenant's emoji menu;
that limitation is a testable interoperability hypothesis, not yet evidence of high-frequency kidney use.

### Gate 4: Public and reviewable record

The final proposal must contain dated screenshots, a citation or letter from the product owner describing the
measurement, and enough method detail for a reviewer to understand what was counted. Obtain permission to publish
the screenshots and aggregated data in a public PDF.

## Microsoft evidence request

Heena Purohit and David Rhew can route one tightly scoped request to the Teams, Windows emoji-panel, SwiftKey, or
Microsoft design/product owner:

1. Does a kidney emoji, reaction, sticker, or tenant-wide custom emoji already exist in a deployed Microsoft
   product or large tenant?
2. Can the owner provide a dated screenshot showing the pictograph, name, and search result?
3. Can the owner provide aggregated use or search counts for the exact pictograph over a defined 30- or 90-day
   period, with no message content or personal data?
4. What happens when it is sent across tenants or opened on a product that lacks the asset?
5. May the screenshot and aggregate figures be published in a Unicode proposal?

Peter Constable is a useful standards/product-routing contact, but a private opinion or endorsement is not a
substitute for the product screenshot and usage measurement.

## Proposal integration rule

If all gates pass, create a new packet version and replace Section G with a concise claim containing:

- the existing system and exact kidney pictograph;
- the measured usage and date range;
- the documented interoperability failure; and
- the dated screenshots and public source or authorized product-owner statement.

If any gate fails, keep Section G as `Not applicable`. Place a Windows or Teams search-failure screenshot, if
obtained, under Breaks new ground, Already representable, or Other Information. It can strengthen the user
experience case without being mislabeled as formal Compatibility.

## Decision deadline

Because the 2026 emoji intake closes at the end of 2026-07-31, only already-existing, immediately publishable
evidence should be used in this cycle. Do not manufacture a short pilot and describe it as organic high-frequency
use. If qualifying evidence cannot be obtained in time, file with Compatibility `Not applicable`; that factor is
not mandatory, and an accurate N/A is safer than an unsupported positive claim.
