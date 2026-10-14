"""Privacy policy and terms of service, English and Arabic.

Policy numbers below are industry standard defaults. Dima management must confirm them before launch.
"""
import content as C

CLAIM_HOURS = 48          # time to report a problem after delivery
LIABILITY_TIMES = 10      # compensation cap, times the cleaning charge of the item
UNCLAIMED_DAYS = 90       # days before uncollected items may be donated or disposed of

EN_PRIVACY = [
    ("Who we are", f"Dima Laundry LLC (\"Dima Laundry\", \"we\") runs laundry and dry cleaning services in Dubai, United Arab Emirates. Our head office is at {C.HQ_ADDRESS}, Dubai. For any privacy question, email {C.EMAIL} or call {C.TOLL}."),
    ("What this policy covers", "This policy explains how we collect and use personal data when you visit dimalaundry.com, fill in a form, contact us on WhatsApp or by phone, use the Dima Laundry app, or use our branches. We handle personal data in line with the UAE Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)."),
    ("Data we collect", "Name, phone number, email address, pickup and delivery address, area, order details and preferences, payment status, messages you send us, and for business customers your company name and contact details. When you browse the website we may collect technical data such as pages visited, device and browser type, and approximate location, through cookies and similar tools."),
    ("How we use it", "To arrange pickups and deliveries, process and track your orders, contact you about your order, answer questions and quotes, take payment, improve our services and website, and, only where you have agreed, send you offers. We do not sell your personal data."),
    ("Who we share it with", "Service providers who help us run the business and are bound to protect your data: our customer management system (GoHighLevel), our ordering and app platform (CleanCloud), website hosting and security (Cloudflare), messaging (WhatsApp, operated by Meta), and website analytics and maps (Google). We may also share data where the law requires it."),
    ("Where your data is stored", "Some of these providers store data outside the UAE. Where that happens we rely on the safeguards allowed under UAE law."),
    ("How long we keep it", "We keep order and customer records for as long as you use our services and for the period required by UAE law for accounting and tax purposes. Form enquiries that do not lead to an order are deleted after 24 months."),
    ("Your rights", f"You can ask to see the personal data we hold about you, correct it, delete it, restrict or object to how we use it, or withdraw consent to marketing at any time. Email {C.EMAIL} and we will reply within 30 days."),
    ("Cookies", "The website uses essential cookies to work properly and, where enabled, analytics cookies to understand how it is used. You can block cookies in your browser settings. Some features may not work without them."),
    ("Changes to this policy", "We may update this policy. The date at the bottom shows when it last changed."),
]

EN_TERMS = [
    ("About these terms", f"These terms apply to every order placed with Dima Laundry LLC, at a branch, by phone, on WhatsApp, on the website or in the Dima Laundry app. By placing an order you accept them."),
    ("Prices and payment", "Prices follow our published price list, which is the same at every branch. Specialist items, heavy stains, restoration work and unusual garments are priced after inspection, and we confirm the price before cleaning. Payment is due on collection or delivery unless you have a commercial account."),
    ("Care labels and inspection", "We inspect every item at intake and follow the manufacturer's care label. If an item has no label, a damaged label, or a label we believe is wrong, we will clean it at the customer's risk or ask you first. Please tell us about stains, delicate trims and anything special when you hand items over."),
    ("Pockets and valuables", "Please empty all pockets. We are not responsible for money, jewellery, documents, electronics or other items left in garments."),
    ("Things we cannot guarantee", "Some stains, colour loss, shrinkage, fabric wear, loose buttons and trims, and faults in the garment's manufacture cannot be fully prevented or removed. We will always do our best and tell you if we see a risk before cleaning."),
    ("Problems with an order", f"Please check your order when it arrives and report any problem within {CLAIM_HOURS} hours with photos, keeping the item as returned. We will inspect it and, where we are at fault, re-clean it free of charge or offer compensation."),
    ("Compensation limit", f"If an item is lost or damaged through our fault, our liability is limited to {LIABILITY_TIMES} times the cleaning charge for that item, or the item's depreciated value if lower. We are not liable for indirect losses."),
    ("Pickup and delivery", "We collect and deliver at the times agreed when you book. Please make sure someone is available or leave clear instructions. Delivery times are estimates and can change at busy times such as before Eid."),
    ("Uncollected items", f"Items not collected within {UNCLAIMED_DAYS} days of the ready date may be donated or disposed of after we have tried to contact you."),
    ("Commercial accounts", "Commercial customers are covered by their service agreement, which takes priority over these terms where the two differ."),
    ("Governing law", "These terms are governed by the laws of the Emirate of Dubai and the United Arab Emirates. Disputes go to the courts of Dubai."),
    ("Contact", f"Questions about these terms: {C.EMAIL} or {C.TOLL}."),
]

