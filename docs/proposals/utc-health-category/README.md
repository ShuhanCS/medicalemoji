# UTC document: Health as a Category in Emoji Ordering

**DUE 2026-07-21.** Seven days before UTC #188 (July 28–30, 2026, Redmond, WA).

- Draft: `health-category-utc-doc.md`
- Built PDF: `health-category-utc-doc.pdf` (8 pages, 92 KB, all fonts embedded)
- Spec: [`../../plans/2026-07-09-utc-doc-health-category-spec.md`](../../plans/2026-07-09-utc-doc-health-category-spec.md)

Rebuild:

```
pandoc health-category-utc-doc.md -o health-category-utc-doc.pdf --pdf-engine=xelatex
```

## Pre-flight checklist — do not send until every box is ticked

- [ ] **The document claims a CLDR ticket has been filed.** Section 3 says "A parallel ticket has been
      filed in the CLDR issue tracker and cross-references this document." **This is not yet true.**
      Either file the ticket at <https://unicode-org.atlassian.net/projects/CLDR/> first and insert its
      number, or reword the sentence. Do not send a document containing a false statement of fact.
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
