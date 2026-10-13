"""Dima Laundry site generator.

Run:  python3 src/build.py
Writes every page as static HTML into the repo root. Edit content in src/content.py,
prices in src/prices.json, styles in src/site.css, behaviour in src/site.js.
"""
import html, json, os, re, shutil, sys
from urllib.parse import quote_plus

SRC = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SRC)
sys.path.insert(0, SRC)
import content as C  # noqa: E402

DOMAIN = "https://www.dimalaundry.com"
CSS = open(os.path.join(SRC, "site.css"), encoding="utf-8").read()
JS = open(os.path.join(SRC, "site.js"), encoding="utf-8").read()
P = json.load(open(os.path.join(SRC, "prices.json"), encoding="utf-8"))

WA_ICON = re.search(r"(<svg.*?</svg>)", open(os.path.join(SRC, "_wa_ref.html"), encoding="utf-8").read(), re.S).group(1)
_foot = open(os.path.join(SRC, "_footer_ref.html"), encoding="utf-8").read()
APPLE_SVG, GPLAY_SVG = re.findall(r'(<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="[^"]+"/></svg>)', _foot)[:2]
WAVE = '<svg class="wave" viewBox="0 0 1440 60" preserveAspectRatio="none" aria-hidden="true"><path d="M0,32 C180,58 360,6 540,26 C720,46 900,62 1080,34 C1260,8 1350,22 1440,30 L1440,60 L0,60 Z"/></svg>'

esc = html.escape
PAGES = []  # (path, html) for sitemap


# ---------- helpers ----------
def money(v):
    if v in (None, "--", ""):
        return "n/a"
    if isinstance(v, (int, float)):
        return f"{v:.2f}" if v != int(v) else f"{int(v)}"
    return str(v)


NAME_FIX = {
    "Pyjma suit - 2 Pcs": "Pyjama suit (2 pcs)", "Pyjama Top": "Pyjama top", "Pyjama Bottom": "Pyjama bottom",
    "Slippers/ Sandles": "Slippers / sandals", "Curtain - Schiffon (Sq.Mt)": "Curtain, chiffon (per sq m)",
    "Curtain - Black Out (Sq.Mt)": "Curtain, blackout (per sq m)", "Curtain - Normal (Sq.Mt)": "Curtain, standard (per sq m)",
    "Carpet (Sq.Mt)": "Carpet (per sq m)", "Carpet - Handmade (Sq.Mt)": "Carpet, handmade (per sq m)",
    "Carpet - Leather (Sq.Mt)": "Carpet, leather (per sq m)", "Carpet - Woolen (Sq.Mt)": "Carpet, wool (per sq m)",
    "Shiela/ Scarf": "Sheila / scarf", "Shiela/ Scarf Wool": "Sheila / scarf, wool", "Bag Pack": "Backpack",
    "Leather Bag -  Big": "Leather bag, big", "Leather Bag - Small": "Leather bag, small",
    "Hand Bag small/Purse": "Handbag, small / purse", "Handbag - Big / Oversized": "Handbag, big / oversized",
    "Suit 2Pcs": "Suit (2 pcs)", "Suit 3 Pcs": "Suit (3 pcs)", "Track Suit 2 pcs": "Tracksuit (2 pcs)",
    "Salwar Suit - 2Pcs": "Salwar suit (2 pcs)", "Salwar Suit - 3Pcs": "Salwar suit (3 pcs)",
    "Trouser - Leather (From)": "Trouser, leather (from)", "Baniyan/ Under Shirt": "Vest / undershirt",
    "Sofa Shampooing (Per Seat)": "Sofa shampooing (per seat)", "Sofa Cover - B": "Sofa cover, big",
    "Sofa Cover - M": "Sofa cover, medium", "Sofa Cover - S": "Sofa cover, small", "Mattress - K": "Mattress, king",
    "Mattress - Q": "Mattress, queen", "Mattress - Single": "Mattress, single", "Over Coat (Long)": "Overcoat, long",
    "Over Coat": "Overcoat", "Pull Over": "Pullover", "Duck feather Pillow": "Duck feather pillow",
    "Duck feather Duvet": "Duck feather duvet", "Cushion Case S/M": "Cushion case, small / medium",
    "Cushion Case Big": "Cushion case, big", "Cushion S/M": "Cushion, small / medium", "Cushion Big": "Cushion, big",
    "Socks (Pair)": "Socks (pair)", "Napkin/Duster": "Napkin / duster", "Blouse/Top": "Blouse / top",
    "Blouse/Top Delicate": "Blouse / top, delicate", "Alteration - Fitting": "Alteration, fitting",
    "Alteration - Minor": "Alteration, minor", "Tape Charges (Per Mtr)": "Curtain tape (per metre)",
    "Dhoti/Lungi": "Dhoti / lungi", "Fixing Tape on Curtains": "Fixing tape on curtains",
    "Kandura Wool": "Kandura, wool", "Ghutra Wool": "Ghutra, wool", "Abaya Delicate": "Abaya, delicate",
    "Jalabiya Delicate": "Jalabiya, delicate", "Jacket Leather": "Jacket, leather", "Dress Leather": "Dress, leather",
    "Skirt Pleated": "Skirt, pleated", "Dress Short": "Dress, short", "Dress Long": "Dress, long",
    "Party Dress Regular": "Party / evening dress", "Party Dress Heavy": "Party / evening dress, heavy",
    "Bed Protector": "Mattress protector", "Blanket Woolen": "Blanket, wool", "MOP": "Mop", "Sports  Shoes": "Sports shoes",
}


