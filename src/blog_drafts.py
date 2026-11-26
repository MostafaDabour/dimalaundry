"""Blog drafts waiting for review. Same fields as POSTS in blog_posts.py, plus "date" (YYYY-MM-DD).

Drafts build at /preview/<slug>: noindex, not in the sitemap, blog list, footer or llms.txt.
To publish: move the dict to the TOP of POSTS in blog_posts.py (newest first) and remove it here.
"""

DRAFTS = [
{
 "slug": "sweat-stains-white-shirts",
 "short": "Sweat stains on white shirts",
 "date": "2026-11-26",
 "title": "How to Remove Sweat Stains and Yellow Marks from White Shirts",
 "desc": "Why white shirts go yellow under the arms and at the collar in Dubai, how to treat sweat stains at home, what to avoid, and when to hand them to a dry cleaner.",
 "h1": "How to Remove Sweat Stains and Yellow Marks from White Shirts",
 "answer": "Treat sweat stains as early as you can. Rinse the area in cool water, work in a stain remover or a paste of baking soda and water, leave it for 30 minutes, then wash. Avoid hot water, the dryer and chlorine bleach until the mark is gone. Dima Laundry treats stains before cleaning, from AED 14 a shirt.",
 "sections": [
  ("Why white shirts turn yellow in Dubai",
   "<p>The yellow patch under the arms is not sweat alone. Sweat mixes with body oils and with the ingredients in deodorant or antiperspirant, and that mix sinks into the cotton. At first you may see nothing. Over days and weeks it builds up, oxidises and turns yellow, and the fabric around it can go stiff.</p>"
   "<p>Dubai makes this happen faster. A short walk from the car park to the office in summer is enough to soak a shirt, and many people wear a work shirt for a full day in and out of air conditioning. Collars and cuffs pick up the same mix of sweat and skin oils, which is why they go grey or yellow long before the rest of the shirt.</p>"
   "<p>The key point: a fresh sweat mark is easy to remove. A mark that has been washed and dried several times without being treated is much harder, because heat sets it into the fibres.</p>"),
  ("How to treat sweat stains at home",
   "<p>Check the care label first. These steps are for washable cotton and cotton blend shirts. If the label says dry clean only, skip to the last section.</p>"
   "<ol><li><strong>Rinse from the back.</strong> Turn the shirt inside out and run cool water through the stained area to flush out fresh sweat.</li>"
   "<li><strong>Apply a treatment.</strong> Use a laundry stain remover, a little liquid detergent, or a paste of baking soda and water. Work it gently into the stain with your fingers or a soft brush.</li>"
   "<li><strong>Give it time.</strong> Leave it for about 30 minutes. For older marks, soak the shirt in cool water with an oxygen based stain remover, following the instructions on the pack.</li>"
   "<li><strong>Wash as normal.</strong> Wash with other whites only, at the temperature the label allows.</li>"
   "<li><strong>Check before drying.</strong> Look at the underarms and collar while the shirt is still wet. If the mark is still there, repeat the treatment. Do not put it in the dryer or iron it yet.</li></ol>"
   "<p>White vinegar diluted in water is another common home option for underarm marks. Test any treatment on an inside seam first, and never mix vinegar or other products with bleach.</p>"),
  ("What to avoid",
   "<ul><li><strong>Chlorine bleach on yellow marks.</strong> It can react with sweat and deodorant residue and make the yellow darker. It can also weaken cotton over time.</li>"
   "<li><strong>Hot water before the stain is out.</strong> Heat helps set sweat marks. Start cool.</li>"
   "<li><strong>The dryer and the iron.</strong> Both apply heat directly to the stain. Air dry until you are sure it has gone.</li>"
   "<li><strong>Hard scrubbing.</strong> It roughens the fabric and can leave a fuzzy patch. Work the treatment in gently.</li>"
   "<li><strong>Mixing whites with colours.</strong> A white shirt washed with darker clothes slowly turns grey, which makes any yellow mark look worse.</li>"
   "<li><strong>Drying in strong sun for hours.</strong> Dubai sun is harsh. A few hours on a hot balcony can yellow some fabrics, so dry whites in the shade where your building allows it.</li></ul>"),
  ("How to stop the marks coming back",
   "<ul><li><strong>Let deodorant dry.</strong> Give it a minute or two before you put the shirt on, so less of it transfers to the fabric.</li>"
   "<li><strong>Use less product.</strong> A thick layer of antiperspirant leaves more residue in the shirt. Some people find switching products helps.</li>"
   "<li><strong>Wear an undershirt.</strong> A thin cotton undershirt takes most of the sweat before it reaches your shirt, and is cheaper to replace.</li>"
   "<li><strong>Wash after every wear.</strong> In Dubai heat, a shirt worn once has already picked up sweat at the collar and underarms, even if it looks clean.</li>"
   "<li><strong>Do not leave worn shirts in the basket for days.</strong> The longer sweat sits in the fabric, the harder it is to remove. If you cannot wash soon, at least rinse the underarms.</li>"
   "<li><strong>Pre-treat collars and cuffs every time.</strong> A little detergent rubbed into the collar line before each wash stops the grey ring from building up.</li></ul>"
   "<p>For more on keeping whites bright, see our guide to <a href='/blog/how-to-keep-kanduras-white'>keeping kanduras white</a>. The same habits work for white shirts.</p>"),
  ("When to hand it to a dry cleaner",
   "<p>Some shirts are better left to a professional:</p>"
   "<ul><li>Shirts labelled dry clean only, or made of silk, linen blends or fine cotton you do not want to risk.</li>"
   "<li>Marks that have been through the wash and the dryer several times.</li>"
   "<li>Good work shirts you need looking sharp every week, with no time to soak and repeat.</li></ul>"
   "<p>At Dima Laundry, stains are treated before the main clean, and whites are kept apart from colours. Every item is tagged, inspected, cleaned, pressed and quality checked in Dima's own Al Quoz centres. Fresh stains have the best chance of full removal, so bring stained shirts in as soon as you can and point the marks out at drop off or when you book a pickup. Light yellowing often improves with professional treatment. Old, set stains may not fully come out, and the team will tell you what to expect.</p>"
   "<p>Prices for a shirt or blouse:</p>"
   "<ul><li>Shirt, cleaned and pressed: AED 14, or AED 20 with premium service</li>"
   "<li>Blouse or top: AED 15</li>"
   "<li>Undershirt: AED 10</li>"
   "<li>Pressing only, for shirts you have already washed: AED 9.80</li></ul>"
   "<p>You can drop shirts at any of the 8 branches, open 10am to 10pm daily, or book a pickup on WhatsApp on +971 50 639 8093. Express service is available if you need a shirt back quickly. Ask the team for today's cut-off time. See <a href='/services/dry-cleaning'>dry cleaning</a>, <a href='/services/wash-and-fold'>everyday laundry</a> or the <a href='/prices'>full price list</a>.</p>"),
 ],
 "faqs": [
  ("Can yellow sweat stains be removed from white shirts?", "Often, yes. Fresh marks usually come out with a cool rinse, a stain remover and a normal wash. Older marks that have been dried with heat are harder, and may only fade. Light yellowing often improves with professional treatment."),
  ("Does bleach remove sweat stains?", "Chlorine bleach is not a good choice for yellow underarm marks. It can react with sweat and deodorant residue and make the stain darker. An oxygen based stain remover is a gentler option for white cotton."),
  ("Why do my white shirts go yellow even after washing?", "Sweat, body oils and deodorant build up in the fabric when stains are not treated before washing, and heat from the dryer or iron sets them. Pre-treat the underarms and collar every time and air dry until the marks are gone."),
  ("How much does Dima Laundry charge to clean a shirt?", "A shirt is AED 14 to clean and press at Dima Laundry, or AED 20 with premium service. Pressing only is AED 9.80. Prices are the same at every branch."),
 ],
 "links": [("Dry cleaning", "/services/dry-cleaning"), ("Everyday laundry", "/services/wash-and-fold"), ("Keeping kanduras white", "/blog/how-to-keep-kanduras-white"), ("Full price list", "/prices")],
},
]