AR_PRIVACY = [
    ("من نحن", f"ديما لاندري ذ.م.م (\"ديما لاندري\" أو \"نحن\") تقدم خدمات الغسيل والتنظيف الجاف في دبي، الإمارات العربية المتحدة. يقع مكتبنا الرئيسي في شارع 24a رقم 22، القوز الصناعية 3، دبي. لأي استفسار عن الخصوصية راسلنا على {C.EMAIL} أو اتصل على {C.TOLL}."),
    ("نطاق هذه السياسة", "توضح هذه السياسة كيف نجمع بياناتك الشخصية ونستخدمها عند زيارة موقع dimalaundry.com أو تعبئة أحد النماذج أو التواصل معنا عبر واتساب أو الهاتف أو استخدام تطبيق ديما لاندري أو زيارة فروعنا. نتعامل مع البيانات الشخصية وفق قانون حماية البيانات الشخصية في دولة الإمارات (المرسوم بقانون اتحادي رقم 45 لسنة 2021)."),
    ("البيانات التي نجمعها", "الاسم ورقم الهاتف والبريد الإلكتروني وعنوان الاستلام والتوصيل والمنطقة وتفاصيل الطلبات وتفضيلاتك وحالة الدفع والرسائل التي ترسلها إلينا، وبالنسبة للشركات اسم الشركة وبيانات التواصل. وعند تصفح الموقع قد نجمع بيانات تقنية مثل الصفحات التي زرتها ونوع الجهاز والمتصفح والموقع التقريبي من خلال ملفات تعريف الارتباط وأدوات مشابهة."),
    ("كيف نستخدمها", "لترتيب الاستلام والتوصيل، وتنفيذ طلباتك وتتبعها، والتواصل معك بشأن طلبك، والرد على الاستفسارات وطلبات الأسعار، وتحصيل المدفوعات، وتحسين خدماتنا وموقعنا، وإرسال العروض فقط إذا وافقت على ذلك. نحن لا نبيع بياناتك الشخصية."),
    ("مع من نشاركها", "مع مزودي خدمات يساعدوننا في إدارة العمل وملزمين بحماية بياناتك: نظام إدارة العملاء (GoHighLevel)، ومنصة الطلبات والتطبيق (CleanCloud)، واستضافة الموقع وحمايته (Cloudflare)، والمراسلة (واتساب التابع لشركة Meta)، وتحليلات الموقع والخرائط (Google). وقد نشارك البيانات عندما يلزمنا القانون بذلك."),
    ("أين تحفظ بياناتك", "يحفظ بعض هؤلاء المزودين البيانات خارج الإمارات، وفي هذه الحالة نعتمد على الضمانات التي يسمح بها القانون الإماراتي."),
    ("مدة الاحتفاظ", "نحتفظ بسجلات الطلبات والعملاء طوال مدة استخدامك لخدماتنا وللمدة التي يتطلبها القانون الإماراتي لأغراض المحاسبة والضرائب. أما استفسارات النماذج التي لا ينتج عنها طلب فتحذف بعد 24 شهرا."),
    ("حقوقك", f"يحق لك طلب الاطلاع على بياناتك الشخصية لدينا أو تصحيحها أو حذفها أو تقييد استخدامها أو الاعتراض عليه، أو سحب موافقتك على الرسائل التسويقية في أي وقت. راسلنا على {C.EMAIL} وسنرد خلال 30 يوما."),
    ("ملفات تعريف الارتباط", "يستخدم الموقع ملفات تعريف ارتباط أساسية ليعمل بشكل صحيح، وملفات تحليلية عند تفعيلها لفهم طريقة استخدامه. يمكنك حظرها من إعدادات المتصفح، وقد لا تعمل بعض الخصائص بدونها."),
    ("التعديلات", "قد نحدّث هذه السياسة، ويظهر تاريخ آخر تحديث في أسفل الصفحة."),
]

