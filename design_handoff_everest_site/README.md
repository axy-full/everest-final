# Handoff: Everest Entertainment Website (Editorial Poster Redesign)

## Overview
A 5-page marketing site for Everest Entertainment — a Mumbai-based Marathi & Hindi production house (est. 2000) — migrated 1:1 in content from the previous deployment (https://everest-site-nu.vercel.app) and redesigned in a white, editorial cinema-poster direction: condensed display caps (Anton), technical mono labels (IBM Plex Mono), thin black rules and frames, oversized numerals, scrolling marquee strips, film-grain texture, letterboxed stills, and grayscale-to-color hover posters. Everest blue is the only accent color.

## About the Design Files
The files in this bundle are **design references created in HTML** — prototypes showing intended look and behavior, not production code to copy directly. They are authored as "Design Component" files (`*.dc.html`) for a proprietary preview runtime (`support.js`, not included): the markup between `<x-dc>` and `</x-dc>` is the template (plain HTML with inline styles; `{{ name }}` holes are data bindings), and the `<script data-dc-script>` class at the bottom holds the page's data arrays and interaction logic. Both read cleanly as source.

**The task is to recreate these designs in the target codebase's existing environment** (React, Next.js, Vue, etc.) using its established patterns — or, if no environment exists yet, choose an appropriate framework (a static-friendly React/Next.js or Astro site fits this content) and implement the designs there.

Template-syntax cheat sheet for reading the files:
- `{{ x }}` — bound value from the logic class `renderVals()`
- `<sc-for list="{{ arr }}" as="item">…</sc-for>` — loop
- `<sc-if value="{{ flag }}">…</sc-if>` — conditional render
- `style-hover="…"` — hover-state styles (implement as `:hover` CSS)
- `<helmet>` — document head content (fonts, keyframes, body resets)

## Fidelity
**High-fidelity.** Colors, typography, spacing, borders, and interactions are final. Recreate pixel-perfectly. All copy is migrated verbatim from the client's previous site — do not rewrite it.

## Global System (all pages)

### Design Tokens
Colors:
- Ink / primary text: `#0a0a0a`
- Canvas: `#ffffff`
- Everest blue (sole accent — links, numerals, labels, hovers): `#0A4DA6`
- Blue on dark backgrounds: `#6FA8FF`
- Blue hover (buttons): `#0E5FC7`
- Body copy: `#424245`; secondary: `#6e6e73`; faint: `#a1a1a6`
- Hover fill / quiet surface: `#f5f5f7`
- Image placeholder bg: `#f2f2f3`
- Dark bands: `#0a0a0a`; rules on dark: `rgba(255,255,255,.25–.35)`
- Selection: blue bg, white text

Typography:
- Display: **Anton** (Google Fonts, single weight 400), always `text-transform: uppercase`, `line-height .92–.96`, tight sizes via clamp (H1 up to `clamp(46px, 7.2vw, 116px)`; giant hero wordmark `clamp(84px, 16.5vw, 252px)`; section H2 `clamp(38px, 5.4vw, 76px)`; card titles 19–22px; oversized numerals 34–96px)
- Labels/UI: **IBM Plex Mono** 400/500/600, 10.5–13px, `letter-spacing .04–.12em`, uppercase. Eyebrow convention: `( Section name )` left + `/ 01` index right, sitting on a 1px black rule
- Body: system Helvetica stack (`-apple-system, 'Helvetica Neue', Helvetica, Arial`), 13.5–17px, line-height 1.5–1.7
- NO serif fonts anywhere. No border-radius anywhere (sharp corners; buttons are rectangles)

Rules & frames:
- Section top rules: `1px solid #0a0a0a`; footer top rule: `2px solid #0a0a0a`
- Framed cards: `border: 1px solid #0a0a0a`, white bg, padding 18–28px
- Images carry an inset hairline: `outline: 1px solid #0a0a0a; outline-offset: -1px` (white 30% on dark bands)
- Stat/value strips: grid rows bounded by 1px rules top/bottom with 1px vertical dividers (`border-left` per cell)

Spacing: content max-width 1200px, centered; page gutter `clamp(20px, 3.5vw, 40px)`; section bottom padding ~110px; section rule → header gap 46px.

Buttons:
- Primary: black rectangle, white mono uppercase 12.5px `.12em`, padding 16px 28–30px, label ends with `→`; hover bg `#0A4DA6`
- Ghost: 1px black frame, transparent; hover inverts to black/white
- Text links: mono uppercase 12.5px, blue, `→` suffix

### Signature motifs
1. **Film grain**: full-viewport fixed overlay, `pointer-events:none`, `opacity:.05`, z-index above everything, tiled 200×200 SVG `feTurbulence` noise (data URI in the files). Plain overlay — deliberately NO `mix-blend-mode` (it forced full-page re-blending every animation frame; keep it removed).
2. **Marquee strips**: full-width black bands, Anton 22–26px white uppercase items separated by blue `▲`, content duplicated twice inside a `width:max-content` flex row animated `translateX(0 → -50%)` linear infinite 30s. One per page below the hero.
3. **Hover-reveal posters**: images default `filter: grayscale(1)`, on hover `grayscale(0)` (+ `translateY(-4px)` in the Films library), `transition: filter .35–.4s`.
4. **Oversized numerals**: Anton, blue or ink, for stats (56–96px), section-card indices (44px), division rows (34–52px), the giant "50" on Films (up to 240px).
5. **Letterboxed stills**: hero carousel sits inside a black band with ~18–34px black bars above/below.
6. **Scroll fades**: section headers/grids use `animation: fadeUp .9s both; animation-timeline: view(); animation-range: entry 0% entry 42%` (scroll-driven; degrades to a one-shot fade where unsupported). Keyframes: fadeUp (opacity 0→1, translateY 26px→0), fadeIn (opacity).

### Navigation (all pages)
- Transparent absolute bar (no fixed positioning; it scrolls away), height 64px: Anton wordmark "EVEREST ▲" (17px, `.08em`, blue triangle) top-left; burger top-right (two 20×2px bars). White variant over dark heroes (About, Jallosh).
- Burger opens a full-screen overlay: `rgba(255,255,255,.96)` + `backdrop-filter: blur(24px)`, wordmark + `×` close in the same 64px header row, then a stacked link list — each row `1px` top rule, mono index `/01…/05`, Anton link `clamp(38px, 6vw, 64px)` uppercase (Home, Films, About, Jallosh, Contact; current page in blue), then `INFO@EVERESTENT.IN` mono small. Fade-in .25s.

### Footer (all pages)
2px black top rule; single row (wrap-friendly): Anton wordmark · mono uppercase links (Films, About, Jallosh, Contact, info@everestent.in) · mono `© 2026 EVEREST ENTERTAINMENT LLP · MUMBAI` in `#a1a1a6`.

## Screens / Views

### 1. Home (`Home.dc.html`)
- **Hero**: giant centered Anton wordmark "EVEREST ▲" (`clamp(84px,16.5vw,252px)`, blue triangle at .32em size); beneath it a spec strip — 1px rules top/bottom, three mono items justified: `( A Marathi & Hindi entertainment house )` / `Mumbai ▲ Since 2000` (blue) / `260+ films · 50 nataks · 800+ songs`.
- **Letterboxed carousel**: full-width black band; inside, a horizontal card track (`gap:22px`, `padding-left: calc(50% - min(40vw,600px))` so the active card centers) translated by `-idx * (min(80vw,1200px) + 22px)` with `.95s cubic-bezier(.32,.72,0,1)`. 7 slides: 21:10 cover-image cards `min(80vw,1200px)` wide, inactive at `opacity:.45; scale(.97)`, white 30% inset outline. Each card has a bottom-left black caption tag: mono white title + blue year. Slides (title/year/file): Mee Shivajiraje Bhosale Boltoy/2009, Pawankhind/2022, Gulkand/2025, Tukaram/2012, Mumbai Pune Mumbai/2010, Premachi Goshta/2013, Daagdi Chaawl/2015 (files `assets/heros/hero-*-wide.jpg`). Autoplay every 5s (tweakable), resets on manual nav.
- **Carousel controls**: below band — `←` and `→` buttons (44×40px, 1px black frame, hover inverts) at the row edges, 7×7px square dots centered (active blue, idle `#d2d2d7`).
- **Intro**: mono eyebrow `( Stories that reach the summit )`, H1 "Stories that reach the summit." `clamp(46px,7vw,108px)`, dek (verbatim), primary button "Explore our films →" + ghost "Our story".
- **Marquee**: PRODUCTION ▲ SYNDICATION ▲ DIGITAL ▲ MUSIC repeated.
- **Stats strip**: 4 cells (25+ Years in motion / 260+ Films in the collection [blue] / 50 Iconic Nataks / 800+ Songs), Anton `clamp(56px,6.5vw,96px)`, mono labels.
- **Who we are** `/01`: centered H2 + lead paragraph; two further paragraphs behind a mono expander button "READ THE FULL STORY +" / "CLOSE −"; link "More about us →".
- **Divisions accordion** `/02` ("Four divisions, one summit."): 4 rows bounded by 1px rules — blue Anton number (01–04), Anton title (Production / Syndication / Digital / Music), one-line gray dek, blue mono `+`/`−`; row hover `#f5f5f7`; one panel open at a time. Each panel: 250px poster (2:3, hairline outline) + content column with mono sub-labels `( … )`, verbatim paragraphs, 2-col capability lists (rule-topped items), framed cards (title categories, where-to-watch homes, indie artists), chip rows (jukeboxes: 1px framed mono chips), link lists (13 YouTube channels with tag/name/desc/`→`; 8 FAST channels), mini stat rows (Anton 34px), and a closing mono link. All copy verbatim from the source site's Production/Syndication/Digital/Music pages (data lives in the logic class arrays).
- **Jallosh band** `/03`: black; Jallosh logo PNG left, Anton H2 "Jallosh Entertainment." + verbatim dek + white button "Explore Jallosh →" (hover blue).
- **Slate** `/04`: H2 left + "View full library →" right; 4 hover-reveal posters (Picasso 2021 · 67th NFA special mention; Aamhi Doghi 2018; Baapjanma 2017; Aajcha Divas Majha 2013 · National Award) with mono caption rows (title left, blue year right).
- **Watch** `/05`: centered H2 "New launches & the catalogue." + dek; 8 hover-reveal 16:9 YouTube thumbnails with blue mono category labels (New launch ×3, Movies on demand, Most popular · song, Drama · natak, Featured ×2) linking to the videos; closing network link.
- **Values** `/06`: 4-cell rule-bounded grid (01 Heritage / 02 Reach / 03 Craft / 04 Catalogue — blue Anton 44px numerals, Anton 22px titles, gray body); then centered pull-quote in Anton `clamp(24px,3.4vw,44px)`: "At Everest, we are committed to living our values regardless of the challenges we face." — Everest Entertainment.
- **CTA**: 1px-framed box, `( Let's talk )`, H2 "Have a story, a title, or a screen?", dek, "Get in touch →".

### 2. Films (`Films.dc.html`)
- Header: rule row `( The Everest Collection )` / breadcrumb `Home / Films & Library`; centered H1 "Over 260 films. One collection." + verbatim intro; expander "READ ABOUT THE LIVING LEGACY +" reveals two verbatim paragraphs (incl. the Dada Kondke collection).
- Marquee: 260+ FILMS ▲ 50 NATAKS ▲ 800+ SONGS ▲ SIX DECADES.
- **Sticky filter bar** (`top:0`, white 92% + blur, 1px black bottom rule): centered mono chips — All films / 2020s / 2010s / 2000s / 90s / 80s / 70s / 60s; 1px black frames; active = black bg, white text.
- Count line: `[ 155 titles · 1968 — 2021 ]` (updates with filter).
- **Library grid**: `repeat(auto-fill, minmax(158px, 1fr))`, gap 26×22px; all 155 posters (2:3 cover, hairline outline, grayscale→color + lift on hover, lazy-loaded), mono caption: uppercase title left, blue year right. The full 155-entry data array (year, title, poster filename) is embedded in the logic class of `Films.dc.html` — treat it as the content source of truth. Captions can be toggled off (design option).
- Note line + "Request the full catalogue" link (verbatim).
- **Nataks band** (black): rule row `( The Everest Collection · Nataks )` `/02`; giant blue Anton "50" (`clamp(130px,17vw,240px)`) + mono label left; right column H2 "50 iconic Nataks." + two verbatim paragraphs + faint mono note.
- Stats strip (260+ blue / 50 / 800+ / 25+) and framed CTA "Want the full catalogue?" as on Home.

### 3. About (`About.dc.html`)
- **Hero**: 64vh full-bleed `about-header.jpg`, grayscale, veil gradient `rgba(0,0,0,.55) → .38 (40%) → .72`; white nav variant; bottom-left: mono `( About Everest ) — Home / About` in `#6FA8FF`, Anton H1 "A home for Marathi storytelling." `clamp(42px,7vw,110px)` white, verbatim dek.
- Marquee (on black, top rule): SINCE 2000 ▲ MUMBAI ▲ 25 YEARS, ONE CLIMB ▲ THE JOY OF MAHARASHTRA.
- **Journey** `/01`: centered H2 "25 years, one climb.", lead verbatim + 3 more paragraphs behind "READ THE FULL JOURNEY +".
- **Founder** `/02`: 360px 4:5 grayscale portrait (`founder.jpg`) with mono figure caption `Fig. 01 / Founder`; right column Anton H2 "Sanjay Chhabria.", first paragraph visible + 4 more behind "READ THE FULL FOUNDER'S NOTE +"; signature block (rule-topped: Anton "Sanjay Chhabria" + mono role).
- **What we do** `/03`: 4 rule-bounded link cells (01 Production … 04 Music, verbatim one-liners) linking to Home; hover `#f5f5f7`. Below: stats strip (2000 Founded / 260+ blue / 50 / 800+).
- **Values** `/04`: 4 rule-bounded cells — Story First / Rooted & Reaching / Integrity / Built to Last (verbatim copy).
- **Media room** `/05`: 4 framed cards — Press Releases (Coming soon), In the News (Coming soon), Brand Assets (mailto, "Request · Email us →"), Media Contact (mailto, "Press · Get in touch →").
- Framed CTA "Join the climb."

### 4. Jallosh (`Jallosh.dc.html`)
- **Hero** (black): rule row `( The Marathi Entertainment Ecosystem )` / `Home / Jallosh`; centered Jallosh logo PNG, Anton H1 "Jallosh Entertainment." `clamp(46px,7.2vw,116px)` white, verbatim dek. White nav variant.
- Marquee: JALLOSH ▲ FAST CHANNELS ▲ SMART TVS ▲ PRIME VIDEO CHANNELS ▲ THE APP.
- **Same summit, new trail** `/01`: centered H2 + two verbatim paragraphs + "Work with Jallosh →".
- **Statement box**: 1px frame; Anton `clamp(26px,4vw,54px)`: "More than a streaming platform — JALLOSH [blue] is the Marathi entertainment ecosystem: films, theatre, music and original programming in one destination." + mono subline verbatim.
- **On every screen** `/02`: 4 rule-bounded cells (01 FAST Channels / 02 Smart TVs / 03 Amazon Prime Video Channels / 04 The JALLOSH App — verbatim descriptions, blue mono "Launching soon"); two framed mono chips "Download the App — coming soon" / "Watch on your Smart TV — coming soon".
- **On every platform** `/03`: 4 framed cards — LinkedIn "Jallosh Entertainment", Instagram "@jalloshent", YouTube "@JalloshEntertainment", Website "jalloshent.in" — each marked "Handle TBC — placeholder" (links intentionally dead until confirmed).
- Framed CTA "Have a story for Jallosh?".

### 5. Contact (`Contact.dc.html`)
- Header: rule row `( Contact us )` / `Home / Contact`; centered H1 "Let's create the next chapter of Marathi entertainment — together." + verbatim dek.
- **Two columns** (80px gap, wrapping): LEFT `/01` "Start here." — form: Name, Email, Company/Org (text), "I'm here about" select (General Enquiries / Content Acquisition & Production / Content Licensing & Distribution / Platform Partnerships / Advertising & Brand Collaborations / Press & Media), Message textarea; 1px black inputs, sharp corners, mono uppercase labels, blue focus outline; submit "Send message →" (black→blue) composes a `mailto:info@everestent.in` with the field values (no backend — replace with a real endpoint in production); faint mono disclosure line underneath. RIGHT `/02` "The details." — Email `info@everestent.in`; Studio address (Everest Entertainment LLP, Mumbai, Maharashtra, India); rule-topped "Direct to a division" chip row (mailto: production@ / licensing@ / digital@ / music@everestent.in — 1px frames, hover invert); rule-topped Follow links (YouTube Everest Talkies, X @sgchhabria, LinkedIn Sanjay Chhabria).
- **What brings you here?** `/03`: 5 framed cards (blue Anton numeral, Anton title, verbatim body).
- **FAQ** `/04`: 14 accordion rows (1px rules; question 16px semibold left, blue mono `+`/`−` right; hover `#f5f5f7`; one open at a time, answer 15px `#424245`). All 14 Q&As verbatim in the logic class of `Contact.dc.html`.

## Interactions & Behavior
- Hero carousel: 5s autoplay (configurable 3–10s, on/off), wraps; arrows/dots set index and reset the timer; track/card transitions `.95s cubic-bezier(.32,.72,0,1)`; inactive cards dim+shrink.
- Accordions (divisions, FAQ): single-open; open panels fade in `.4–.5s`; +/− sign swap.
- Expanders ("Read the full story +"): toggle hidden verbatim paragraphs; label swaps to "Close −".
- Burger menu: toggles fixed overlay; page scroll behind should lock in production.
- Hover: posters/thumbs grayscale→color; buttons black→blue (or invert for ghost/white); framed link-cards fill `#f5f5f7`; global link hover opacity .75.
- Films filter: instant client-side filter by decade bucket (2020s ≥2020, 2010s, 2000s, 90s, 80s, 70s, 60s <1970); count label updates.
- Marquees: continuous, linear, 30s per half-loop; duplicate content for the seamless wrap; respect `prefers-reduced-motion` in production.
- Scroll fades: subtle only — do not add heavier motion. No opening/intro video (explicit client requirement).

## State Management
Per page, all client-side and trivial: `carouselIndex` (+ autoplay timer), `menuOpen`, `openDivision: null|0–3`, `whoExpanded`, `legacyExpanded`, `journeyExpanded`, `founderExpanded`, `openFaq: null|0–13`, `decadeFilter`. Films/FAQ/division content are static arrays (in the `.dc.html` logic classes). No data fetching.

## Assets
All imagery is currently **hotlinked from the previous deployment** — download and self-host for production:
- Base: `https://everest-site-nu.vercel.app/assets/`
- Hero stills: `heros/hero-{me-shivajiraje|pawankhind|gulkand|tukaram|mumbai-pune-mumbai|premachi-goshta|daagdi-chaawl}-wide.jpg`
- 155 posters: `posters/<slug>.jpg|png` — complete filename list in the `Films.dc.html` data array
- Logos: `logos/jallosh-logo.png` (plus 13 channel logos `logos/channel-*.png` on the old site, currently unused)
- About: `about-header.jpg`, `founder.jpg`
- YouTube thumbnails: `https://img.youtube.com/vi/<id>/hqdefault.jpg` (ids in Home.dc.html)
- Fonts: Google Fonts — Anton (400), IBM Plex Mono (400/500/600)
- Grain texture: inline SVG feTurbulence data URI (in each file's overlay div)
- The EVEREST wordmark is set in live type (Anton), not an image. No real logo file was provided — swap in the brand mark when available.

## Performance Notes
- Do NOT put `mix-blend-mode` on the full-viewport grain overlay (previously caused whole-page re-blending during marquee/carousel animation).
- Lazy-load the 155-poster grid (`loading="lazy"` in the reference); consider `content-visibility:auto` per grid row and pausing marquees off-screen.

## Files
- `Home.dc.html` — home page (hero wordmark, letterboxed carousel, divisions accordion with all four division pages' verbatim content, Jallosh band, slate, watch grid, values, CTA)
- `Films.dc.html` — library (155-poster data array, decade filter, Nataks band)
- `About.dc.html` — journey, founder's note, what-we-do, values, media room
- `Jallosh.dc.html` — consumer brand page
- `Contact.dc.html` — form, details, help topics, 14-item FAQ (verbatim data array)

An earlier Apple-style iteration of the same content exists in the project's `archive/` folder (not included here) if a softer direction is ever needed.
