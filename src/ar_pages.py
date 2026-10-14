"""Arabic pages under /ar/. Mirrors pages.py and home.py with native Arabic copy from content_ar.py."""
import content as C
import content_ar as A

AR = "ar"


def paths():
    """English paths that get an Arabic twin (used for hreflang and the language switch)."""
    p = ["/", "/services", "/prices", "/branches", "/business", "/about-us", "/contact", "/faq", "/privacy", "/terms",
         "/branches/al-quoz-head-office"]
    p += ["/services/" + s["slug"] for s in C.SERVICES]
    p += ["/branches/" + b["slug"] for b in C.BRANCHES]
    p += ["/business/" + x["slug"] for x in C.BUSINESS]
    return set(p)


def build_ar(B):
    esc = B.esc
    U = B.UI[AR]
    money = B.money

    def aed(v):
        return "غير متاح" if v in (None, "--", "") else f"{money(v)} درهم"

    def it(n):
        return A.ITEMS.get(n, n)

    def table(rows, cols):
        head = "".join(f"<th>{c}</th>" for c in cols)
        body = "".join("<tr><td>" + esc(it(r[0])) + "</td>" + "".join(f"<td>{aed(v)}</td>" for v in r[1:]) + "</tr>" for r in rows)
        return f'<div class="tbl"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'

    def bullets(xs):
        return '<ul class="ticks">' + "".join(f"<li>{esc(x)}</li>" for x in xs) + "</ul>"

    def steps(xs):
        return '<ol class="steps">' + "".join(f"<li><strong>{esc(t)}</strong> {esc(d)}</li>" for t, d in xs) + "</ol>"

    def faq(qas, h=None):
        return B.faq_html(qas, heading=h or U["faq_h"])

    def wrap(body):
        return f'<section class="content"><div class="wrap prose">{body}</div></section>'

    def rv(keys, rating=False, live="all", rh=None):
        return B.reviews_block(keys, heading="ماذا يقول عملاؤنا على جوجل", rating=rating, live=live, rating_html=rh, lang=AR)

    P = B.P
    svc = {s["slug"]: s for s in C.SERVICES}

    def service_prices(s):
        out = ""
        cols4 = ["القطعة", "عادي، تنظيف وكوي", "مميز، تنظيف وكوي"]
        if s.get("prices"):
            rows = []
            for g, sec, names in s["prices"]:
                rows += [B.find_item(n, P[g][sec]) for n in names]
            if s.get("press_only"):
                out += table([[r[0], r[2], r[4]] for r in rows], ["القطعة", "كوي عادي", "كوي مميز"])
            else:
                out += table([[r[0], r[1], r[2], r[3]] for r in rows], ["القطعة", "عادي، تنظيف وكوي", "عادي، كوي فقط", "مميز، تنظيف وكوي"])
        for key, prefix in s.get("flat", []):
            out += table(P[key], cols4)
        if s.get("flat_alt"):
            out += table(P["alterations"], ["الخدمة", "السعر"])
        if s.get("fabric_rows"):
            out += table([B.find_item(n, P["home_fabrics"]) for n in s["fabric_rows"]], ["القطعة", "التنظيف في المركز", "التنظيف في المنزل"])
        if s.get("onsite_rows"):
            out += table([B.find_item(n, P["onsite"]) for n in s["onsite_rows"]], ["القطعة", "السعر"])
        if out:
            out += '<p class="small">الأسعار بالدرهم الإماراتي، محدثة في 12 أكتوبر 2026 وموحدة في جميع الفروع. الخدمة المميزة تمنح كل قطعة عناية وتشطيبا إضافيا. للقطع الخاصة والبقع الصعبة وأعمال الترميم يؤكد فريقنا السعر قبل التنظيف. <a href="/ar/prices">قائمة الأسعار الكاملة</a>.</p>'
        return out

    # ---- services ----
    for s in C.SERVICES:
        a = A.SERVICES[s["slug"]]
        path = "/ar/services/" + s["slug"]
        hero, cs = B.page_hero(path, a["short"], a["h1"], a["sub"], lang=AR, wa_text=f"مرحبا ديما لاندري، أرغب بحجز خدمة {a['short']}.")
        body = f'<h2>{a["why_h"]}</h2>' + bullets(a["why"])
        pr = service_prices(s)
        if pr:
            body += f'<h2>{a["prices_h"]}</h2>{pr}'
        body += f'<h2>{a["what_h"]}</h2>' + bullets(a["what"])
        body += f'<h2>الخدمة العادية والسريعة</h2><p>{esc(a["turn"])}</p>'
        body += '<h2>كيف نتعامل مع طلبك</h2>' + steps(A.HOW_STEPS)
        body += rv(s["reviews"]) + faq(a["faqs"]) + B.updated(AR)
        sch = {"@context": "https://schema.org", "@type": "Service", "serviceType": a["short"], "name": a["h1"], "inLanguage": "ar",
               "provider": {"@id": B.DOMAIN + "/#org"}, "areaServed": {"@type": "City", "name": "دبي"}, "url": B.DOMAIN + path, "description": a["sub"]}
        page = hero + wrap(body) + B.cta_band(f'احجز {a["short"]} مع الاستلام من بابك، أو سلّم في أي من فروعنا الثمانية.', lang=AR)
        B.write(path, B.shell(path, a["title"], a["desc"], page, [B.ORG, cs, sch, B.faq_schema(a["faqs"])], lang=AR))

    # ---- services hub ----
    path = "/ar/services"
    hero, cs = B.page_hero(path, U["services"], "خدمات الغسيل والتنظيف الجاف في دبي",
                           f"تقدم ديما لاندري {len(C.SERVICES)} خدمة تنظيف في دبي، من الغسيل اليومي والكوي إلى التنظيف الجاف والعبايات والكنادير وفساتين السهرة والأحذية والحقائب والسجاد والكنب والستائر، وكل قطعة تنظف في مراكز ديما الخاصة في القوز.", lang=AR)
    groups = [("العناية بالملابس", ["dry-cleaning", "wash-and-fold", "ironing", "abaya-kandura-cleaning", "express-laundry", "wedding-dress-cleaning", "alterations"]),
              ("الأحذية والحقائب", ["shoe-cleaning", "bag-cleaning"]), ("المنزل والمفروشات", ["carpet-cleaning", "sofa-cleaning", "curtain-cleaning"])]
    body = ""
    for g, slugs in groups:
        body += f"<h2>{g}</h2><div class=\"cards\">" + "".join(f'<a class="card" href="/ar/services/{x}"><strong>{A.SERVICES[x]["short"]}</strong><span>{A.SERVICES[x]["card"]}</span></a>' for x in slugs) + "</div>"
    qas = [("ما الخدمات التي تقدمها ديما لاندري؟", "تقدم ديما لاندري التنظيف الجاف والغسيل اليومي والكوي والعناية بالعبايات والكنادير وتنظيف فساتين السهرة والزفاف والخدمة السريعة وتعديل الملابس وتنظيف الأحذية والحقائب والسجاد والستائر، وغسيل الكنب والمراتب في المنزل."),
           ("هل تتوفر كل الخدمات مع الاستلام؟", "نعم. يمكن حجز أي خدمة من ديما لاندري مع الاستلام والتوصيل في دبي، أو التسليم في أي من الفروع الثمانية.")]
    body += faq(qas) + B.updated(AR)
    B.write(path, B.shell(path, "خدمات الغسيل والتنظيف الجاف في دبي | ديما لاندري",
                          "تنظيف جاف وغسيل يومي وكوي وعبايات وكنادير وفساتين وأحذية وحقائب وسجاد وكنب وستائر. ننظف في مراكز ديما الخاصة في القوز منذ 2001.",
                          hero + wrap(body) + B.cta_band("لست متأكدا من الخدمة التي تحتاجها؟ راسلنا على واتساب.", lang=AR), [B.ORG, cs, B.faq_schema(qas)], lang=AR))

    # ---- prices ----
    path = "/ar/prices"
    hero, cs = B.page_hero(path, U["prices"], "أسعار واضحة وشفافة",
                           "تبدأ أسعار ديما لاندري من 14 درهما لتنظيف القميص وكيه، و48 درهما للبدلة المكونة من قطعتين، و20 درهما للعباية أو الكندورة، والكوي فقط من 9.80 درهم. الأسعار موحدة في جميع الفروع ومحدثة في 12 أكتوبر 2026. للقطع الخاصة والبقع الصعبة والقطع الحساسة وأعمال الترميم يؤكد فريقنا السعر قبل التنظيف.", lang=AR)
    pop = [("قميص", "من 14 درهم", "تنظيف وكوي"), ("بدلة قطعتين", "من 48 درهم", "تنظيف وكوي"), ("عباية", "من 20 درهم", "تنظيف وكوي"),
           ("كندورة", "من 20 درهم", "تنظيف وكوي"), ("شرشف سرير", "20 درهم", "تنظيف وكوي"), ("كوي قميص", "من 9.80 درهم", "كوي فقط")]
    body = '<h2>الأسعار الأكثر طلبا</h2><div class="price-cards">' + "".join(f'<div class="pcard"><span>{a}</span><strong>{b}</strong><small>{c}</small></div>' for a, b, c in pop) + "</div>"
    body += '<p class="small">نعرض سعر الخدمة العادية والمميزة لكل قطعة. "تنظيف وكوي" يعني الغسيل أو التنظيف الجاف ثم الكوي، و"كوي فقط" للملابس النظيفة. جميع الأسعار بالدرهم الإماراتي.</p>'
    cols = ["القطعة", "عادي، تنظيف وكوي", "عادي، كوي فقط", "مميز، تنظيف وكوي", "مميز، كوي فقط"]
    for key, label in [("men", "ملابس رجالية"), ("women", "ملابس نسائية"), ("baby", "ملابس الأطفال"), ("common", "إكسسوارات وملابس داخلية ومفروشات")]:
        body += f'<h2 id="{key}">{label}</h2>'
        for sec, rows in P[key].items():
            body += f"<h3>{A.SECTIONS.get(sec, sec)}</h3>" + table(rows, cols)
    body += '<h2 id="specialist">الأحذية والحقائب</h2><h3>الحقائب</h3>' + table(P["bags"], ["القطعة", "عادي", "مميز"])
    body += "<h3>الأحذية</h3>" + table(P["shoes"], ["القطعة", "عادي", "مميز"]) + "<h3>أحذية الأطفال</h3>" + table(P["baby_shoes"], ["القطعة", "عادي", "مميز"])
    body += '<h2 id="home">الستائر والسجاد والكنب والمراتب</h2>' + table(P["home_fabrics"], ["القطعة", "التنظيف في المركز", "التنظيف في المنزل"])
    body += "<h3>التنظيف في المنزل وقطع أخرى</h3>" + table(P["onsite"], ["القطعة", "السعر"])
    body += '<h2 id="alt">تعديل الملابس</h2>' + table(P["alterations"], ["الخدمة", "السعر"])
    qas = [("كم سعر تنظيف البدلة تنظيفا جافا في دبي؟", "لدى ديما لاندري تنظيف البدلة المكونة من قطعتين وكيها بسعر 48 درهما، أو 80 درهما مع الخدمة المميزة للبدلات الرجالية."),
           ("كم سعر الكوي في دبي؟", "يبدأ الكوي فقط لدى ديما لاندري من 9.80 درهم للقميص و10.50 درهم للبنطلون."),
           ("ما الفرق بين الخدمة العادية والمميزة؟", "الخدمة المميزة تمنح كل قطعة عناية وتشطيبا إضافيا. اسأل الفريق عما تشمله لقطعك."),
           ("هل الأسعار موحدة في كل الفروع؟", "نعم. تعتمد ديما لاندري قائمة أسعار واحدة في جميع فروع دبي."),
           ("كيف يمكنني الدفع؟", "ادفع في الفرع أو عند التوصيل أو عبر تطبيق ديما لاندري، وحسابات الشركات تصدر لها فاتورة شهرية.")]
    body += faq(qas) + B.updated(AR)
    B.write(path, B.shell(path, "أسعار المغسلة في دبي 2026 | قائمة أسعار ديما لاندري",
                          "قائمة أسعار ديما لاندري الكاملة: القميص من 14 درهما، البدلة من 48 درهما، العباية والكندورة من 20 درهما، الكوي من 9.80 درهم. محدثة في 12 أكتوبر 2026.",
                          hero + f'<section class="content"><div class="wrap prose wide">{body}</div></section>' + B.cta_band("عرفت ما تحتاجه؟ احجز الاستلام في دقيقة.", lang=AR),
                          [B.ORG, cs, B.faq_schema(qas)], lang=AR))

    # ---- branches ----
    for b in C.BRANCHES:
        a = A.BRANCHES[b["slug"]]
        path = "/ar/branches/" + b["slug"]
        hero, cs = B.page_hero(path, a["name"], a["h1"], a["intro"], book_label=f'احجز استلام في {a["area"]}', lang=AR,
                               wa_text=f"مرحبا ديما لاندري، أرغب بحجز استلام في {a['area']}.")
        maps = "https://www.google.com/maps/search/?api=1&query=" + B.quote_plus("Dima Laundry " + b["address"])
        body = (f'<h2>زوروا ديما {esc(a["name"])}</h2><div class="tbl"><table><tbody>'
                f'<tr><td>العنوان</td><td>{esc(a["address"])}</td></tr><tr><td>ساعات العمل</td><td>{A.RETAIL_HOURS}</td></tr>'
                f'<tr><td>الهاتف</td><td><a href="tel:{C.TEL}" dir="ltr">{C.TOLL}</a> أو <a href="tel:+971506398093" dir="ltr">{C.RETAIL}</a></td></tr>'
                f'<tr><td>واتساب</td><td><a href="{B.wa_link()}" dir="ltr">{C.RETAIL}</a></td></tr>'
                f'<tr><td>الاتجاهات</td><td><a href="{maps}" rel="noopener" target="_blank">افتح في خرائط جوجل</a></td></tr></tbody></table></div>')
        body += f'<div class="map"><iframe title="خريطة ديما لاندري {esc(a["name"])}" loading="lazy" src="https://www.google.com/maps?q={B.quote_plus("Dima Laundry " + b["address"])}&amp;hl=ar&amp;output=embed"></iframe></div>'
        body += f'<h2>الاستلام والتوصيل حول {esc(a["area"])}</h2><p>تستلم ديما لاندري من المنازل والمكاتب في:</p>' + bullets(a["areas"])
        body += '<h2>الخدمات الأكثر طلبا هنا</h2><div class="cards">' + "".join(
            f'<a class="card" href="/ar/services/{C.POPULAR[k][0]}"><strong>{A.SERVICES[C.POPULAR[k][0]]["short"]}</strong><span>{A.SERVICES[C.POPULAR[k][0]]["card"]}</span></a>' for k in b["popular"]) + "</div>"
        body += f'<h2>{a["why_h"]}</h2><p>{esc(a["why"])}</p>'
        rh = None
        if b.get("rating"):
            rh = f'تقييم <strong>{b["rating"][0]} من {b["rating"][1]} مراجعة على جوجل</strong> لهذا الفرع (أكتوبر 2026). <a href="{C.GMAPS[b["gkey"]]}" rel="noopener" target="_blank">اقرأ كل التقييمات على جوجل</a>'
        body += rv(b["reviews"], live=b["slug"] if b.get("gkey") and b["slug"] != "dubai-marina-crown" else "all", rh=rh)
        body += faq(a["faqs"])
        body += '<p class="nearby">فروع قريبة: ' + "، ".join(f'<a href="/ar/branches/{n}">{esc(A.BRANCHES[n]["name"])}</a>' for n in b["nearby"]) + '، أو <a href="/ar/branches">كل الفروع</a>.</p>' + B.updated(AR)
        sch = {"@context": "https://schema.org", "@type": "DryCleaningOrLaundry", "@id": B.DOMAIN + "/branches/" + b["slug"] + "#branch",
               "name": "ديما لاندري " + a["name"], "alternateName": "Dima Laundry " + b["name"], "inLanguage": "ar", "url": B.DOMAIN + path,
               "parentOrganization": {"@id": B.DOMAIN + "/#org"}, "telephone": "+971-800-3462", "priceRange": "AED 6 to AED 300",
               "address": {"@type": "PostalAddress", "streetAddress": a["address"], "addressLocality": "دبي", "addressCountry": "AE"},
               "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:00", "closes": "22:00"}],
               "hasMap": maps, "description": a["intro"]}
        if b.get("rating"):
            sch["aggregateRating"] = {"@type": "AggregateRating", "ratingValue": b["rating"][0], "reviewCount": b["rating"][1]}
        page = hero + wrap(body) + B.cta_band(f'احجز استلاما في {a["area"]} اليوم، أو زرنا من 10 صباحا حتى 10 مساء.', book_label=f'احجز استلام في {a["area"]}', lang=AR)
        B.write(path, B.shell(path, a["title"], a["desc"], page, [B.ORG, cs, sch, B.faq_schema(a["faqs"])], lang=AR))

    # ---- processing centres ----
    path = "/ar/branches/al-quoz-head-office"
    hero, cs = B.page_hero(path, U["proc"], "مراكز تنظيف ديما لاندري في القوز",
                           "تنظف ديما لاندري كل قطعة في مراكزها الخاصة في القوز التي تعمل 24 ساعة. المكتب الرئيسي في شارع 24a رقم 22، القوز الصناعية 3، مع مراكز أخرى في القوز الصناعية 4 والقوز 3، ومركز جديد في مجمع دبي للاستثمار 2 يفتتح قريبا.", lang=AR)
    rows = "".join(f"<tr><td>{esc(n)}</td><td>{esc(ad)}</td><td>{esc(r)}</td></tr>" for n, ad, r in A.PROCESSING)
    body = f'<h2>مراكزنا</h2><div class="tbl"><table><thead><tr><th>المركز</th><th>العنوان</th><th>ملاحظات</th></tr></thead><tbody>{rows}</tbody></table></div>'
    body += "<h2>ماذا يحدث في الداخل</h2>" + bullets(["ترقيم كل قطعة عند الوصول", "الفرز حسب القماش والخدمة", "التنظيف والكوي ومراجعة الجودة", "التغليف للتوصيل أو للاستلام من الفرع"])
    body += f'<h2>لعملاء الشركات</h2><p>يمكن للفنادق والمشغلين ترتيب زيارة للاطلاع على العمل قبل التعاقد. اتصل بفريق الشركات على <a href="tel:+971569984493" dir="ltr">{C.BIZ}</a> أو <a href="/ar/business#quote">اطلب عرض سعر</a>.</p>'
    qas = [("أين تنظف ديما لاندري الملابس؟", "في مراكزها الخاصة في القوز الصناعية 3 و4 في دبي، والتي تعمل 24 ساعة."),
           ("أين يقع المكتب الرئيسي لديما لاندري؟", "في شارع 24a رقم 22، القوز الصناعية 3، دبي.")]
    body += rv(["q4_great", "q3_satin", "f3_b2b"], rating=True) + faq(qas) + B.updated(AR)
    B.write(path, B.shell(path, "مراكز تنظيف ديما لاندري والمكتب الرئيسي | القوز دبي",
                          "مراكز التنظيف الخاصة بديما لاندري في القوز الصناعية 3 و4 تعمل 24 ساعة. المكتب الرئيسي في شارع 24a رقم 22، القوز 3.",
                          hero + wrap(body) + B.cta_band("كل قطعة تنظف في مراكزنا الخاصة. احجز الاستلام.", lang=AR), [B.ORG, cs, B.faq_schema(qas)], lang=AR))

    # ---- locations hub ----
    path = "/ar/branches"
    hero, cs = B.page_hero(path, U["locations"], "اعثر على أقرب فرع لديما",
                           f"لدى ديما لاندري {C.BRANCH_COUNT} فروع في دبي مفتوحة {A.RETAIL_HOURS}: فرعان في دبي مارينا، إضافة إلى الصفوح وجميرا وداون تاون دبي وشارع الشيخ زايد والكرامة وداماك أيكون سيتي. كثير منها داخل السوبرماركت فتسلّم ملابسك أثناء التسوق، وكل فرع يرتب الاستلام والتوصيل في المناطق القريبة.", lang=AR)
    cards = ""
    for b in C.BRANCHES:
        a = A.BRANCHES[b["slug"]]
        maps = "https://www.google.com/maps/search/?api=1&query=" + B.quote_plus("Dima Laundry " + b["address"])
        cards += (f'<article class="loc"><h3>{esc(a["name"])}</h3><p class="loc-place">{esc(a["place"])}</p><p>نخدم {esc("، ".join(a["areas"][:4]))} والمناطق المجاورة.</p>'
                  f'<p class="small">{A.RETAIL_HOURS}</p><div class="loc-links"><a href="{maps}" rel="noopener" target="_blank">الاتجاهات</a><a href="/ar/branches/{b["slug"]}">تفاصيل الفرع</a><a href="/ar/contact#book">احجز استلام</a></div></article>')
    body = '<div class="map map-big"><iframe title="خريطة فروع ديما لاندري في دبي" loading="lazy" src="https://www.google.com/maps?q=Dima+Laundry+Dubai&amp;hl=ar&amp;output=embed"></iframe></div>'
    body += f'<h2>فروعنا الثمانية</h2><div class="locs">{cards}</div>'
    body += '<h2>مراكز التنظيف</h2><p>كل قطعة تنظف في مراكزنا الخاصة في القوز التي تعمل 24 ساعة، مع مركز جديد في مجمع دبي للاستثمار 2 يفتتح قريبا. <a href="/ar/branches/al-quoz-head-office">تعرف على مراكز التنظيف</a>.</p>'
    qas = [("أين أقرب فرع لديما لاندري؟", f"لدى ديما لاندري {C.BRANCH_COUNT} فروع في دبي: دبي مارينا (مارينا سكيب وكراون) والصفوح وجميرا وداون تاون دبي وشارع الشيخ زايد والكرامة وداماك أيكون سيتي."),
           ("ما مواعيد عمل ديما لاندري؟", f"الفروع مفتوحة {A.RETAIL_HOURS}، ومراكز التنظيف في القوز تعمل 24 ساعة."),
           ("هل توفر كل الفروع الاستلام والتوصيل؟", "نعم. كل فرع يرتب الاستلام والتوصيل في المناطق المحيطة به.")]
    body += faq(qas) + B.updated(AR)
    B.write(path, B.shell(path, "فروع ديما لاندري في دبي | 8 فروع من 10 صباحا حتى 10 مساء",
                          "8 فروع لديما لاندري في دبي: دبي مارينا والصفوح وجميرا وداون تاون وشارع الشيخ زايد والكرامة وداماك أيكون سيتي. مفتوحة من 10 صباحا حتى 10 مساء يوميا.",
                          hero + f'<section class="content"><div class="wrap prose wide">{body}</div></section>' + B.cta_band("مشغول ولا وقت للتسليم؟ نستلم من بابك.", lang=AR),
                          [B.ORG, cs, B.faq_schema(qas)], lang=AR))

    # ---- business ----
    quote_btn = "اطلب عرض سعر للشركات"
    for x in C.BUSINESS:
        a = A.BUSINESS[x["slug"]]
        path = "/ar/business/" + x["slug"]
        hero, cs = B.page_hero(path, a["short"], f'{a["h1"]} <span class="kicker">{esc(a["kicker"])}</span>', a["sub"], book_label=quote_btn, lang=AR, book_href="#quote")
        hero = hero.replace(B.wa_link(U["wa_book_text"]), B.wa_link(U["wa_quote_text"], C.BIZ_WA))
        body = "<h2>ما الذي نتولاه</h2>" + bullets(a["items"]) + "<h2>ما الذي يمكنك الاعتماد عليه</h2>" + bullets(a["outcomes"])
        body += "<h2>كيف نعمل</h2>" + steps(A.BIZ_STEPS)
        body += f'<h2>قدراتنا للشركات</h2><p>تخدم ديما لاندري دبي منذ 2001 وتنظف كل طلب في مراكزها الخاصة في القوز التي تعمل 24 ساعة، مع مركز جديد في مجمع دبي للاستثمار 2 يفتتح قريبا. تصل استفسارات الشركات مباشرة إلى فريق الشركات على <a href="tel:+971569984493" dir="ltr">{C.BIZ}</a>.</p>'
        body += rv(["f3_b2b"]) + faq(a["faqs"]) + B.quote_form(AR) + B.updated(AR)
        sch = {"@context": "https://schema.org", "@type": "Service", "serviceType": a["short"], "name": a["h1"], "inLanguage": "ar",
               "provider": {"@id": B.DOMAIN + "/#org"}, "areaServed": {"@type": "City", "name": "دبي"}, "url": B.DOMAIN + path, "description": a["sub"]}
        B.write(path, B.shell(path, a["title"], a["desc"], hero + wrap(body), [B.ORG, cs, sch, B.faq_schema(a["faqs"])], lang=AR))

    path = "/ar/business"
    hero, cs = B.page_hero(path, U["commercial"], "مغسلة موثوقة لشركات دبي",
                           "مفارشك ومناشفك وزي موظفيك تستلم في موعدها، وتنظف باحترافية في مراكز ديما لاندري الخاصة في القوز، وتعود عندما تحتاجها. تخدم ديما لاندري شركات دبي منذ 2001.",
                           book_label=quote_btn, lang=AR, book_href="#quote")
    hero = hero.replace(B.wa_link(U["wa_book_text"]), B.wa_link(U["wa_quote_text"], C.BIZ_WA))
    body = '<h2>القطاعات التي نخدمها</h2><div class="cards">' + "".join(f'<a class="card" href="/ar/business/{s}"><strong>{n}</strong></a>' for n, s in A.INDUSTRY_CARDS) + "</div>"
    body += "<h2>لماذا تختار الشركات ديما</h2>" + bullets(["مواعيد استلام ثابتة يمكنك التخطيط حولها", "تسليم موثوق في موعده", "طاقة تشغيلية في مراكزنا الخاصة التي تعمل 24 ساعة", "فريق شركات يمكنك التواصل معه مباشرة", "عدّ القطع في كل استلام", "فاتورة شهرية", "دون أي جهات تنظيف خارجية"])
    body += "<h2>كيف نعمل</h2>" + steps(A.BIZ_STEPS)
    body += f'<h2>قدراتنا</h2><p>تدير ديما لاندري {C.BRANCH_COUNT} فروع و3 مراكز تنظيف في القوز، ومركزا رابعا في مجمع دبي للاستثمار 2 يفتتح قريبا. كل طلبات الشركات تنظف داخليا. <a href="/ar/branches/al-quoz-head-office">تعرف على مراكز التنظيف</a>.</p>'
    qas = [("هل تقدم ديما لاندري خدمة مغسلة للشركات؟", "نعم. تخدم ديما لاندري الفنادق وبيوت العطلات والمطاعم والصالونات والسبا والأندية الرياضية والعيادات والشركات في دبي."),
           ("كيف تسعّر خدمة مغسلة الشركات؟", "تسعّر ديما لاندري خدمة الشركات بالكيلو أو بالقطعة حسب الكمية، مع فاتورة شهرية."),
           ("بمن أتواصل لطلب عرض سعر؟", f"اتصل أو راسل فريق الشركات على واتساب {C.BIZ}، أو استخدم نموذج عرض السعر في هذه الصفحة.")]
    body += rv(["f3_b2b"]) + faq(qas) + B.quote_form(AR) + B.updated(AR)
    B.write(path, B.shell(path, "مغسلة الشركات في دبي | الفنادق وبيوت العطلات وزي الموظفين | ديما لاندري",
                          "مغسلة موثوقة للفنادق وبيوت العطلات والمطاعم والصالونات والأندية والعيادات وزي الموظفين في دبي. استلام ثابت وفاتورة شهرية.",
                          hero + wrap(body), [B.ORG, cs, B.faq_schema(qas)], lang=AR))

    # ---- about ----
    path = "/ar/about-us"
    hero, cs = B.page_hero(path, U["about"], "في خدمة دبي منذ 2001",
                           f"ديما لاندري ذ.م.م شركة غسيل وتنظيف جاف في دبي تأسست عام 2001. تدير اليوم {C.BRANCH_COUNT} فروع و3 مراكز تنظيف في القوز، وتنظف كل قطعة داخليا، وتخدم المنازل والفنادق وبيوت العطلات والشركات في أنحاء المدينة.", lang=AR)
    body = "<h2>قصتنا</h2><p>بدأت ديما لاندري في دبي عام 2001 بهدف بسيط: تنظيف الملابس كما يجب وإعادتها في موعدها. وعلى مدى 25 عاما كبرت لتصبح شبكة فروع داخل السوبرماركت والأبراج التي يتسوق ويسكن فيها أهل دبي، من دبي مارينا إلى الكرامة.</p><p>منذ البداية تدير ديما عمليات التنظيف بنفسها. كل قميص وعباية وبدلة وشرشف ينظفه فريق ديما في القوز، ولا يرسل أبدا إلى جهة خارجية.</p>"
    body += f'<h2>الأمس واليوم</h2><ol class="timeline"><li><strong>2001</strong> ديما لاندري تبدأ خدمة دبي.</li><li><strong>اليوم</strong> {C.BRANCH_COUNT} فروع مفتوحة {A.RETAIL_HOURS}، و3 مراكز تنظيف تعمل 24 ساعة، واستلام وتوصيل، وتطبيق ديما على آيفون وأندرويد، وخدمة للمنازل والشركات.</li><li><strong>القادم</strong> مركز تنظيف جديد في مجمع دبي للاستثمار 2 يفتتح قريبا.</li></ol>'
    body += "<h2>ما يميز ديما</h2>" + bullets(["مراكز تنظيف خاصة دون جهات خارجية", "فريق خبير، كثير منه يعمل مع ديما منذ سنوات", "ترقيم وتتبع كل قطعة", "استلام وتوصيل في كل دبي", "قائمة أسعار موحدة في كل الفروع", "طاقة للمنازل والشركات"])
    rows = "".join(f"<tr><td>{x}</td><td>{y}</td></tr>" for x, y in [("التأسيس", "2001"), ("الفروع", f"{C.BRANCH_COUNT}، مفتوحة {A.RETAIL_HOURS}"), ("مراكز التنظيف", "3 في القوز تعمل 24 ساعة، ومجمع دبي للاستثمار 2 قريبا"), ("المكتب الرئيسي", "شارع 24a رقم 22، القوز الصناعية 3، دبي"), ("الهاتف", f'<span dir="ltr">{C.TOLL}</span>'), ("البريد", C.EMAIL)])
    body += f'<h2>ديما لاندري في سطور</h2><div class="tbl"><table><tbody>{rows}</tbody></table></div>'
    qas = [("متى تأسست ديما لاندري؟", "تأسست ديما لاندري في دبي عام 2001."), ("هل تنظف ديما لاندري الملابس داخليا؟", "نعم. كل قطعة تنظف في مراكز ديما لاندري الخاصة في القوز."),
           ("كم عدد فروع ديما لاندري؟", f"لدى ديما لاندري {C.BRANCH_COUNT} فروع في دبي و3 مراكز تنظيف في القوز.")]
    body += rv(["sufouh_2yrs", "karama_raju", "jumeirah_7yrs"], rating=True) + faq(qas) + B.updated(AR)
    B.write(path, B.shell(path, "عن ديما لاندري | في خدمة دبي منذ 2001",
                          f"ديما لاندري ذ.م.م تنظف ملابس منازل وشركات دبي منذ 2001، مع {C.BRANCH_COUNT} فروع ومراكز تنظيف خاصة في القوز.",
                          hero + wrap(body) + B.cta_band("25 عاما من الغسيل في دبي. احجز الاستلام.", lang=AR), [B.ORG, cs, B.faq_schema(qas)], lang=AR))

    # ---- contact ----
    path = "/ar/contact"
    hero, cs = B.page_hero(path, U["contact"], "احجز استلام الملابس في دبي",
                           f'احجز مع ديما لاندري بالاتصال على <span dir="ltr">{C.TOLL}</span>، أو المراسلة على واتساب <span dir="ltr">{C.RETAIL}</span>، أو عبر تطبيق ديما، أو النموذج أدناه. استفسارات الشركات على <span dir="ltr">{C.BIZ}</span>. المكتب الرئيسي في شارع 24a رقم 22، القوز الصناعية 3، دبي.', lang=AR)
    rows = "".join(f"<tr><td>{x}</td><td>{y}</td></tr>" for x, y in [
        ("الرقم المجاني", f'<a href="tel:{C.TEL}" dir="ltr">{C.TOLL}</a>'), ("واتساب", f'<a href="{B.wa_link()}" dir="ltr">{C.RETAIL}</a>'),
        ("خط الفروع", f'<a href="tel:+971506398093" dir="ltr">{C.RETAIL}</a>'), ("استفسارات الشركات", f'<a href="tel:+971569984493" dir="ltr">{C.BIZ}</a>'),
        ("البريد الإلكتروني", f'<a href="mailto:{C.EMAIL}">{C.EMAIL}</a>'), ("دعم الطلبات", f'<a href="mailto:{C.SUPPORT_EMAIL}">{C.SUPPORT_EMAIL}</a>'), ("المكتب الرئيسي", "شارع 24a رقم 22، القوز الصناعية 3، دبي"),
        ("ساعات الفروع", A.RETAIL_HOURS), ("مراكز التنظيف", "تعمل 24 ساعة")])
    body = B.booking_form(AR)
    body += f'<div class="app-inline"><h2>أو احجز عبر التطبيق</h2><p>احجز الاستلام وتابع طلباتك وادفع من تطبيق ديما لاندري.</p>{B.app_badges(lang=AR)}</div>'
    body += f'<h2>بيانات التواصل</h2><div class="tbl"><table><tbody>{rows}</tbody></table></div><p><a href="/ar/branches">عناوين كل الفروع</a>.</p>'
    B.write(path, B.shell(path, "تواصل مع ديما لاندري دبي | احجز استلام الملابس",
                          f"احجز استلام الملابس مع ديما لاندري في دبي. اتصل على {C.TOLL} أو واتساب {C.RETAIL} أو استخدم النموذج. الشركات {C.BIZ}.",
                          hero + wrap(body), [B.ORG, cs], lang=AR))

    # ---- faq ----
    path = "/ar/faq"
    hero, cs = B.page_hero(path, U["faq"], "ديما لاندري: الأسئلة الشائعة",
                           "إجابات عن الحجز والاستلام والأسعار ومواعيد العمل والفروع والعناية بالملابس وحسابات الشركات لدى ديما لاندري، شركة الغسيل والتنظيف الجاف في دبي منذ 2001.", lang=AR)
    sections = [
        ("الحجز والاستلام", [("كيف أحجز استلام الملابس مع ديما لاندري؟", f"اتصل على {C.TOLL}، أو راسل {C.RETAIL} على واتساب، أو احجز عبر تطبيق ديما لاندري، أو استخدم نموذج الحجز في الموقع."),
                             ("ما المناطق التي تغطيها ديما لاندري؟", "تستلم ديما لاندري وتوصل في أنحاء دبي، ومنها دبي مارينا وجي بي آر وأبراج بحيرات جميرا والصفوح ونخلة جميرا وجميرا وداون تاون والخليج التجاري وشارع الشيخ زايد والكرامة."),
                             ("هل لدى ديما لاندري تطبيق؟", "نعم. تطبيق ديما لاندري مجاني على متجر آبل وجوجل بلاي، ويمكنك من خلاله حجز الاستلام ومتابعة الطلبات والدفع.")]),
        ("الفروع والمواعيد", [("كم عدد فروع ديما لاندري؟", f"لدى ديما لاندري {C.BRANCH_COUNT} فروع في دبي و3 مراكز تنظيف في القوز."),
                              ("ما مواعيد عمل ديما لاندري؟", f"الفروع مفتوحة {A.RETAIL_HOURS}، ومراكز التنظيف تعمل 24 ساعة.")]),
        ("الأسعار والدفع", [("كم أسعار ديما لاندري؟", "يبدأ التنظيف والكوي من 14 درهما للقميص و48 درهما للبدلة المكونة من قطعتين و20 درهما للعباية أو الكندورة، والكوي فقط من 9.80 درهم."),
                            ("هل الأسعار موحدة في كل الفروع؟", "نعم. تعتمد ديما لاندري قائمة أسعار واحدة في جميع الفروع."),
                            ("ما هي الخدمة المميزة؟", "الخدمة المميزة تمنح كل قطعة عناية وتشطيبا إضافيا، وهي متاحة لكل القطع.")]),
        ("مدة التنفيذ", [("كم تستغرق ديما لاندري؟", "تتوفر خدمة عادية وخدمة سريعة. القطع الخاصة مثل فساتين الزفاف والحقائب والأحذية والسجاد تحتاج وقتا أطول، ويؤكد الفريق موعد الجاهزية عند الحجز.")]),
        ("العناية والجودة", [("هل تزيل ديما لاندري البقع الصعبة؟", "تعالج ديما لاندري البقع قبل التنظيف، ومعظم بقع الطعام والزيت والمكياج والعرق تزول. البقع القديمة أو الثابتة قد لا تزول تماما وسيخبرك الفريق بذلك عند التسليم."),
                             ("هل تنظف ديما لاندري العبايات والكنادير؟", "نعم. تنظف ديما لاندري العبايات والكنادير والغتر والجلابيات والشيلات وتكويها، مع أسعار خاصة للقطع المطرزة والصوفية."),
                             ("هل تنظف ديما لاندري الملابس داخليا؟", "نعم. كل قطعة تنظف في مراكز ديما لاندري الخاصة في القوز.")]),
        ("الشركات", [("هل تخدم ديما لاندري الشركات؟", "نعم. تقدم ديما لاندري خدمة مغسلة للفنادق وبيوت العطلات والمطاعم والصالونات والسبا والأندية الرياضية والعيادات وزي الموظفين."),
                     ("من يتولى استفسارات الشركات؟", f"فريق الشركات على {C.BIZ}.")]),
        ("عن ديما", [("منذ متى تعمل ديما لاندري؟", "تعمل ديما لاندري في دبي منذ عام 2001.")]),
    ]
    body = ""
    allq = []
    for t, qs in sections:
        body += faq(qs, t)
        allq += qs
    body += B.updated(AR)
    B.write(path, B.shell(path, "الأسئلة الشائعة | ديما لاندري دبي",
                          "إجابات عن الحجز والاستلام والأسعار والمواعيد والفروع والعناية بالعبايات والبقع وحسابات الشركات لدى ديما لاندري في دبي.",
                          hero + wrap(body) + B.cta_band("لديك سؤال آخر؟ اسألنا على واتساب.", lang=AR), [B.ORG, cs, B.faq_schema(allq)], lang=AR))

    # ---- home ----
    trust = ["منذ 2001", f"{C.BRANCH_COUNT} فروع", "تنظيف داخلي", "استلام وتوصيل", "خدمة سريعة متاحة"]
    rail = "".join(f'<li><span class="hook" aria-hidden="true"></span><span class="rail-tag">{t}</span></li>' for t in trust)
    popular = ["dry-cleaning", "wash-and-fold", "ironing", "abaya-kandura-cleaning", "express-laundry", "curtain-cleaning"]
    pop_names = {"curtain-cleaning": ("المنزل والمفروشات", "ستائر وسجاد وكنب ومراتب.")}
    cards = "".join(f'<a class="card svc-card" href="/ar/services/{s}"><strong>{pop_names.get(s, (A.SERVICES[s]["short"],))[0]}</strong><span>{pop_names.get(s, (None, A.SERVICES[s]["card"]))[1]}</span></a>' for s in popular)
    why = [("ملابسك تبقى معنا", "تنظف ديما لاندري كل قطعة في مراكزها الخاصة في القوز ولا تعتمد على أي جهات تنظيف خارجية."),
           ("في خدمة دبي منذ 2001", "أكثر من عقدين من العناية بملابس منازل وشركات دبي."), ("نستلم من بابك", "احجز الاستلام عبر الموقع أو واتساب أو الهاتف أو تطبيق ديما."),
           ("كل قطعة متتبعة", "ترقّم الملابس وتتبع من الاستلام مرورا بالتنظيف وحتى التوصيل."), (f"{C.BRANCH_COUNT} فروع في دبي", f"زر فرعا من دبي مارينا إلى الكرامة، مفتوحا {A.RETAIL_HOURS}، أو دعنا نأتي إليك.")]
    whys = "".join(f'<div class="why-card"><h3>{t}</h3><p>{d}</p></div>' for t, d in why)
    prices = [("قميص", "من 14 درهم"), ("بدلة قطعتين", "من 48 درهم"), ("عباية", "من 20 درهم"), ("كندورة", "من 20 درهم"), ("شرشف سرير", "20 درهم"), ("غسيل الكنب", "70 درهم للمقعد")]
    pcards = "".join(f'<div class="pcard"><span>{a}</span><strong>{b}</strong></div>' for a, b in prices)
    locs = "".join(f'<a class="card" href="/ar/branches/{b["slug"]}"><strong>{esc(A.BRANCHES[b["slug"]]["name"])}</strong><span>{esc(A.BRANCHES[b["slug"]]["place"])}</span></a>' for b in C.BRANCHES)
    inds = "".join(f'<a class="chip" href="/ar/business/{s}">{n}</a>' for n, s in A.INDUSTRY_CARDS)
    faqs = [("هل توفر ديما لاندري الاستلام والتوصيل؟", "نعم. تستلم ديما لاندري من المنازل والمكاتب في أنحاء دبي. احجز عبر الموقع أو واتساب أو الهاتف أو تطبيق ديما."),
            ("كم أسعار ديما لاندري؟", "يبدأ التنظيف والكوي من 14 درهما للقميص و48 درهما للبدلة و20 درهما للعباية أو الكندورة، والكوي فقط من 9.80 درهم."),
            ("أين تقع ديما لاندري؟", f"لدى ديما لاندري {C.BRANCH_COUNT} فروع في دبي: دبي مارينا (مارينا سكيب وكراون) والصفوح وجميرا وداون تاون دبي وشارع الشيخ زايد والكرامة وداماك أيكون سيتي، وكلها مفتوحة {A.RETAIL_HOURS}."),
            ("هل تنظف ديما لاندري الملابس داخليا؟", "نعم. كل قطعة تنظف في مراكز ديما لاندري الخاصة في القوز التي تعمل 24 ساعة."),
            ("هل تخدم ديما لاندري الشركات؟", "نعم. تقدم ديما لاندري خدمة مغسلة للفنادق وبيوت العطلات والمطاعم والصالونات والسبا والأندية والعيادات وزي الموظفين."),
            ("هل لدى ديما لاندري تطبيق؟", "نعم. تطبيق ديما لاندري مجاني على آيفون وأندرويد لحجز الاستلام ومتابعة الطلبات والدفع.")]
    body = f'''
<section class="hero">
  <div class="bubbles" data-count="14" aria-hidden="true"></div>
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <h1 class="eyebrow">مغسلة وتنظيف جاف في دبي</h1>
      <p class="hero-big">نستلم. ننظف باحتراف. ونعيدها إلى بابك.</p>
      <p class="lede">ديما لاندري في خدمة دبي منذ 2001، بتنظيف داخلي في مراكزها الخاصة في القوز، واستلام وتوصيل، و{C.BRANCH_COUNT} فروع في أنحاء المدينة مفتوحة {A.RETAIL_HOURS}.</p>
      {B.btns(lang=AR)}
    </div>
    <div class="hero-tag" aria-hidden="true"><div class="string"></div><div class="big-tag"><span class="tag-hole"></span><img class="tag-logo" src="/logo.png" alt="" width="150" height="47"><div class="tag-no">No. 2001</div>
      <dl><div><dt>القطع</dt><dd>3 قمصان، عباية، بدلة</dd></div><div><dt>الخدمة</dt><dd>تنظيف وكوي</dd></div><div><dt>الاستلام</dt><dd>دبي مارينا، 7 مساء</dd></div><div><dt>الحالة</dt><dd>تمت مراجعة الجودة</dd></div></dl>
      <div class="tag-perf"></div><div class="tag-stub">احتفظ بهذا الإيصال</div></div></div>
  </div>
  <div class="rail-wrap"><ul class="rail wrap" aria-label="لماذا ديما">{rail}</ul></div>
</section>
<section class="home-sec"><div class="wrap"><div class="sec-head"><h2>الخدمات الأكثر طلبا</h2><a href="/ar/services">كل الخدمات</a></div><div class="cards cards-3">{cards}</div></div></section>
<section class="home-sec tint"><div class="wrap"><h2>لماذا تثق دبي بديما</h2><div class="why-grid">{whys}</div></div></section>
<div class="how-wave">{B.WAVE}</div><section class="how"><div class="wrap"><h2>غسيل دون عناء</h2>{steps(A.HOW_STEPS)}<p><a class="btn btn-tag" href="/ar/contact#book">احجز الاستلام</a></p></div></section>
<section class="home-sec"><div class="wrap"><h2>موثوقون من عملاء في أنحاء دبي</h2><p class="rating-line">{A.RATING_LINE} <a href="{C.GMAPS["karama"]}" rel="noopener" target="_blank">اقرأ كل التقييمات على جوجل</a></p>
  <div class="rv-grid" data-live="all" data-lang="ar">{"".join(B.review_card(k, AR) for k in ["sufouh_2yrs", "karama_raju", "jumeirah_7yrs", "szr_6yrs", "q3_satin", "marina_zeeshan"])}</div></div></section>
<section class="home-sec tint"><div class="wrap"><div class="sec-head"><h2>الأسعار الأكثر طلبا</h2><a href="/ar/prices">قائمة الأسعار الكاملة</a></div><div class="price-cards">{pcards}</div><p class="small">الخدمة العادية شاملة التنظيف والكوي. الأسعار موحدة في كل الفروع ومحدثة في 12 أكتوبر 2026.</p></div></section>
<section class="home-sec"><div class="wrap"><div class="sec-head"><h2>اعثر على ديما بالقرب منك</h2><a href="/ar/branches">كل الفروع</a></div>
  <div class="loc-split"><div class="map"><iframe title="خريطة فروع ديما لاندري" loading="lazy" src="https://www.google.com/maps?q=Dima+Laundry+Dubai&amp;hl=ar&amp;output=embed"></iframe></div><div class="cards cards-2">{locs}</div></div></div></section>
<section class="app-sec"><div class="wrap app-grid"><div class="phone" aria-hidden="true"><div class="phone-screen"><img src="/logo.png" alt="" width="120" height="37"><div class="ph-row"><b>تم حجز الاستلام</b><span>اليوم 7 مساء</span></div><div class="ph-row"><b>طلب رقم 2001</b><span>قيد التنظيف</span></div><div class="ph-bar"><i></i></div><div class="ph-row"><b>التوصيل</b><span>غدا 6 مساء</span></div></div></div>
  <div><h2>أعد الحجز في ثوان مع تطبيق ديما</h2><p>احجز الاستلام بلمسات قليلة، وتابع كل طلب من الاستلام حتى التوصيل، وادفع من هاتفك. مجاني على آيفون وأندرويد.</p>{B.app_badges(lang=AR)}</div></div></section>
<section class="biz-band"><div class="wrap two-col"><div><h2>حلول مغسلة لشركات دبي</h2><p>مفارش ومناشف وزي موظفين تستلم في موعدها، وتنظف في مراكزنا الخاصة، وتعود عندما تحتاجها.</p></div>
  <div><div class="chips">{inds}</div><p><a class="btn btn-tag" href="/ar/business#quote">اطلب عرض سعر للشركات</a></p></div></div></section>
<section class="content"><div class="wrap prose">{faq(faqs)}<p><a href="/ar/faq">كل الأسئلة الشائعة</a></p></div></section>
<section class="cta-band final"><div class="bubbles" data-count="8" aria-hidden="true"></div><div class="wrap"><p class="big">غسيلك؟ اعتبره منتهيا.</p><div><a class="btn btn-tag" href="/ar/contact#book">احجز استلام</a><a class="btn btn-onblue" href="{B.wa_link(U["wa_book_text"])}">واتساب ديما</a></div></div></section>
'''
    local = {"@context": "https://schema.org", "@type": "DryCleaningOrLaundry", "name": "ديما لاندري", "alternateName": "Dima Laundry", "inLanguage": "ar",
             "parentOrganization": {"@id": B.DOMAIN + "/#org"}, "url": B.DOMAIN + "/ar/", "telephone": "+971-800-3462", "priceRange": "AED 6 to AED 300",
             "address": {"@type": "PostalAddress", "streetAddress": "شارع 24a رقم 22، القوز الصناعية 3", "addressLocality": "دبي", "addressCountry": "AE"}}
    B.write("/ar/", B.shell("/ar/", "ديما لاندري | مغسلة وتنظيف جاف في دبي منذ 2001",
                            f"مغسلة وتنظيف جاف في دبي منذ 2001. استلام وتوصيل و{C.BRANCH_COUNT} فروع وتنظيف داخلي. القميص من 14 درهما. احجز على {C.TOLL} أو واتساب.",
                            body, [B.ORG, local, B.faq_schema(faqs)], lang=AR))
