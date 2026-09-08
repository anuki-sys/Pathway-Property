# Landing pages

Standalone HTML landing pages built to sit as sub pages of
[pathwayprop.com.au](https://www.pathwayprop.com.au/) (Webflow site id
`64d063d22c0ee57d46bfca71`).

## Design tokens

Read from the live Webflow site so these pages match it rather than approximate it.

| Token | Value | Where it comes from |
| --- | --- | --- |
| Page ground | `#BCD3D0` | `.primary-body` — the site's pale sage |
| Surfaces | `#FAF8F5` | `Untitled UI Gray50` — navbar pill, light buttons, dropdowns |
| Card / band fill | `#F5F2EB` | `.article-card`, `.offering-card`, `.review-card` |
| Star gold | `#E9A02C` | the "Rated 5 Stars on Google" row |
| Midnight (ink + outlines) | `#090D2B` | `Midnight` variable |
| Body text | `rgba(9,13,43,.6)` | tag style on `p` |
| Pathway green | `#206E65` | `PATHWAY GREEN` variable |
| On-green text | `#F1EFE9` | green panels and footer |

The site also defines a sand `#ECD4B3` (`Background 01`) and a blanched almond
`#E5DCC9`. **Do not use them as the page ground** — the ground is the sage.

Because the sage is darker than an off-white, the muted inks are set at 70%
and 62% rather than 60% and 45%, which keeps body copy and small labels above
4.5:1 on both the sage and the cream cards.

## House rules the site follows

- **One typeface:** Plus Jakarta Sans, everywhere. `h1` 700 / tight negative
  tracking, `h2` 700, `h3` 600, body 16px / 1.7.
- **Outlines, not shadows:** almost every surface is a `1.5px solid #090D2B`
  border. The one shadow in use is the green cast
  `11px 22px 20px 0 rgba(32,110,101,.25)` (`.service-card`).
- **Big radii:** buttons, inputs and the navbar are fully round (`1000px`);
  cards are 30px or 50px; the footer slab is `100px 100px 0 0`.
- **Navbar:** fixed, 15px from the top, a floating off-white pill with a
  midnight outline — not a full-width sticky bar. The logo is the brand mark
  (dark green field, white path sweeping through it, Pathway green sail) with
  the two-line wordmark set in Plus Jakarta Sans 600/400.
- **Buttons:** primary is green fill + midnight outline + white text;
  secondary is transparent + midnight outline. Both 14px/400, 300ms ease.
- **Footer:** Pathway green slab with rounded top corners.
- **Region map:** four agent pins sit over the map — Tanuj (South East),
  Arshad (West), Nirvan (North) and Abhimaan (East). Each is a teardrop whose
  **tip** is the anchor point, with the headshot in the head circle 87 units
  above it. Hovering or focusing fills the pin cream, lights its region and
  shows the name; clicking selects that person in the agent slider and scrolls
  to it. Both the tip and the head centre are verified inside the right region
  with `isPointInFill`, so moving a region's geometry or a pin means re-running
  that check. The headshots come from the Webflow CDN and fall back to two-letter
  initials if they fail — two letters because Arshad and Abhimaan would
  otherwise both show "A". They sit on a **cream** disc, so a cut-out PNG or a
  dark portrait still reads.
  Each photo is framed at runtime rather than by `preserveAspectRatio`, which
  only offers 0/50/100%: the script measures the source and sets the box so the
  image covers the circle with the focal point 28% down, matching the agent
  slider. The four sources are different shapes, which is why some faces sat
  lower than others before this.
  The map itself is the nine ABS SA4 regions of greater Melbourne, traced from
  boundary paths supplied by the client (`melbournesa4map.html`) and simplified
  with Douglas-Peucker at a 1.1-unit tolerance — sub-pixel at display size, and
  it halves the path data from 43KB to 23KB. Clicking or keyboard-selecting a
  region updates the name on the card beside it. **No region is selected on
  load** — this is the Melbourne page, so no one corner of the city is the
  focus.
  The section is a two-column grid set to `stretch`: the region card carries
  `margin-top:auto` so its bottom edge lands on the map box's, rather than the
  two columns floating centred with dead space above and below. The card holds
  the region name, a fixed row of Melbourne areas (North, East, South East,
  West, Inner Melbourne, and everywhere in between) and the CTA.
  **Check the licence on that boundary data before launch** — if it derives
  from ABS Statistical Area boundaries it is CC BY 4.0 and needs attribution.
- **Motifs:** a "Rated 5 Stars on Google" row above the headline and soft
  white clouds drifting behind the hero, in the spirit of the main site's
  illustrations. The clouds hide below 1080px, where the hero becomes a
  single column and they would land on the headline. A flat-vector scene
  along the hero's bottom edge was tried and removed — with the photo
  composition already in the hero, it made the header too busy.

## The numbers on the page

| Figure | Source | Used on the page |
| --- | --- | --- |
| 90+ inspections attended each week | Deck 1/9 | Hero stat |
| 200+ off-market properties across Melbourne each week | Deck 2/9 | Hero stat |
| 100+ Melbourne off markets every week | Client, 8 Sep | Off-market section heading |
| 100 due diligence reports a day | Client, 8 Sep (deck says 50) | "Why buyers bring us in" |
| 3.7% average discount negotiated | Deck 4/9 | Hero stat only (removed from the value list 8 Sep) |
| 7+ professionals coordinated to settlement | Deck 5/9 | "Why buyers bring us in" |
| 120 hours saved on a typical purchase | Deck 6/9 | Process intro |
| 9 weeks average time to secure | Deck 7/9 | Process intro |
| Over 1,000 properties purchased | Client, 8 Sep | Hero lede, "Why buyers bring us in", FAQ |
| Thousands of families | Client, 8 Sep | "Why buyers bring us in" section lede |