def nm(n):
    n = NAME_FIX.get(n, n)
    return n[:1].upper() + n[1:] if n else n


def find_item(name, *groups):
    for g in groups:
        for row in g:
            if row[0] == name:
                return row
    raise KeyError(name)


def garment_table(rows, caption=None, press=True):
    head = "<tr><th>Item</th><th>Standard, cleaned and pressed</th>" + ("<th>Standard, pressing only</th>" if press else "") + "<th>Premium, cleaned and pressed</th></tr>"
    body = ""
    for r in rows:
        body += f"<tr><td>{esc(nm(r[0]))}</td><td>AED {money(r[1])}</td>" + (f"<td>AED {money(r[2])}</td>" if press else "") + f"<td>AED {money(r[3])}</td></tr>"
    cap = f"<caption>{esc(caption)}</caption>" if caption else ""
    return f'<div class="tbl"><table>{cap}<thead>{head}</thead><tbody>{body}</tbody></table></div>'


def simple_table(rows, cols, caption=None):
    head = "".join(f"<th>{esc(c)}</th>" for c in cols)
    body = ""
    for r in rows:
        cells = f"<td>{esc(nm(r[0]))}</td>" + "".join(f"<td>{('AED ' + money(v)) if isinstance(v, (int, float)) else esc(str(v) if v not in (None, '--') else 'n/a')}</td>" for v in r[1:])
        body += f"<tr>{cells}</tr>"
    cap = f"<caption>{esc(caption)}</caption>" if caption else ""
    return f'<div class="tbl"><table>{cap}<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'


def ld(o):
    return '<script type="application/ld+json">' + json.dumps(o, ensure_ascii=False) + "</script>"


ORG = {
    "@context": "https://schema.org", "@type": "Organization", "@id": DOMAIN + "/#org", "name": "Dima Laundry",
    "legalName": "Dima Laundry LLC", "url": DOMAIN + "/", "logo": DOMAIN + "/logo.png", "foundingDate": "2001",
    "email": C.EMAIL,
    "description": "Dubai laundry and dry cleaning company operating since 2001, with 8 retail branches, 3 processing centres in Al Quoz, pickup and delivery, and commercial laundry for hotels and businesses.",
    "address": {"@type": "PostalAddress", "streetAddress": C.HQ_ADDRESS, "addressLocality": "Dubai", "addressCountry": "AE"},
    "areaServed": {"@type": "City", "name": "Dubai"},
    "contactPoint": [
        {"@type": "ContactPoint", "telephone": "+971-800-3462", "contactType": "customer service", "availableLanguage": ["English", "Arabic"]},
        {"@type": "ContactPoint", "telephone": "+971-56-998-4493", "contactType": "sales", "description": "Commercial laundry enquiries"},
    ],
    "sameAs": ["https://www.facebook.com/p/Dima-Laundry-100089460412002/", C.APP_IOS, C.APP_ANDROID],
}


