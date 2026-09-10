# The Melbourne Buyer's Digest - email design system

`issue-01.html` is the production build of Issue 01, structured so every
following issue is a content swap rather than a rebuild.

---

## Look

The email follows the **Pathway Instagram grid**, not a generic newsletter
layout: cream cards floating on the deep green ground, the brand gradient
behind the masthead and the closing block, and every number pulled out as a
display numeral or a pill rather than buried in a sentence.

The header runs as two sections: an Alabaster band carrying the Cyprus logo, then the green plate carrying the title lockup.

Section headings use the same device as the client review cards - the small
Ecru diamond, then a lowercase heading with a full stop. `The read.`
`The numbers.` `The weird one.` `What's on.`

| Token | Hex | Name | Used for |
|---|---|---|---|
| Main | `#206e65` | Elm | the diamond, sub-labels, rules, the mid-tier budget pill |
| Dark contrast | `#0f3e3a` | Cyprus | the ground, display numerals, dark pills |
| Black text | `#010a09` | Black green | body copy, the podcast card, the footer |
| White text | `#f5f2eb` | Alabaster | every card face, text on dark |
| Accent light text | `#feeacd` | Blanched Almond | the takeaway blocks, the take, pill text, the Close |
| Accent icons | `#c5b085` | Ecru | the Listen button, chips, section marks on dark |

Type is **Plus Jakarta Sans** throughout, one family, the brand logo font.
System fallbacks for Outlook and Gmail.

Cards are 12px radius on a 24px gutter, images 6 to 12px, pills fully round.
Outlook squares the corners off - that degradation is accepted.

---

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
| `CRAZY_LISTING_IMAGE` | 552 x 360 |
| `EPISODE_IMAGE` | 552 x 300 |
| `SUBURB_IMAGE` | 552 x 300 |
| `TANUJ_PHOTO` | 88 x 88, square, rendered round |
| `EVENT_1..3_IMAGE` | 208 x 160 |

Supply all of them at 2x and let the template scale down.

---

## Content, and what was cut

Issue 01 went from roughly 1,400 words to about 430. What changed:

| Section | Was | Now |
|---|---|---|
| The read | unchanged | unchanged. Still Tanuj's own 60 to 100 words |
| The numbers | six bullets of clearance and RBA detail | 55% as a display numeral with a "16 pts" pill, cash rate and countdown below, one takeaway. National figures cut |
| The weird one | a bullet | a photo card with a result pill |
| On the pod | three "what you'll get" bullets | episode art, guest, one hook line, one button |
| Suburb in focus | seven numbered sub-headings | photo, three-row spec strip, three budget pills, three one-liners, the take |
| Good to know | five legal bullets | three numerals (3 days / None / 0.2%) and two sentences |
| What's on | six events | three with thumbnails, one line each, plus the transport line |
| Sources | its own section | folded into the footer at 12px |

Two cuts need a human decision:

- **The suburb panel lost "who lives here", and "best pockets" became one
  line.** The spine is intact and the panel is far more scannable, but if the
  run sheet depends on all seven headings appearing, restore them.
- **The cooling off exclusions were trimmed** - industrial or commercial use,
  farmland over 20 hectares, a prior contract on substantially the same terms,
  and buyers who are agents or companies. They sit in a build comment in block
  06. Restore them if Nirvan wants them stated in the send copy.

---

## Slots

45 tokens. Grep must return **0** before scheduling:

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
the ESP field: *What's on before school holidays, and the cooling off trap that
catches auction buyers.*

---

## Pre-send checklist

### Refresh - the Monday before send

Every figure was verified on **10 September 2026** and will have moved.

- [ ] Melbourne clearance rate and the year-earlier comparison (Domain)
- [ ] Cash rate, and confirm the 29 September meeting still stands (rba.gov.au)
- [ ] The days-until-RBA countdown - it is hard-coded at 13
- [ ] Every event still running, not sold out, dates unchanged

**If a figure cannot be verified against a named public source on the Monday,
cut the line.** Never publish an unsourced number.

Hard-coded figures to re-check: `55%`, `71%`, `16 pts`, `4.35%`, `13 days`,
`4.6%`, and the three cooling off numerals.

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
