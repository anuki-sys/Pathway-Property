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
- **Region map:** the nine SA4 regions are grouped into **four territories**
  (`data-territory` on each path), each painted a different shade of the one
  base colour so the region strokes still delineate inside a territory:

  | Territory | Regions | Pin |
  | --- | --- | --- |
  | `north` | North West, North East | Nirvan |
  | `west` | West, Inner | Arshad |
  | `east` | Inner East, Outer East | Abhimaan |
  | `south` | Inner South, South East, Mornington | Tanuj |

  Every region belongs to a territory, which is what stops Mornington reading
  as unstaffed. Hovering a pin lights its **whole** territory rather than the
  single region under it, for the same reason.

  Inner sits with West and Mornington with South because they have to sit
  somewhere: nine regions across four people does not divide evenly.

  **Abhimaan Bhargava is a buyer's agent**, not Support and Settlement. The
  owner-occupier deck (slide 11) still has him under Support and Settlement and
  is wrong; the client corrected it on 14 Sep.

  Each pin is a teardrop whose
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
- **Motifs:** a "Rated 5 Stars on Google" row above the headline, its wording
  linked to the Google Maps listing (`maps.app.goo.gl/A6pDCRD7zQeitpSq8`), and soft
  white clouds drifting behind the hero, in the spirit of the main site's
  illustrations. The clouds hide below 1080px, where the hero becomes a
  single column and they would land on the headline. A flat-vector scene
  along the hero's bottom edge was tried and removed — with the photo
  composition already in the hero, it made the header too busy.

## The numbers on the page

| Figure | Source | Used on the page |
| --- | --- | --- |
| 2000+ agent partnerships across Melbourne | Client, 14 Sep | Hero stat |
| 100+ off-market properties across Melbourne each week | Client, 14 Sep | Hero stat, off-market section heading |
| 3.7% average discount negotiated for clients | Deck 4/9, restored to the hero 15 Sep | Hero stat |
| 100 due diligence reports produced every day | Client, 8 Sep (deck says 50) | "Why buyers bring us in" |
| 7+ professionals coordinated to settlement | Deck 5/9 | "Why buyers bring us in" |
| 120 hours saved on a typical purchase | Deck 6/9 | Process intro |
| 7 weeks average time to secure | Client, 15 Sep | Process intro |
| $100m+ in transactions (Tanuj) | Bio copy, client, 15 Sep | Agent slider |
| $10bn+ in real estate transactions (Nirvan) | Bio copy, client, 15 Sep | Agent slider |
| 10,000+ real estate interactions (Arshad) | Bio copy, client, 15 Sep | Agent slider |
| ~~Over 1,000 properties purchased~~ | **Withdrawn 14 Sep, inaccurate (Nirvan)** | Removed from the meta description, hero lede, value list and FAQ |
| ~~Thousands of families~~ | **Withdrawn 14 Sep** | Removed: it cannot be true if the properties figure was not |

The off-market figure carries its cadence everywhere it appears. The hero stat
once read "100+ off-market properties across Melbourne" with no time period
while the section heading said "every week", which read as two different
claims. Both now carry the week.

**3.7% came back on 15 Sep**, taking the third hero slot from the due diligence
figure, which still appears in "Why buyers bring us in". It had been retired on
14 Sep as part of the sweep below, so treat the retired list as a record of what
was pulled and why, not as a permanent ban.

**The average time to secure has now been three different numbers.** The deck
and the original page said nine weeks, confirmed on 14 Sep; the flyer said six;
the client set it to **seven** on 15 Sep, and seven is what the page says. Every
piece of collateral needs to land on the same figure, and the deck and the flyer
are both still wrong. That is outside this repo.

Retired on 14 Sep and swept from the whole page, body copy, FAQ answers and the
JSON-LD mirrors alike: **90+ inspections a week**, **200+ off-markets** and
**50 due diligence reports a day**. The **3.7% average discount** went with them
and was restored to the hero on 15 Sep at the client's request. If any of the
others come back, put them everywhere or nowhere.

