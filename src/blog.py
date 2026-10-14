"""Blog hub and guide pages."""
import content as C
from blog_posts import POSTS

DATE_ISO = "2026-10-14"
DATE_TXT = "14 October 2026"


def build_blog(B):
    esc = B.esc
    for p in POSTS:
        path = "/blog/" + p["slug"]
        ch, cs = B.crumbs(path, p["h1"])
        body = f'<p class="byline">By the Dima Laundry team, {DATE_TXT}</p>'
        body += f'<div class="answer tag-card"><span class="tag-hole" aria-hidden="true"></span><p>{esc(p["answer"])}</p></div>'
        for h, htm in p["sections"]:
            body += f"<h2>{esc(h)}</h2>{htm}"
        body += B.faq_html(p["faqs"])
        body += '<p class="nearby">Related: ' + ", ".join(f'<a href="{u}">{esc(t)}</a>' for t, u in p["links"]) + "</p>"
        others = [x for x in POSTS if x["slug"] != p["slug"]][:3]
        body += '<h2>More laundry guides</h2><div class="cards">' + "".join(f'<a class="card" href="/blog/{o["slug"]}"><strong>{esc(o["h1"])}</strong></a>' for o in others) + "</div>"
        art = {"@context": "https://schema.org", "@type": "Article", "headline": p["h1"], "description": p["desc"], "datePublished": DATE_ISO,
               "dateModified": DATE_ISO, "inLanguage": "en", "mainEntityOfPage": B.DOMAIN + path, "image": B.DOMAIN + "/og-image.jpg",
               "author": {"@type": "Organization", "name": "Dima Laundry", "@id": B.DOMAIN + "/#org"}, "publisher": {"@id": B.DOMAIN + "/#org"}}
        page = (f'<section class="page-hero"><div class="bubbles" data-count="6" aria-hidden="true"></div><div class="wrap">{ch}<h1>{esc(p["h1"])}</h1></div></section>'
                f'<section class="content"><div class="wrap prose">{body}</div></section>' + B.cta_band("Let Dima handle it. Book a pickup across Dubai."))
        B.write(path, B.shell(path, p["title"] + " | Dima Laundry", p["desc"], page, [B.ORG, cs, art, B.faq_schema(p["faqs"])]))

    path = "/blog"
    ch, cs = B.crumbs(path, "Laundry guides")
    cards = "".join(f'<a class="card post-card" href="/blog/{p["slug"]}"><strong>{esc(p["h1"])}</strong><span>{esc(p["desc"])}</span></a>' for p in POSTS)
    page = (f'<section class="page-hero"><div class="bubbles" data-count="6" aria-hidden="true"></div><div class="wrap">{ch}<h1>Laundry and Garment Care Guides</h1>'
            f'<div class="answer tag-card"><span class="tag-hole" aria-hidden="true"></span><p>Practical guides from Dima Laundry, cleaning clothes in Dubai since 2001: prices, care labels, abayas and kanduras, wedding dresses, carpets, sneakers, and laundry for holiday homes and hotels.</p></div></div></section>'
            f'<section class="content"><div class="wrap prose wide"><div class="cards cards-2 blog-list">{cards}</div></div></section>')
    blog_s = {"@context": "https://schema.org", "@type": "Blog", "name": "Dima Laundry guides", "url": B.DOMAIN + path, "publisher": {"@id": B.DOMAIN + "/#org"},
              "blogPost": [{"@type": "BlogPosting", "headline": p["h1"], "url": B.DOMAIN + "/blog/" + p["slug"], "datePublished": DATE_ISO} for p in POSTS]}
    B.write(path, B.shell(path, "Laundry and Garment Care Guides | Dima Laundry Dubai",
                          "Dubai laundry guides from Dima Laundry: prices, care labels, abaya and kandura care, wedding dresses, carpets, sneakers, holiday home and hotel laundry.",
                          page, [B.ORG, cs, blog_s]))
