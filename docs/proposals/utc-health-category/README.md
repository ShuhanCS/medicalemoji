# UTC document: Health as a Category in Emoji Ordering

**DUE 2026-07-21.** Seven days before UTC #188 (July 28–30, 2026, Redmond, WA).

- Draft: `health-category-utc-doc.md`
- Built PDF: `health-category-utc-doc.pdf` (8 pages, 92 KB, all fonts embedded)
- Spec: [`../../plans/2026-07-09-utc-doc-health-category-spec.md`](../../plans/2026-07-09-utc-doc-health-category-spec.md)

Rebuild:

```
pandoc health-category-utc-doc.md -o health-category-utc-doc.pdf --pdf-engine=xelatex
```

## What this document can and cannot achieve

Audited against Unicode's rules on 2026-07-09. Read this before setting expectations with anyone.

**Filing on 2026-07-21 will not produce a decision at UTC #188.** The seven-day deadline has a condition
that is easy to miss. `docsubmit.html` says: "most proposal documents must be pre-screened and reviewed by
specialized groups of experts prior to their placement on the UTC agenda for discussion and decision," and
the seven-day rule applies only to "document submissions which do not require pre-screening or further
review." Emoji matters are referred to the Emoji Standard and Research Working Group (ESR). Expect this
document to be noted and referred, not decided. That is still worth doing: it earns a permanent, public
`L2/26-nnn` number and puts the argument on the record.

**Submit it through Microsoft's UTC delegate, not as an outside individual.** From
<https://www.unicode.org/consortium/tc-procedures.html>: "Proposals may be submitted by any Delegate. The
group may also provide mechanisms for proposals from other organizations or individuals, **but is not
obliged to consider or respond to such proposals.**" Microsoft is a Full Member and holds a board seat.
Routing the document through its delegate converts it from a request the committee may ignore into a
proposal it handles as business. This is the single highest-leverage step available.

**The real owner is the ESR working group, and the real artifact is a text file.** The taxonomy is authored
in `emojiOrdering.txt` in `unicode-org/unicodetools` (`@@ Objects` at line 605, `@ medical` at line 640),
generated into `emoji-test.txt`, and only then incorporated into CLDR. CLDR consumes the grouping rather
than defining it, so a CLDR ticket alone would change nothing. Do not file one as the primary channel.

**There is no precedent for an outside party changing emoji grouping by document.** The Emoji 12.0
regrouping came from inside, through Emoji Subcommittee recommendations (L2/18-024 and related). Searches
of the L2 registers from 2016 to 2026 find no externally authored ordering or grouping proposal.

**The grouping is unprotected, which cuts both ways.** `emoji-test.txt` states "the groups and subgroups
are illustrative," and the Unicode stability policies do not cover group membership. So the change is
cheap and no stability rule forbids it. The same fact invites the response that the question does not
matter. The document answers that in its objections section: the groups are the section headings of every
major vendor's emoji keyboard.

## Pre-flight checklist — do not send until every box is ticked

- [ ] **Route through Microsoft's UTC delegate.** See above. Ask Vishal Chowdhary (Microsoft's board
      director) who the delegate is.
- [ ] **The document claims the census is published.** Appendix C links to
      <https://github.com/ShuhanCS/medicalemoji/blob/main/evidence/emoji_group_census.py> and
      <https://github.com/ShuhanCS/medicalemoji/blob/main/evidence/census-2026-07-09.txt>.
      Both currently live on `feat/stakeholder-outreach`, not `main`. Merge to `main`, or change the
      links, before the URLs are cited to a standards committee.
- [ ] **Recompute the census** against the then-current `emoji-test.txt` and update the retrieval date
      throughout. The numbers are dated 2026-07-09.
- [ ] David Rhew agrees to be named author and point of contact.
- [ ] Microsoft Communications clears the use of the Copilot and Nature Health data in a public document.
- [ ] Decide whether to offer the fallback request or hold firm on the top-level group.
- [ ] Confirm the PDF renders on a machine without Georgia or Consolas installed.
- [ ] Consider approaching the ESR working group directly, in parallel, since it owns the data.

## Sending it

```
To:      docsubmit@unicode.org
Subject: UTC Doc: Health as a Category in Emoji Ordering
Attach:  health-category-utc-doc.pdf
```

Requirements, verbatim from <https://www.unicode.org/pending/docsubmit.html>:

- "Do not submit emoji or character proposals to this address." (This document proposes no character.)
- "The preferred document format is PDF."
- "**Font embedding is required:** Please embed all of your fonts when you create PDF files for
  submission. This is extremely important!" — verified: Georgia and Consolas are embedded as subsets.
- "On the first page, a document must clearly identify the author or submitter, the subject, and the date
  of submission." — verified.
- "The deadline for document submissions which do not require pre-screening or further review is seven
  days before the start of the meeting."

Unicode will assign an `L2/26-nnn` number. Record it here when it arrives.

**Assigned L2 number:** _pending_

## Fallback

If 2026-07-21 is missed: UTC #189, October 26–28, 2026, Nancy, France. Deadline approximately
2026-10-19.