The one figure the deck and the client disagree on is due diligence: the deck
says **50** a day, the client says **100**, and the page says 100. Deck slide
7/9 also contradicts itself on speed, its heading saying many clients secure
"in just 4 to 5" weeks and its own bullet saying "3 to 4 weeks"; neither is on
the page, only the average above.

With 3.7% back, the page again carries one figure expressed as a benefit to the
reader rather than as a measure of Pathway's own activity. It is the only one,
and it is the one a buyer is most likely to repeat, so it is also the one most
worth being able to substantiate on request.

Each figure is an average or a business-wide throughput number, not a promise
to an individual buyer. If this page is going to make these claims publicly,
they need to be substantiable — keep the underlying records.

### Legal advice: do not claim it

**Pathway Property Law is a separate entity to the Melbourne buyer's agency,
and this page must not offer or imply legal advice.** "What the contract
actually says" was removed from the value list on 14 Sep for exactly this
reason, and "review the contract and the section 32" came out of the FAQ on the
same grounds on 14 Sep. Keep contracts, section 32s and anything a lawyer would
sign off out of the service description. The page is now clear of both words;
grep for them before shipping any new copy.

### The FAQ and its JSON-LD twin

The FAQ is mirrored in an `FAQPage` JSON-LD block at the foot of the page, and
the two had silently drifted: the block still carried a deleted question and two
superseded answers. **The block is now generated from the rendered FAQ**, so
regenerate it rather than hand-editing, and check the two match after any FAQ
change. Inline links are stripped from the JSON-LD text, which is what schema
expects.

Two standing rules the FAQ answers have to hold to:
- **No individual agents by name.** "Tanuj in the south east, Arshad in the
  west" came out on 14 Sep: enquiries all route to Tanuj anyway, and naming
  people boxes the business into an allocation it may not keep. The answer now
  says buyer's agents work across every corner of the city and the right one is
  put on the search. Note the map and the agent slider still name all four and
  tag them by territory, which is the same commitment made visually. If the
  boxing-in concern applies there too, that is a bigger change than this one.
- **No legal advice.** See the section above.

"What does a buyer's agent do in Melbourne?" was removed on 14 Sep as too basic
for a reader who has got this far.

### The off-market section

**The weekly list is an automation, not a walkthrough.** It is a static list
generated and emailed each week, so no copy anywhere may suggest someone walks
the reader through the properties in person or tailors the list to them. What
is offered in person is the consult, and the hook for it is the deals already
shortlisted for clients, which are deliberately not on the free list.

The form collects name, email, phone, the suburbs they are watching and a
graded readiness select: ready to buy now, buying in 3 to 6 months, or just
looking for now. Its first option is a disabled "Select one" placeholder, so an
unanswered field records nothing rather than silently recording whichever
option happens to sit first. **The team does the filtering, the form does
not** — nothing on the page promises the list is filtered to the suburbs given.

Note this sits next to the booking form's own "When are you buying?", which
uses four different bands. If the two ever need to feed the same segmentation,
align the bands.

The suburb field is a chip combobox, not free text: typing filters a list, a
click or Enter adds a chip, Backspace on an empty input removes the last one,
and the chips are written into a hidden `#om-suburbs-value` field for whatever
handler eventually receives the form. Free text is still accepted on Enter so a
missing suburb never blocks a submission. The suburb list is a **fixed array of
about 130 Melbourne suburbs in the page** and is not complete; before launch it
wants extending or replacing with a real dataset.

### Pin photos: one focal point per face

The four pin sources are not interchangeable. Tanuj's and Abhimaan's are 500x500
with the head centred; Arshad's and Nirvan's are 500x750 portraits with the head
sitting right of centre and lower in frame. A single shared focal point framed
the two squares well and left the two portraits low and off to the right, which
is what Tanuj was seeing on 16 Sep.

Each `.pin-photo` now carries **`data-fx` / `data-fy`**, the face centre as a
fraction of its own source, measured off the file. The script places that point
at the same spot in every disc: horizontally centred, 35px down of 92, which is
how a face reads right in a circle. All four now land identically.

