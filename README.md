# Everest Final Version

Everest Entertainment — editorial cinema-poster redesign. Built from the Claude-Code design
handoff in `design_handoff_everest_site/` (5 `.dc.html` reference files + spec README),
recreated 1:1 as a static multi-page site.

**Design language:** white canvas, ink `#0a0a0a`, Everest blue `#0A4DA6` as the sole accent
(`#6FA8FF` on dark). Anton display caps + IBM Plex Mono labels, system Helvetica body.
Thin 1px rules and frames, sharp corners everywhere, film-grain overlay (no blend mode),
black marquee strips, grayscale→color hover posters, letterboxed hero carousel,
scroll-driven fade-ups (`animation-timeline: view()`, degrades to one-shot fades).

## Pages

| Route      | File           | Notes |
|------------|----------------|-------|
| `/`        | `index.html`   | Giant wordmark hero, 7-slide letterboxed carousel (5s autoplay), divisions accordion carrying all four division pages' verbatim content, Jallosh band, slate, watch grid, values, CTA |
| `/films`   | `films.html`   | 202-poster library (155 handoff posters + 47 films from the V3 artwork delivery), sticky decade filter (All/2020s…60s) with live count, Nataks band |
| `/about`   | `about.html`   | 64vh grayscale hero, journey + founder's note expanders, what-we-do, values, media room |
| `/jallosh` | `jallosh.html` | Black hero with logo, statement box, on-every-screen cells, platform placeholders |
| `/contact` | `contact.html` | mailto-composing form, division chips, 5 help topics, 14-item FAQ accordion |

All copy migrated verbatim from the previous deployment (everest-site-nu.vercel.app) via the
handoff. Everything self-hosted in `assets/` (~127MB) — nothing hotlinks the old deployments:

- 155 library posters + 7 wide & 7 tall hero stills + about/founder photos (from `~/Downloads/everest-site`)
- **`assets/art/` — the 100-film client artwork delivery migrated from Everest V3**
  (`~/Downloads/everest-site-v2`, live at everest-v3.vercel.app): card (3:4 box art) / still
  (16:9 textless) / key (16:9 with title lockup) per film. Its index lives at `data/art-data.js`
  (`window.ART`: slug → title, year, Devanagari display title, art paths, `inData` flag marking
  films already covered by the old 155-poster set). The 47 films **without** `inData` are wired
  into the `/films` grid via their card art (Gulkand 2025, Premachi Goshta 2 2025, Naach Ga
  Ghuma 2024, Chandramukhi 2022, Mumbai Pune Mumbai 3, Boyz 2, …) — library now spans 1968–2025.
  Stills/keys are staged for future hero/slate use.
- `assets/yt/` — the watch-grid thumbnails, downloaded from YouTube. Three of the handoff's
  eight videos were deleted on YouTube (`qP5OPfxCcKU`, `FdLjn74JWzY`, `ht4RhEPH_tU`); they were
  replaced with alive tiles from the old site's own curated grid (`N2hEFyXAe0A`, `fywuFgnYYfM`
  new-launch slots, `DRCpiuuuQnw` Baghtos Kay Mujara Kar for the movies-on-demand slot).
- `assets/logos/` — full brand set (Everest color/white/icon, Jallosh logo + banner, 13 YouTube
  channel logos; the channel logos are unused by this design but kept as site data).

## Run locally

```bash
python3 serve.py   # http://localhost:4552 — clean URLs + no-store cache headers
```

`vercel.json` has `cleanUrls: true` so extensionless links work identically on Vercel.

## Capture helpers (in `site.js`)

- `?capture` — kills all animation/transitions, forces lazy images eager
- `&top=N` — in capture mode shifts the page via `body { transform: translateY(-N px) }`
  (real scroll paints white in headless screenshots); outside capture mode does a normal scroll
- `&open=N` — opens the Nth accordion item (home divisions / contact FAQ)
- `&xtra` — expands every "Read the full …" block

Headless Chrome gotcha: layout has a ~500px minimum width, so mobile-width screenshots
lay out at 500px and crop — use a real browser/device emulation for mobile proof.

## Structure

- `styles.css` — full design system (tokens, nav/menu, marquee, stats, cells, cards, per-page sections)
- `site.js` — burger menu (scroll-locks body), single-open accordions, expanders, hero carousel
  (autoplay pauses under `prefers-reduced-motion`), decade filter, contact mailto compose, capture helpers
- Film grid data lives in `films.html` (generated from the handoff's 155-entry array; each card
  carries `data-y` for the decade filter)
