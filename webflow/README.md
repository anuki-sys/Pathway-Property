# Pathway Property - Webflow custom code

Webflow site id `64d063d22c0ee57d46bfca71` ("Pathway Property Website"), serving
`pathwayprop.com.au`, `www.pathwayprop.com.au` and `www.zackyproperty.com.au`.

| File | Where it goes in Webflow |
| --- | --- |
| `site-head-custom-code.html` | Site settings > Custom code > Head code |
| `site-footer-custom-code.html` | Site settings > Custom code > Footer code |
| `book-a-call-page-footer-custom-code.html` | "Book a Call" page > Page settings > Custom code > Footer code |

The site-level copies here carry a header comment naming the site and the
settings panel; the live boxes drop those two lines because they are redundant
once you are standing in the panel. Everything below them is identical.

## The enquiry form is not a Webflow form

The enquiry form on the Contact page is a **GoHighLevel form in an iframe**,
sitting in an HTML Embed inside `.contact-form-wrapper`. The Webflow form still
in that column carries a `legacy-hidden` class and is not used.

This matters: its "thank you" message is rendered by GoHighLevel *inside* the
iframe, so no custom code on the Webflow page can see the submission or replace
that message. Anything that has to happen after an enquiry is configured in
GoHighLevel, not here.

## Book a Call page

`/book-a-call` (page id `6a9a6dba4b76f8336b841f2f`) is a duplicate of the
Contact page, so it inherits the navbar, footer and the two-column card layout.
The enquiry form, the hidden legacy form and the FAQ section were removed from
it; the right column now holds the booking heading, a short "what to expect"
list, and an empty `.pp-booking-calendar` block that the page footer code fills
with the calendar.

GoHighLevel's "Website Enquiry Form" is set to redirect to this page on submit
(Sites > Forms > Builder > Settings > On Submit).