`ZOOM` (1.25) is load-bearing, not decoration. At plain cover scale a 500x750
source comes out exactly disc-width, so any sideways nudge would pull a photo
edge inside the circle. Cropping in slightly buys the room to move. The x and y
are then clamped so a photo can never be dragged far enough to show an edge.

**A new or replaced pin photo needs its own `data-fx` / `data-fy`.** Without
them it falls back to 0.5 / 0.38, which suits a centred square headshot and
little else. The values in use: Tanuj 0.50/0.38, Arshad 0.565/0.40, Nirvan
0.545/0.41, Abhimaan 0.49/0.35.

### The agent bios

Rewritten from client-supplied copy on 15 Sep, in a warmer voice that uses "he"
rather than the clipped third person the cards carried before. They run 60 to 67
words against the old 40 and still fit the card with room to spare, but that is
close to the ceiling: much longer and the body outgrows the portrait beside it.

Two things in the new copy to keep an eye on:
- **Abhimaan's bio claims the inner CBD**, and on the map the inner Melbourne
  SA4 is shaded as Arshad's. One of the two is wrong, and a reader can see both.
- **Nirvan's opens "Corporate and commercial lawyer first."** Describing a
  background is not the same as offering legal advice, and this is his own copy,
  so it stands. But it sits beside "every offer and contract Pathway sends out
  the door" on a page that must not imply legal services, so it is worth him
  reading once more with the Pathway Property Law separation in mind.

The three career figures in these bios are the only numbers on the page attached
to a person rather than to the business. They are in the table above and need the
same substantiation as the rest.

### Navigation

This page sits at **Services > Buyer advocacy > Melbourne**, set on 15 Sep. The
"Where we buy" top level menu was removed entirely at the same time.

Services is now the dropdown: `.nav-item.has-menu` with a `.nav-trigger`
button. The dropdown JS is generic over `.nav-item.has-menu`, so moving the
menu from one top level item to another needs no script change. The second
level row carries `.dd-sub`, which indents it and rules it off against its
parent so it reads as a child page rather than a sibling.

Only this page's branch is shown. The real Services menu lives in Webflow's
global navbar component, so on the Webflow build this markup is a stand-in.

### Two lines Tanuj questioned, 16 Sep

**"found with you, not sold to you" keeps "with".** "For you" is what every
buyer's agency says and it puts the reader back in the passenger seat; "with"
is the partner positioning the team asked for on 8 Sep, and with/to is a
sharper opposition than for/to. Worth revisiting only if "with" ever reads as
though the buyer is expected to do the work.

**"and we have the keys" came off the booking headline.** It claims possession
of a home nobody has found yet, and it was the only line on the page that
promised rather than described. Now "Your dream home is out there. Let's go and
find it." The original was the client's own wording from the 8 Sep changes
document, so putting it back is a one-line revert if they prefer it.

### The discovery call is thirty minutes

Set on 15 Sep, and the page now says thirty everywhere it names a length: the
step 1 card and its timing chip, the booking lede and the line above the submit
button. If it changes again, change all four.

**The Google Calendar booking link has to match.** Every "Book a consult" CTA
drops straight into `calendar.app.google/8NCaGay2AG5pu6yo9`, which was set up as
a fifteen minute slot. Until that event's duration is changed in Google
Calendar, the page promises half an hour and the calendar books fifteen minutes.
That is a setting outside this repo, and the same applies to the other agents'
links when they are wired up.

### The booking form

The "Or book straight in" panel, which let a reader skip the form for Tanuj's
calendar, was removed on 14 Sep: the form is the filter, so a bypass next to it
defeats the point. **That decision was then narrowed on 15 Sep**: every "Book a
consult" CTA elsewhere on the page goes straight to the calendar, so the form is
no longer the only route to a booking, it is just the only route offered from
inside the booking section. Its submit button is the one "Book a consult" on the
page that does not link to the calendar. The form gained the submit button it had been missing
entirely, and its suburb field is now the same chip combobox as the off-market
form. Both mount from one list; each keeps its own chips.

The lede promised "five quick questions" against a seven field form and now
just says what it does. If fields are added, do not put a count back in.

### The process section

