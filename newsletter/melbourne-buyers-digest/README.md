# The Melbourne Buyer's Digest - email design system

`issue-01.html` is the production build of Issue 01, structured so every
following issue is a content swap rather than a rebuild.

---

## Who it is for, and how it sounds

People buying a home to live in, corridor-weighted Dandenong to Pakenham.
Written to be read by whoever is actually carrying the decision, which in a
home purchase is usually a woman.

The voice is warm, calm and on the reader's side. We name what buying actually
feels like - the Saturday grind, the fear of overpaying, the pressure of the
auction floor - and then give something useful about it. Never technical for
its own sake, never breathless, never talking down. **A number only ever
appears alongside the sentence that says what it means for her.**

Three rules that keep it honest:

- **Never say anything negative about a property, or about the people selling
  it.** Notes on featured homes stay positive. They still have to be useful,
  so frame them as fit rather than fault: who this home suits, not what is
  wrong with it. "Ideal for a one-car household" does the same work as naming
  the single garage, without criticising someone's home. Each note sits under
  a "Why we like it" label, which is a standing reminder of what the note is
  for.
- The standing line under Featured homes ("we don't sell homes") is what makes
  that section trust-building rather than an ad. Do not remove it.
- Tanuj's note is written by Tanuj, from his own voice note. If it is invented
  it destroys the only thing it exists to build.

## Look

Cream cards floating on the deep green ground, matching the Pathway Instagram
grid. The header runs as two sections: an Alabaster band carrying the Cyprus
logo, then the green plate carrying the title lockup.

Tanuj's note is the **only** card on Blanched Almond, because it is the only
section that is a person talking rather than information. Everything factual
sits on Alabaster.

Section headings use the same device as the client review cards - the small Elm
diamond, then a lowercase heading with a full stop. `A note from Tanuj.`
`What this means for you.` `Three we'd walk through.` `Your weekend.`

| Token | Hex | Name | Used for |
|---|---|---|---|
| Main | `#206e65` | Elm | the diamond, sub-labels, price guides, the mid budget pill |
| Dark contrast | `#0f3e3a` | Cyprus | the ground, display numerals, the action blocks |
| Black text | `#010a09` | Black green | body copy, the podcast card, the footer |
| White text | `#f5f2eb` | Alabaster | factual cards, text on dark |
| Accent light text | `#feeacd` | Blanched Almond | Tanuj's card, the take, text on Cyprus blocks |
| Accent icons | `#c5b085` | Ecru | the Listen button, chips, hairlines, marks on dark |

`#c1531b` is the unfilled-slot marker and **must never be used as a design
colour.** It was previously used for the word "None" in the cooling off block,
which read as alarm; that is now Cyprus like the other two numerals.

Type is **Plus Jakarta Sans** throughout, the brand logo font, with system
fallbacks. Body line height is open (28 to 30px on 16 to 17px type) because
that is most of what makes the tone feel unhurried.


## Assets

`../assets/` holds the static brand files, extracted from
`Pathway_Property_Law_Logo.pdf`:

| File | What it is |
|---|---|
| `logo-cyprus.png` | green logo, transparent, 440px for retina. The Alabaster logo band at the top, renders at 186px |
| `logo-alabaster.png` | cream logo, same source. The Black green footer, renders at 132px |
| `bg-masthead.jpg` | the Instagram green gradient, masthead |
| `bg-close.jpg` | same gradient, mirrored, behind The Close |
| `mark-elm.png` / `mark-ecru.png` | the section diamond, on light and dark |

**Upload these to your CDN or ESP asset folder and set `{{SLOT:ASSET_BASE}}` to
that folder once, with no trailing slash.** Every image in an email must be
hosted at a public URL - Gmail and Outlook strip data URIs.

Weekly photos have their own slots. Sizes the template expects, at 1x:

| Slot | Size |
|---|---|
| `HERO_IMAGE` | 600 x 340 |
| `LISTING_1..3_IMAGE` | 172 x 132 |
| `CRAZY_LISTING_IMAGE` | 552 x 360 |
| `EPISODE_IMAGE` | 104 x 104, square |
| `SUBURB_IMAGE` | 552 x 300 |
| `TANUJ_PHOTO` | 88 x 88, square, rendered round |
| `EVENT_1..3_IMAGE` | 208 x 160 |

Supply all of them at 2x and let the template scale down.

---

## Structure

Value first, promotion last.