**Three numbers need settling before this goes public.**

1. **Off-markets: 200+ or 100+?** The hero stat says 200+ a week (deck slide
   2/9); the off-market section heading now says 100+ a week (8 Sep changes).
   Both are on the page and they contradict each other in the reader's eye.
2. **Due diligence reports: 50 or 100 a day?** The deck says 50, the 8 Sep
   changes say 100. The page now says 100.
3. **Speed.** Deck slide 7/9's heading says many clients secure "in just 4 to
   5" weeks while its own bullet says "3 to 4 weeks". Neither is on the page —
   only the 9-week average is.

Each figure is an average or a business-wide throughput number, not a promise
to an individual buyer. If this page is going to make these claims publicly,
they need to be substantiable — keep the underlying records.

## House style

**No em dashes anywhere in reader-facing copy.** Use a comma, a full stop or a
colon instead. This applies to body copy, headings, meta description, form
placeholders, `aria-label`s and the JSON-LD blocks, which mirror the FAQ answers
and are easy to miss. Code comments are exempt.

The tone is warm and supportive without giving up the specifics: the reader is
often the decision maker in a household, not a spreadsheet. Lead with what the
choice means to them, then let a number back it up.

## Imagery

Every photo and video slot is a `<figure class="shot">`. The figure paints a
green rooflines placeholder with a label describing the shot; an `<img>` sits
on top of it, so dropping a real photo in is a one-line change and a missing
photo degrades to the labelled placeholder rather than a broken image.

The hero carries the "purchased off-market" client photo from the Webflow
CDN, framed 4:3.6 with `object-position: 50% 46%` so the sky and footpath are
trimmed and the faces and the sign sit centred.

Eight headshots are also served from the Webflow CDN: Tanuj, Arshad, Nirvan
and Abhimaan in the agent slider, and Rahul, Shamindri, Ali Al Hilo and
Shashyani in Meet the team. They sit at `object-position: 50% 28%`, which keeps a face high in a
tall frame rather than centred.

Two photos are **inlined as data URIs** rather than pulled from the CDN, so the
page still shows them when it is opened as a single file or in a preview that
blocks remote images:

| Slot | Inlined file | Note |
| --- | --- | --- |
| Hero inset (square, beside the main hero photo) | `assets/keys-handover.jpg` | Keys in an open doorway; the keyring's green happens to match the brand |
| "Why buyers bring us in" | `assets/approaching-home.jpg` | A buyer walking up to a front door. The frame has **no aspect ratio**: the grid is `align-items: stretch`, so it takes whatever height the list beside it ends up being and the two columns always end level. Below 900px the columns stack and it falls back to 4:5. |

Both are in `assets/` at exactly the bytes that are inlined. When this moves
into Webflow, upload them to the site asset library and replace each data URI
with its CDN URL — data URIs are a preview convenience, not how the live page
should ship.

Both are Unsplash stock (João Emanuel; Jakub Żerdzicki) and read as stock.
Swap them for real Pathway photography when there is some.

Still needed: a headshot for **Rumeysa** and the "Recent buys" strip, which
must be actual clients. The podcast thumbnail is wired to the Webflow CDN.

Role chips are solid once the role is confirmed and dashed while it is still a
placeholder, so an unconfirmed card is obvious at a glance.

"Recent buys" is an auto-scrolling marquee. Its tiles are written out twice so
the loop is seamless: **whatever you change in the first set, change in the
second**. Six tiles is the target; three works too. It pauses on hover and on
focus, and becomes a plain horizontal scroller under reduced motion.

Candidate assets already on the site (from the Webflow asset library):
`tom-rumble-…`, `dillon-kydd-…`, `r-architecture-…`, `pat-whelen-…`,
`blaire-harmon-…`, `esther-zheng-…`, `cristine-enero-…`, `opollo-photography-…`,
plus `Gal 1–5.webp` and `Hero 1–4.webp`.

## Pages

| File | Intended path | Status |
| --- | --- | --- |
| `buyers-agent-melbourne.html` | TBC (e.g. `/melbourne`) | Draft |

This started as a Melbourne South East page and was widened to cover all of
Melbourne on 8 Sep. A separate South East page is still to be built; when it is,
it inherits this structure and narrows the copy, the map and the team back down.

### Open items on the Melbourne page

- Photography and video testimonials for all image slots.
- Booking calendar links for Arshad, Nirvan and Abhimaan — only Tanuj's
  (`calendar.app.google/uVUJEXzLsU1i73S97`) is wired; the others show a
  "calendar link to confirm" state.
- Rumeysa's full name and role. The other four in Meet the team are confirmed:
  Shashyani de Silva (Client Success Specialist), Rahul Vilvarajah (Property
  Operations Specialist), Shamindri Jayawarna (Settlement Specialist) and Ali
  Al Hilo (Property Analyst).
- Form endpoints: the off-market, booking and newsletter forms are marked up
  but not wired to a handler.
- Real YouTube and Spotify links on the podcast section (both are `#`).
- The nav logo is an inline SVG redraw of the brand mark. Swap it for the
  official logo file before this goes live — on the Webflow build it will use
  the site's own logo asset anyway.
- Nav submenu contents for About, Services, Partners and Event — the carets
  match the live nav but the items themselves come from the site's global
  navbar component in Webflow, which isn't readable through the API.
- The three other areas in the "Where we buy" nav dropdown (East, North,
  West) are marked "coming soon" and need real URLs once those pages exist.
  Note this sits slightly against the 3 Sep call, which asked for coverage to
  stay open-ended — the page body no longer assigns agents to corridors, but
  the nav dropdown still lists locations because that is where the page lives.