def faq_schema(qas):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in qas]}


def faq_html(qas, heading="Frequently asked questions"):
    items = "".join(f'<details class="qa"><summary>{esc(q)}</summary><p>{a}</p></details>' for q, a in qas)
    return f'<h2>{heading}</h2>{items}'


def crumbs(path, name):
    segs = [s for s in path.strip("/").split("/") if s]
    labels = {"services": ("Services", "/services"), "branches": ("Locations", "/branches"), "business": ("Commercial Laundry", "/business")}
    trail = [("Home", "/")]
    for i, s in enumerate(segs):
        if i == len(segs) - 1:
            trail.append((name, "/" + "/".join(segs)))
        else:
            trail.append(labels.get(s, (s.title(), "/" + s)))
    htm = '<nav class="crumbs" aria-label="Breadcrumb"><ol>' + "".join(
        f'<li><a href="{u}">{esc(t)}</a></li>' if i < len(trail) - 1 else f'<li aria-current="page">{esc(t)}</li>'
        for i, (t, u) in enumerate(trail)) + "</ol></nav>"
    sch = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": t, "item": DOMAIN + u} for i, (t, u) in enumerate(trail)]}
    return htm, sch


def app_badges(cls=""):
    return (f'<div class="app-badges {cls}">'
            f'<a class="store" href="{C.APP_IOS}" rel="noopener" target="_blank">{APPLE_SVG}<span><small>Download on the</small> App Store</span></a>'
            f'<a class="store" href="{C.APP_ANDROID}" rel="noopener" target="_blank">{GPLAY_SVG}<span><small>Get it on</small> Google Play</span></a></div>')


def wa_link(text=None, number=None):
    number = number or C.WA
    return f"https://wa.me/{number}" + (f"?text={quote_plus(text)}" if text else "")


def btns(book_label="Book a Pickup", wa_text=None, extra=""):
    return (f'<div class="hero-actions"><a class="btn btn-main" href="/contact#book">{book_label}</a>'
            f'<a class="btn btn-line" href="{wa_link(wa_text or "Hi Dima Laundry, I would like to book a pickup.")}">WhatsApp Us</a>{extra}</div>')


# ---------- page shell ----------
def nav(active):
    items = [("Services", "/services"), ("Prices", "/prices"), ("Locations", "/branches"),
             ("Commercial Laundry", "/business"), ("About", "/about-us")]
    lis = "".join(f'<li><a href="{u}"{" aria-current=\"page\"" if (active == u or active.startswith(u + "/")) else ""}>{t}</a></li>' for t, u in items)
    return f'''<div class="app-bar" hidden><span>Get the Dima Laundry app</span><a class="app-bar-go" data-ios="{C.APP_IOS}" data-android="{C.APP_ANDROID}" href="{C.APP_IOS}">Open</a><button type="button" class="app-bar-x" aria-label="Close">&times;</button></div>
<header class="site-head">
  <div class="wrap head-row">
    <a class="logo" href="/"><img src="/logo.png" alt="Dima Laundry" width="141" height="44"></a>
    <nav aria-label="Main"><ul>{lis}</ul></nav>
    <div class="head-cta"><a class="tel" href="tel:{C.TEL}">{C.TOLL}</a><a class="btn btn-main btn-book" href="/contact#book">Book a Pickup</a></div>
  </div>
</header>'''


