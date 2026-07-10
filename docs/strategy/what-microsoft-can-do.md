# What Microsoft can do that Shuhan cannot

Assumption: Shuhan files the emoji proposals himself, as an individual, because
[the submission form requires it](https://forms.gle/6KSiYHrUdBkTMNaB8). The question is what Microsoft
contributes that changes the odds, rather than what looks impressive.

Every item below is something an individual submitter structurally cannot supply.

---

## The two named reasons a good proposal gets declined

From Unicode's own FAQ, verbatim:[^1]

> "Various factors may cause a **well-formed** proposal to be declined, including **lack of compelling
> evidence for popularity as an emoji** and **lack of anticipated support by major vendors**."

And:

> "Emoji are useful only if they are broadly deployed by major vendors. If they are not, the Unicode
> Standard should not be burdened with emoji-like pictographic symbols that are never 'emojified' by major
> vendors."

So a proposal that is already well-formed fails for exactly two reasons. **Microsoft can speak to both.**
Shuhan can speak to neither.

---

## 1. Anticipated vendor support. The highest-value thing Microsoft owns

Microsoft ships **Segoe UI Emoji** on every Windows device. It is, by any definition Unicode uses, a major
vendor.

A written statement from Rhew's organization that Microsoft intends to implement the proposed characters in
Segoe UI Emoji directly removes one of the two named decline reasons.

**No proposal in our corpus has ever carried one.** I searched all 55 winners and all 29 losers. The word
"vendor" appears only in discussions of how vendors *draw* existing emoji, never as a commitment to ship. A
vendor commitment letter would be novel, on-point, and impossible for an individual submitter to obtain.

This is the ask. It is not a favour to a colleague, it is a statement of product intent, and it belongs in
`Other Information` of the proposal and in a short covering letter.

## 2. Artwork whose licence is already clean

A missing or unclear image licence is an **automatic rejection**.[^2] So is artwork containing text, digits
or barcodes.[^2] Our existing candidate art fails both tests: the blood bag has a label, the IV bag has a
barcode, the pill box has weekday letters, the weight scale has a digital readout.

Microsoft already runs [`microsoft/fluentui-emoji`](https://github.com/microsoft/fluentui-emoji), an
MIT-licensed public emoji set. Microsoft design can originate textless glyphs at 18×18 and 72×72, in colour
and black and white, and grant the irrevocable perpetual licence the Consortium requires. The submitter
warrants the rights; a corporate design team makes that warranty true.

An individual physician cannot solve this. A design organization solves it in a week.

## 3. A seat in the room where the proposals die

Every one of the fourteen medical concepts was declined inside the **Emoji Standard and Research Working
Group**, without ever reaching the UTC, leaving no public record. See
[`unicode-map-and-strategy.md`](unicode-map-and-strategy.md).

Member companies staff Unicode's working groups. Google's Jennifer Daniel chairs ESR. Apple's Ned Holbrook
co-edits UTS #51. **Whether Microsoft has anyone inside ESR is not published**, and cannot be discovered
from outside. Only Chowdhary or Constable can answer it.

This is the highest-leverage, lowest-cost question in the entire project, and it costs one email.

## 4. First-party frequency evidence

The five mandated frequency sources are Google properties.[^2] They stay mandatory. But winners routinely
add sources nobody asked for, and Orca's Wikipedia pageviews are a good example.

**Microsoft owns Bing.** It can supply real query volumes rather than screenshots of a results count. It has
already published, in *Nature Health*, the largest measurement of how people raise health in a text
interface.[^3] Both are supplementary evidence for `Expected usage level` that an individual cannot generate.

State plainly what it is and is not: it measures that people discuss health constantly. It does not measure
that anyone would type a kidney. Presenting it as the frequency case would repeat the 2022 mistake.

## 5. A delegate filing on the record

Members file feedback documents on emoji candidates. These get L2 numbers and are read. When a proposal
reaches ESR review, a Microsoft delegate can file a short document supporting it, and that document is
member business rather than a proposal the committee *"is not obliged to consider."*[^4]

Constable's `L2/16-228` is the shape: four named Microsoft authors, and a body that opens *"Microsoft would
like to see…"*.

## 6. The vote, last and least

Only about four and a half voting members attend the UTC regularly, and Microsoft is one of them.[^5] But
the vote happens only if ESR advances the proposal. **The vote is worthless until item 3 is solved.**

---

## What Microsoft should not do first

**The Health category document does not touch either named decline reason.** Grouping is presentation, the
groups are labelled *"illustrative"* in Unicode's own data file, and no selection factor mentions the
category. It is a good long-term correctness argument and a poor opening move. Filing it first spends
Microsoft's first ask on the one thing that cannot approve an emoji.

## The ethical line

Peter Constable chairs the UTC on behalf of the Consortium, not on behalf of Microsoft. Asking him to favour
a Microsoft-associated proposal would be improper and would damage both. Asking him, as a colleague, **who
at Microsoft participates in ESR** and **what a persuasive submission looks like** is entirely proper.

Ask about process. Never about outcome.

---

## The order

1. Chowdhary answers: does Microsoft sit on ESR? If not, can it?
2. Microsoft commits, in writing, to implement in Segoe UI Emoji.
3. Microsoft design originates textless artwork and grants the licence.
4. Shuhan files one emoji, to [the template](../proposals/TEMPLATE-emoji-proposal.md), with the vendor
   commitment in `Other Information`.
5. Microsoft supplies Bing and Copilot data as supplementary evidence.
6. A Microsoft delegate files a supporting document when the proposal is under review.
7. The category document, later, once there is standing.

---

[^1]: Unicode Emoji Submission FAQ. https://www.unicode.org/faq/emoji_submission.html (retrieved 2026-07-09)

[^2]: Guidelines for Submitting Unicode Emoji Proposals. https://unicode.org/emoji/proposals.html

[^3]: Costa-Gomes B, Tolmachev P, et al. *Public use of a generalist LLM chatbot for health queries.* Nature Health, 2026. doi:10.1038/s44360-026-00117-x

[^4]: Unicode Technical Group Procedures. https://www.unicode.org/consortium/tc-procedures.html

[^5]: UTC #186 Minutes, L2/26-003: "Voting members in regular attendance = 4.5: Adobe, Apple, Google, Microsoft, UCB." https://www.unicode.org/L2/L2026/26003.htm
