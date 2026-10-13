# Dima Laundry website

Static site for dimalaundry.com, hosted on Cloudflare. Every page is plain HTML so Google, ChatGPT, Gemini and other AI crawlers can read it.

## Editing
All content is generated. Do not edit the HTML files directly.

- Facts, branches, services, reviews: `src/content.py`
- Prices: `src/prices.json` (from the client's retail price list, 12 Oct 2026)
- Page layouts: `src/pages.py` and `src/home.py`
- Styles and scripts: `src/site.css`, `src/site.js`

Pages are written to `public/`, which is what Cloudflare serves. Rebuild with `python3 src/build.py`, then commit and push. Cloudflare deploys automatically.

Every push to main deploys automatically.
