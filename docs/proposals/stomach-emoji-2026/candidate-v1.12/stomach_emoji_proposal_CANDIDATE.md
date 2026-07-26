# Proposal for Emoji: Stomach

**Submitter:** Shuhan He, MD<br>
**Main point of contact:** Shuhan He<br>
**Date:** 2026-07-26

## Identification

**Suggested name:** Stomach<br>
**Suggested keywords:** digestion; gut; belly; abdomen; hunger; appetite; fullness; nausea; indigestion; reflux<br>
**Suggested category:** People & Body - body-parts<br>
**Suggested sort location:** Near anatomical heart, lungs, and brain in the body-parts subgroup.

## Required Example Images

| Size | Color | Black and white |
| --- | --- | --- |
| 18x18 | ![Stomach color 18x18](images/stomach_color_18x18_SUBMIT.png) | ![Stomach black-and-white 18x18](images/stomach_bw_18x18_SUBMIT.png) |
| 72x72 | ![Stomach color 72x72](images/stomach_color_72x72_SUBMIT.png) | ![Stomach black-and-white 72x72](images/stomach_bw_72x72_SUBMIT.png) |

The paradigm is a bold asymmetric J-shaped stomach with a long inlet, deep open inner concavity, broad lower
body, and distinct short outlet. These cues separate it from food, beans, a generic blob, and other solid
organs. Vendors may vary angle, color, outline, and shading while preserving the inlet, open concavity, and
outlet at typical emoji sizes.

I, Shuhan He, certify that these example images are original work created for this proposal, that I own all IP
Rights in them, and that they contain no third-party artwork, logo, trademark, or text. I release the images
under the CC0 1.0 Universal Public Domain Dedication and grant the rights required by the Unicode Emoji
Proposal Agreement and License.

CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/

## Factors for Inclusion

### A. Multiple meanings

Stomach has established anatomical, emotional, and figurative meanings. It can refer to the digestive organ,
hunger or fullness, a nervous stomach, butterflies in the stomach, tolerance expressed through a strong
stomach, and the ability to accept something unpleasant. These meanings support ordinary communication about
food, sensation, emotion, and tolerance without depending on a newly invented pun.

Cambridge Dictionary documents both the expression butterflies in your stomach and the verb sense of stomach,
meaning to accept or deal with something unpleasant:

https://dictionary.cambridge.org/us/dictionary/english/butterflies-in-stomach

https://dictionary.cambridge.org/us/dictionary/english/stomach

### B. Use in sequences

Stomach adds a specific organ meaning to several short combinations:

- Stomach + fork and knife: hunger, a meal's effect, fullness, or digestion.
- Stomach + nauseated face: an upset stomach, nausea, or a stomach bug.
- Stomach + butterfly: nervous anticipation or butterflies in the stomach.
- Stomach + pill or hospital: antacid use, digestive treatment, or stomach-specific care.

### C. Breaks new ground

**Yes.** Nauseated Face expresses a symptom, and food emoji represent what is eaten. Neither identifies the
stomach itself. No current emoji or short sequence directly represents the stomach as an organ and broad
semantic building block. Stomach therefore adds a distinct concept for digestion, hunger, fullness, physical
sensation, figurative expression, education, and health.

### D. Distinctiveness

The selected image uses an asymmetric J shape, long inlet, deep inner concavity, broad lower body, and separate
outlet. Its identity rests on silhouette rather than color or fine internal texture. The open concavity and two
connected passages distinguish it from Anatomical Heart, Beans, Meat on Bone, Kidney, Liver, and a generic
organ shape.

Deterministic validation checked exact dimensions, true black-and-white palette, foreground connectedness, and
normalized 18x18 silhouette separation against those six declared confusers using pinned assets. Both 18x18
Stomach assets passed: the maximum normalized silhouette intersection-over-union was 0.638 against a 0.72
ceiling, and the minimum 64-bit difference-hash distance was 19 against a 16 floor. These checks establish
machine-visible separation; they do not substitute for human semantic recognition.

### E. Expected usage level

Stomach is an ordinary term used in communication about digestion, eating, hunger, appetite, fullness, nausea,
stomach aches, indigestion, reflux, medication, education, and figurative emotion. The National Institute of
Diabetes and Digestive and Kidney Diseases describes the stomach's central role in receiving food, mixing it
with digestive juices, and emptying its contents into the small intestine:

https://www.niddk.nih.gov/health-information/digestive-diseases/digestive-system-how-it-works