| # | Section | Job |
|---|---|---|
| 1 | Logo band | Alabaster, Cyprus logo |
| 2 | Masthead | green plate, title lockup, issue line |
| 3 | Hero image | full bleed |
| 4 | **A note from Tanuj** | the warm card. Proof he was on the floor |
| 5 | **What this means for you** | the market, in plain language, plus one action |
| 6 | **Three we'd walk through** | featured homes, honest notes |
| 7 | **What it's like to live in [suburb]** | a Saturday there, then the practical detail |
| 8 | **How long you get to change your mind** | cooling off, as a two-sided comparison. Private sale vs auction, one point |
| 9 | **One we had to show you** | the light moment. Most forwarded item |
| 10 | **Your weekend** | three things, family-weighted |
| 11 | **On the pod** | compact, sits late because it is promotion |
| 12 | **The Close** | one reply CTA. Never two |
| 13 | Footer | sources, compliance |

About 1,000 rendered words, roughly a 4 minute read. The masthead says 4 min;
if a future issue grows past about 1,100 words, cut before you change the
label.

### Judgement calls to review

- **The suburb panel is down from seven fixed sub-headings to five blocks.**
  "Who lives here" is gone, and "it's a fit if" was folded into The Take. If
  the run sheet depends on all seven appearing, say so and they come back.
- **The cooling off exclusions are out of the send copy** - industrial or
  commercial use, farmland over 20 hectares, a prior contract on substantially
  the same terms, and buyers who are agents or companies. They sit in a build
  comment in section 08. Restore if Nirvan wants them stated.
- **Section 08 was restructured after review.** It first ran as three loose
  figures (3 days / $1,600 / None), which read as three parallel facts when
  two of them describe private sales and one describes auctions. It is now a
  two-column comparison with the label above each numeral, and the $1,600 sits
  in the body text where it belongs. It also opens by stating what the block
  is for, because it was not self-evident.
- **The "investment read" cross-promo line was dropped** from the podcast
  block. It was the deliberate single piece of investment content, but it
  clashed with the owner-occupier voice. Easy to reinstate.


## Slots

62 tokens. Grep must return **0** before scheduling:

```sh
grep -c '{{SLOT:' issue-01.html
```

Unfilled slots render in orange with a dotted underline. If you can see orange,
the email is not finished.

Four exist only for compliance and are usually ESP merge tags:
`BUSINESS_NAME_AND_POSTAL_ADDRESS`, `UNSUBSCRIBE_URL`, `PREFERENCES_URL`,
`WEBVIEW_URL`. The Spam Act 2003 requires a working unsubscribe and a real
sender address on commercial email.

---

## Subject lines

Pick one, delete the rest from the header comment:

1. One in two Melbourne auctions now passes in
2. 55%. That's the number that matters this week.
3. The RBA meets in 13 days. Read this before you bid.

**Preheader** is set in the hidden div at the top and must also be pasted into
the ESP field: *Plus what your budget really buys in Officer, and the thing
nobody tells you about bidding.*

---

## Pre-send checklist

### Refresh - the Monday before send

Every figure was verified on **10 September 2026** and will have moved.

- [ ] Melbourne clearance rate and the year-earlier comparison (Domain)
- [ ] Cash rate, and confirm the 29 September meeting still stands (rba.gov.au)
- [ ] Every featured listing is still live, and the price guide has not moved
- [ ] Every event still running, not sold out, dates unchanged

**If a figure cannot be verified against a named public source on the Monday,
cut the line.** Never publish an unsourced number.

Hard-coded figures to re-check: `55%`, `71%`, the 29 September RBA date, and
the three cooling off numerals (`3 days`, `$1,600`, `None`).

### Build gate

- [ ] `grep -c '{{SLOT:' issue-01.html` returns **0**
- [ ] `grep -n '—\|–' issue-01.html` returns nothing (hyphens only)
- [ ] `ASSET_BASE` points at a live folder and every image loads with images off then on
- [ ] Sender name, sender email and reply-to set (all three still TBC)
- [ ] One CTA only, in The Close
- [ ] Nirvan has signed off block 06
- [ ] Read on a phone before scheduling

### Legal gate, block 06

Sale of Land Act 1962 (Vic) s31, per the LIV and REIV prescribed contract
notice. The notice says the period runs from "the day that you sign the
contract"; this build uses that wording rather than the secondary sources that
tie it to receipt of the section 32. Settle the framing once, because it
recurs.

---

## Reusing this for Issue 02 onward

1. Swap the masthead headline, issue number and date.
2. Replace the figures in The numbers and the three events.
3. Refill every slot and re-point the weekly photos.
4. No episode that week: keep the same card, change the eyebrow to
   **From the archive** and run a second rotating section in place of the
   suburb panel.
5. From Issue 02, The Close can carry a Reader Question fed by Issue 01
   replies. Still exactly one CTA.

## Client support

Table-based, inline-styled, 600px, single column, `role="presentation"`
throughout. MSO conditional wrappers and `PixelsPerInch` fix Outlook, the
gradient bands carry VML fallbacks with a solid Cyprus bgcolor beneath, and
both buttons are bulletproof. `color-scheme: light` limits dark-mode inversion.
The mobile breakpoint is **560px** so that a 600px desktop preview does not
trip the stacked layout.
