# Making Emoji Properties a Part of the UCD for Unicode 13.0

Unicode document **L2/19-298**. Authors: Ken Whistler.

**Outcome:** An emoji property/data change filed by a UTC insider.

Source: <https://www.unicode.org/L2/L2019/19298-emoji-props.txt> (retrieved 2026-07-09). Text-layer word count: 618.

---

```text
L2/19-298

Title: Making Emoji Properties a Part of the UCD for Unicode 13.0

Author: Ken Whistler

Date: July 25, 2019

Action: For consideration by the UTC

Background

After discussion by the UTC, it seems advisable to take the steps necessary
to formally incorporate emoji character properties into the UCD for Unicode
13.0. This document catalogs the particular actions required to make that
happen in the 13.0 time frame. Having the emoji properties as a part of the
UCD will simplify certain aspects of their maintenance as part of each
future release, and will regularize their relationship to other character
properties which depend on them.

Details

1. The basic decision to be recorded is a formal decision to promote the
properties defined in UTS #51 to the status of formal character properties
declared and documented as a part of the Unicode Character Database -- hence
an integral part of the Unicode Standard.

The properties in question are the 6 binary properties of emoji characters
defined in emoji-data.txt and documented currently in UTS #51.

These should each be incorporated into the UCD as a *normative* property,
because of their definitional importance for various types of emoji and
emoji sequences, the use of those sequence types in the enumeration of RGI
sets of emoji, and the interaction of emoji with various Unicode
segmentation algorithms.

2. The emoji-data.txt file, which defines all the binary emoji properties,
should be deployed (starting with Unicode 13.0) in the /Public/13.0.0/ucd/
directory, instead of the /Public/emoji/ directory. For simplest rollout and
maintenance, the *entire* emoji data directory, which also includes the 3
data files defining the RGI emoji sequences and emoji-test.txt, should move
at the same time, and all should be deployed to a new subdirectory:
/Public/13.0.0/ucd/emoji/ Note that depending on other UTC decisions, the 3
emoji sequences files will also be defining new properties of the emoji RGI
sequences, so it is appropriate to move them all together into the UCD.

3. The headers of all the emoji data files need to be adjusted to UCD data
file specs.

4. Long and short aliases for each of these properties needs to be added to
PropertyAliases.txt.

5. The text of UTS #51 for Unicode 13.0 needs to be adjusted slightly to
document that the properties are now a part of the UCD, to list the correct
location of the data files, and to correct the references section
accordingly.

6. The text of UAX #44 for Unicode 13.0 needs to be adjusted to correctly
document the new UCD subdirectory, the files it contains, and the list of
all the new properties and their types.

7. Documentation of the emoji character properties needs to be added to UAX
#42 for Unicode 13.0, adjusting the dtd, adding a new subsection on emoji
properties, and correctly defining the attribute list for each.

8. The tooling for UCDXML maintenance needs some adjustment, so that it
parses the data files in the new ucd/emoji/ subdirectory and correctly adds
the new properties and their values to the ucdxml output files.

9. The text of UAX #41 for Unicode 13.0 needs additional entries for the
emoji data files.

10. The release plan for the Unicode Standard (the "Big Red Switch") needs
adjustment to incorporate the planning for the preparation, testing and
release of the additional emoji data files as part of the UCD for each
release.

11. In particular, the ucd/emoji subdirectory needs to be incorporated into
the zipped version of the non-Unihan part of the UCD: UCD.zip.

12. The release plan for UTS #51 needs adjustment to account for any
dependencies between the emoji-specific release steps for defining values
for all the emoji data files, and coordinating with the release cycle for
the UCD.




```