Seven steps, sticky-stacked. Each card's `--i` drives its sticky offset, so a
new step needs the next value in sequence or it will stack on top of its
neighbour rather than below it.

Step 7 fires a **celebration every time it scrolls back into view**: a ring
pulsing out from the step number and eighteen thin slivers in the greens and
the star gold. No cream, which is invisible on a cream card. It runs for 1.5s,
clears its own DOM after 2s, and is suppressed entirely under reduced motion.

Repeating needs two guards, and dropping either one makes it feel broken:
- It fires at 50% visible but only re-arms below 15%, so nudging the scroll
  wheel around the trigger point cannot set it off again and again.
- A `running` flag stops a second burst landing on top of one still playing;
  it releases when the cleanup timer clears the DOM.

Two things make it work, and both are easy to break:
- It waits for the card's **computed opacity** to pass 0.9, not for the card to
  intersect. The cards fade in on scroll, so a burst fired on arrival plays out
  while the card is still transparent and the reader sees nothing.
- It does not test for the `js-reveal` class, because the reveal script runs
  after it and the class is not set yet at that point.

Step 7 is the post-settlement step and has to stay carefully worded: **it is not
a promise of ongoing service.** Tracking equity, being an easy first call and
connecting people to trades are the commitments; renovation and value-add work
is a separate service and the page should only ever offer the introduction.

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

The hero carries two client photos from the Webflow CDN: the main one framed
4:3.6 with `object-position: 50% 46%`, and a square inset overlapping its
bottom-left corner.

**The inset needs `z-index:2`.** `.shot img` is `z-index:1` and `.shot` itself
creates no stacking context, so both photos' images land in the hero grid's
stacking context at the same level while the inset's own frame sits at auto.
Without the explicit z-index the main photo's image paints over the inset's
border, and the outline vanishes exactly where the two overlap.

The inset covers about **26%** of the main photo's width. It was 39%, which cut
the subject in half; the fix was to shrink the inset to 38% and raise
`.hero-media`'s left padding to 84px, which shifts the main photo right and out
from behind it. If a future hero photo puts its subject somewhere else, that
padding is the dial.

Four headshots are also served from the Webflow CDN: Tanuj, Arshad, Nirvan and
Abhimaan in the agent slider. They sit at `object-position: 50% 28%`, which
keeps a face high in a tall frame rather than centred.

One photo is **inlined as a data URI** rather than pulled from the CDN, so the
page still shows it when it is opened as a single file or in a preview that
blocks remote images:

| Slot | Inlined file | Note |
| --- | --- | --- |
| "Why buyers bring us in" | `assets/approaching-home.jpg` | A buyer walking up to a front door. The frame has **no aspect ratio**: the grid is `align-items: stretch`, so it takes whatever height the list beside it ends up being and the two columns always end level. Below 900px the columns stack and it falls back to 4:5. |

It is in `assets/` at exactly the bytes that are inlined. When this moves into
Webflow, upload it to the site asset library and replace the data URI with its
CDN URL — data URIs are a preview convenience, not how the live page
should ship.

It is Unsplash stock (João Emanuel) and reads as stock. Swap it for real
Pathway photography when there is some. Both hero photos are now real clients.

Still needed: a headshot for **Rumeysa**. Everything else is wired to the
Webflow CDN, including the podcast thumbnail and all eight Recent buys tiles.
There are no local image placeholders left on the page.

Role chips are solid once the role is confirmed and dashed while it is still a
placeholder, so an unconfirmed card is obvious at a glance.

"Recent buys" is an auto-scrolling marquee carrying **eight real client
photos**. Its tiles are written out twice so the loop is seamless: **whatever
you change in the first set, change in the second**, and keep the duplicate set
`aria-hidden` so screen readers do not read every photo twice.

The loop relies on `translateX(calc(-50% - 10px))` matching one set plus one
20px gap. At eight 300px tiles the track is 5100px and the shift is 2560px,
which is exactly right. Change the tile count, the tile width or the gap and
that offset has to be re-checked or the loop will visibly jump.

