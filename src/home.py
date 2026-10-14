import content as C


def build_home(B):
    esc = B.esc
    svc = {s["slug"]: s for s in C.SERVICES}
    trust = ["Since 2001", f"{C.BRANCH_COUNT} Locations", "In-House Cleaning", "Pickup and Delivery", "Express Available"]
    rail = "".join(f'<li><span class="hook" aria-hidden="true"></span><span class="rail-tag">{t}</span></li>' for t in trust)

    popular = [("dry-cleaning", "Dry Cleaning", "Suits, dresses and delicate fabrics, from AED 14."),
               ("wash-and-fold", "Everyday Laundry", "Washed, pressed and folded, priced per item."),
               ("ironing", "Ironing", "Pressing only, from AED 9.80 a shirt."),
               ("abaya-kandura-cleaning", "Abaya and Kandura", "Gentle care and a sharp press, from AED 20."),
               ("express-laundry", "Express Laundry", "For the days it cannot wait."),
               ("curtain-cleaning", "Home and Household", "Curtains, carpets, sofas and mattresses.")]
    cards = "".join(f'<a class="card svc-card" href="/services/{s}"><strong>{t}</strong><span>{d}</span></a>' for s, t, d in popular)

    why = [("Your clothes stay with us", "Dima Laundry cleans every garment in its own Al Quoz processing centres instead of relying on third party cleaners."),
           ("Serving Dubai since 2001", "Dima Laundry has cared for clothes for Dubai households and businesses for more than two decades."),
           ("We collect from your door", "Book a pickup online, on WhatsApp, by phone or in the Dima app."),
           ("Every item is tracked", "Garments are tagged and tracked from collection through cleaning and delivery."),
           (f"{C.BRANCH_COUNT} locations across Dubai", f"Visit a branch from Dubai Marina to Karama, open {C.RETAIL_HOURS}, or let us come to you.")]
    whys = "".join(f'<div class="why-card"><h3>{t}</h3><p>{d}</p></div>' for t, d in why)

    pop_prices = [("Shirt", "From AED 14"), ("Two piece suit", "From AED 48"), ("Abaya", "From AED 20"),
                  ("Kandura", "From AED 20"), ("Bed sheet", "AED 20"), ("Sofa shampoo", "AED 70 per seat")]
    pcards = "".join(f'<div class="pcard"><span>{a}</span><strong>{b}</strong></div>' for a, b in pop_prices)

    locs = "".join(f'<a class="card" href="/branches/{b["slug"]}"><strong>{esc(b["name"])}</strong><span>{esc(b["place"])}</span></a>' for b in C.BRANCHES)
    inds = "".join(f'<a class="chip" href="/business/{s}">{n}</a>' for n, s in C.INDUSTRY_CARDS)

    faqs = [("Does Dima Laundry offer pickup and delivery?", "Yes. Dima Laundry collects from homes and offices across Dubai. Book online, on WhatsApp, by phone or in the Dima app."),
            ("How much does Dima Laundry charge?", "Cleaning and pressing starts at AED 14 for a shirt, AED 48 for a two piece suit and AED 20 for an abaya or kandura. Pressing only starts at AED 9.80."),
            ("Where is Dima Laundry located?", f"Dima Laundry has {C.BRANCH_COUNT} branches in Dubai: Dubai Marina (Marinascape and Crown), Al Sufouh, Jumeirah, Downtown Dubai, Sheikh Zayed Road, Karama and Damac Aykon City, all open {C.RETAIL_HOURS}."),
            ("Does Dima Laundry clean clothes in-house?", "Yes. Every item is cleaned in Dima Laundry's own processing centres in Al Quoz, which run 24 hours."),
            ("Does Dima Laundry serve businesses?", "Yes. Dima Laundry provides commercial laundry for hotels, holiday homes, restaurants, salons, spas, gyms, clinics and corporate uniforms."),
            ("Does Dima Laundry have an app?", "Yes. The Dima Laundry app is free on iPhone and Android for booking pickups, tracking orders and paying.")]

    app = f'''<section class="app-sec"><div class="wrap app-grid">
  <div class="phone" aria-hidden="true"><div class="phone-screen"><img src="/logo.webp" alt="" width="120" height="37"><div class="ph-row"><b>Pickup booked</b><span>Today, 7pm</span></div><div class="ph-row"><b>Order No. 2001</b><span>Cleaning</span></div><div class="ph-bar"><i></i></div><div class="ph-row"><b>Delivery</b><span>Tomorrow, 6pm</span></div></div></div>
  <div><h2>Rebook in seconds with the Dima app</h2><p>Schedule pickups in a few taps, track every order from collection to delivery, and pay from your phone. Free on iPhone and Android.</p>{B.app_badges()}</div>
</div></section>'''

    body = f'''
<section class="hero">
  <div class="bubbles" data-count="14" aria-hidden="true"></div>
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <h1 class="eyebrow">Laundry and Dry Cleaning in Dubai</h1>
      <p class="hero-big">Picked Up. Professionally Cleaned. Delivered Back to Your Door.</p>
      <p class="lede">Dima Laundry has served Dubai since 2001, with in-house cleaning in its own Al Quoz centres, pickup and delivery, and {C.BRANCH_COUNT} branches across the city open {C.RETAIL_HOURS}.</p>
      {B.btns()}
    </div>
    <div class="hero-tag" aria-hidden="true">
      <div class="string"></div>
      <div class="big-tag">
        <span class="tag-hole"></span>
        <img class="tag-logo" src="/logo.webp" alt="" width="150" height="47">
        <div class="tag-no">No. 2001</div>
        <dl>
          <div><dt>Items</dt><dd>3 shirts, 1 abaya, 1 suit</dd></div>
          <div><dt>Service</dt><dd>Clean and press</dd></div>
          <div><dt>Picked up</dt><dd>Dubai Marina, 7pm</dd></div>
          <div><dt>Status</dt><dd>Quality checked</dd></div>
        </dl>
        <div class="tag-perf"></div>
        <div class="tag-stub">Keep this stub</div>
      </div>
    </div>
  </div>
  <div class="rail-wrap"><ul class="rail wrap" aria-label="Why Dima">{rail}</ul></div>
</section>

<section class="home-sec"><div class="wrap">
  <div class="sec-head"><h2>Popular services</h2><a href="/services">View all services</a></div>
  <div class="cards cards-3">{cards}</div>
</div></section>

<section class="home-sec tint"><div class="wrap">
  <h2>Why Dubai trusts Dima</h2>
  <div class="why-grid">{whys}</div>
</div></section>

<div class="how-wave">{B.WAVE}</div><section class="how"><div class="wrap">
  <h2>Laundry without the hassle</h2>
  {B.how_steps()}
  <p><a class="btn btn-tag" href="/contact#book">Book Your Pickup</a></p>
</div></section>

<section class="home-sec"><div class="wrap">
  <h2>Trusted by customers across Dubai</h2>
  <p class="rating-line">{C.RATING_LINE} <a href="{C.GMAPS["karama"]}" rel="noopener" target="_blank">Read all reviews on Google</a></p>
  <div class="rv-grid" data-live="all" data-lang="en">{"".join(B.review_card(k) for k in ["sufouh_2yrs", "karama_raju", "jumeirah_7yrs", "szr_6yrs", "q3_satin", "marina_zeeshan"])}</div>
</div></section>

<section class="home-sec tint"><div class="wrap">
  <div class="sec-head"><h2>Popular laundry prices</h2><a href="/prices">View full price list</a></div>
  <div class="price-cards">{pcards}</div>
  <p class="small">Standard service, cleaned and pressed. The same prices at every branch, updated 12 October 2026.</p>
</div></section>

<section class="home-sec"><div class="wrap">
  <div class="sec-head"><h2>Find Dima near you</h2><a href="/branches">View all locations</a></div>
  <div class="loc-split">
    <div class="map"><iframe title="Map of Dima Laundry branches in Dubai" data-map="https://www.google.com/maps?q=Dima+Laundry+Dubai&amp;output=embed"></iframe></div>
    <div class="cards cards-2">{locs}</div>
  </div>
</div></section>

{app}

<section class="biz-band"><div class="wrap two-col">
  <div><h2>Laundry solutions for Dubai businesses</h2><p>Linen, towels and uniforms collected on schedule, cleaned in our own centres and returned when you need them.</p></div>
  <div><div class="chips">{inds}</div><p><a class="btn btn-tag" href="/business#quote">Request a Commercial Quote</a></p></div>
</div></section>

<section class="content"><div class="wrap prose">{B.faq_html(faqs)}<p><a href="/faq">View all FAQs</a></p></div></section>

<section class="cta-band final"><div class="bubbles" data-count="8" aria-hidden="true"></div><div class="wrap"><p class="big">Your laundry, off your to-do list.</p><div><a class="btn btn-tag" href="/contact#book">Book a Pickup</a><a class="btn btn-onblue" href="{B.wa_link("Hi Dima Laundry, I would like to book a pickup.")}">WhatsApp Dima</a></div></div></section>
'''
    local = {"@context": "https://schema.org", "@type": "DryCleaningOrLaundry", "name": "Dima Laundry",
             "parentOrganization": {"@id": B.DOMAIN + "/#org"}, "url": B.DOMAIN + "/", "telephone": "+971-800-3462",
             "priceRange": "AED 6 to AED 300", "image": B.DOMAIN + "/og-image.jpg",
             "address": {"@type": "PostalAddress", "streetAddress": C.HQ_ADDRESS, "addressLocality": "Dubai", "addressCountry": "AE"},
             "areaServed": {"@type": "City", "name": "Dubai"}}
    app_s = {"@context": "https://schema.org", "@type": "MobileApplication", "name": "Dima Laundry", "operatingSystem": "iOS, Android",
             "applicationCategory": "LifestyleApplication", "publisher": {"@id": B.DOMAIN + "/#org"},
             "description": "Book laundry and dry cleaning pickups in Dubai, track orders and pay from your phone.",
             "installUrl": [C.APP_IOS, C.APP_ANDROID], "offers": {"@type": "Offer", "price": "0", "priceCurrency": "AED"}}
    B.write("/", B.shell("/", "Dima Laundry | Laundry and Dry Cleaning in Dubai Since 2001",
                         f"Laundry and dry cleaning in Dubai since 2001. Pickup and delivery, {C.BRANCH_COUNT} branches, in-house cleaning. Shirts from AED 14. Book on {C.TOLL} or WhatsApp.",
                         body, [B.ORG, local, B.faq_schema(faqs), app_s]))
