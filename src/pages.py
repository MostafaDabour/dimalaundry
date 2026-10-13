"""Page templates. build_all(B) receives the build module (helpers, data)."""
import os
import shutil

import content as C


def build_all(B):
    esc = B.esc
    P = B.P
    svc_by_slug = {s["slug"]: s for s in C.SERVICES}
    CARD = {"dry-cleaning": "Suits, dresses and delicate fabrics, from AED 14.", "wash-and-fold": "Everyday clothes and home linen, priced per item.",
            "ironing": "Pressing only, from AED 9.80 a shirt.", "abaya-kandura-cleaning": "Gentle care and a sharp press, from AED 20.",
            "wedding-dress-cleaning": "Evening dresses from AED 100, gowns priced on inspection.", "express-laundry": "For the days it cannot wait.",
            "shoe-cleaning": "Hand cleaned sneakers, leather and boots, from AED 100.", "bag-cleaning": "Handbags, leather bags and luggage, from AED 80.",
            "alterations": "Hems, repairs and fittings, from AED 40.", "carpet-cleaning": "Carpets and rugs from AED 30 per sq m.",
            "sofa-cleaning": "On-site sofa shampooing, AED 70 per seat.", "curtain-cleaning": "Curtains from AED 12 per sq m, at home or at our centre."}
    br_by_slug = {b["slug"]: b for b in C.BRANCHES}

    # ---- clean old generated pages (keep src, assets) ----
    for d in ["services", "branches", "business", "about-us", "faq", "contact", "prices", "thanks",
              "best-laundry-services-dubai"]:
        p = os.path.join(B.ROOT, d)
        if os.path.isdir(p):
            shutil.rmtree(p)

    def price_rows(group, section, names):
        src = P[group][section]
        return [B.find_item(n, src) for n in names]

    def service_prices(s):
        out = ""
        if s.get("prices"):
            if s.get("press_only"):
                rows = []
                for g, sec, names in s["prices"]:
                    for r in price_rows(g, sec, names):
                        rows.append([r[0], r[2], r[4]])
                out += B.simple_table(rows, ["Item", "Standard pressing", "Premium pressing"])
            else:
                rows = []
                for g, sec, names in s["prices"]:
                    rows += price_rows(g, sec, names)
                out += B.garment_table(rows)
        for key, prefix in s.get("flat", []):
            rows = [[(prefix or "") + B.nm(r[0]).lower() if prefix else r[0], r[1], r[2]] for r in P[key]]
            out += B.simple_table(rows, ["Item", "Standard", "Premium"])
        if s.get("flat_alt"):
            out += B.simple_table(P["alterations"], ["Service", "Price"])
        if s.get("fabric_rows"):
            rows = [B.find_item(n, P["home_fabrics"]) for n in s["fabric_rows"]]
            out += B.simple_table(rows, ["Item", "Cleaned at our centre", "Cleaned on site at your home"])
        if s.get("onsite_rows"):
            rows = [B.find_item(n, P["onsite"]) for n in s["onsite_rows"]]
            out += B.simple_table(rows, ["Item", "Price"])
        if out:
            out += '<p class="small">Prices in AED, updated 12 October 2026, the same at every branch. Premium service gives each piece extra care and finishing. For specialist garments, heavy stains or restoration work, our team confirms the price before cleaning. <a href="/prices">Full price list</a>.</p>'
        return out

    # ================= SERVICE PAGES =================
    for s in C.SERVICES:
        path = "/services/" + s["slug"]
        hero, cs = B.page_hero(path, s["short"], s["h1"], s["sub"],
                               wa_text=f"Hi Dima Laundry, I would like to book {s['short'].lower()}.")
        body = f'<h2>{esc(s["why_h"])}</h2>' + B.bullets(s["why"])
        pr = service_prices(s)
        if pr:
            body += f'<h2>{esc(s["prices_h"])}</h2>{pr}'
        body += f'<h2>{esc(s["what_h"])}</h2>' + B.bullets(s["what"])
        body += f'<h2>Standard and express turnaround</h2><p>{esc(s["turn"])}</p>'
        body += '<h2>How your order is handled</h2>' + B.how_steps()
        body += B.reviews_block(s["reviews"])
        body += B.faq_html(s["faqs"])
        related = [x for x in C.SERVICES if x["slug"] != s["slug"]][:0]
        rel = [svc_by_slug[k] for k in {"dry-cleaning": ["ironing", "express-laundry"], "wash-and-fold": ["ironing", "dry-cleaning"],
               "ironing": ["wash-and-fold", "dry-cleaning"], "abaya-kandura-cleaning": ["dry-cleaning", "ironing"],
               "wedding-dress-cleaning": ["dry-cleaning", "alterations"], "express-laundry": ["dry-cleaning", "ironing"],
               "shoe-cleaning": ["bag-cleaning", "dry-cleaning"], "bag-cleaning": ["shoe-cleaning", "dry-cleaning"],
               "alterations": ["dry-cleaning", "curtain-cleaning"], "carpet-cleaning": ["curtain-cleaning", "sofa-cleaning"],
               "sofa-cleaning": ["carpet-cleaning", "curtain-cleaning"], "curtain-cleaning": ["carpet-cleaning", "sofa-cleaning"]}[s["slug"]]]
        body += '<p class="nearby">Related: ' + ", ".join(f'<a href="/services/{r["slug"]}">{esc(r["short"])}</a>' for r in rel) + ', <a href="/prices">all prices</a>, <a href="/branches">locations</a>.</p>'
        body += B.updated()
        schema = {"@context": "https://schema.org", "@type": "Service", "serviceType": s["short"], "name": s["h1"],
                  "provider": {"@id": B.DOMAIN + "/#org"}, "areaServed": {"@type": "City", "name": "Dubai"},
                  "url": B.DOMAIN + path, "description": s["sub"]}
        page = hero + f'<section class="content"><div class="wrap prose">{body}</div></section>' + B.cta_band(f'Book {s["short"].lower()} with pickup, or drop off at any of {C.BRANCH_COUNT} branches.')
        B.write(path, B.shell(path, s["title"], s["desc"], page, [B.ORG, cs, schema, B.faq_schema(s["faqs"])]))

    # ================= SERVICES HUB =================
    path = "/services"
    hero, cs = B.page_hero(path, "Services", "Laundry and Dry Cleaning Services in Dubai",
                           f"Dima Laundry offers {len(C.SERVICES)} cleaning services in Dubai, from everyday laundry and pressing to dry cleaning, abayas and kanduras, evening dresses, shoes, bags, carpets, sofas and curtains. Every item is cleaned in Dima's own Al Quoz centres.")
    def card(s):
        return f'<a class="card" href="/services/{s["slug"]}"><strong>{esc(s["short"])}</strong><span>{CARD[s["slug"]]}</span></a>'
    groups = [("Clothing care", ["dry-cleaning", "wash-and-fold", "ironing", "abaya-kandura-cleaning", "express-laundry", "wedding-dress-cleaning", "alterations"]),
              ("Shoes and bags", ["shoe-cleaning", "bag-cleaning"]),
              ("Home and household", ["carpet-cleaning", "sofa-cleaning", "curtain-cleaning"])]
    body = ""
    for g, slugs in groups:
        gid = "home" if g.startswith("Home") else g.split()[0].lower()
        body += f'<h2 id="{gid}">{g}</h2><div class="cards">' + "".join(card(svc_by_slug[x]) for x in slugs) + "</div>"
    qas = [("What services does Dima Laundry offer?", "Dima Laundry offers dry cleaning, everyday laundry, ironing and pressing, abaya and kandura care, evening and wedding dress cleaning, express service, alterations, shoe and bag cleaning, carpet and curtain cleaning, and on-site sofa and mattress cleaning."),
           ("Are all services available with pickup?", "Yes. Every Dima Laundry service can be booked for pickup and delivery across Dubai, or dropped off at any of the 8 branches.")]
    body += B.faq_html(qas) + B.updated()
    B.write(path, B.shell(path, "Laundry and Dry Cleaning Services in Dubai | Dima Laundry",
                          "Dry cleaning, everyday laundry, pressing, abayas, kanduras, dresses, shoes, bags, carpets, sofas and curtains. Cleaned in Dima's own Al Quoz centres since 2001.",
                          hero + f'<section class="content"><div class="wrap prose">{body}</div></section>' + B.cta_band("Not sure which service you need? Message us on WhatsApp."),
                          [B.ORG, cs, B.faq_schema(qas)]))

    # ================= PRICES =================
    path = "/prices"
    hero, cs = B.page_hero(path, "Prices", "Simple, Transparent Laundry Pricing",
                           "Dima Laundry prices start at AED 14 to clean and press a shirt, AED 48 for a two piece suit and AED 20 for an abaya or kandura, with pressing only from AED 9.80. Prices are the same at every branch and were updated on 12 October 2026. For specialist garments, heavy stains, delicate items or restoration work, our team confirms the price before cleaning.")
    pop = [("Shirt", "From AED 14", "cleaned and pressed"), ("Two piece suit", "From AED 48", "cleaned and pressed"),
           ("Abaya", "From AED 20", "cleaned and pressed"), ("Kandura", "From AED 20", "cleaned and pressed"),
           ("Bed sheet", "AED 20", "cleaned and pressed"), ("Shirt pressing", "From AED 9.80", "pressing only")]
    popular = '<div class="price-cards">' + "".join(f'<div class="pcard"><span>{a}</span><strong>{b}</strong><small>{c}</small></div>' for a, b, c in pop) + "</div>"
    body = '<h2>Popular prices</h2>' + popular
    body += '<p class="small">Standard and premium prices are shown for every item. Cleaned and pressed means washed or dry cleaned, then pressed. Pressing only is for clothes that are already clean. All prices in AED.</p>'
    toc = [("men", "Men's clothing"), ("women", "Women's clothing"), ("baby", "Baby and children's clothing"),
           ("common", "Accessories, underwear and home linen"), ("specialist", "Shoes and bags"), ("home", "Curtains, carpets, sofas and mattresses"), ("alt", "Alterations")]
    body += '<nav class="toc" aria-label="Price list sections"><strong>Jump to:</strong> ' + " ".join(f'<a href="#{k}">{v}</a>' for k, v in toc) + "</nav>"
    def ptable(rows):
        return B.simple_table([[r[0], r[1], r[2], r[3], r[4]] for r in rows], ["Item", "Standard, cleaned and pressed", "Standard, pressing only", "Premium, cleaned and pressed", "Premium, pressing only"])
    for key, label in toc[:4]:
        body += f'<h2 id="{key}">{label}</h2>'
        for sec, rows in P[key].items():
            body += f'<h3>{esc(sec)}</h3>' + ptable(rows)
    body += '<h2 id="specialist">Shoes and bags</h2><h3>Bags</h3>' + B.simple_table(P["bags"], ["Item", "Standard", "Premium"])
    body += '<h3>Shoes</h3>' + B.simple_table(P["shoes"], ["Item", "Standard", "Premium"])
    body += "<h3>Children's shoes</h3>" + B.simple_table(P["baby_shoes"], ["Item", "Standard", "Premium"])
    body += '<h2 id="home">Curtains, carpets, sofas and mattresses</h2>' + B.simple_table(P["home_fabrics"], ["Item", "Cleaned at our centre", "Cleaned on site"])
    body += '<h3>On-site cleaning and other items</h3>' + B.simple_table(P["onsite"], ["Item", "Price"])
    body += '<h2 id="alt">Alterations</h2>' + B.simple_table(P["alterations"], ["Service", "Price"])
    qas = [("How much does it cost to dry clean a suit in Dubai?", "At Dima Laundry, cleaning and pressing a two piece suit costs AED 48, or AED 80 with premium service for men's suits."),
           ("How much is ironing in Dubai?", "Pressing only at Dima Laundry starts at AED 9.80 for a shirt and AED 10.50 for trousers."),
           ("What is the difference between standard and premium service?", "Premium service gives each piece extra care and finishing. Ask the team what is included for your items."),
           ("Are prices the same at every branch?", "Yes. Dima Laundry uses one price list across all Dubai branches."),
           ("How can I pay?", "Pay at the counter, on delivery or in the Dima Laundry app. Commercial accounts are invoiced monthly.")]
    body += B.reviews_block(["sufouh_chetan"]) + B.faq_html(qas) + B.updated()
    B.write(path, B.shell(path, "Laundry Prices in Dubai 2026 | Dima Laundry Price List",
                          "Full Dima Laundry price list: shirts from AED 14, suits from AED 48, abayas and kanduras from AED 20, pressing from AED 9.80. Updated 12 October 2026.",
                          hero + f'<section class="content"><div class="wrap prose wide">{body}</div></section>' + B.cta_band("Know what you need? Book a pickup in a minute."),
                          [B.ORG, cs, B.faq_schema(qas)]))

    # ================= BRANCH PAGES =================
    for b in C.BRANCHES:
        path = "/branches/" + b["slug"]
        hero, cs = B.page_hero(path, b["name"], b["h1"], b["intro"], book_label=f'Book a Pickup in {b["area"]}',
                               wa_text=f"Hi Dima Laundry, I would like to book a pickup in {b['area']}.")
        maps = "https://www.google.com/maps/search/?api=1&query=" + B.quote_plus("Dima Laundry " + b["address"])
        visit = (f'<h2>Visit Dima {esc(b["name"])}</h2><div class="tbl"><table><tbody>'
                 f'<tr><td>Address</td><td>{esc(b["address"])}</td></tr>'
                 f'<tr><td>Hours</td><td>{C.RETAIL_HOURS}</td></tr>'
                 f'<tr><td>Phone</td><td><a href="tel:{C.TEL}">{C.TOLL}</a> or <a href="tel:+971506398093">{C.RETAIL}</a></td></tr>'
                 f'<tr><td>WhatsApp</td><td><a href="{B.wa_link()}">{C.RETAIL}</a></td></tr>'
                 f'<tr><td>Directions</td><td><a href="{maps}" rel="noopener" target="_blank">Open in Google Maps</a></td></tr>'
                 f'</tbody></table></div>')
        mapblock = f'<div class="map"><iframe title="Map: Dima Laundry {esc(b["name"])}" loading="lazy" src="https://www.google.com/maps?q={B.quote_plus("Dima Laundry " + b["address"])}&amp;output=embed"></iframe></div>'
        body = visit + mapblock
        body += f'<h2>Pickup and delivery around {esc(b["area"])}</h2><p>Dima Laundry collects from homes and offices in:</p>' + B.bullets(b["areas"])
        body += '<h2>Popular services here</h2><div class="cards">' + "".join(
            f'<a class="card" href="/services/{C.POPULAR[k][0]}"><strong>{C.POPULAR[k][1]}</strong><span>{CARD[C.POPULAR[k][0]]}</span></a>' for k in b["popular"]) + "</div>"
        body += f'<h2>{esc(b["why_h"])}</h2><p>{esc(b["why"])}</p>'
        body += B.reviews_block(b["reviews"], rating=bool(b.get("rating")))
        body += B.faq_html(b["faqs"])
        body += '<p class="nearby">Other branches nearby: ' + ", ".join(f'<a href="/branches/{n}">{esc(br_by_slug[n]["name"])}</a>' for n in b["nearby"]) + ', or <a href="/branches">see all locations</a>.</p>' + B.updated()
        sch = {"@context": "https://schema.org", "@type": "DryCleaningOrLaundry", "@id": B.DOMAIN + path + "#branch",
               "name": "Dima Laundry " + b["name"], "parentOrganization": {"@id": B.DOMAIN + "/#org"}, "url": B.DOMAIN + path,
               "telephone": "+971-800-3462", "priceRange": "AED 6 to AED 300", "image": B.DOMAIN + "/og-image.jpg",
               "address": {"@type": "PostalAddress", "streetAddress": b["address"], "addressLocality": "Dubai", "addressCountry": "AE"},
               "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:00", "closes": "22:00"}],
               "areaServed": b["areas"], "hasMap": maps, "description": b["intro"]}
        if b.get("rating"):
            sch["aggregateRating"] = {"@type": "AggregateRating", "ratingValue": b["rating"][0], "reviewCount": b["rating"][1]}
        page = hero + f'<section class="content"><div class="wrap prose">{body}</div></section>' + B.cta_band(f'Book a pickup in {b["area"]} today, or drop by 10am to 10pm.', book_label=f'Book a Pickup in {b["area"]}')
        B.write(path, B.shell(path, b["title"], b["desc"], page, [B.ORG, cs, sch, B.faq_schema(b["faqs"])]))

    # ================= PROCESSING CENTRES =================
    path = "/branches/al-quoz-head-office"
    hero, cs = B.page_hero(path, "Processing centres", "Dima Laundry Processing Centres, Al Quoz",
                           f"Dima Laundry cleans every item in its own processing centres in Al Quoz, which run 24 hours. The head office is at {C.HQ_ADDRESS}, with further centres in Al Quoz Industrial Area 4 and Al Quoz 3, and a new centre in Dubai Investments Park 2 opening soon.")
    rows = "".join(f"<tr><td>{esc(n)}</td><td>{esc(a)}</td><td>{esc(r)}</td></tr>" for n, a, r in C.PROCESSING)
    body = f'<h2>Our centres</h2><div class="tbl"><table><thead><tr><th>Centre</th><th>Address</th><th>Notes</th></tr></thead><tbody>{rows}</tbody></table></div>'
    body += '<h2>What happens inside</h2>' + B.bullets(["Every item tagged on arrival", "Sorted by fabric and service", "Cleaned, pressed and quality checked", "Packed for delivery or branch collection"])
    body += '<h2>Commercial customers</h2><p>Hotels and operators can arrange a visit to see the operation before signing. Call the commercial team on <a href="tel:+971569984493">' + C.BIZ + '</a> or <a href="/business#quote">request a quote</a>.</p>'
    qas = [("Where does Dima Laundry clean its clothes?", "In its own processing centres in Al Quoz Industrial Areas 3 and 4, Dubai, which run 24 hours."),
           ("Where is the Dima Laundry head office?", f"At {C.HQ_ADDRESS}, Dubai.")]
    body += B.reviews_block(["q4_great", "q3_satin", "f3_b2b"], rating=True) + B.faq_html(qas) + B.updated()
    sch = {"@context": "https://schema.org", "@type": "DryCleaningOrLaundry", "name": "Dima Laundry Head Office, Al Quoz 3",
           "parentOrganization": {"@id": B.DOMAIN + "/#org"}, "url": B.DOMAIN + path, "telephone": "+971-800-3462",
           "address": {"@type": "PostalAddress", "streetAddress": C.HQ_ADDRESS, "addressLocality": "Dubai", "addressCountry": "AE"},
           "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "00:00", "closes": "23:59"}]}
    B.write(path, B.shell(path, "Dima Laundry Processing Centres and Head Office | Al Quoz Dubai",
                          "Dima Laundry's own processing centres in Al Quoz Industrial Areas 3 and 4 run 24 hours. Head office at 22, 24a Street, Al Quoz 3.",
                          hero + f'<section class="content"><div class="wrap prose">{body}</div></section>' + B.cta_band("Every item is cleaned in our own centres. Book a pickup."),
                          [B.ORG, cs, sch, B.faq_schema(qas)]))

    # ================= LOCATIONS HUB =================
    path = "/branches"
    hero, cs = B.page_hero(path, "Locations", "Find Your Nearest Dima",
                           f"Dima Laundry has {C.BRANCH_COUNT} retail branches across Dubai, open {C.RETAIL_HOURS}: two in Dubai Marina, plus Al Sufouh, Jumeirah, Downtown Dubai, Sheikh Zayed Road, Karama and Damac Aykon City. Many sit inside supermarkets, so you can drop off while you shop, and every branch arranges pickup and delivery nearby.")
    cards = ""
    for b in C.BRANCHES:
        maps = "https://www.google.com/maps/search/?api=1&query=" + B.quote_plus("Dima Laundry " + b["address"])
        cards += (f'<article class="loc"><h3>{esc(b["name"])}</h3><p class="loc-place">{esc(b["place"])}</p>'
                  f'<p>Serving {esc(", ".join(b["areas"][:4]))} and nearby areas.</p><p class="small">{C.RETAIL_HOURS}</p>'
                  f'<div class="loc-links"><a href="{maps}" rel="noopener" target="_blank">Directions</a><a href="/branches/{b["slug"]}">Branch details</a><a href="/contact#book">Book pickup</a></div></article>')
    body = '<div class="map map-big"><iframe title="Map of Dima Laundry branches in Dubai" loading="lazy" src="https://www.google.com/maps?q=Dima+Laundry+Dubai&amp;output=embed"></iframe></div>'
    body += f'<h2>Our {C.BRANCH_COUNT} branches</h2><div class="locs">{cards}</div>'
    body += '<h2>Processing centres</h2><p>Everything is cleaned in our own centres in Al Quoz, open 24 hours, with a new centre in Dubai Investments Park 2 opening soon. <a href="/branches/al-quoz-head-office">See our processing centres</a>.</p>'
    rows = "".join(f'<tr><td><a href="/branches/{b["slug"]}">{esc(b["name"])}</a></td><td>{esc(b["address"])}</td><td>{C.RETAIL_HOURS}</td></tr>' for b in C.BRANCHES)
    body += f'<h2>All addresses</h2><div class="tbl"><table><thead><tr><th>Branch</th><th>Address</th><th>Hours</th></tr></thead><tbody>{rows}</tbody></table></div>'
    qas = [("Where is the nearest Dima Laundry?", f"Dima Laundry has {C.BRANCH_COUNT} branches in Dubai: Dubai Marina (Marinascape and Crown), Al Sufouh, Jumeirah, Downtown Dubai, Sheikh Zayed Road, Karama and Damac Aykon City."),
           ("What are Dima Laundry's opening hours?", f"Dima Laundry branches are open {C.RETAIL_HOURS}. The Al Quoz processing centres run 24 hours."),
           ("Do all branches offer pickup and delivery?", "Yes. Every branch arranges pickup and delivery in its surrounding areas.")]
    body += B.faq_html(qas) + B.updated()
    B.write(path, B.shell(path, "Dima Laundry Locations in Dubai | 8 Branches Open 10am to 10pm",
                          "8 Dima Laundry branches in Dubai: Dubai Marina, Al Sufouh, Jumeirah, Downtown, Sheikh Zayed Road, Karama and Damac Aykon City. Open 10am to 10pm daily.",
                          hero + f'<section class="content"><div class="wrap prose wide">{body}</div></section>' + B.cta_band("Too busy to drop off? We collect from your door."),
                          [B.ORG, cs, B.faq_schema(qas)]))

    # ================= BUSINESS PAGES =================
    for x in C.BUSINESS:
        path = "/business/" + x["slug"]
        hero, cs = B.page_hero(path, x["short"], f'{x["h1"]}<span class="kicker">{esc(x["kicker"])}</span>', x["sub"],
                               book_label="Request a Commercial Quote", wa_text="Hi Dima Laundry, I would like a commercial laundry quote.")
        hero = hero.replace('href="/contact#book">Request a Commercial Quote', 'href="#quote">Request a Commercial Quote').replace(B.wa_link("Hi Dima Laundry, I would like a commercial laundry quote."), B.wa_link("Hi Dima Laundry, I would like a commercial laundry quote.", C.BIZ_WA))
        body = '<h2>What we handle</h2>' + B.bullets(x["items"])
        body += '<h2>What you can count on</h2>' + B.bullets(x["outcomes"])
        body += '<h2>How it works</h2>' + B.how_steps(C_BIZ_STEPS)
        body += f'<h2>Commercial capability</h2><p>Dima Laundry has served Dubai since 2001 and processes every order in its own Al Quoz centres, which run 24 hours, with a new centre in Dubai Investments Park 2 opening soon. Commercial enquiries go straight to the commercial team on <a href="tel:+971569984493">{C.BIZ}</a>.</p>'
        body += B.reviews_block(["f3_b2b"]) + B.faq_html(x["faqs"]) + B.quote_form() + B.updated()
        sch = {"@context": "https://schema.org", "@type": "Service", "serviceType": "Commercial laundry: " + x["short"], "name": x["h1"],
               "provider": {"@id": B.DOMAIN + "/#org"}, "areaServed": {"@type": "City", "name": "Dubai"}, "url": B.DOMAIN + path, "description": x["sub"]}
        B.write(path, B.shell(path, x["title"], x["desc"], hero + f'<section class="content"><div class="wrap prose">{body}</div></section>', [B.ORG, cs, sch, B.faq_schema(x["faqs"])]))

    path = "/business"
    hero, cs = B.page_hero(path, "Commercial Laundry", "Reliable Commercial Laundry for Dubai Businesses",
                           "Your linen, towels and uniforms collected on schedule, professionally cleaned in Dima Laundry's own Al Quoz centres and returned when you need them. Dima Laundry has served Dubai businesses since 2001.",
                           book_label="Request a Commercial Quote")
    hero = hero.replace('href="/contact#book">Request a Commercial Quote', 'href="#quote">Request a Commercial Quote').replace(B.wa_link("Hi Dima Laundry, I would like to book a pickup."), B.wa_link("Hi Dima Laundry, I would like a commercial laundry quote.", C.BIZ_WA))
    body = '<h2>Industries we serve</h2><div class="cards">' + "".join(f'<a class="card" href="/business/{s}"><strong>{n}</strong></a>' for n, s in C.INDUSTRY_CARDS) + "</div>"
    body += '<h2>Why businesses choose Dima</h2>' + B.bullets(["Scheduled collections you can plan around", "Reliable turnaround", "Commercial capacity in our own centres, running 24 hours", "A commercial team you can reach directly", "Item counts for every collection", "Monthly invoicing", "No third party cleaners"])
    body += '<h2>How it works</h2>' + B.how_steps(C_BIZ_STEPS)
    body += f'<h2>Commercial capability</h2><p>Dima Laundry runs {C.BRANCH_COUNT} retail branches and 3 processing centres in Al Quoz, with a fourth centre in Dubai Investments Park 2 opening soon. Every commercial order is cleaned in-house. <a href="/branches/al-quoz-head-office">See our processing centres</a>.</p>'
    qas = [("Does Dima Laundry handle commercial laundry?", "Yes. Dima Laundry serves hotels, holiday homes, restaurants, salons, spas, gyms, clinics and companies across Dubai."),
           ("How is commercial laundry priced?", "Dima Laundry prices commercial laundry per kg or per piece, based on volume, with monthly invoicing."),
           ("Who do I contact for a commercial quote?", f"Call or WhatsApp the commercial team on {C.BIZ}, or use the quote form on this page.")]
    body += B.reviews_block(["f3_b2b"]) + B.faq_html(qas) + B.quote_form() + B.updated()
    B.write(path, B.shell(path, "Commercial Laundry in Dubai | Hotels, Holiday Homes, Uniforms | Dima Laundry",
                          "Reliable commercial laundry for Dubai hotels, holiday homes, restaurants, salons, gyms, clinics and uniforms. Scheduled collections and monthly invoicing.",
                          hero + f'<section class="content"><div class="wrap prose">{body}</div></section>', [B.ORG, cs, B.faq_schema(qas)]))

    # ================= ABOUT =================
    path = "/about-us"
    hero, cs = B.page_hero(path, "About", "Serving Dubai Since 2001",
                           f"Dima Laundry LLC is a Dubai laundry and dry cleaning company founded in 2001. Today it runs {C.BRANCH_COUNT} retail branches and 3 processing centres in Al Quoz, cleans every item in-house, and serves households, hotels, holiday homes and businesses across the city.")
    body = '<h2>Our story</h2><p>Dima Laundry opened in Dubai in 2001 with a simple goal: clean clothes properly and return them on time. Over 25 years it grew into a network of branches inside the supermarkets and towers where Dubai residents already shop and live, from Dubai Marina to Karama.</p><p>Dima has always run its own cleaning operation. Every shirt, abaya, suit and bed sheet is cleaned by the Dima team in Al Quoz, never sent to a third party.</p>'
    body += '<h2>Then and now</h2><ol class="timeline"><li><strong>2001</strong> Dima Laundry begins serving Dubai.</li>' \
            f'<li><strong>Today</strong> {C.BRANCH_COUNT} retail branches open {C.RETAIL_HOURS}, 3 processing centres running 24 hours, pickup and delivery, the Dima app on iPhone and Android, and laundry for homes and businesses.</li>' \
            '<li><strong>Next</strong> A new processing centre in Dubai Investments Park 2, opening soon.</li></ol>'
    body += '<h2>What makes Dima different</h2>' + B.bullets(["Our own processing centres, no third party cleaners", "Experienced team, many with years at Dima", "Every item tagged and tracked", "Pickup and delivery across Dubai", "One price list across every branch", "Residential and commercial capacity"])
    rows = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in [("Founded", "2001"), ("Retail branches", f"{C.BRANCH_COUNT}, open {C.RETAIL_HOURS}"), ("Processing centres", "3 in Al Quoz, open 24 hours, DIP-2 opening soon"), ("Head office", C.HQ_ADDRESS + ", Dubai"), ("Phone", C.TOLL), ("Email", C.EMAIL)])
    body += f'<h2>Dima Laundry at a glance</h2><div class="tbl"><table><tbody>{rows}</tbody></table></div>'
    qas = [("When was Dima Laundry founded?", "Dima Laundry was founded in Dubai in 2001."),
           ("Does Dima Laundry clean clothes in-house?", "Yes. Every item is cleaned in Dima Laundry's own processing centres in Al Quoz."),
           ("How many branches does Dima Laundry have?", f"Dima Laundry has {C.BRANCH_COUNT} retail branches in Dubai and 3 processing centres in Al Quoz.")]
    body += B.reviews_block(["sufouh_2yrs", "q4_great", "q3_satin"], rating=True) + B.faq_html(qas) + B.updated()
    B.write(path, B.shell(path, "About Dima Laundry | Serving Dubai Since 2001",
                          f"Dima Laundry LLC has cleaned clothes for Dubai homes and businesses since 2001, with {C.BRANCH_COUNT} branches and its own processing centres in Al Quoz.",
                          hero + f'<section class="content"><div class="wrap prose">{body}</div></section>' + B.cta_band("25 years of Dubai laundry. Book your pickup."),
                          [B.ORG, cs, B.faq_schema(qas)]))

    # ================= CONTACT =================
    path = "/contact"
    hero, cs = B.page_hero(path, "Contact", "Book a Laundry Pickup in Dubai",
                           f"Book Dima Laundry by calling {C.TOLL}, messaging {C.RETAIL} on WhatsApp, using the Dima app or the form below. Commercial enquiries go to {C.BIZ}. The head office is at {C.HQ_ADDRESS}, Dubai.")
    rows = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in [
        ("Toll free", f'<a href="tel:{C.TEL}">{C.TOLL}</a>'), ("WhatsApp", f'<a href="{B.wa_link()}">{C.RETAIL}</a>'),
        ("Retail line", f'<a href="tel:+971506398093">{C.RETAIL}</a>'), ("Commercial enquiries", f'<a href="tel:+971569984493">{C.BIZ}</a>'),
        ("Email", f'<a href="mailto:{C.EMAIL}">{C.EMAIL}</a>'), ("Head office", C.HQ_ADDRESS + ", Dubai"),
        ("Branch hours", C.RETAIL_HOURS), ("Processing centres", "Open 24 hours")])
    body = booking_wrap = B.booking_form()
    body += f'<div class="app-inline"><h2>Or book in the app</h2><p>Book pickups, track orders and pay in the Dima Laundry app.</p>{B.app_badges()}</div>'
    body += f'<h2>Contact details</h2><div class="tbl"><table><tbody>{rows}</tbody></table></div><p><a href="/branches">See all branch addresses</a>.</p>'
    B.write(path, B.shell(path, "Contact Dima Laundry Dubai | Book a Laundry Pickup",
                          f"Book a Dima Laundry pickup in Dubai. Call {C.TOLL}, WhatsApp {C.RETAIL} or use the form. Commercial enquiries {C.BIZ}.",
                          hero + f'<section class="content"><div class="wrap prose">{body}</div></section>', [B.ORG, cs]))

    # ================= FAQ =================
    path = "/faq"
    hero, cs = B.page_hero(path, "FAQ", "Dima Laundry: Frequently Asked Questions",
                           "Answers about booking, pickup, prices, opening hours, branches, garment care and commercial accounts at Dima Laundry, Dubai's laundry and dry cleaning company since 2001.")
    sections = [
        ("Booking and pickup", [
            ("How do I book a laundry pickup with Dima Laundry?", f"Call {C.TOLL}, message {C.RETAIL} on WhatsApp, book in the Dima Laundry app, or use the booking form at dimalaundry.com."),
            ("What areas does Dima Laundry cover?", "Dima Laundry picks up and delivers across Dubai, including Dubai Marina, JBR, JLT, Al Sufouh, Palm Jumeirah, Jumeirah, Downtown, Business Bay, Sheikh Zayed Road and Karama."),
            ("Does Dima Laundry have an app?", "Yes. The Dima Laundry app is free on the App Store and Google Play. You can book pickups, track orders and pay from your phone."),
        ]),
        ("Branches and hours", [
            ("How many branches does Dima Laundry have?", f"Dima Laundry has {C.BRANCH_COUNT} retail branches in Dubai and 3 processing centres in Al Quoz."),
            ("What are Dima Laundry's opening hours?", f"Branches are open {C.RETAIL_HOURS}. The processing centres run 24 hours."),
        ]),
        ("Prices and payment", [
            ("How much does Dima Laundry charge?", "Cleaning and pressing starts at AED 14 for a shirt, AED 48 for a two piece suit and AED 20 for an abaya or kandura. Pressing only starts at AED 9.80."),
            ("Are prices the same at every branch?", "Yes. Dima Laundry uses one price list across all branches."),
            ("What is premium service?", "Premium service gives each piece extra care and finishing, and is available on every item."),
        ]),
        ("Turnaround", [
            ("How long does Dima Laundry take?", "Standard and express turnaround are both available. Specialist items such as wedding dresses, bags, shoes and carpets take longer. The team confirms the ready time when you book."),
        ]),
        ("Care and quality", [
            ("Can Dima Laundry remove tough stains?", "Dima Laundry treats stains before cleaning. Most food, oil, makeup and sweat stains come out. Old or set stains may not fully remove, and staff will tell you at drop off."),
            ("Does Dima Laundry clean abayas and kanduras?", "Yes. Dima Laundry cleans and presses abayas, kanduras, ghutras, jalabiyas and sheilas, with separate prices for delicate and wool pieces."),
            ("Does Dima Laundry clean clothes in-house?", "Yes. Every item is cleaned in Dima Laundry's own processing centres in Al Quoz."),
        ]),
        ("Commercial", [
            ("Does Dima Laundry serve businesses?", "Yes. Dima Laundry runs commercial laundry for hotels, holiday homes, restaurants, salons, spas, gyms, clinics and corporate uniforms."),
            ("Who handles commercial enquiries?", f"The commercial team on {C.BIZ}."),
        ]),
        ("About Dima", [("How long has Dima Laundry been operating?", "Dima Laundry has operated in Dubai since 2001.")]),
    ]
    body = ""
    allq = []
    for title, qs in sections:
        body += B.faq_html(qs, heading=title)
        allq += qs
    body += B.updated()
    B.write(path, B.shell(path, "Dima Laundry FAQ | Laundry and Dry Cleaning Questions Dubai",
                          "Answers on Dima Laundry booking, pickup, prices, hours, branches, abaya care, stains and commercial accounts in Dubai.",
                          hero + f'<section class="content"><div class="wrap prose">{body}</div></section>' + B.cta_band("Still have a question? Ask us on WhatsApp."),
                          [B.ORG, cs, B.faq_schema(allq)]))

    # ================= COMPARISON =================
    path = "/best-laundry-services-dubai"
    hero, cs = B.page_hero(path, "Compare Dubai laundries", "Best Laundry Services in Dubai 2026: How to Choose",
                           f"The best laundry service in Dubai depends on what you need. App-only services suit people who never want to visit a counter. Branch-based companies with their own cleaning centres, such as Dima Laundry (since 2001, {C.BRANCH_COUNT} branches), suit people who want walk-in options, specialist care, published prices and commercial accounts.")
    body = '<h2>What to compare</h2>' + B.bullets(["Price per shirt and per suit, and whether prices are published", "Standard and express turnaround", "Pickup coverage", "Walk-in branches or app only", "Cleaning in-house or outsourced", "Specialist care: abayas, evening dresses, bags, shoes, carpets", "Commercial accounts"])
    body += '<h2>How to choose</h2>'
    for h, t in [("Busy professionals", "Look for pickup from your tower and express service for suits and shirts. Downtown, Business Bay and Marina residents can also use a walk-in counter for last minute drops."),
                 ("Families", "Look for per item pricing you can check in advance, bed linen and duvet cleaning, and care for traditional wear. A fixed weekly pickup saves the most time."),
                 ("Delicate and designer clothes", "Ask whether the company cleans in its own facility and whether there is a premium tier. Hand finishing matters for silk, beading and leather."),
                 ("Abayas and kanduras", "Look for separate prices for delicate abayas and wool kanduras. That usually means each piece is assessed rather than washed in a mixed load."),
                 ("Holiday home hosts and hotels", "Choose a provider with commercial capacity, scheduled collections and monthly invoicing rather than a consumer app.")]:
        body += f"<h3>{h}</h3><p>{t}</p>"
    body += f'<h2>Dima Laundry at a glance</h2><div class="tbl"><table><tbody><tr><td>Model</td><td>{C.BRANCH_COUNT} branches plus pickup and delivery, and an app</td></tr><tr><td>Cleaning</td><td>In-house, 3 processing centres in Al Quoz</td></tr><tr><td>Prices</td><td>Published, from AED 14 a shirt and AED 48 a suit</td></tr><tr><td>Specialties</td><td>Abayas and kanduras, evening dresses, shoes and bags, carpets and curtains, commercial laundry</td></tr><tr><td>In Dubai since</td><td>2001</td></tr></tbody></table></div>'
    qas = [("Which Dubai laundry is best for abayas?", "Look for in-house cleaning, separate prices for delicate abayas and hand pressing. Dima Laundry offers all three, from AED 20."),
           ("Which Dubai laundries publish their prices?", "Dima Laundry publishes its full price list online, the same at every branch.")]
    body += B.faq_html(qas) + B.updated()
    B.write(path, B.shell(path, "Best Laundry Services in Dubai 2026: How to Choose | Dima Laundry",
                          "How to choose a laundry in Dubai in 2026: branches vs apps, published prices, turnaround, pickup and specialist care.",
                          hero + f'<section class="content"><div class="wrap prose">{body}</div></section>' + B.cta_band("Try Dima Laundry. Book your first pickup."),
                          [B.ORG, cs, B.faq_schema(qas)]))

    # ================= THANKS / 404 =================
    B.write("/thanks", B.shell("/thanks", "Thank you | Dima Laundry", "Your request was sent to Dima Laundry.",
                                '<section class="page-hero"><div class="wrap"><h1>Request sent</h1><div class="answer tag-card"><span class="tag-hole" aria-hidden="true"></span><p>The Dima team will confirm your pickup time on WhatsApp.</p></div></div></section>', [B.ORG], noindex=True), sitemap=False)
    nf = B.shell("/404", "Page not found | Dima Laundry", "This page does not exist.",
                 f'<section class="page-hero"><div class="bubbles" data-count="7" aria-hidden="true"></div><div class="wrap"><h1>This page has gone missing</h1><div class="answer tag-card"><span class="tag-hole" aria-hidden="true"></span><p>Like a sock in the wash. Try our services, prices or locations, or call {C.TOLL}.</p></div><div class="hero-actions"><a class="btn btn-main" href="/services">Services</a><a class="btn btn-line" href="/branches">Locations</a></div></div></section>', [B.ORG], noindex=True)
    open(os.path.join(B.ROOT, "404.html"), "w", encoding="utf-8").write(nf)

    # ================= HOME =================
    from home import build_home
    build_home(B)

    # ================= SITEMAP / LLMS / REDIRECTS =================
    order = ["/"] + [p for p in B.PAGES if p != "/"]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"  <url><loc>{B.DOMAIN}{p}</loc><lastmod>2026-10-14</lastmod></url>\n" for p in order) + "</urlset>\n"
    open(os.path.join(B.ROOT, "sitemap.xml"), "w").write(sm)
    llms = f"""# Dima Laundry

> Dima Laundry LLC is a Dubai laundry and dry cleaning company operating since 2001. It runs {C.BRANCH_COUNT} retail branches (open {C.RETAIL_HOURS}) and 3 processing centres in Al Quoz (open 24 hours), cleans every item in-house, and offers pickup and delivery across Dubai. Prices start at AED 14 for a shirt and AED 48 for a two piece suit. Phone {C.TOLL}. WhatsApp {C.RETAIL}. Commercial {C.BIZ}. Email {C.EMAIL}.

Mobile app: iOS {C.APP_IOS} | Android {C.APP_ANDROID}

## Key pages
- [Services]({B.DOMAIN}/services)
- [Prices]({B.DOMAIN}/prices)
- [Locations]({B.DOMAIN}/branches)
- [Commercial laundry]({B.DOMAIN}/business)
- [FAQ]({B.DOMAIN}/faq)
- [About]({B.DOMAIN}/about-us)
- [Contact]({B.DOMAIN}/contact)

## Services
""" + "".join(f"- [{s['short']}]({B.DOMAIN}/services/{s['slug']})\n" for s in C.SERVICES) + "\n## Branches\n" + "".join(
        f"- [{b['name']}]({B.DOMAIN}/branches/{b['slug']}): {b['address']}\n" for b in C.BRANCHES) + f"- [Processing centres]({B.DOMAIN}/branches/al-quoz-head-office)\n\n## Commercial\n" + "".join(
        f"- [{x['short']}]({B.DOMAIN}/business/{x['slug']})\n" for x in C.BUSINESS)
    open(os.path.join(B.ROOT, "llms.txt"), "w").write(llms)
    redirects = """/about-us/   /about-us   301
/dimasobha/   /branches   301
/dimasobha   /branches   301
/contact-us/   /contact   301
/contact-us   /contact   301
/branches/trade-centre   /branches/sheikh-zayed-road   301
/branches/jvc   /branches   301
/branches/umm-suqeim   /branches/jumeirah   301
/branches/garhoud   /branches   301
/branches/silicon-oasis   /branches   301
/branches/sobha-hartland   /branches   301
"""
    open(os.path.join(B.ROOT, "_redirects"), "w").write(redirects)
    print(len(B.PAGES), "pages")


C_BIZ_STEPS = [
    ("Tell us your requirements.", "Items, volumes and how often you need collections."),
    ("We set a schedule.", "A fixed pickup and return routine that fits your operation."),
    ("We collect.", "Items are counted at every collection."),
    ("We clean and check.", "Processed and quality checked in our own Al Quoz centres."),
    ("We return.", "Folded, packed and sorted the way you need them."),
    ("Ongoing service.", "One contact for changes and one monthly invoice."),
]