Duration is 62s, scaled up from 46s when the set grew from six tiles to eight
so the scroll speed stayed the same. It pauses on hover and on focus, and
becomes a plain horizontal scroller under reduced motion.

## The Webflow build

Rebuilt into Webflow on 18 Sep and published to **staging only**:
`pathwayproperty.webflow.io/melbourne` (page id `6aac8e9b4ed859874f97b3af`).
Production domains were not published.

**The elements are native Webflow; the styling is not.** The Data API's WHTML
builder rejects any CSS selector that is not a plain class, which rules out
`:root` (where every design token lives), all the element selectors, every
descendant selector like `.nav-dropdown a`, and the attribute selectors. Only
126 of the page's 257 rules would have gone through, and without `:root` those
126 would have rendered with broken `var()` references. So the full stylesheet is
served as an asset and linked from the page head instead. What that means in
practice: **the team can edit text and structure in the Designer, but not
styling.** Styling changes go to `buyers-agent-melbourne.html` in this repo, and
the asset is re-uploaded.

Three assets carry the page, all uploaded through the Data API:

| Asset | Purpose |
| --- | --- |
| `melbourne-page.css` | the whole stylesheet, linked from the page head |
| `melbourne-page.js` | the whole script, linked from the page footer |
| `melbourne-approaching-home.jpg` | the one photo that had been a data URI |

The head also carries the Plus Jakarta Sans links. The JS and CSS went in as
assets rather than page custom code to sidestep Webflow's custom-code character
limit, which 32KB of CSS and 15KB of JS would have blown through.

**Link assets by their `hostedUrl`, not the `cdn.prod.website-files.com` URL
returned by `create_asset`.** The first staging publish came out almost entirely
unstyled because both the stylesheet and the script were linked from the CDN
form, and the CDN does not serve an asset the API uploaded. The `hostedUrl`
`get_asset` reports (`s3.amazonaws.com/webflow-prod-assets/…`) serves all three
files correctly, verified: 200, right MIME type, right byte counts.

**Ignore `size: 0` on an API-uploaded asset.** All three report zero bytes while
serving their full contents, so the field is stale metadata rather than a failed
upload. Do not re-upload on the strength of it.

**Re-uploading a changed asset does not update the page.** Webflow content-
addresses assets, so a new upload gets a new URL and the `<link>`/`<script>` in
the page head and footer has to be repointed.

The whole page is 28KB of CSS and 12KB of JS, well past Webflow's 10,000
character per-block custom-code limit, which is why they are assets at all. If
the asset route ever fails, the fallback is several HtmlEmbed elements each
carrying a chunk under that limit, not page custom code.

**Register every class before inserting markup that uses it.** This is the one
that actually broke the page. The WHTML builder silently **drops any class that
is not already a Webflow style** — the element goes in, the class does not, and
nothing warns you. The first build looked fine through the API (`styleNames`
came back populated for `navbar` and `section`) because those classes already
existed in the site's own stylesheet; everything unique to this page went in
naked, so the stylesheet loaded correctly and had nothing to match.

The fix is a one-off registration pass: extract every class in the markup and
send them through the `css` parameter as inert shells (`.wrap{--r:1}` and so on,
127 of them, about 2KB) on the first insert. The real styling still comes from
the linked stylesheet, which loads after Webflow's CSS and therefore wins. After
that, classes stick and stay.

**`a` is a reserved Webflow style name.** The FAQ answer wrapper was
`<div class="a">` and was rejected outright. Renamed to `faq-a` in the source.
If a class is rejected, the whole insert still succeeds and you get a
`dropped_style` warning buried in the response, so read those warnings.

Things the builder changed on the way in, worth knowing before editing:
- **Every form field must sit inside a `<form>`.** Webflow rejects a stray
  `<label>` or text input outright, which is why the off-market, booking and
  newsletter fields are now wrapped in real forms in the source too. That is an
  improvement, not a workaround: they need to be forms to be wired up anyway.
- `<button>` became a Webflow **Link**, so the nav toggle and slider arrows are
  links. Their ids and ARIA survived, so the script still binds.
