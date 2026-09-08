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
- **Region map:** the nine ABS SA4 regions of greater Melbourne, traced from
  boundary paths supplied by the client (`melbournesa4map.html`) and simplified
  with Douglas-Peucker at a 1.1-unit tolerance — sub-pixel at display size, and
  it halves the path data from 43KB to 23KB. Clicking or keyboard-selecting a
  region updates the name and the call to action on the card beside it. South
  East is selected on load.
  The section is a two-column grid set to `stretch`: the region card carries
  `margin-top:auto` so its bottom edge lands on the map box's, rather than the
  two columns floating centred with dead space above and below. The card holds
  the region name, a fixed row of location tags (Ringwood, Glen Waverley,
  Brighton, Oakleigh, and everywhere in between) and the CTA — the tags are
  deliberately spread across Melbourne rather than tied to the selected region.
  **Check the licence on that boundary data before launch** — if it derives
  from ABS Statistical Area boundaries it is CC BY 4.0 and needs attribution.
- **Motifs:** a "Rated 5 Stars on Google" row above the headline and soft
  white clouds drifting behind the hero, in the spirit of the main site's
  illustrations. The clouds hide below 1080px, where the hero becomes a
  single column and they would land on the headline. A flat-vector scene
  along the hero's bottom edge was tried and removed — with the photo
  composition already in the hero, it made the header too busy.

## The numbers on the page

Every figure comes from the **Owner Occ Sales Deck** and nowhere else. Do not
invent, round up, or extrapolate from them.

| Figure | Deck slide | Used on the page |
| --- | --- | --- |
| 90+ inspections attended each week | 1/9 Local market intelligence | Hero headline + stat, "Why buyers bring us in" |
| 200+ off-markets across Melbourne each week | 2/9 Sourcing | Hero stat, off-market panel |
| 50 due diligence reports produced daily | 3/9 DD & pricing | "Why buyers bring us in" |
| 3.7% average discount negotiated | 4/9 Negotiation | Hero lede + stat, "Why buyers bring us in", Recent buys |
| 7+ professionals coordinated to settlement | 5/9 Settlement & process | "Why buyers bring us in", process step 6 |
| 120hrs+ saved on a typical purchase | 6/9 Save time | Process intro |
| 9 weeks average time to secure | 7/9 Speed to result | Hero lede, process intro, Recent buys |

**The deck contradicts itself on one figure.** Slide 7/9's heading says many
clients secure "in just 4 to 5" weeks while its own bullet says "3 to 4 weeks".
Neither is on the page — only the 9-week average is. Settle which is right
before anyone uses the faster number in marketing.

Each figure is an average or a business-wide throughput number, not a promise
to an individual buyer. If this page is going to make these claims publicly,
they need to be substantiable — keep the underlying records.

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
| `buyers-agent-melbourne-south-east.html` | TBC (e.g. `/melbourne-south-east`) | Draft |

### Open items on the south east page

- Photography and video testimonials for all image slots.
- Booking calendar links for Arshad, Nirvan and Abhimaan — only Tanuj's
  (`calendar.app.google/uVUJEXzLsU1i73S97`) is wired; the others show a
  "calendar link to confirm" state.
- Rumeysa's full name and role. The other four in Meet the team are confirmed:
  Shashyani de Silva (Client Success Specialist), Rahul (Property Operations
  Specialist), Shamindri Jayawarna (Settlement Specialist) and Ali Al Hilo
  (Property Analyst). Rahul still needs a surname.
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