The five frequency sources below measure public use from complementary perspectives. Google Trends and Google
Books compare `stomach` with Unicode's reference term `elephant`.

#### Google Search

Captured 2026-07-26. The page displays an estimated 353,000,000 results. This volatile estimate is presented
only as the result-count measure requested by the proposal guidelines, not as a count of users or intended
emoji uses. Reproducible query:
https://www.google.com/search?q=stomach&hl=en&filter=0

![Google Search results for stomach](evidence/frequency/stomach_google_search_2026-07-26_CANDIDATE.png)

#### Google Video Search

Captured 2026-07-26. The page displays an estimated 139,000,000 video results. This volatile estimate is not a
count of users or intended emoji uses. Reproducible query:
https://www.google.com/search?tbm=vid&q=stomach&hl=en&num=10&pws=0

![Google Video Search results for stomach](evidence/frequency/stomach_google_video_search_2026-07-26_CANDIDATE.png)

#### Google Trends - Web Search

Captured 2026-07-26 using Worldwide, 2004-present, All categories, and Web Search. Stomach has the higher
displayed average across the full range and a strong sustained lead in recent years. Reproducible query:
https://trends.google.com/trends/explore?date=all&q=stomach,elephant

![Google Trends Web Search for stomach and elephant](evidence/frequency/stomach_google_trends_web_elephant_2026-07-26_CANDIDATE.png)

#### Google Trends - Image Search

Captured 2026-07-26 using Worldwide, 2008-present, All categories, and Image Search. Elephant has the higher
long-run average. Stomach nevertheless shows durable worldwide image-search interest across the full available
range and a sharp recent peak that briefly exceeds elephant. This graph is included with that limitation
visible rather than treated as a favorable result. Reproducible query:
https://trends.google.com/trends/explore?date=all&gprop=images&q=stomach,elephant

![Google Trends Image Search for stomach and elephant](evidence/frequency/stomach_google_trends_image_elephant_2026-07-26_CANDIDATE.png)

#### Google Books Ngram Viewer

Captured 2026-07-26 using the English corpus, 1500-2022, case-insensitive matching, and smoothing 3. Stomach
substantially exceeds elephant in the latest displayed years and shows durable published-book use across the
longest available range. Reproducible query:
https://books.google.com/ngrams/graph?content=elephant%2Cstomach&year_start=1500&year_end=2022&corpus=en&smoothing=3

![Google Books Ngram for elephant and stomach](evidence/frequency/stomach_google_books_ngram_elephant_2026-07-26_CANDIDATE.png)

### F. Completeness

Not applicable. Stomach is independently useful and is not proposed to complete a set of organs.

### G. Compatibility

Not applicable. This proposal does not rely on a legacy carrier emoji or another encoded pictograph.

## Factors for Exclusion

### A. Already represented

Nauseated Face can express nausea, and food emoji can identify meals or ingredients, but neither identifies the
stomach itself. Hospital and pill can imply care or treatment without naming the affected organ. These
substitutes cannot clearly express stomach-specific anatomy, digestion, hunger, fullness, discomfort, or
figurative stomach meanings.

### B. Overly specific

Stomach is a broad, familiar organ concept, not a disease, procedure, specialty, campaign, subtype,
organization, or brand. It supports ordinary communication across food, digestion, sensation, emotion,
education, nutrition, and health.

### C. Open-ended

Encoding Stomach would not imply encoding liver, kidney, intestine, or every anatomical structure. Stomach
stands on its own demonstrated usage, established figurative meanings, independent semantic gap, and compact
J-shaped visual paradigm. Other concepts can be judged independently under the same criteria.

### D. Transient

Stomach is a durable term and concept. The long-range Google Books record documents published use across
centuries, while established expressions such as butterflies in the stomach and the verb sense of stomach are
documented in current dictionaries. The proposal is not tied to a temporary event, product, or campaign.

### E. Faulty comparison

The proposal does not depend on Anatomical Heart, Lungs, Brain, or another organ already being encoded. Its
case rests on Stomach's own ordinary usage, established meanings, recognizable paradigm, and remaining gap in
the emoji vocabulary.

## Other Information

The singular common name Stomach is concise and searchable. Essential design cues are an asymmetric J-shaped
hollow-organ body, a long visible inlet, a deep open inner concavity, and a distinct rounded outlet. Fine
anatomical detail is optional and should yield to legibility at 18x18. Vendors should avoid a form that reads
primarily as food, a bean, or a generic pink shape.
