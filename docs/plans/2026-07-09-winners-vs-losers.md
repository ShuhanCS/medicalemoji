# Winners versus losers: what actually separates them

The template lives at [`../proposals/TEMPLATE-emoji-proposal.md`](../proposals/TEMPLATE-emoji-proposal.md).
This document is the evidence behind it.

## The comparison

Between 2017 and 2021, Unicode published **every** submitted emoji proposal in its document register, not
only the ones it advanced. That accident of process gives a controlled comparison: same registers, same era,
same submission channel, some encoded and some not.

- **Winners:** 55 proposals written 2020 or later whose emoji were encoded in Emoji 13.1 through 17.0,
  identified from Unicode's [emoji proposals chart](https://unicode.org/emoji/charts/emoji-proposals.html).
- **Losers:** 29 community emoji proposals from the 2017 to 2021 registers that appear nowhere in that
  chart, so their emoji were never encoded. Meta documents (comments, notes, modifier and sequence
  proposals) were excluded.

Both groups downloaded and measured identically on 2026-07-09. Texts archived in
[`../proposals/reference-winners-2020-2024/`](../proposals/reference-winners-2020-2024/).

**Method caveat.** Measurements read the PDF text layer. Most evidence in these proposals is screenshots,
and a screenshot of an Ngram chart contains no searchable text. One winner, `L2/20-214` (X-ray), is a fully
scanned PDF with zero extractable text. So citation rates are floors, not compliance rates. Length, image
count and section structure are measured reliably.

## The result

| Measure | Winners (n=55) | Losers (n=29) |
|---|---|---|
| Median words | **907** | **1,485** |
| Median pages | 7 | 9 |
| Median images | **26** | **18** |
| Median count of `N/A` | 1 | 0 |
| Has an Exclusion section | 94% | 93% |
| Answers Open-ended | 94% | 89% |
| Answers Already representable | 96% | 89% |
| Answers Overly specific | 92% | 89% |
| Answers Transient | 94% | 86% |
| **Answers Faulty comparison** | **92%** | **72%** |
| **States a sort location** | **30%** | **10%** |
| Cites Google Trends | 87% | 65% |
| **Shows the `elephant` comparator** | **32%** | **13%** |
| **Cites a petition or social media** | **45%** | **75%** |
| **Uses awareness, stigma or advocacy language** | **1%** | **13%** |

## What this says

**Structure is not the discriminator.** Both groups fill in the selection factors at roughly the same rate.
Ninety-three percent of losers have an exclusion section. Writing the headings is table stakes and it wins
nothing.

**Losers write more and show less.** Sixty percent more prose, more pages, and a third fewer images. The
proposals that succeed are evidence documents with connective prose. The ones that fail are essays with
evidence attached.

**Winners write `N/A`.** Median once, against zero for losers. The guidelines say *"Mark this as n/a unless
there are compelling examples."* Losers argue every factor, which reads as advocacy and drowns the factors
that are genuinely strong.

**Three signals separate them cleanly:**

1. **Faulty comparison**, answered by 92% of winners and 72% of losers. Twenty points. A proposal that
   forgets this factor is often the same proposal whose whole case is "look what else got encoded."
2. **Petitions and social media**, cited by 75% of losers against 45% of winners. Unicode's text is
   unambiguous: *"Petitions or 'frequent requests' play no role in emoji encoding approval, and are not
   acceptable as evidence for citation."*
3. **Cause language.** Awareness, stigma, advocacy, "deserves representation": 13% of losers against 1% of
   winners. Thirteen to one. *"A proposal may be advanced despite a 'cause' argument… but will not be
   advanced because of it."*

The 45% of winners citing social media is worth stating honestly: doing it is not fatal, and correlation is
not cause. But it appears in three quarters of the documents that failed.

## The exemplars

**Treasure Chest, `L2/24-255`.** One individual, 672 words, encoded in Emoji 17.0.
Open-ended, in full: *"No, this is not part of a set."*
Licence, in full: *"I certify that I am the creator of this image and have appropriate licenses for use by
the UTC."*
Multiple meanings, made concrete: *"finding an earring under a car seat or a keepsake in your grandma's
attic."*
Design guidance to vendors: *"it is recommended that only gold coins be used. At small resolutions, other
contents may become muddled."*

**Orca, `L2/24-249`.** One individual, a personal email address, 781 words, encoded in Emoji 17.0.
Concedes the loss: *"Google Trends shows that the popularity worldwide of the orca is less than that of the
elephant."*
Then wins a narrower comparison: *"the interest seems to be roughly the same for both animals in the
Hispanic community… specially for South America."*
Explains its method: *"it has been selected as 'animal' instead of 'search term' to get correct results
regardless of naming or language."*
Adds an unrequested source: *"Wikipedia shows that the popularity in term of pageviews is roughly the same."*

**Fingerprint, `L2/23-258`.** Kills the obvious counterargument by name: *"One might argue that FINGERPRINT
could be represented by 'index pointing up' (U+261D), but this character shows an entire hand and does not
show friction ridge structure. It is a different emoji entirely."*
Files sixteen keywords, none redundant with the name.

**X-ray, `L2/20-214`.** Two individuals, Alijan Ozkiral and Christian Krenek. A **medical** emoji, filed in
the same window as fifteen of ours, encoded in Emoji 14.0. Christian Krenek alone authored or co-authored
the slide, the bird's nest, the heavy equals sign, the flute and the x-ray.

**Shovel, `L2/23-259`.** The Justdiggit Foundation, a reforestation NGO, encoded in Emoji 16.0. An
organization with a cause won by never arguing the cause. Its case is that a shovel is a common tool: *"A
shovel is one of the most used outdoor tools… The use of a shovel starts from a young age."* Not one
sentence about deforestation.

## A correction

I earlier argued that an organization must carry the proposal, on the evidence that every medical emoji in
the standard was filed by Emojination or its people. That evidence is real and the conclusion was too
strong. Orca, Treasure Chest, Bigfoot and Leafless Tree were each filed by one individual, alone. X-ray was
filed by two. **Craft separates winners, not letterhead.** An organization helps because it teaches the
craft and knows the route, and it is not a substitute for the craft.

## A second correction

An earlier version of this analysis reported that "46 of 55 winners name a credit or a licence." That used a
loose pattern matching the bare word "license" anywhere in the document. Measured strictly, requiring a
licence statement or a credit line, it is **25 of 55 (45%) of winners and 16 of 29 (55%) of losers.** The
licence is mandatory today and its absence is an automatic rejection, but it does **not** discriminate
between these two historical groups. Do not cite it as a success factor.
