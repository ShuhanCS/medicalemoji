# Examining Emoji Color Spaces: A Strategy for Improving the Coverage of Heart Emoji

Unicode document **L2/21-075**. Authors: ESC / Jennifer Daniel.

**This proposal succeeded.** Its emoji was encoded in Emoji 15.0.

Source PDF: <https://www.unicode.org/L2/L2021/21075-heart-emoji-coverage.pdf> (retrieved 2026-07-09). Text extracted with `pdftotext -layout`; the
evidence screenshots live in the PDF, not here. Text-layer word count: 1,661.

---

```text
                                                                                            L2/21-075

Examining Emoji Color Spaces:
A Strategy for Improving the Coverage of Heart Emoji

Author: Jennifer Daniel on behalf of the Unicode Emoji Subcommittee
To: Unicode Technical Committee
Date: November 15, 2020
Last Updated: April 11, 2021

I. Background

Hearts are among the most frequently used emoji. Users of emoji often

juxtapose the existing nine colored-heart emoji next to each other to denote

  markers of emotion, identity or affiliation that are not represented with atomic
emoji in the Unicode Standard (ex. Support of Belarus:  , Bisexuality:

, etc. ).1 It has also recently come to our attention that colored hearts are

the most common emoji used in non-messaging spaces like Twitter bios.

Identifying emoji additions that have multiple-uses is increasingly
important as emoji gain in popularity. The more emoji can operate as
building blocks instead of specific images the more versatile, fluid, and
useful they become.

What follows does not constitute a proposal but lays the strategy regarding
intent to draft proposals for a small set of colored hearts: PINK HEART, GRAY
HEART, and LIGHT BLUE HEART, thus completing the set of colored hearts to
align with what we understand about color theory and meet digital
communication needs.

  1 This follows similar behavior with other types of emoji, pairing two together to convey something more

specific like, " " to say "so cute" or " " to communicate italian dumplings aka ravioli ;-)
                                                                             1

Introduction

The original intent of adding a small set of colored emoji to the Unicode

standard was to lay the technical groundwork to standardize color variation

using ZWJs; however, there has been little to nearly no adoption.

 So what to do about it? This is where  come in.

What follows is a strategy that looks at some of the most frequently used
emoji (hearts) and how to improve their coverage. Early analysis indicates that
there are only a few gaps in the color spectrum of emoji offerings to complete the
set. By encoding a finite number of additional colored hearts we unlock a much
broader range of expression and representation.

We want to avoid new single use-case emoji like flags. Flag emoji are the bulk of
emoji fonts' file size and yet they are the least frequently used of all emoji. See:
Regarding Multiple Uses.

Identifying strategies and solutions such as this one is critical to meet user
demand and keep up with the speed of language online.

We want to do three things:
1. Investigate one of the most frequently used emoji type -- hearts -- and
strengthen the set by broadening their range of utility as described in
Background and Regarding Multiple Uses.
2. Identify new colors and understand the impact of these additions
3. Slightly modify the color of existing heart emoji for more equal distribution of
color in pursuit of adding a small number of new colored heart emoji to complete
the set.
                                                                                                                     2

Investing Gaps in Colored Hearts

Working with closed sets is important when making emoji additions. In pursuit of
understanding what this looks like for color we first have to understand the
status quo. Below is a visualization where vendors currently fall with regard to
the existing color spectrum. It neatly illustrates color spaces that are more
dense than others. When adding new emoji ensuring that they definitively break
new ground without risk of needing to add more later is a top priority.

Note: RGB converted to hue only. The different radiuses are the different vendors. Caption: While the upper left quadrant
is quite crowded, there are clear leaps between red and purple, purple, and blue, cyan and green, and green and yellow.
Most vendors put Purple too close to Blue, and Blue too close to Cyan. Green is often too yellow. Image with permission
and courtesy of @fakeunicode
                                                                                                                                         3

Above: Color spectrums broken down by vendor. Image with permission and courtesy of @fakeunicode

         These charts clearly illustrate the large gaps between blue and green and red and pink. They
         also suggest that if vendors slightly adjust the color of their yellow, green, and blue emoji we'd
         have a more even distribution without the need to add new colors. Note: The platform vendors
         are onboard for this action.
                                                                                                                               4

Identifying the Additional Colors

There is an existing literature in cross-linguistic study of color terms that suggests there are a
maximum of 11 basic color terms across cultures (Basic Color Terms, Berlin & Kay 1969). Of
these, the current set of emoji hearts are only missing PINK and GREY, both `Stage VII' color
terms. We also suggest adding LIGHT BLUE as well, as there are languages, including Russian
and Korean, which do not have a single basic color term for blue, but divide the space in two.

             Caption: As you can see in the above, the "blue" area in English is used almost to the left end of the graph where the
             greens are, while in Korean and Russian, the dark blues ("" and "") only extend part way to green, and there is a
             significant light blue color ("" and " ") which extends the rest of the way to green.
             Source: https://medium.com/hci-design-at-uw/there-is-no-blue-in-korean-ea6ac0d25d34
                                                                                                                               5