def footer():
    def col(title, m):
        return f'<div><h2>{title}</h2><ul>' + "".join(f'<li><a href="{u}">{esc(t)}</a></li>' for t, u in m) + "</ul></div>"
    svc = [(s["short"], "/services/" + s["slug"]) for s in C.SERVICES]
    loc = [(b["name"], "/branches/" + b["slug"]) for b in C.BRANCHES] + [("Processing centres", "/branches/al-quoz-head-office")]
    biz = [("Commercial laundry", "/business")] + [(b["short"], "/business/" + b["slug"]) for b in C.BUSINESS]
    return f'''<div class="foot-wave">{WAVE}</div><footer class="site-foot">
  <div class="wrap foot-grid">
    <div class="foot-brand">
      <a class="logo" href="/"><img src="/logo-white.png" alt="Dima Laundry" width="167" height="52"></a>
      <p>Laundry and dry cleaning in Dubai since 2001. Dima Laundry LLC, {esc(C.HQ_ADDRESS)}, Dubai.</p>
      <p>Toll free <a href="tel:{C.TEL}">{C.TOLL}</a><br>WhatsApp <a href="{wa_link()}">{C.RETAIL}</a><br>Commercial <a href="tel:+971569984493">{C.BIZ}</a><br><a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p>
      {app_badges("on-dark")}
    </div>
    {col("Services", svc)}
    {col("Locations", loc)}
    {col("Commercial Laundry", biz)}
  </div>
  <div class="wrap foot-base"><span>Dima Laundry LLC. Serving Dubai since 2001.</span><span><a href="/prices">Prices</a> <a href="/faq">FAQ</a> <a href="/contact">Contact</a> <a href="/best-laundry-services-dubai">Compare Dubai laundries</a></span></div>
</footer>
<div class="mobile-bar"><a href="tel:{C.TEL}">Call</a><a href="{wa_link()}">WhatsApp</a><a href="/contact#book" class="mb-book">Book Pickup</a></div>
<a class="wa-float" href="{wa_link()}" aria-label="Chat with Dima Laundry on WhatsApp">{WA_ICON}<span class="wa-label">Chat on WhatsApp</span></a>'''


def shell(path, title, desc, body, schemas, noindex=False):
    canon = DOMAIN + path
    t = esc(title)
    d = esc(desc)
    robots = '<meta name="robots" content="noindex">' if noindex else ""
    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<script>document.documentElement.classList.add("js")</script>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t}</title>
