# Proposal to Define Variation Sequences for Emoji Mapped to Legacy Computing Symbols

Unicode document **L2/23-142**. Authors: Charlotte Buff (private individual, gmail address).

**Outcome:** UTC #176: "Discussion. Remanding to ESC and PAG to review." UTC #177: "Discussion. UTC took no action at this time." The Terminals Working Group then wrote L2/23-252, crediting her, and it was adopted.

Source: <https://www.unicode.org/L2/L2023/23142-legacy-computing-emoji-vs.pdf> (retrieved 2026-07-09). Text-layer word count: 550.

---

```text
                                                  L2/23-142

                         Proposal to Define Variation Sequences for Emoji Mapped to Legacy Computing Symbols

 Proposal to Define Variation Sequences for Emoji Mapped
                      to Legacy Computing Symbols

                                     Author: Charlotte Buff
                         Mail: irgendeinbenutzername@gmail.com

                                     Submitted: 2023-06-26

1. Background
The character repertoire proposed in L2/21-235r (Bettencourt et al., Proposal to add further
characters from legacy computers and teletext to the UCS), AKA "Legacy Computing
Supplement", unifies a number of different character sets. Symbols from these sets map to
both newly proposed characters (planned to be released in Unicode 16.0) as well as existing
code points, some of which are classified as emoji.
Whenever a Unicode character is mapped to both emoji and non-emoji sources, it is
customary to define emoji variation sequences for it to allow proper usage in both contexts.
This was most recently done in Unicode 9.0 for a number of emoji originating from
Japanese carrier sets that were unified with symbols from Wingdings and Webdings.
Colourful, whimsical emoji glyphs would be especially out of place when emulating
terminals and retro computers, so in this document I propose giving the same treatment to
the Legacy Computing Supplement source sets for the Unicode 16.0 release.

2. Proposed Sequences
As of (draft) Unicode Emoji 15.1 there are nine emoji that are mapped to Legacy Computing
Supplement characters and don't already have emoji variation sequences defined. One
additional such character (U+1F514) was identified in the character sets that were the
subject of the original legacy computing proposal, L2/19-025 (Ewell et al., Proposal to add
characters from legacy computers and teletext to the UCS), for a total of ten. Mappings were
taken from the various tables attached to both documents.

Unicode Code Point       Source Set               Source Code Point

U+1F333 DECIDUOUS TREE   Ohio Scientific          0x0D
U+1F34E RED APPLE        Sharp MZ (EU alternate)  0x9D
U+1F352 CHERRIES         Sharp MZ (EU alternate)  0x9E
U+1F353 STRAWBERRY       Sharp MZ (EU alternate)  0x90
U+1F377 WINE GLASS       Sharp MZ (EU alternate)  0x74
U+1F3E2 OFFICE BUILDING  Sharp MZ (EU alternate)  0xFB
U+1F40D SNAKE            Sharp MZ (JP primary)    0xDF
U+1F443 NOSE             Sharp MZ-80 (EU)         0xBE

                         1
                       Proposal to Define Variation Sequences for Emoji Mapped to Legacy Computing Symbols

U+1F514 BELL           Atari ST               0x0A
U+1F6F8 FLYING SAUCER  Sharp MZ (JP primary)  0xC7

If this proposal is accepted, the following lines need to be added to emoji-variation-
sequences.txt:

1F333 FE0E ; text style; # (6.0) DECIDUOUS TREE
1F333 FE0F ; emoji style; # (6.0) DECIDUOUS TREE
1F34E FE0E ; text style; # (6.0) RED APPLE
1F34E FE0F ; emoji style; # (6.0) RED APPLE
1F352 FE0E ; text style; # (6.0) CHERRIES
1F352 FE0F ; emoji style; # (6.0) CHERRIES
1F353 FE0E ; text style; # (6.0) STRAWBERRY
1F353 FE0F ; emoji style; # (6.0) STRAWBERRY
1F377 FE0E ; text style; # (6.0) WINE GLASS
1F377 FE0F ; emoji style; # (6.0) WINE GLASS
1F3E2 FE0E ; text style; # (6.0) OFFICE BUILDING
1F3E2 FE0F ; emoji style; # (6.0) OFFICE BUILDING
1F40D FE0E ; text style; # (6.0) SNAKE
1F40D FE0F ; emoji style; # (6.0) SNAKE
1F443 FE0E ; text style; # (6.0) NOSE
1F443 FE0F ; emoji style; # (6.0) NOSE
1F514 FE0E ; text style; # (6.0) BELL
1F514 FE0F ; emoji style; # (6.0) BELL
1F6F8 FE0E ; text style; # (10.0) FLYING SAUCER
1F6F8 FE0F ; emoji style; # (10.0) FLYING SAUCER

                       2

```
