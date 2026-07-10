# Reference: UTC documents that change emoji data, not characters

Six documents in the genre our [Health category document](../utc-health-category/) belongs to. Downloaded
and converted 2026-07-09. Each file links to its source on unicode.org.

| Document | Author | Words | Outcome |
|---|---|---|---|
| [`L2/16-228`](16_228-mod-base-add.md) | Peter Constable + 3, **Microsoft** | **96** | Posted. Its lead author now chairs the UTC |
| [`L2/19-298`](19_298-emoji-props.md) | Ken Whistler | 618 | Emoji properties moved into the UCD |
| [`L2/23-142`](23_142-legacy-computing-emoji-vs.md) | Charlotte Buff | 550 | Discussed, **remanded to ESC and PAG** |
| [`L2/23-252`](23_252-legacy-disunification.md) | Bettencourt, Ewell | 1,647 | **Adopted.** Ten code points provisionally assigned |
| [`L2/19-084`](19_084-trans-flag.md) | Charlotte Buff | 3,376 | Read, and argued against on the merits |
| [`L2/17-232`](17_232-gender-gap.md) | Charlotte Buff | 5,660 | Structural argument, 20 pages |

## Who these people are

Their own documents answer this, and the answer is encouraging.

**Charlotte Buff** files as `Author: Charlotte Buff / Mail: irgendeinbenutzername@gmail.com`. A private
individual with a Gmail address. Not a committee member, not a delegate, no institution. She has filed
repeatedly since 2016. The UTC reads her documents, discusses them by name in the minutes, and remands them
to working groups.

**Rebecca Bettencourt and Doug Ewell** file as `Source: Terminals Working Group`, `Status: Individual
Contribution`.

The **Terminals Working Group is not a Unicode body.** It appears nowhere on Unicode's technical group
leadership page. Its own document explains its origin: *"a list discussion concerning the 'PETSCII'
character set led to the creation of an ad-hoc Terminals Working Group in charge of proposing characters
found in computer systems manufactured in the 1970s and 1980s."* It is self-formed, it concerns legacy
computer terminals, and **it cannot be joined by anyone working on medical emoji.** Its relevance is only
as a pattern: a group of people named themselves, filed consistently, and became the recognized source for
their domain. `Status: Individual Contribution` is Unicode recording that they contribute as individuals,
not as a member organization.

**Peter Constable** filed `L2/16-228` as a Microsoft employee in 2016. He is now **Chair of the Unicode
Technical Committee**.

**None of them needed to be committee members.** And the chain is worth studying: Buff, a private
individual, filed `L2/23-142`. The UTC remanded it. The Terminals Working Group then wrote `L2/23-252`,
which says in its History section, *"In June 2023, Charlotte Buff submitted L2/23-142, a proposal to define
variation sequences for 10 characters from legacy computer systems that had been unified with emoji."*
That document was **adopted**. Ten code points were provisionally assigned.

A remand is not a rejection. It is the idea being handed to the people who own the file.

## Can our document carry Shuhan He alongside Microsoft? Yes

The "must be an individual" rule belongs to the **emoji submission form**, not to UTC documents. UTC
documents have no such restriction. `docsubmit.html` requires only that the first page *"clearly identify
the author or submitter, the subject, and the date of submission."*

The precedent is Microsoft's own. `L2/16-228` lists **four named authors**, and its first sentence of body
text reads:

> "**Microsoft would like to see** the following characters added to the Emoji_Modifier_Base property in
> version 4.0 of UTR #51"

Named individuals author. The organization speaks. That is exactly the shape we want: David Rhew and Shuhan
He as authors, Microsoft named as the voice, Massachusetts General Hospital as an affiliation.

`L2/23-252` shows the fuller header, with an explicit `Source` and `Status` line.

## What they did well

### 1. They are short

Constable's entire document is **96 words**. It states what Microsoft wants, lists the characters, and
stops. Buff's remanded proposal is 550 words. The adopted `L2/23-252` is 1,647.

Length correlates with nothing. The 96-word document was posted; the 5,660-word document was not adopted.

### 2. They use a header block, and the right one depends on the genre

**Do not copy `L2/23-252`'s header.** It is the ISO/IEC JTC1/SC2/WG2 **character proposal** template, and
the document carries the full ISO Proposal Summary Form: questions about the Basic Multilingual Plane,
combining characters and ideographic compatibility. It is addressed `For consideration by JTC1/SC2/WG2 and
UTC` because it proposes new code points. A document that proposes no character does not go to WG2.

The correct model for our genre is **Ken Whistler's `L2/19-298`**, a UTC-only emoji data document:

```
L2/19-298

Title: Making Emoji Properties a Part of the UCD for Unicode 13.0

Author: Ken Whistler

Date: July 25, 2019

Action: For consideration by the UTC
```

Four lines. The `Action:` line tells the committee what you want done with it. Constable's `L2/16-228` is
even lighter: `Title`, `Authors`, `Date`, and then straight into the body. Buff uses `Author`, `Mail`,
`Submitted`.

Our document now follows Whistler.

### 3. They number their sections and lead with history

`L2/23-252`: `1. Introduction. 2. History. 3. Rationale. 5. Unicode character properties. 6. References.`

The History section does the persuading. It recounts what was decided before, by whom, and why the earlier
decision no longer holds. That is precisely the argument available to us: the Emoji Subcommittee assigned
the anatomical heart and lungs to `body-parts` in `L2/19-190R` because no better destination existed.

### 4. They credit the people who came before

`L2/23-252` names Buff, cites her document number, and explains how the Script Ad-Hoc routed it. It reads
as a contribution to a shared record rather than a demand.

### 5. They ask for one thing

Disunify ten characters. Add these characters to one property. Define these variation sequences. Every one
of these documents has a single, checkable ask.

## Does our document match?

Checked against [`../utc-health-category/health-category-utc-doc.md`](../utc-health-category/health-category-utc-doc.md):

| | Precedent | Ours | Verdict |
|---|---|---|---|
| Header block with `Doc Type` / `Source` / `Status` / `Action` | `L2/23-252` | **was missing** | **fixed** |
| First page names author, subject, date | required | yes | ok |
| Numbered sections | yes | yes | ok |
| History section carrying the argument | `L2/23-252` | yes, section 4.4 and the `L2/19-190R` citation | ok |
| One checkable ask | all six | yes, plus a fallback | ok |
| Credits prior documents by number | `L2/23-252` | yes | ok |
| Length | 96 to 5,660 words | ~2,000 | ok |
| Requests no character | our genre | stated in the first sentence | ok |
| Organization named in the body | `L2/16-228` | **now mirrors "Microsoft would like to see"** | **fixed** |

**The approach is right.** The format needed the canonical header block and an `Action:` line, which have
been added.
