# Page images

Drop files in here with these exact names and they appear on the page — no
code change needed. A name that isn't filled yet shows the labelled green
placeholder instead of a broken image, so the page is safe to publish with
some of them missing.

| File | Where it appears | Shape |
| --- | --- | --- |
| *(hero is already live)* | Hero, beside the headline | Served from the Webflow CDN. Framed 4:3.6 with `object-position: 50% 46%`, which trims the sky and the footpath and centres the faces and the sign |
| `recent-01.jpg` … `recent-06.jpg` | "Recent buys" scrolling strip | Portrait 4:5 |
| `team-rumeysa.jpg` | Meet the team — Rahul, Shamindri, Ali Al Hilo and Shashyani are already served from the Webflow CDN | Square |
| `podcast-latest.jpg` | Podcast section | Landscape 16:9 |

Two slots still point at the Webflow asset library rather than this folder —
the small hero inset and the photo in the value section. Add `hero-inset.jpg`
and `value.jpg` here and change those two `src` attributes if you'd rather
they were local too.

Notes:

- The "Recent buys" tiles are written out twice in the HTML so the marquee
  loops seamlessly. Both copies already point at the same six filenames, so
  adding the files is all that's needed.
- Three photos is a workable fallback if six aren't ready — delete the tiles
  you can't fill, from **both** copies.
- Export at roughly 1600px on the long edge. Anything larger is wasted.