AR_TERMS = [
    ("حول هذه الشروط", "تسري هذه الشروط على كل طلب يقدم إلى ديما لاندري ذ.م.م سواء في الفرع أو عبر الهاتف أو واتساب أو الموقع أو تطبيق ديما لاندري، وتقديمك للطلب يعني موافقتك عليها."),
    ("الأسعار والدفع", "تطبق الأسعار حسب قائمة الأسعار المنشورة وهي موحدة في جميع الفروع. القطع الخاصة والبقع الصعبة وأعمال الترميم والملابس غير المعتادة تسعّر بعد الفحص، ونؤكد لك السعر قبل البدء بالتنظيف. يستحق الدفع عند الاستلام أو التوصيل ما لم يكن لديك حساب للشركات."),
    ("بطاقات العناية والفحص", "نفحص كل قطعة عند الاستلام ونتبع تعليمات بطاقة العناية من الشركة المصنعة. إذا لم تكن على القطعة بطاقة أو كانت تالفة أو نعتقد أنها غير صحيحة، فإما ننظفها على مسؤولية العميل أو نسألك أولا. يرجى إخبارنا بالبقع والزينة الحساسة وأي ملاحظات خاصة عند تسليم الملابس."),
    ("الجيوب والأغراض الثمينة", "يرجى إفراغ جميع الجيوب، فنحن غير مسؤولين عن النقود أو المجوهرات أو المستندات أو الأجهزة أو أي أغراض تترك داخل الملابس."),
    ("ما لا يمكننا ضمانه", "بعض البقع وبهتان الألوان والانكماش وتآكل القماش وارتخاء الأزرار والزينة وعيوب التصنيع لا يمكن منعها أو إزالتها بالكامل. نبذل دائما أقصى جهدنا ونخبرك مسبقا إذا لاحظنا أي خطر قبل التنظيف."),
    ("المشاكل في الطلب", f"يرجى فحص طلبك عند وصوله وإبلاغنا بأي مشكلة خلال {CLAIM_HOURS} ساعة مع الصور، مع الاحتفاظ بالقطعة كما سلّمت. سنفحصها وإذا كان الخطأ من جهتنا نعيد تنظيفها مجانا أو نقدم تعويضا."),
    ("حد التعويض", f"في حال فقدان قطعة أو تلفها بسبب خطأ منا، تكون مسؤوليتنا بحد أقصى {LIABILITY_TIMES} أضعاف رسوم تنظيف تلك القطعة، أو القيمة المستهلكة للقطعة إذا كانت أقل. ولا نتحمل أي خسائر غير مباشرة."),
    ("الاستلام والتوصيل", "نستلم ونوصل في المواعيد المتفق عليها عند الحجز. يرجى التأكد من وجود شخص لاستلام الطلب أو ترك تعليمات واضحة. مواعيد التوصيل تقديرية وقد تتغير في أوقات الذروة مثل ما قبل العيد."),
    ("القطع غير المستلمة", f"القطع التي لا تستلم خلال {UNCLAIMED_DAYS} يوما من تاريخ جاهزيتها قد يتم التبرع بها أو التخلص منها بعد محاولتنا التواصل معك."),
    ("حسابات الشركات", "يخضع عملاء الشركات لاتفاقية الخدمة الخاصة بهم، والتي تقدم على هذه الشروط عند وجود أي اختلاف."),
    ("القانون المطبق", "تخضع هذه الشروط لقوانين إمارة دبي ودولة الإمارات العربية المتحدة، وتختص محاكم دبي بالنظر في أي نزاع."),
    ("التواصل", f"لأي استفسار حول هذه الشروط: {C.EMAIL} أو {C.TOLL}."),
]


def build_legal(B):
    for lang, pages in (("en", [("privacy", "Privacy Policy", EN_PRIVACY, "How Dima Laundry collects, uses and protects your personal data, in line with UAE data protection law."),
                                ("terms", "Terms of Service", EN_TERMS, "Terms for laundry and dry cleaning orders with Dima Laundry LLC, Dubai: prices, care labels, claims and compensation.")]),
                        ("ar", [("privacy", "سياسة الخصوصية", AR_PRIVACY, "كيف تجمع ديما لاندري بياناتك الشخصية وتستخدمها وتحميها وفق قانون حماية البيانات في الإمارات."),
                                ("terms", "شروط الخدمة", AR_TERMS, "شروط طلبات الغسيل والتنظيف الجاف لدى ديما لاندري في دبي: الأسعار وبطاقات العناية والمطالبات والتعويض.")])):
        for slug, title, sections, desc in pages:
            path = B.pfx(lang) + "/" + slug
            alt = ("/ar/" + slug) if lang == "en" else ("/" + slug)
            ch, cs = B.crumbs(path, title, lang)
            body = "".join(f"<h2>{B.esc(h)}</h2><p>{B.esc(t)}</p>" for h, t in sections)
            page = (f'<section class="page-hero"><div class="wrap">{ch}<h1>{title}</h1></div></section>'
                    f'<section class="content"><div class="wrap prose">{body}{B.updated(lang)}</div></section>')
            B.write(path, B.shell(path, f"{title} | Dima Laundry" if lang == "en" else f"{title} | ديما لاندري", desc, page, [B.ORG, cs], lang=lang, alt=alt))
