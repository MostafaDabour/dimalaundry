"""Dima Laundry site generator.

Run:  python3 src/build.py
Writes every page as static HTML into the repo root. Edit content in src/content.py,
prices in src/prices.json, styles in src/site.css, behaviour in src/site.js.
"""
import html, json, os, re, shutil, sys
from urllib.parse import quote_plus

SRC = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(os.path.dirname(SRC), "public")
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
    "legalName": "Dima Laundry LLC", "alternateName": ["ديما لاندري", "Dima Dry Cleaning", "DIMA Laundry"], "url": DOMAIN + "/", "logo": DOMAIN + "/logo.png", "foundingDate": "2001",
    "email": C.EMAIL,
    "description": "Dubai laundry and dry cleaning company operating since 2001, with 8 retail branches, 3 processing centres in Al Quoz, pickup and delivery, and commercial laundry for hotels and businesses.",
    "address": {"@type": "PostalAddress", "streetAddress": C.HQ_ADDRESS, "addressLocality": "Dubai", "addressCountry": "AE"},
    "areaServed": {"@type": "City", "name": "Dubai"},
    "knowsAbout": ["Laundry", "Dry cleaning", "Ironing", "Abaya cleaning", "Kandura laundry", "Wedding dress cleaning", "Shoe cleaning", "Handbag cleaning", "Carpet cleaning", "Curtain cleaning", "Sofa shampooing", "Commercial laundry", "Hotel linen laundry"],
    "contactPoint": [
        {"@type": "ContactPoint", "telephone": "+971-800-3462", "email": C.SUPPORT_EMAIL, "contactType": "customer service", "availableLanguage": ["English", "Arabic"]},
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


UI = {
    "en": {
        "home": "Home", "services": "Services", "prices": "Prices", "locations": "Locations", "commercial": "Commercial Laundry",
        "about": "About", "book": "Book a Pickup", "wa_us": "WhatsApp Us", "wa_dima": "WhatsApp Dima", "faq_h": "Frequently asked questions",
        "skip": "Skip to content", "app_bar": "Get the Dima Laundry app", "open": "Open", "close": "Close",
        "foot_intro": f"Laundry and dry cleaning in Dubai since 2001. Dima Laundry LLC, {C.HQ_ADDRESS}, Dubai.",
        "toll": "Toll free", "wa": "WhatsApp", "biz": "Commercial", "foot_base": "Dima Laundry LLC. Serving Dubai since 2001.",
        "faq": "FAQ", "contact": "Contact", "compare": "Compare Dubai laundries", "blog": "Blog", "privacy": "Privacy", "terms": "Terms",
        "call": "Call", "book_short": "Book Pickup", "chat": "Chat on WhatsApp", "proc": "Processing centres",
        "dl_on": "Download on the", "get_on": "Get it on", "lang_switch": "العربية", "updated": "Last updated October 2026.",
        "wa_book_text": "Hi Dima Laundry, I would like to book a pickup.", "wa_quote_text": "Hi Dima Laundry, I would like a commercial laundry quote.",
    },
    "ar": {
        "home": "الرئيسية", "services": "الخدمات", "prices": "الأسعار", "locations": "الفروع", "commercial": "مغسلة الشركات",
        "about": "من نحن", "book": "احجز استلام", "wa_us": "راسلنا واتساب", "wa_dima": "واتساب ديما", "faq_h": "الأسئلة الشائعة",
        "skip": "انتقل إلى المحتوى", "app_bar": "حمّل تطبيق ديما لاندري", "open": "فتح", "close": "إغلاق",
        "foot_intro": "مغسلة وتنظيف جاف في دبي منذ 2001. ديما لاندري ذ.م.م، شارع 24a رقم 22، القوز الصناعية 3، دبي.",
        "toll": "الرقم المجاني", "wa": "واتساب", "biz": "الشركات", "foot_base": "ديما لاندري ذ.م.م. في خدمة دبي منذ 2001.",
        "faq": "الأسئلة الشائعة", "contact": "تواصل معنا", "compare": "مقارنة مغاسل دبي", "blog": "المدونة", "privacy": "الخصوصية", "terms": "الشروط",
        "call": "اتصل", "book_short": "احجز", "chat": "تحدث معنا واتساب", "proc": "مراكز التنظيف",
        "dl_on": "حمّله من", "get_on": "احصل عليه من", "lang_switch": "English", "updated": "آخر تحديث: أكتوبر 2026.",
        "wa_book_text": "مرحبا ديما لاندري، أرغب بحجز استلام للملابس.", "wa_quote_text": "مرحبا ديما لاندري، أرغب بعرض سعر لخدمة مغسلة الشركات.",
    },
}


def pfx(lang):
    return "/ar" if lang == "ar" else ""


def crumbs(path, name, lang="en"):
    u = UI[lang]
    base = pfx(lang)
    rel = path[len(base):] if base and path.startswith(base) else path
    segs = [s for s in rel.strip("/").split("/") if s]
    labels = {"services": (u["services"], base + "/services"), "branches": (u["locations"], base + "/branches"),
              "business": (u["commercial"], base + "/business"), "blog": (u["blog"], base + "/blog")}
    trail = [(u["home"], base + "/")]
    for i, s in enumerate(segs):
        if i == len(segs) - 1:
            trail.append((name, path))
        else:
            trail.append(labels.get(s, (s.title(), base + "/" + s)))
    htm = '<nav class="crumbs" aria-label="Breadcrumb"><ol>' + "".join(
        f'<li><a href="{u_}">{esc(t)}</a></li>' if i < len(trail) - 1 else f'<li aria-current="page">{esc(t)}</li>'
        for i, (t, u_) in enumerate(trail)) + "</ol></nav>"
    sch = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": t, "item": DOMAIN + u_} for i, (t, u_) in enumerate(trail)]}
    return htm, sch


def app_badges(cls="", lang="en"):
    u = UI[lang]
    return (f'<div class="app-badges {cls}">'
            f'<a class="store" href="{C.APP_IOS}" rel="noopener" target="_blank">{APPLE_SVG}<span><small>{u["dl_on"]}</small> App Store</span></a>'
            f'<a class="store" href="{C.APP_ANDROID}" rel="noopener" target="_blank">{GPLAY_SVG}<span><small>{u["get_on"]}</small> Google Play</span></a></div>')


def wa_link(text=None, number=None):
    number = number or C.WA
    return f"https://wa.me/{number}" + (f"?text={quote_plus(text)}" if text else "")


def btns(book_label=None, wa_text=None, extra="", lang="en", book_href=None):
    u = UI[lang]
    book_label = book_label or u["book"]
    book_href = book_href or pfx(lang) + "/contact#book"
    return (f'<div class="hero-actions"><a class="btn btn-main" href="{book_href}">{book_label}</a>'
            f'<a class="btn btn-line" href="{wa_link(wa_text or u["wa_book_text"])}">{u["wa_us"]}</a>{extra}</div>')


# ---------- page shell ----------
def nav(active, lang="en", alt=None):
    u = UI[lang]
    b = pfx(lang)
    items = [(u["services"], b + "/services"), (u["prices"], b + "/prices"), (u["locations"], b + "/branches"),
             (u["commercial"], b + "/business"), (u["about"], b + "/about-us")]
    lis = "".join(f'<li><a href="{x}"{" aria-current=\"page\"" if (active == x or active.startswith(x + "/")) else ""}>{t}</a></li>' for t, x in items)
    sw = f'<a class="lang-sw" href="{alt}" hreflang="{"en" if lang == "ar" else "ar"}" lang="{"en" if lang == "ar" else "ar"}">{u["lang_switch"]}</a>' if alt else ""
    return f'''<div class="app-bar" hidden><span>{u["app_bar"]}</span><a class="app-bar-go" data-ios="{C.APP_IOS}" data-android="{C.APP_ANDROID}" href="{C.APP_IOS}">{u["open"]}</a><button type="button" class="app-bar-x" aria-label="{u["close"]}">&times;</button></div>
<header class="site-head">
  <div class="wrap head-row">
    <a class="logo" href="{b}/"><img src="/logo.png" alt="Dima Laundry" width="141" height="44"></a>
    <nav aria-label="Main"><ul>{lis}</ul></nav>
    <div class="head-cta">{sw}<a class="tel" href="tel:{C.TEL}" dir="ltr">{C.TOLL}</a><a class="btn btn-main btn-book" href="{b}/contact#book">{u["book"]}</a></div>
  </div>
</header>'''


def blog_col(lang="en"):
    from blog_posts import POSTS
    u = UI[lang]
    title = u["blog"] + (" (English)" if lang == "ar" else "")
    items = "".join(f'<li><a href="/blog/{p["slug"]}">{esc(p.get("short") or p["h1"].split(":")[0])}</a></li>' for p in POSTS[:6])
    allg = "All guides" if lang == "en" else "كل المقالات"
    return f'<div><h2><a href="/blog">{title}</a></h2><ul>{items}<li><a href="/blog"><strong>{allg}</strong></a></li></ul></div>'


def footer(lang="en"):
    u = UI[lang]
    b = pfx(lang)
    def col(title, m):
        return f'<div><h2>{title}</h2><ul>' + "".join(f'<li><a href="{x}">{esc(t)}</a></li>' for t, x in m) + "</ul></div>"
    if lang == "ar":
        import content_ar as A
        svc = [(A.SERVICES[s["slug"]]["short"], b + "/services/" + s["slug"]) for s in C.SERVICES]
        loc = [(A.BRANCHES[x["slug"]]["name"], b + "/branches/" + x["slug"]) for x in C.BRANCHES] + [(u["proc"], b + "/branches/al-quoz-head-office")]
        biz = [(u["commercial"], b + "/business")] + [(A.BUSINESS[x["slug"]]["short"], b + "/business/" + x["slug"]) for x in C.BUSINESS]
    else:
        svc = [(s["short"], "/services/" + s["slug"]) for s in C.SERVICES]
        loc = [(x["name"], "/branches/" + x["slug"]) for x in C.BRANCHES] + [(u["proc"], "/branches/al-quoz-head-office")]
        biz = [(u["commercial"], "/business")] + [(x["short"], "/business/" + x["slug"]) for x in C.BUSINESS]
    return f'''<div class="foot-wave">{WAVE}</div><footer class="site-foot">
  <div class="wrap foot-grid">
    <div class="foot-brand">
      <a class="logo" href="{b}/"><img src="/logo-white.png" alt="Dima Laundry" width="167" height="52"></a>
      <p>{u["foot_intro"]}</p>
      <p>{u["toll"]} <a href="tel:{C.TEL}" dir="ltr">{C.TOLL}</a><br>{u["wa"]} <a href="{wa_link()}" dir="ltr">{C.RETAIL}</a><br>{u["biz"]} <a href="tel:+971569984493" dir="ltr">{C.BIZ}</a><br><a href="mailto:{C.EMAIL}">{C.EMAIL}</a><br><a href="mailto:{C.SUPPORT_EMAIL}">{C.SUPPORT_EMAIL}</a></p>
      {app_badges("on-dark", lang)}
    </div>
    {col(u["services"], svc)}
    {col(u["locations"], loc)}
    {col(u["commercial"], biz)}
    {blog_col(lang)}
  </div>
  <div class="wrap foot-base"><span>{u["foot_base"]}</span><span><a href="{b}/prices">{u["prices"]}</a> <a href="{b}/faq">{u["faq"]}</a> <a href="/blog">{u["blog"] + (" (English)" if lang == "ar" else "")}</a> <a href="{b}/contact">{u["contact"]}</a> <a href="{b}/privacy">{u["privacy"]}</a> <a href="{b}/terms">{u["terms"]}</a> <a href="/best-laundry-services-dubai">{u["compare"] + (" (English)" if lang == "ar" else "")}</a></span></div>
</footer>
<div class="mobile-bar"><a href="tel:{C.TEL}">{u["call"]}</a><a href="{wa_link()}">{u["wa"]}</a><a href="{b}/contact#book" class="mb-book">{u["book_short"]}</a></div>
<a class="wa-float" href="{wa_link()}" aria-label="{u["chat"]}">{WA_ICON}<span class="wa-label">{u["chat"]}</span></a>'''


AR_PATHS = set()  # English paths that have an Arabic version


def shell(path, title, desc, body, schemas, noindex=False, lang="en", alt=None):
    canon = DOMAIN + path
    t = esc(title)
    d = esc(desc)
    robots = '<meta name="robots" content="noindex">' if noindex else ""
    hreflang = ""
    if alt is None:
        if lang == "en" and path in AR_PATHS:
            alt = "/ar" + (path if path != "/" else "/")
        elif lang == "ar":
            alt = path[3:] or "/"
    if alt:
        en_p, ar_p = (path, alt) if lang == "en" else (alt, path)
        hreflang = (f'<link rel="alternate" hreflang="en" href="{DOMAIN + en_p}">'
                    f'<link rel="alternate" hreflang="ar" href="{DOMAIN + ar_p}">'
                    f'<link rel="alternate" hreflang="x-default" href="{DOMAIN + en_p}">')
    else:
        hreflang = f'<link rel="alternate" hreflang="{lang}" href="{canon}">'
    font = '<link rel="preload" href="/fonts/outfit-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>' if lang == "en" else \
        '<link rel="preload" href="/fonts/ibm-plex-sans-arabic-arabic-700-normal.woff2" as="font" type="font/woff2" crossorigin>'
    page = f'''<!DOCTYPE html>
<html lang="{lang}" dir="{"rtl" if lang == "ar" else "ltr"}">
<head>
<meta charset="utf-8">
<script>document.documentElement.classList.add("js")</script>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t}</title>
<meta name="description" content="{d}">{robots}
<link rel="canonical" href="{canon}">
{hreflang}
<meta property="og:type" content="website">
<meta property="og:locale" content="{"ar_AE" if lang == "ar" else "en_AE"}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{DOMAIN}/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/favicon.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#8C267D">
{font}
<style>{CSS}</style>
{"".join(ld(s) for s in schemas)}
</head>
<body>
<a class="skip" href="#main">{UI[lang]["skip"]}</a>
{nav(path, lang, alt)}
<main id="main">
{body}
</main>
{footer(lang)}
<script>{JS}</script>
</body>
</html>'''
    for bad in ("\u2014", "\u2013"):
        assert bad not in page, f"dash in {path}"
    return page


def write(path, page, sitemap=True):
    fp = os.path.join(ROOT, "index.html") if path == "/" else os.path.join(ROOT, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w", encoding="utf-8").write(page)
    if sitemap:
        PAGES.append(path)


def page_hero(path, name, h1, sub, book_label=None, wa_text=None, extra_btn="", lang="en", book_href=None):
    ch, cs = crumbs(path, name, lang)
    return (f'<section class="page-hero"><div class="bubbles" data-count="7" aria-hidden="true"></div><div class="wrap">{ch}'
            f'<h1>{h1}</h1><div class="answer tag-card"><span class="tag-hole" aria-hidden="true"></span><p>{sub}</p></div>'
            f'{btns(book_label, wa_text, extra_btn, lang, book_href)}</div></section>'), cs


def cta_band(text, book_label=None, wa_text=None, lang="en", book_href=None):
    u = UI[lang]
    return (f'<section class="cta-band"><div class="bubbles" data-count="6" aria-hidden="true"></div><div class="wrap"><p>{text}</p>'
            f'<div><a class="btn btn-tag" href="{book_href or pfx(lang) + "/contact#book"}">{book_label or u["book"]}</a><a class="btn btn-onblue" href="{wa_link(wa_text or u["wa_book_text"])}">{u["wa_dima"]}</a></div></div></section>')


def how_steps(steps=None):
    steps = steps or C.HOW_STEPS
    lis = "".join(f"<li><strong>{esc(t)}</strong> {esc(d)}</li>" for t, d in steps)
    return f"<ol class=\"steps\">{lis}</ol>"


def review_card(k, lang="en"):
    text, place, gkey = C.REVIEWS[k]
    lbl = "Google review" if lang == "en" else "\u062a\u0642\u064a\u064a\u0645 \u062c\u0648\u062c\u0644"
    return (f'<figure class="rv"><div class="stars" aria-label="5 out of 5 stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
            f'<blockquote lang="en" dir="ltr">{esc(text)}</blockquote><figcaption>{lbl}, <a href="{C.GMAPS[gkey]}" rel="noopener" target="_blank">{esc(place)}</a></figcaption></figure>')


def reviews_block(keys, heading="What customers say on Google", rating=False, live="all", rating_html=None, lang="en"):
    if rating_html:
        rl = f'<p class="rating-line">{rating_html}</p>'
    elif rating:
        more = "Read all reviews on Google" if lang == "en" else "\u0627\u0642\u0631\u0623 \u0643\u0644 \u0627\u0644\u062a\u0642\u064a\u064a\u0645\u0627\u062a \u0639\u0644\u0649 \u062c\u0648\u062c\u0644"
        line = C.RATING_LINE if lang == "en" else C_AR_RATING_LINE()
        rl = f'<p class="rating-line">{line} <a href="{C.GMAPS["karama"]}" rel="noopener" target="_blank">{more}</a></p>'
    else:
        rl = ""
    attr = f' data-live="{live}" data-lang="{lang}"' if live else ""
    return f'<section class="rv-sec"><h2>{heading}</h2>{rl}<div class="rv-grid"{attr}>{"".join(review_card(k, lang) for k in keys)}</div></section>'


def C_AR_RATING_LINE():
    import content_ar as A
    return A.RATING_LINE


def bullets(items):
    return "<ul class=\"ticks\">" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def updated(lang="en"):
    return f'<p class="updated">{UI[lang]["updated"]}</p>'


# ---------- forms ----------
FORM_TXT = {
    "en": {
        "book_h": "Book a pickup", "book_p": "Send your details and the Dima team confirms your pickup time by phone or WhatsApp.",
        "name": "Name", "phone": "Phone", "email": "Email (optional)", "area": "Area", "area_ph": "e.g. Dubai Marina", "address": "Address",
        "date": "Pickup date", "slot": "Time slot", "slots": ["Morning", "Afternoon", "Evening"], "services": "Services needed",
        "services_ph": "Dry cleaning, laundry, abayas, curtains...", "heard": "How did you hear about us?",
        "heard_opts": ["Google", "ChatGPT or another AI assistant", "Instagram", "Friend", "Walked past a branch"], "notes": "Notes",
        "send": "Request my pickup", "talk": "Prefer to talk? Call", "privacy": "By sending this form you agree to our <a href=\"/privacy\">privacy policy</a>.",
        "quote_h": "Request a commercial quote", "quote_p": "Send your details and the commercial team replies within one working day. Or call",
        "company": "Company", "btype": "Business type",
        "btypes": ["Hotel or serviced apartments", "Holiday homes or Airbnb", "Restaurant or cafe", "Salon or spa", "Gym", "Clinic", "Corporate uniforms", "Other"],
        "volume": "Weekly volume (kg or pieces)", "cname": "Contact name", "items": "What do you need cleaned?", "items_ph": "Bed linen, towels, uniforms, table linen...",
        "qsend": "Send quote request", "ok": "Thank you. Your request has reached the Dima team and they will be in touch shortly.",
        "ok_wa": "Want a faster reply? Message us on WhatsApp", "intro_book": "New pickup request from the Dima Laundry website", "intro_quote": "Commercial laundry quote request from the Dima Laundry website",
    },
    "ar": {
        "book_h": "احجز استلام الملابس", "book_p": "أرسل بياناتك وسيتواصل معك فريق ديما لتأكيد موعد الاستلام عبر الهاتف أو واتساب.",
        "name": "الاسم", "phone": "رقم الهاتف", "email": "البريد الإلكتروني (اختياري)", "area": "المنطقة", "area_ph": "مثال: دبي مارينا", "address": "العنوان",
        "date": "تاريخ الاستلام", "slot": "الفترة", "slots": ["صباحا", "بعد الظهر", "مساء"], "services": "الخدمات المطلوبة",
        "services_ph": "تنظيف جاف، غسيل، عبايات، ستائر...", "heard": "كيف عرفت عنا؟",
        "heard_opts": ["جوجل", "ChatGPT أو مساعد ذكاء اصطناعي", "إنستغرام", "صديق", "مررت بأحد الفروع"], "notes": "ملاحظات",
        "send": "اطلب الاستلام", "talk": "تفضّل الاتصال؟ اتصل على", "privacy": "بإرسال النموذج فإنك توافق على <a href=\"/ar/privacy\">سياسة الخصوصية</a>.",
        "quote_h": "اطلب عرض سعر للشركات", "quote_p": "أرسل بياناتك وسيرد عليك فريق الشركات خلال يوم عمل واحد. أو اتصل على",
        "company": "اسم الشركة", "btype": "نوع النشاط",
        "btypes": ["فندق أو شقق فندقية", "بيوت عطلات أو Airbnb", "مطعم أو مقهى", "صالون أو سبا", "نادي رياضي", "عيادة", "زي موظفين", "أخرى"],
        "volume": "الكمية الأسبوعية (كغ أو قطع)", "cname": "اسم المسؤول", "items": "ما الذي تحتاج تنظيفه؟", "items_ph": "مفارش، مناشف، زي موظفين، مفارش طاولات...",
        "qsend": "أرسل طلب عرض السعر", "ok": "شكرا لك. وصل طلبك إلى فريق ديما وسيتواصلون معك قريبا.",
        "ok_wa": "تريد ردا أسرع؟ راسلنا على واتساب", "intro_book": "طلب استلام جديد من موقع ديما لاندري", "intro_quote": "طلب عرض سعر للشركات من موقع ديما لاندري",
    },
}


def _opts(xs):
    return "".join(f"<option>{esc(x)}</option>" for x in xs)


def booking_form(lang="en"):
    f = FORM_TXT[lang]
    return f'''<form class="book-form js-lead-form" id="book" data-form="booking" data-lang="{lang}" data-wa="{C.WA}" data-intro="{esc(f["intro_book"])}" data-ok="{esc(f["ok"])}" data-okwa="{esc(f["ok_wa"])}" action="https://wa.me/{C.WA}" method="get" novalidate>
  <h2>{f["book_h"]}</h2>
  <p class="small">{f["book_p"]}</p>
  <div class="hp" aria-hidden="true"><label>Website<input name="website" tabindex="-1" autocomplete="off"></label></div>
  <div class="f-grid">
    <label>{f["name"]}<input name="Name" autocomplete="name" required></label>
    <label>{f["phone"]}<input name="Phone" type="tel" autocomplete="tel" required dir="ltr"></label>
    <label>{f["email"]}<input name="Email" type="email" autocomplete="email" dir="ltr"></label>
    <label>{f["area"]}<input name="Area" placeholder="{f["area_ph"]}" required></label>
    <label class="wide">{f["address"]}<input name="Address" autocomplete="street-address"></label>
    <label>{f["date"]}<input name="Pickup date" type="date"></label>
    <label>{f["slot"]}<select name="Time slot">{_opts(f["slots"])}</select></label>
    <label class="wide">{f["services"]}<input name="Services" placeholder="{f["services_ph"]}"></label>
    <label class="wide">{f["heard"]}<select name="Heard about us">{_opts(f["heard_opts"])}</select></label>
    <label class="wide">{f["notes"]}<textarea name="Notes" rows="3"></textarea></label>
  </div>
  <button class="btn btn-main" type="submit">{f["send"]}</button>
  <p class="small form-msg" role="status" aria-live="polite"></p>
  <p class="small">{f["talk"]} <a href="tel:{C.TEL}" dir="ltr">{C.TOLL}</a>. {f["privacy"]}</p>
</form>'''


def quote_form(lang="en"):
    f = FORM_TXT[lang]
    return f'''<form class="book-form js-lead-form" id="quote" data-form="business-quote" data-lang="{lang}" data-wa="{C.BIZ_WA}" data-intro="{esc(f["intro_quote"])}" data-ok="{esc(f["ok"])}" data-okwa="{esc(f["ok_wa"])}" action="https://wa.me/{C.BIZ_WA}" method="get" novalidate>
  <h2>{f["quote_h"]}</h2>
  <p class="small">{f["quote_p"]} <a href="tel:+971569984493" dir="ltr">{C.BIZ}</a>.</p>
  <div class="hp" aria-hidden="true"><label>Website<input name="website" tabindex="-1" autocomplete="off"></label></div>
  <div class="f-grid">
    <label>{f["company"]}<input name="Company" required></label>
    <label>{f["btype"]}<select name="Business type">{_opts(f["btypes"])}</select></label>
    <label>{f["volume"]}<input name="Weekly volume"></label>
    <label>{f["area"]}<input name="Area"></label>
    <label>{f["cname"]}<input name="Contact name" required></label>
    <label>{f["phone"]}<input name="Phone" type="tel" required dir="ltr"></label>
    <label class="wide">{f["email"]}<input name="Email" type="email" dir="ltr"></label>
    <label class="wide">{f["items"]}<textarea name="Items" rows="3" placeholder="{f["items_ph"]}"></textarea></label>
  </div>
  <button class="btn btn-main" type="submit">{f["qsend"]}</button>
  <p class="small form-msg" role="status" aria-live="polite"></p>
  <p class="small">{f["privacy"]}</p>
</form>'''


# ---------- build steps ----------
from pages import build_all  # noqa: E402

if __name__ == "__main__":
    build_all(sys.modules[__name__])
