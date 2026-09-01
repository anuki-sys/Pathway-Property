# Landing pages

Standalone HTML landing pages built to sit as sub pages of
[pathwayprop.com.au](https://www.pathwayprop.com.au/) (Webflow site id
`64d063d22c0ee57d46bfca71`).

## Design tokens

Read from the live Webflow site so these pages match it rather than approximate it.

| Token | Value | Where it comes from |
| --- | --- | --- |
| Page ground | `#FAF8F5` | `Untitled UI Gray50` — the site's off-white, also its navbar fill |
| Card / band fill | `#F5F2EB` | `.article-card`, `.offering-card`, `.review-card` |
| Midnight (ink + outlines) | `#090D2B` | `Midnight` variable |
| Body text | `rgba(9,13,43,.6)` | tag style on `p` |
| Pathway green | `#206E65` | `PATHWAY GREEN` variable |
| On-green text | `#F1EFE9` | green panels and footer |

The site also defines a sand `#ECD4B3` (`Background 01`) and a blanched almond
`#E5DCC9`. **Do not use them as the page ground** — the brief is an off-white
page, not a peach one.

## House rules the site follows

- **One typeface:** Plus Jakarta Sans, everywhere. `h1` 700 / tight negative
  tracking, `h2` 700, `h3` 600, body 16px / 1.7.
- **Outlines, not shadows:** almost every surface is a `1.5px solid #090D2B`
  border. The one shadow in use is the green cast
  `11px 22px 20px 0 rgba(32,110,101,.25)` (`.service-card`).
- **Big radii:** buttons, inputs and the navbar are fully round (`1000px`);
  cards are 30px or 50px; the footer slab is `100px 100px 0 0`.
- **Navbar:** fixed, 15px from the top, a floating off-white pill with a
  midnight outline — not a full-width sticky bar.
- **Buttons:** primary is green fill + midnight outline + white text;
  secondary is transparent + midnight outline. Both 14px/400, 300ms ease.
- **Footer:** Pathway green slab with rounded top corners.

## Imagery

Every photo and video slot is a `<figure class="shot">`. The figure paints a
green rooflines placeholder with a label describing the shot; an `<img>` sits
on top of it, so dropping a real photo in is a one-line change and a missing
photo degrades to the labelled placeholder rather than a broken image.

Three slots are already wired to existing site assets as a starting point
(hero, hero inset, good-fit). Everything else needs real photography —
particularly the proof strip and the video testimonials, which must be actual
clients, and the agent and team portraits.

Candidate assets already on the site (from the Webflow asset library):
`tom-rumble-…`, `dillon-kydd-…`, `r-architecture-…`, `pat-whelen-…`,
`blaire-harmon-…`, `esther-zheng-…`, `cristine-enero-…`, `opollo-photography-…`,
plus `Gal 1–5.webp` and `Hero 1–4.webp`.

## Pages

| File | Intended path | Status |
| --- | --- | --- |
| `buyers-agent-melbourne-south-east.html` | TBC (e.g. `/melbourne-south-east`) | Draft |

### Open items on the south east page

- Photography and video testimonials for all image slots.
- Corridors for Arshad, Nirvan and Abhimaan (only Tanuj's is confirmed).
- Booking calendar links for Arshad, Nirvan and Abhimaan — only Tanuj's
  (`calendar.app.google/uVUJEXzLsU1i73S97`) is wired; the others show a
  "calendar link to confirm" state.
- Individual roles for Rahul, Shamindri, Ali Al Hilo, Rumeysa and Shashyani.
- Form endpoints: the off-market, booking and newsletter forms are marked up
  but not wired to a handler.
- Interactive corridor map to replace the placeholder SVG.
- Nav submenu contents for About, Services, Partners and Event — the carets
  match the live nav but the items themselves come from the site's global
  navbar component in Webflow, which isn't readable through the API.
- The three other corridors in the "Where we buy" dropdown (East, North,
  West) are marked "coming soon" and need real URLs once those pages exist.
