# Proposal for Emoji: White Blood Cell

**Submitters:** Shuhan He, MD; David Rhew, MD (Global Chief Medical Officer and Vice President of Healthcare,
Microsoft); Heena Purohit (Director, AI Startups, Microsoft)<br>
**Main point of contact:** Shuhan He<br>
**Date:** 2026-07-26

## 1. Identification

**Keywords:** leukocyte; immunity; infection; inflammation; laboratory<br>
**Category:** People & Body body-parts

## 2. Images

|  | 18x18 | 72x72 |
| --- | --- | --- |
| **Colour** | ![White Blood Cell colour 18x18](images/white-blood-cell_color_18x18_SUBMIT.png) | ![White Blood Cell colour 72x72](images/white-blood-cell_color_72x72_SUBMIT.png) |
| **Black and white** | ![White Blood Cell black and white 18x18](images/white-blood-cell_bw_18x18_SUBMIT.png) | ![White Blood Cell black and white 72x72](images/white-blood-cell_bw_72x72_SUBMIT.png) |

The image uses the standard [neutrophil form](https://www.ncbi.nlm.nih.gov/books/NBK563148/) - a pale,
irregular cell body with one connected, multi-lobed nucleus - as the visual model for the broader
white-blood-cell category. Neutrophils are the most numerous circulating leukocytes, and these cues remain
legible at actual keyboard size while separating the image from a spiked microbe, a teardrop-shaped Drop of
Blood, and a generic cell diagram.

I, Shuhan He, certify that these example images are original Medical Emoji artwork, that I own or control all
IP Rights in them, and that they contain no third-party artwork, logo, trademark, text, digit, or barcode. I
release the images under the CC0 1.0 Universal Public Domain Dedication and grant the rights required by the
Unicode Emoji Proposal Agreement and License.

[CC0 1.0 Universal Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/)

## 3. Factors for inclusion

### a. Multiple meanings

Not applicable.

### b. Use in sequences

White Blood Cell can combine with existing emoji to express clear messages without standardized sequences:

- White Blood Cell + Microbe: immune response to infection.
- White Blood Cell + up arrow or down arrow: high or low white-cell count.
- White Blood Cell + Test Tube: blood count, laboratory testing, or research.

### c. Breaks new ground

**Yes.** The current Unicode emoji vocabulary has no human immune cell. Microbe represents a microscopic
organism rather than the body's defense cell; Drop of Blood represents blood as a fluid; and Test Tube
represents a container or laboratory activity. White Blood Cell adds the missing host immune cell, so a user
can distinguish the body's defense cell from the microbe it is responding to.

[Current Unicode Emoji List](https://www.unicode.org/emoji/charts/full-emoji-list.html)

### d. Distinctiveness

White Blood Cell uses a neutrophil as its visual model: a pale, irregular cell body and one
bold, connected, three-lobed nucleus. NCBI describes neutrophils as 50% to 70% of circulating leukocytes and
their nuclei as three to five connected segments. At 18 pixels, the enclosed lobed nucleus distinguishes the
image from the spiked outline of Microbe, the teardrop silhouette of Drop of Blood, the separate circles of
Bubbles, and a generic cell diagram. The image does not assert that every leukocyte has neutrophil morphology;
it uses the most numerous type as the visible exemplar for the broader category. Vendors may vary the cell
outline, lobe count, and internal shading while keeping a pale irregular body and one connected lobed nucleus.

[NCBI Bookshelf: Histology, White Blood Cell](https://www.ncbi.nlm.nih.gov/books/NBK563148/)

The colour and black-and-white examples on page 1 show that these visible cues remain clear at both required
sizes and do not depend on colour alone. All artwork displayed in this proposal as proposed emoji artwork is
the original work identified in Section 2.

### e. Usage level

The clearest uses are talking about the body's immune response and communicating a high, low, or monitored
white blood cell count. The required five-source evidence below shows current Search and Video results,
recurring Web and Image search interest, and durable published-book usage. Its relative Trends and Ngram
levels are below `elephant`, while the term remains present across the modern record.

The [National Cancer Institute](https://www.cancer.gov/publications/dictionaries/cancer-terms/def/white-blood-cell)
defines a white blood cell as a blood cell found in blood and lymph tissue that forms part of the immune system
and helps fight infection and other diseases. [MedlinePlus](https://medlineplus.gov/lab-tests/white-blood-count-wbc/)
documents white blood count as a routine test used to diagnose and monitor conditions affecting white blood
cells. Search and Video figures below are indexed-result estimates, not counts of individual users or direct
measures of emoji demand.

The concept also has documented use in digital health standards. The active
[LOINC 6690-2](https://loinc.org/6690-2) term standardizes automated leukocyte counts, appears in multiple
complete-blood-count panels, and supplies language variants for international implementations. The
[HL7 US Core Implementation Guide](https://www.hl7.org/fhir/us/core/Observation-cbc-leukocytes.html) publishes
a laboratory-result example for a White Blood Cell count using that LOINC code. These sources demonstrate
routine interchange of the concept in digital records; they are usage evidence, not a pictographic
compatibility claim.

### f. Completeness

Not applicable.

### g. Compatibility

Not applicable.

## 4. Counterarguments to factors for exclusion

### a. Already represented

No existing emoji or sequence identifies a white blood cell. Microbe + Shield can suggest protection from a
germ, but it cannot express the host immune cell or the standardized white-cell-count observation used in
laboratory records. Drop of Blood, Test Tube, Microscope, and Hospital provide context without supplying the
missing concept.

### b. Overly specific

White Blood Cell is the broad leukocyte category, not a particular subtype, disease, procedure, specialty,
treatment, or campaign. The representative artwork uses neutrophil morphology because neutrophils are the
most numerous circulating leukocytes and their connected lobed nucleus supplies a stable small-size cue. The
character name and intended meaning remain White Blood Cell, covering the five major types counted together
in the routine white blood count described by MedlinePlus.

### c. Open-ended

Red Blood Cell, Platelet, a generic Cell, and individual leukocyte subtypes are the most likely follow-on
candidates. White Blood Cell has a specific boundary: it is the upper-level immune-cell concept, the host-cell
counterpart to Microbe, and a named count exchanged in LOINC- and HL7-based laboratory records. Individual
leukocyte types are narrower members of this proposed category, while a generic Cell would not convey immune
defense or a white-cell count. Red Blood Cell and Platelet would present different semantic and substitute
questions and are not implied by this proposal. Selection of White Blood Cell therefore stops at the broad
leukocyte category rather than beginning a series of blood components or human cells.

### d. Transient

White blood cells are a durable biological and medical concept. The Google Books record below extends through
2022 and shows increasing modern published use, while the current Search and Trends evidence documents ongoing
use across web, image, and video formats.

### e. Faulty comparison

The `elephant` comparisons measure relative frequency only; they do not claim that another emoji creates a
precedent. White Blood Cell addresses the specific gap between the body's immune cell and the Microbe it
responds to.

## 5. Other information

Vendors should use a neutrophil-like form as the visual model for the broader White Blood Cell
meaning: a pale or neutral irregular cell body and one bold, connected nucleus with three to five lobes. Fine
microscopic detail is optional and should yield to legibility at 18x18. Radiating spikes should be avoided
because they imply Microbe, and the nucleus should remain a single connected feature rather than a face-like
arrangement. The character name should remain White Blood Cell rather than a leukocyte subtype.

## 6. Evidence of frequency

All data are from July 2026 and were obtained in a Firefox Private Browsing window. Search queries disable
personalized results. Trends use Worldwide, all categories, and the full available period. Books uses the
English corpus, 1500-2022, and smoothing 3.

### Google Search

Captured 2026-07-26 using the required grouped term `white-blood-cell`. The result page reports about 125
results, compared with about 491,000,000 for `elephant` under the same settings.

[Open the reproducible Google Search query](https://www.google.com/search?q=white-blood-cell&hl=en&num=10&pws=0)

![Google Search results for white blood cell](evidence/frequency/white-blood-cell_google_search_2026-07-26_SUBMIT.png)

![Google Search results for elephant](evidence/frequency/white-blood-cell_google_search_elephant_2026-07-26_SUBMIT.png)

<div class="page-break"></div>

### Google Video Search

Captured 2026-07-26 using the required grouped term `white-blood-cell`. The video result page reports about
14,100,000 results, compared with about 86,300,000 for `elephant` under the same settings.

[Open the reproducible Google Video Search query](https://www.google.com/search?tbm=vid&q=white-blood-cell&hl=en&num=10&pws=0)

![Google Video Search results for white blood cell](evidence/frequency/white-blood-cell_google_video_search_2026-07-26_SUBMIT.png)

![Google Video Search results for elephant](evidence/frequency/white-blood-cell_google_video_search_elephant_2026-07-26_SUBMIT.png)

<div class="page-break"></div>

### Google Trends - Web Search

Captured 2026-07-26 using Worldwide, 2004-present, all categories, and Web Search. Average indexed interest was
72 for `elephant` and 3 for `white blood cell`; the white-blood-cell series reaches 4 in 2024, 2025, and 2026.

[Open the Google Trends Web Search comparison](https://trends.google.com/trends/explore?date=all&q=elephant%2Cwhite%20blood%20cell)

![Google Trends Web Search for elephant and white blood cell](evidence/frequency/white-blood-cell_google_trends_web_elephant_2026-07-26_SUBMIT.png)

<div class="page-break"></div>

### Google Trends - Image Search

Captured 2026-07-26 using Worldwide, 2008-present, all categories, and Image Search. Average indexed interest
was 53 for `elephant` and 1 for `white blood cell`, with recurring white-blood-cell interest across the period.

[Open the Google Trends Image Search comparison](https://trends.google.com/trends/explore?date=all_2008&gprop=images&q=elephant%2Cwhite%20blood%20cell)

![Google Trends Image Search for elephant and white blood cell](evidence/frequency/white-blood-cell_google_trends_image_elephant_2026-07-26_SUBMIT.png)

<div class="page-break"></div>

### Google Books Ngram Viewer

Captured 2026-07-26 using the English corpus, 1500-2022, and smoothing 3. In 2022, the frequency of `white blood
cell` was approximately 10.13% of `elephant`, with an increasing modern series.

[Open the Google Books Ngram comparison](https://books.google.com/ngrams/graph?content=elephant%2Cwhite%20blood%20cell&year_start=1500&year_end=2022&corpus=en&smoothing=3)

![Google Books Ngram for elephant and white blood cell](evidence/frequency/white-blood-cell_google_books_ngram_elephant_2026-07-26_SUBMIT.png)
