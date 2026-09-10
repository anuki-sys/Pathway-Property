# The Melbourne Buyer's Digest - email design system

`issue-01.html` is the production-ready build of Issue 01, structured so every
following issue is a content swap rather than a rebuild.

Source content: `melbournebuyersdigestissue01.md` (Issue 01 brief).

---

## Brand

The email follows the **Pathway Property brand guidelines**, not the slide-deck
palette (the pptx system uses `#0A3D30` / `#25B67A` - that is for decks only).

| Token | Hex | Name | Used for |
|---|---|---|---|
| Main | `#206e65` | Elm | eyebrows, hairline rules, left rules, buttons, links, the year-on-year indicator bar |
| Dark contrast | `#0f3e3a` | Cyprus | dark bands, sub-headings, the hero stat card, bold lead-ins on light |
| Black text | `#010a09` | Black green | body and headings on light bands, cards sitting on dark bands, footer |
| White text | `#f5f2eb` | Alabaster | light band background, all text on dark bands |
| Accent light text | `#feeacd` | Blanched Almond | the timestamp hook, the Close CTA, event headlines, "The point" callout |
| Accent icons | `#c5b085` | Ecru | bullet squares, SOUTH EAST chips, section numerals, the play affordance, dividers |

**Type.** Plus Jakarta Sans (the brand logo font) carries every heading,
eyebrow, numeral, chip and button. Inter carries body copy. Both load from
Google Fonts with a `-apple-system / Segoe UI / Arial` fallback stack, so
Outlook and Gmail degrade to a clean sans rather than a serif.

**Band rhythm.** Alternating Alabaster and Cyprus, the same as the flyer:

```
top bar (Elm)
masthead (Cyprus)
01 The Read (Alabaster)
02 Podcast (Cyprus)
03 Market (Alabaster)
04 What's On (Cyprus)
05 Suburb (Alabaster)
06 Good to Know (Alabaster, framed card - reads as its own object)
07 The Close (Cyprus)
08 Sources (Alabaster)
footer (Black green)
```

Every section opens on a 1px Elm hairline, then an ALL CAPS letter-spaced
eyebrow, exactly as specified.

**Card rule.** Cards on dark bands are filled Black green; cards on light bands
are white with an Ecru or Cyprus border. Two derived tints are in use and are
deliberate: `#e3ddd0` (Alabaster shaded, price-table dividers) and `#fdf0e8`
(build-only slot highlight). `#666666` is the single grey, for sources and
footer meta only.

---

## Block components

One component per `type` in the brief, all built:

| Block | Type | Treatment |
|---|---|---|
| 01 | `hero_read` | Alabaster, no image, 19px body, signature on an Elm rule |
| 02 | `episode_card` | Cyprus band, Black green card, Ecru play affordance, timestamp hook set larger than the bullets, one bulletproof button |
| 03 | `stat_block` | 55% as a filled Cyprus card against 71% outlined, then a full-width Elm indicator bar. Crazy Listing gets an image card of its own, Result of the Week a Blanched Almond callout. "What this means" sits on a 4px Elm left rule |
| 04 | `event_list` | Cyprus band, six items, rule-separated, Ecru SOUTH EAST chips, transport line in its own Black green card |
| 05 | `suburb_panel` | Seven fixed sub-headings numbered in Ecru, price points as a stepped table with widening Elm markers, THE TAKE on a 2px Elm rule |
| 06 | `explainer_callout` | Framed card, 2px Cyprus border, "The point" in a Blanched Almond block |
| 07 | `cta_close` | Cyprus band, one reply CTA in Blanched Almond, no button |
| 08 | `source_footer` | Alabaster, 13px grey, lifted to 14px on mobile |

---

## Slots

31 tokens. Grep must return **0** before scheduling:

```sh
grep -c '{{SLOT:' issue-01.html
```

Unfilled slots render in orange with a dotted underline. If you can see orange,
the email is not finished.

25 come straight from the brief. Six were added because the build needs them:

- `CRAZY_LISTING_IMAGE_URL`, `CRAZY_LISTING_IMAGE_ALT` - the brief requires the
  Crazy Listing to carry an image and its own block. Supply 1072px wide for
  retina; it renders at 534px.
- `BUSINESS_NAME_AND_POSTAL_ADDRESS`, `UNSUBSCRIBE_URL`, `PREFERENCES_URL`,
  `WEBVIEW_URL` - Spam Act 2003 requires a working unsubscribe and a real
  sender address on commercial email. Most ESPs merge these automatically; if
  yours does, swap the token for the merge tag.

---

## Subject lines

Pick one, delete the rest from the header comment:

1. Melbourne's clearance rate just fell 16 points in a year
2. The RBA meets in 13 days. Here's what it means for your offer.
3. 55%. That's the number that matters this week.

**Preheader** is already set in block 00 and must be copied into the ESP field
as well: *Plus what's on before school holidays, and the cooling off trap that
catches auction buyers.*

---

## Pre-send checklist

### Refresh - the Monday before send

Every figure in the build was verified on **10 September 2026** and will have
moved.

- [ ] Melbourne clearance rate, weekend just gone, plus the year-earlier comparison (Domain)
- [ ] National clearance rate and the prior week (PropertyUpdate National Weekly Auction Report)
- [ ] Cash rate, and confirm the 29 September meeting still stands (rba.gov.au)
- [ ] Bank forecasts - these shift weekly, re-check before repeating them
- [ ] Every event - still running, not sold out, dates unchanged

**If a figure cannot be verified against a named public source on the Monday,
cut the line.** Never publish an unsourced number.

Figures hard-coded in the HTML that need re-checking: `55%`, `71%`, `46.1%`,
`47.3%`, `74.4%`, `4.35%`, `29 Sep`, `75 basis points`, `3.5%`, `3.8%`, `3.6%`,
and the down-16-points bar.

### Build gate

- [ ] `grep -c '{{SLOT:' issue-01.html` returns **0**
- [ ] `grep -n '—\|–' issue-01.html` returns nothing (hyphens only)
- [ ] Sender name, sender email and reply-to set (all three are still TBC in the brief frontmatter)
- [ ] One CTA only in block 07
- [ ] Nothing below 16px on mobile in body copy
- [ ] Nirvan has signed off block 06 (legal gate)
- [ ] Rendered and read on a phone before scheduling

### Legal gate, block 06

Verified against the LIV and REIV prescribed contract notice. One precision
point to settle permanently: several secondary sources state the cooling off
period runs from receipt of the contract **and** the section 32. The prescribed
notice says "of the day that you sign the contract." This build uses the
prescribed wording. Confirm which framing the Digest uses from here, because it
will recur.

---

## Reusing this for Issue 02 onward

Copy `issue-01.html`, then:

1. Swap the masthead issue number and date.
2. Replace the block 03 figures and the block 04 event list.
3. Refill every slot.
4. If there is no episode that week, replace the block 02 card with **From the
   archive** (same card component, different eyebrow) and run a second rotating
   section in place of block 05.
5. From Issue 02, block 07 can carry a Reader Question fed by Issue 01 replies.
   It still gets exactly one CTA.

## Client support

Table-based, inline-styled, 600px, single column, `role="presentation"`
throughout. MSO conditional wrappers and `PixelsPerInch` fix Outlook; the
button is bulletproof. `color-scheme: light` limits dark-mode inversion. Two
column stat pairs stack under 620px. Tested structurally: 63 tables, all tags
balanced, no off-palette colour.
