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
