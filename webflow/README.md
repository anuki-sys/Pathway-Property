# Pathway Property - Webflow custom code

Webflow site id `64d063d22c0ee57d46bfca71` ("Pathway Property Website"), serving
`pathwayprop.com.au`, `www.pathwayprop.com.au` and `www.zackyproperty.com.au`.

| File | Where it goes in Webflow |
| --- | --- |
| `site-head-custom-code.html` | Site settings > Custom code > Head code |
| `site-footer-custom-code.html` | Site settings > Custom code > Footer code |

The copies here carry a header comment naming the site and the settings panel;
the live boxes drop those two lines because they are redundant once you are
standing in the panel. Everything below them is identical.

## Designer-side settings these scripts depend on

Some of this only works if a matching setting exists in the Designer. Those are
not in this repo, so they are listed here:

- **Discovery Call calendar.** The Contact page enquiry form
  (`#wf-form-contact-form`) carries the custom attribute
  `data-pp-booking="discovery-call"`. The footer script looks for exactly that
  attribute and swaps the form's success message for the GoHighLevel booking
  calendar. Adding the attribute to another form switches that form over too;
  removing it everywhere turns the feature off without touching the code.