- `style="--i:N"` on the process cards became generated classes
  (`inline-article-0` … `-6`). The sticky offsets depend on `--i`, so check the
  stack still steps correctly on staging.
- Images come in unbound and must be attached to an asset id afterwards. The
  SVG `<image>` pins are DOM elements and keep their `href`, so they are fine.

### Two bugs the port surfaced

**A stray `</g>` in the map SVG.** Abhimaan's pin sat outside `.map-pins` with
the group tree one level unbalanced. Browsers silently corrected it, which is
why it never showed, and `querySelectorAll('.pin')` still found all four. Fixed
in the source on 16 Sep.

**No `<form>` anywhere.** Every field on the page was loose markup. Fixed on 18
Sep, as above.

## Pages

| File | Intended path | Status |
| --- | --- | --- |
| `buyers-agent-melbourne.html` | `/melbourne` | On Webflow staging |

This started as a Melbourne South East page and was widened to cover all of
Melbourne on 8 Sep. A separate South East page is still to be built; when it is,
it inherits this structure and narrows the copy, the map and the team back down.

### Meet the team: removed, not retired

The support team section was taken off the page on 14 Sep because the Sri
Lankan team's headshots need re-taking, and the section is only as good as its
photos. Nothing was wrong with the content, so if it comes back it comes back
whole: Shashyani de Silva (Client Success Specialist), Rahul Vilvarajah
(Property Operations Specialist), Shamindri Jayawarna (Settlement Specialist),
Ali Al Hilo (Property Analyst) and Rumeysa, whose full name and role were never
confirmed. Its markup and its `.team` / `.member` / `.role-chip` styles were
removed with it rather than hidden, so restoring it means rebuilding both. The
git history at this commit has the original if that is easier.

The page now goes straight from the agent slider to the FAQ, and the support
team appears nowhere: the only people named on the page are the four buyer's
agents.

### Open items on the Melbourne page

- Photography and video testimonials for all image slots.
- A booking calendar link for **Abhimaan**, the last one outstanding. Three are
  wired: Tanuj's (`calendar.app.google/8NCaGay2AG5pu6yo9`), which every general
  CTA uses, and Arshad's and Nirvan's own appointment schedules on their cards,
  both added 15 Sep. Abhimaan's card still falls back to Tanuj's link, so a
  reader who clicks it books time with Tanuj.
- Arshad's is a Google Calendar **appointment schedule** URL
  (`calendar.google.com/calendar/u/0/appointments/schedules/…`), a different
  shape from Tanuj's `calendar.app.google` short link. Both work; do not try to
  normalise one into the other.
- **The privacy policy page does not exist yet.** The newsletter line says "by
  subscribing you agree to our privacy policy" and now links to
  `/policies/privacy-policy`, as the footer already did. The page has to be
  written and published before the form collects a single address. It is a
  legal document for the business to produce, not page copy.
- Form endpoints: the off-market, booking and newsletter forms are marked up
  but not wired to a handler. The off-market form now carries phone, suburbs
  and a readiness flag, and the booking form posts chips from a hidden
  `#b-suburbs-value`, so whatever receives them needs those fields.
- The off-market suburb list is a hand-built array of about 130 suburbs and
  does not cover all of Melbourne.
- Real YouTube and Spotify links on the podcast section (both are `#`).
- The nav logo is an inline SVG redraw of the brand mark. Swap it for the
  official logo file before this goes live — on the Webflow build it will use
  the site's own logo asset anyway.
- Nav submenu contents for About, Partners and Event — the carets match the
  live nav but the items themselves come from the site's global navbar
  component in Webflow, which isn't readable through the API. The Services
  dropdown here shows only the one branch this page sits in, not the real
  service list.
- `/services/buyer-advocacy` is the assumed parent URL and needs confirming
  against the live site, as does this page's own path.
- **The four "coming soon" area pages lost their nav home.** Melbourne South
  East, East, North and West were listed under "Where we buy", which was
  removed on 15 Sep. They are not in the nav at all now. When they are built
  they most naturally become siblings of Melbourne under Buyer advocacy, but
  that was not asked for, so nothing was added on their behalf.
