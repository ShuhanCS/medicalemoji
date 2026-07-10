# UTC document: Health as a Category in Emoji Ordering

**DUE 2026-07-21.** Seven days before UTC #188 (July 28–30, 2026, Redmond, WA).

- Draft: `health-category-utc-doc.md`
- Built PDF: `health-category-utc-doc.pdf` (8 pages, 92 KB, all fonts embedded)
- Spec: [`../../plans/2026-07-09-utc-doc-health-category-spec.md`](../../plans/2026-07-09-utc-doc-health-category-spec.md)

Rebuild:

```
pandoc health-category-utc-doc.md -o health-category-utc-doc.pdf --pdf-engine=xelatex
```

## What it is called, and whether anyone has done it before

It is a **UTC document**, also called an **L2 document**. Not a petition. It is emailed to
`docsubmit@unicode.org`, Unicode assigns it a permanent public number of the form `L2/26-nnn`, and it
enters the public register at <https://www.unicode.org/L2/>.

### Do insider filings get posted? Yes. All of them.

Counting documents in the registers whose source field names the Emoji Subcommittee, the working group, the
UTC chair, or the editors of UTS #51:

| Year | Insider documents posted |
|---|---|
| 2015 | 88 |
| 2016 | 98 |
| 2017 | 78 |
| 2018 | 57 |
| 2019 | 84 |
| 2020 | 54 |
| 2021 | 47 |
| 2022 | 76 |
| 2023 | 79 |
| 2024 | 66 |
| 2025 | 56 |
| **Total** | **783** |

The Emoji Subcommittee's quarterly reports, its recommendation documents, the editors' draft data files,
and the chair's own proposals all appear in the same public register as everyone else's.

Two things are **not** public. Emoji proposals that the working group declines never become documents at
all, which is why the kidney has no record. And the working group's internal deliberations are not
published; only its reports are.

### Precedent for a document like ours

Documents that change emoji **data or organization** rather than adding a character are ordinary business,
and they come from members and non-members alike.

| Document | Author | What happened |
|---|---|---|
| `L2/16-228` Proposed Additions to `Emoji_Modifier_Base` | **Peter Constable** (Microsoft; now Chair of the UTC) | An emoji **data** proposal, filed by a Microsoft employee, posted publicly |
| `L2/15-049` Draft Emoji Data Files: Data, **Ordering**, Annotations | Mark Davis | The ordering data itself, filed as a UTC document |
| `L2/19-298` Making Emoji Properties a Part of the UCD | Ken Whistler | Property data change |
| `L2/23-252` Proposal to disunify Symbols for Legacy Computing from emoji | Rebecca Bettencourt, Doug Ewell | **Adopted.** UTC #177: *"[177-C35] Consensus: Provisionally assign the following code points for ten symbols, as described in L2/23-252"*, with action items to Ken Whistler |
| `L2/23-142` Proposal to Define Variation Sequences for Emoji Mapped to Legacy Computing Symbols | Charlotte Buff | UTC #176: *"Discussion. **Remanding to ESC and PAG to review.**"* UTC #177: *"Discussion. UTC took no action at this time."* |
| `L2/19-084` The Curse of Representation by Specificity | Charlotte Buff | Argued **against** the transgender flag. The UTC read it and approved the flag anyway: *"[159-C16] Consensus: Accept the transgender flag as a draft candidate."* |

So the genre exists, it is filed by individuals and by members, it gets numbered, agendized and discussed,
and it is sometimes adopted outright. Buff's `L2/23-142` shows the likeliest path for ours: **discussed,
then remanded to the working group.** That is not failure. It is the argument entering the record and
reaching the body that owns the file.

### Microsoft is not an outsider

The clause in `tc-procedures.html` that the group *"is not obliged to consider or respond"* applies to
proposals from *"other organizations or individuals"*, meaning non-delegates. **Microsoft is a Full Member.**
It has a delegate, it attends every meeting, and `L2/16-228` shows a Microsoft employee filing an emoji data
proposal a decade ago. That employee, Peter Constable, now chairs the UTC.

UTC #172 and UTC #176 were both held in **Redmond, WA**. So was UTC #188, where this document is headed.

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
      <https://github.com/ShuhanCS/medicalemoji/blob/master/evidence/emoji_group_census.py> and
      <https://github.com/ShuhanCS/medicalemoji/blob/master/evidence/census-2026-07-09.txt>.
      Both must exist on `master`. Confirm after the merge, or change the
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
