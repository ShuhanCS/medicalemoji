# Kidney CLDR Compatibility - Primary Sources

Research date: 2026-07-28

## Verified findings

1. The current CLDR English annotations contain `kidney` on U+1FAD8 BEANS:
   `<annotation cp="🫘">beans | food | kidney | legume | small</annotation>`. The immediately following
   short-name annotation is `beans`. No other `kidney` occurrence is present in the current English
   annotation file.
2. CLDR documents keywords as words or short phrases used to search for a character in a user's
   language. Its CLDR 46 release note describes an emoji-search usage model in which words entered in
   a search field determine the emoji shown in the result box.
3. Unicode document L2/25-128 lists three Emoji 19.0 priorities: empirical evidence of use with
   citations; compatibility with social apps, other standards, and/or operating systems; and improving
   the experience of existing emoji users.
4. UTC #185 minutes record that Monarch Butterfly would not have been recommended without its
   compatibility issue and that compatibility was the theme of that year's proposed emoji set.

## Primary sources

- Current CLDR English annotations:
  https://github.com/unicode-org/cldr/blob/main/common/annotations/en.xml
- CLDR emoji names and keyword guidance:
  https://cldr.unicode.org/translation/characters/short-names-and-keywords
- CLDR 46 emoji-search usage model:
  https://cldr.unicode.org/downloads/cldr-46
- ESR priorities for Emoji 19.0, L2/25-128:
  https://www.unicode.org/L2/L2025/25128-esr-priorities.pdf
- UTC #185 minutes, L2/25-226:
  https://www.unicode.org/L2/L2025/25226.htm
- Current Unicode emoji-proposal guidance:
  https://www.unicode.org/emoji/proposals.html

## Proposal-safe inference

Removing `kidney` from the Beans annotations would correct the inaccurate association, but it could
not create an emoji depicting the organ. Encoding Kidney supplies the missing representation and gives
CLDR a semantically accurate character to associate with the search term. This is an inference from the
verified data and the absence of a Kidney character, not a quotation from Unicode.

## Evidence still worth obtaining

Capture reproducible, dated screenshots from Microsoft/Windows and at least one other widely used emoji
search interface. Those exhibits would show whether and how the CLDR mismatch reaches users on named
platforms; no such platform-specific claim should be made before the evidence is captured.
