@AGENTS.md

# Medical Emoji - medicalemoji.org

## Site
- Next.js 16 App Router, Tailwind CSS v4, React 19
- Colors: hero gold #ffcf6d, CTA blue #3452ff, CTA pink #ff1053, footer #313233
- Contact: info@medicalemoji.org

## Structure
- Data files in `src/data/` (emoji.ts, team.ts, press.ts)
- Shared components in `src/components/` (Header, Footer, Hero, EmojiGrid, Timeline, ContactForm, SupportList)
- Dynamic emoji pages at `/emoji/[slug]` using `generateStaticParams`
- Pages: /, /team, /campaign, /visual-analogue-scale, /resources, /emoji/[slug]

## Writing emoji proposals (MANDATORY)

Use `docs/proposals/TEMPLATE-emoji-proposal.md`. Do not write a proposal from scratch, and do not copy the
2020 drafts in `docs/proposals/archive-2020-emojination-drafts/` — none of them ever reached Unicode's
document register.

Evidence: `docs/plans/2026-07-09-winners-vs-losers.md` (55 encoded proposals vs 29 that were not).

- Structure wins nothing. 94% of winners have an exclusion section; so do 93% of losers.
- Under 1,200 words of prose, over 20 images. Losers write 60% more and show a third fewer screenshots.
- Write `N/A` for Completeness and Compatibility unless there is a compelling example.
- Never cite petitions, hashtags, Instagram, or a `Frequently Requested` section. Disallowed evidence.
- Never use awareness, stigma, or advocacy language. It appears 13x more often in proposals that failed.
- Never write "the heart and lungs were encoded, so the kidney should be." Textbook Faulty Comparison.
- Draft the Open-ended answer first, naming the neighbours we will not propose. If it cannot be written
  honestly, the proposal is not ready. It forbids filing kidney, liver and stomach together.
- The submission form rejects company names. A named individual must submit.
- Artwork must contain no text, digits or barcodes. That is an automatic decline.

Facts that must not be repeated as claims: individual UTC delegates and ESR working-group membership are
not published anywhere. Do not name them. See `docs/strategy/unicode-map-and-strategy.md`.