As languages evolve, they acquire new basic color terms in a broadly predictable sequence; if a
basic color term is found in a language, then the colors of all earlier stages are typically present. The
sequence is as follows:

           Stage I: Dark-cool and light-warm (covers a larger set of colors than just English "black"
               and "white".)

           Stage II: Red
           Stage III: Either green or yellow
           Stage IV: Both green and yellow
           Stage V: Blue
           Stage VI: Brown
           Stage VII: Purple, pink, orange, or gray

Basic Color Term theory has been debated and problematised, but we believe it still provides
some useful basis for the approach to the expansion of the range of colored hearts available.
One of the problems is that it doesn't account for major languages that have two distinct basic
terms for blue, as discussed above. We do not presume that the lexical patterns found across
languages represent fixed cognitive perspectives, for example we do not presume that people
can only distinguish between the colors if they have distinct terms for them, or that they will
only be useful if the color terms are lexified in a particular language. We do not presume that all
people will find the additional hearts equally useful, but that each provides more flexibility for
the current emoji set. Using Basic Color Terms as a theoretical underpinning of this strategy
document means we are likely covering the broadest possible set of basic colors in a large
number of languages and cultures.

In the past there has been feedback from the UTC that the concept of "pink" is not a universal
concept and people who didn't grow up with a word for a color could not distinguish it from
other nearby colors. This confusion is not unique to pink -- confusion most of us have over
cyan/blue is similar to what some cultures had over yellow/green. All that being said, just
because a culture doesn't have a word for a particular color does not mean it will result in
confusion; English speakers do not generally consider the distinction between light purple and
dark purple to be a basic distinction, but that doesn't mean we would expect the Los Angeles
Lakers to play in lavender uniforms.

Note, to be a "basic color term," it can't be describable using another color (e.g., because teal
or turquoise can be meaningfully described as "blue-green," it doesn't qualify in English) or a
physical object as a reference (e.g., rose, peach, salmon).
                                                                                                                               6

Required Design Modifications

What would this look like?

Status Quo:                                                   Future: Existing Set with Colors Shifted
Existing Set                                                  to Accommodate Possible Additions

Caption: The current set of saturated emoji (omitting black,  Caption: Yellow has been hue shifted +10 degrees, green +20 deg
gray, and white) mapped to RGB. @fakeunicode                  and blue +25 degrees @fakeunicode

Future: Includes Possible Addition of
Pink Heart and Light Blue Heart

Caption: Cyan and Pink added to the shifted set.
@fakeunicode
                                                                                                                               7
For demonstration only, this is what the hearts could look like cross vendors :

             Caption: A possible future. Note: blue, green, and yellow hearts show proposed shifted hues @fakeunicode

The ESC recommends vendors modify their colored hearts so the color spectrum is more
evenly distributed. The ESC will follow up with three proposals for PINK, LIGHT BLUE, and GREY
heart for review. All major platform vendors support this change.
                                                                                                                               8

Regarding Multiple Uses

The above stated proposals will go in further detail regarding the criteria for inclusion;
however, it is worth reiterating that a primary motivating factor in these recommendations
regards encoding concepts that can operate as building blocks particularly to meet demand
for identity flags (sexuality, gender, sports, subregional, etc.). Many of these flags draw upon
PINK, GREY and LIGHT BLUE in their design:

         PINK
         Bisexual flag
         Pansexual flag
         Polysexual flag
         Genderfluid flag

         GREY
         Aromantic flag
         Asexual flag
         Demiromantic flag
         Demisexual flag
         Agender flag

         LIGHT BLUE
         Pansexual flag

Caption: Sub-regional flags broken down by color. The addition of light blue and gray would extend coverage of representation.
Chart by Adam Peirce, used with permission. Source:
https://blocks.roadtolarissa.com/1wheel/ba7b6295c9e3e9aea7b164e1e22e9366

The world also uses emoji for sports teams, whether local, college or national level. Many
teams are currently accommodated by the range of hearts offered, but expanding the range
allows for more sports fans to show their affection. (ex. Currently fans of the San Antonio
Spurs are missing the sliver/grey heart, and their colors are listed as one of the five most
popular color schemes in US sport today. )

Lastly, the ESC does not propose extending more colors to the circle and square emoji which
are used far less frequently than hearts.

Acknowledgements
Special thanks to @fakeunicode for generously generating many charts for this proposal.
Adam Pearce for his investigation of color in subregional flags. Charles Carson and Lauren
Gawne for their expertise and Mark Davis for his guidance.

```