<meta name="description" content="{d}">{robots}
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="en" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{DOMAIN}/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/favicon.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#8C267D">
<link rel="preload" href="/fonts/outfit-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
<style>{CSS}</style>
{"".join(ld(s) for s in schemas)}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{nav(path)}
<main id="main">
{body}
</main>
{footer()}
<script>{JS}</script>
</body>
</html>'''
    for bad in ("—", "–"):
        assert bad not in page, f"dash in {path}"
    return page


def write(path, page, sitemap=True):
    fp = os.path.join(ROOT, "index.html") if path == "/" else os.path.join(ROOT, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w", encoding="utf-8").write(page)
    if sitemap:
        PAGES.append(path)


def page_hero(path, name, h1, sub, book_label="Book a Pickup", wa_text=None, extra_btn=""):
    ch, cs = crumbs(path, name)
    return (f'<section class="page-hero"><div class="bubbles" data-count="7" aria-hidden="true"></div><div class="wrap">{ch}'
            f'<h1>{h1}</h1><div class="answer tag-card"><span class="tag-hole" aria-hidden="true"></span><p>{sub}</p></div>'
            f'{btns(book_label, wa_text, extra_btn)}</div></section>'), cs


def cta_band(text, book_label="Book a Pickup", wa_text=None):
    return (f'<section class="cta-band"><div class="bubbles" data-count="6" aria-hidden="true"></div><div class="wrap"><p>{text}</p>'
            f'<div><a class="btn btn-tag" href="/contact#book">{book_label}</a><a class="btn btn-onblue" href="{wa_link(wa_text or "Hi Dima Laundry, I would like to book a pickup.")}">WhatsApp Dima</a></div></div></section>')


def how_steps(steps=None):
    steps = steps or C.HOW_STEPS
    lis = "".join(f"<li><strong>{esc(t)}</strong> {esc(d)}</li>" for t, d in steps)
    return f"<ol class=\"steps\">{lis}</ol>"


def review_card(k):
    text, place, gkey = C.REVIEWS[k]
    return (f'<figure class="rv"><div class="stars" aria-label="5 out of 5 stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
            f'<blockquote>{esc(text)}</blockquote><figcaption>Google review, <a href="{C.GMAPS[gkey]}" rel="noopener" target="_blank">{esc(place)}</a></figcaption></figure>')


def reviews_block(keys, heading="What customers say on Google", rating=False):
    rl = f'<p class="rating-line">{C.RATING_LINE} <a href="{C.GMAPS["q4"]}" rel="noopener" target="_blank">Read all reviews on Google</a></p>' if rating else ""
    return f'<section class="rv-sec"><h2>{heading}</h2>{rl}<div class="rv-grid">{"".join(review_card(k) for k in keys)}</div></section>'


def bullets(items):
    return "<ul class=\"ticks\">" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def updated():
    return '<p class="updated">Last updated October 2026.</p>'


# ---------- forms ----------
def booking_form():
    return f'''<form class="book-form js-wa-form" id="book" data-wa="{C.WA}" data-intro="New pickup request from the Dima Laundry website" action="https://wa.me/{C.WA}" method="get">
  <h2>Book a pickup</h2>
  <p class="small">Send the form and WhatsApp opens with your request filled in. Tap send and the Dima team confirms your pickup time.</p>
  <div class="f-grid">
    <label>Name<input name="Name" autocomplete="name" required></label>
    <label>Phone<input name="Phone" type="tel" autocomplete="tel" required></label>
    <label>Area<input name="Area" placeholder="e.g. Dubai Marina" required></label>
    <label>Address<input name="Address" autocomplete="street-address"></label>
    <label>Pickup date<input name="Pickup date" type="date"></label>
    <label>Time slot<select name="Time slot"><option>Morning</option><option>Afternoon</option><option>Evening</option></select></label>
    <label class="wide">Services needed<input name="Services" placeholder="Dry cleaning, laundry, abayas, curtains..."></label>
    <label class="wide">How did you hear about us?<select name="Heard about us"><option>Google</option><option>ChatGPT or another AI assistant</option><option>Instagram</option><option>Friend</option><option>Walked past a branch</option></select></label>
    <label class="wide">Notes<textarea name="Notes" rows="3"></textarea></label>
  </div>
  <button class="btn btn-main" type="submit">Send booking on WhatsApp</button>
  <p class="small">Prefer to talk? Call <a href="tel:{C.TEL}">{C.TOLL}</a>.</p>
</form>'''


def quote_form():
    return f'''<form class="book-form js-wa-form" id="quote" data-wa="{C.BIZ_WA}" data-intro="Commercial laundry quote request from the Dima Laundry website" action="https://wa.me/{C.BIZ_WA}" method="get">
  <h2>Request a commercial quote</h2>
  <p class="small">Send the form and WhatsApp opens to our commercial team with your details filled in. Or call <a href="tel:+971569984493">{C.BIZ}</a>.</p>
  <div class="f-grid">
    <label>Company<input name="Company" required></label>
    <label>Business type<select name="Business type"><option>Hotel or serviced apartments</option><option>Holiday homes or Airbnb</option><option>Restaurant or cafe</option><option>Salon or spa</option><option>Gym</option><option>Clinic</option><option>Corporate uniforms</option><option>Other</option></select></label>
    <label>Weekly volume (kg or pieces)<input name="Weekly volume"></label>
    <label>Area<input name="Area"></label>
    <label>Contact name<input name="Contact name" required></label>
    <label>Phone<input name="Phone" type="tel" required></label>
    <label class="wide">What do you need cleaned?<textarea name="Items" rows="3" placeholder="Bed linen, towels, uniforms, table linen..."></textarea></label>
  </div>
  <button class="btn btn-main" type="submit">Send quote request on WhatsApp</button>
</form>'''


# ---------- build steps ----------
from pages import build_all  # noqa: E402

if __name__ == "__main__":
    build_all(sys.modules[__name__])
