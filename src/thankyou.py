"""Thank-you pages for Google Ads and GA4 conversion tracking.

Forms redirect here only after the lead reaches GoHighLevel, so every visit is a real lead.
Each visit carries ?lid=<id>; the conversion fires once per id (sessionStorage plus Google Ads
transaction_id dedupe), so refreshes and back-button visits are not counted twice.
"""
import content as C

PAGES = {
    ("en", "booking"): ("/thank-you", "Pickup request received", "Thank you. Your pickup request has reached the Dima Laundry team.",
                        ["The team calls or messages you on WhatsApp to confirm your pickup time.", "A driver collects from your door at the agreed time.", "Every item is tagged, cleaned in our Al Quoz centres and returned ready to wear."],
                        "Need it faster? Message us on WhatsApp", "Hi Dima Laundry, I just booked a pickup on the website."),
    ("en", "quote"): ("/thank-you-quote", "Quote request received", "Thank you. Your commercial laundry request has reached the Dima Laundry commercial team.",
                      ["The commercial team reviews your volumes and needs.", "We contact you within one working day to discuss a schedule and pricing.", "If it helps, we arrange a visit to our Al Quoz processing centres."],
                      "Talk to the commercial team on WhatsApp", "Hi Dima Laundry, I just sent a commercial quote request on the website."),
    ("ar", "booking"): ("/ar/thank-you", "تم استلام طلبك", "شكرا لك. وصل طلب الاستلام إلى فريق ديما لاندري.",
                        ["يتواصل معك الفريق هاتفيا أو عبر واتساب لتأكيد موعد الاستلام.", "يستلم السائق ملابسك من بابك في الموعد المتفق عليه.", "ترقّم كل قطعة وتنظف في مراكزنا في القوز وتعود جاهزة للارتداء."],
                        "تريد ردا أسرع؟ راسلنا على واتساب", "مرحبا ديما لاندري، حجزت استلاما للتو عبر الموقع."),
    ("ar", "quote"): ("/ar/thank-you-quote", "تم استلام طلب عرض السعر", "شكرا لك. وصل طلبك إلى فريق الشركات في ديما لاندري.",
                      ["يراجع فريق الشركات الكميات واحتياجاتك.", "نتواصل معك خلال يوم عمل واحد لمناقشة الجدول والأسعار.", "ويمكننا ترتيب زيارة لمراكز التنظيف في القوز."],
                      "تحدث مع فريق الشركات على واتساب", "مرحبا ديما لاندري، أرسلت طلب عرض سعر للشركات عبر الموقع."),
}


def build_thankyou(B):
    for (lang, kind), (path, h1, lead, steps, wa_label, wa_text) in PAGES.items():
        number = C.BIZ_WA if kind == "quote" else C.WA
        home = B.pfx(lang) + "/"
        back = "Back to the homepage" if lang == "en" else "العودة إلى الرئيسية"
        nxt = "What happens next" if lang == "en" else "ماذا يحدث الآن"
        app_h = "Track your order in the Dima app" if lang == "en" else "تابع طلبك في تطبيق ديما"
        conv = C.ADS_LABEL_QUOTE if kind == "quote" else C.ADS_LABEL_BOOKING
        steps_html = '<ol class="steps">' + "".join(f"<li>{B.esc(s)}</li>" for s in steps) + "</ol>"
        body = (f'<section class="page-hero"><div class="bubbles" data-count="10" aria-hidden="true"></div><div class="wrap">'
                f'<h1>{h1}</h1><div class="answer tag-card"><span class="tag-hole" aria-hidden="true"></span><p>{lead}</p></div>'
                f'<div class="hero-actions"><a class="btn btn-main" href="{B.wa_link(wa_text, number)}">{wa_label}</a><a class="btn btn-line" href="{home}">{back}</a></div></div></section>'
                f'<section class="content"><div class="wrap prose"><h2>{nxt}</h2>{steps_html}'
                + (f'<div class="app-inline"><h2>{app_h}</h2>{B.app_badges(lang=lang)}</div>' if kind == "booking" else "")
                + f'</div></section>'
                f'<div id="conv" hidden data-kind="{kind}" data-label="{conv}"></div>')
        B.write(path, B.shell(path, f"{h1} | Dima Laundry", lead, body, [B.ORG], noindex=True, lang=lang, alt=False), sitemap=False)
