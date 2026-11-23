"""Blog drafts waiting for review. Same fields as POSTS in blog_posts.py, plus "date" (YYYY-MM-DD).

Drafts build at /preview/<slug>: noindex, not in the sitemap, blog list, footer or llms.txt.
To publish: move the dict to the TOP of POSTS in blog_posts.py (newest first) and remove it here.
"""

DRAFTS = [
{
 'slug': 'laundry-pickup-and-delivery-dubai',
 'short': 'Laundry pickup and delivery: how it works',
 'date': '2026-11-23',
 'title': 'Laundry Pickup and Delivery in Dubai: How It Works',
 'desc': 'How laundry pickup and delivery works in Dubai: how to book, what happens after collection, per item prices, express options, weekly pickups and the areas Dima Laundry covers.',
 'h1': 'Laundry Pickup and Delivery in Dubai: How It Works',
 'answer': 'Laundry pickup and delivery in Dubai works in four steps: you book on WhatsApp, by phone, online or in an app, a driver collects from your home or office, the clothes are cleaned and pressed, and they come back to your door. Dima Laundry collects across Dubai and cleans every item in its own Al Quoz centres.',
 'sections': [
  ('How pickup and delivery works, step by step',
   '<p>Most Dubai laundries that collect follow the same basic pattern. At Dima Laundry it looks like this:</p>'
   '<ol><li><strong>Book.</strong> Schedule a pickup online, on WhatsApp, by phone or in the Dima app.</li>'
   '<li><strong>We collect.</strong> The team collects your laundry from your home or workplace. In towers, that can be from your lobby or concierge.</li>'
   '<li><strong>We clean.</strong> Every item is tagged, inspected, cleaned, pressed and quality checked in Dima\'s own Al Quoz centres. Nothing is sent out to a third party.</li>'
   '<li><strong>We deliver.</strong> Your clothes come back clean and ready to wear.</li></ol>'
   '<p>You do not need to sort anything before the driver arrives. Everyday laundry is sorted by colour and fabric at the centre and never mixed with other customers\' loads.</p>'),
  ('How to book a pickup',
   '<p>Use whichever channel is easiest for you:</p>'
   '<ul><li><strong>WhatsApp:</strong> +971 50 639 8093. This is the quickest way to book and to ask about express cut-off times.</li>'
   '<li><strong>Phone:</strong> 800 DIMA (3462).</li>'
   '<li><strong>App:</strong> the Dima Laundry app is on the App Store and Google Play.</li>'
   '<li><strong>Online:</strong> through the <a href="/contact">contact and booking page</a>.</li></ul>'
   '<p>When you book, it helps to say:</p>'
   '<ul><li>Your building name, tower and flat or villa number, and whether the driver should collect from you or from reception.</li>'
   '<li>Roughly what is in the bag: everyday laundry, suits, abayas, bed linen or something delicate.</li>'
   '<li>Any stains you want treated, so the team can point them out at intake.</li>'
   '<li>Whether you need anything back by a certain day.</li></ul>'
   '<p>For retail order support after booking, you can also email retail.support@dimalaundry.com.</p>'),
  ('What it costs',
   '<p>Dima Laundry charges per item, from a published price list that is the same at every branch. That means you can work out roughly what a bag will cost before the driver arrives. If you have a question about your pickup order, ask the team when you book.</p>'
   '<p>Some standard prices for cleaning and pressing:</p>'
   '<ul><li>Shirt or T-shirt: AED 14</li><li>Trousers: AED 15</li><li>Two piece suit: AED 48</li>'
   '<li>Abaya or kandura: AED 20</li><li>Bed sheet: AED 20</li><li>Duvet cover: AED 40</li><li>Bath towel: AED 10</li></ul>'
   '<p>If your clothes are already washed and only need pressing, pressing starts at AED 9.80 for a shirt. Premium service, with extra care and finishing for each piece, is priced separately. A two piece suit is AED 80 on premium.</p>'
   '<p>Pickup is not only for clothes. You can add alterations to a laundry pickup, with minor alterations from AED 40 and fitting alterations from AED 60. Carpets and rugs can also be collected and delivered, from AED 30 per square metre. See the <a href="/prices">full price list</a> for every item.</p>'
   '<p>If you are not sure how an item will be priced, such as a wedding gown or a piece with heavy stains, ask the team before collection. Wedding gowns are inspected first and the price is confirmed before any cleaning starts.</p>'),
  ('Weekly pickups and express',
   '<p>There are two ways people in Dubai usually use pickup and delivery.</p>'
   '<p><strong>A fixed weekly pickup.</strong> You choose a fixed day and time and Dima Laundry collects every week. This suits families with a steady flow of school clothes, work shirts, bed linen and towels, and anyone who would rather not think about laundry at all. You leave the bag out, and it comes back.</p>'
   '<p><strong>Express when it cannot wait.</strong> For a suit before a meeting, an interview or an event, express service is available for pickup or for drop off at any branch. Express covers:</p>'
   '<ul><li>Shirts, trousers and suits</li><li>Dresses and blouses</li><li>Kanduras and abayas</li><li>Everyday laundry</li></ul>'
   '<p>Message the team on WhatsApp for today\'s express cut-off time and price, and book as early in the day as you can. Some items cannot be rushed safely: wedding dresses, leather, carpets, curtains, shoes and bags need standard turnaround. Carpets and rugs also need time to dry fully, and the team confirms the return date when collecting. More detail is on the <a href="/services/express-laundry">express laundry page</a>.</p>'),
  ('Which areas are covered',
   '<p>Dima Laundry has 8 branches, open 10am to 10pm daily, and each one arranges pickup and delivery for the communities around it. These are some of the areas covered:</p>'
   '<ul><li><strong>Dubai Marina and JBR:</strong> Marina towers, JBR, Dubai Harbour, Bluewaters, Emaar Beachfront and JLT.</li>'
   '<li><strong>Al Sufouh:</strong> Al Sufouh 1 and 2, Knowledge Park, Media City, Internet City and Palm Jumeirah.</li>'
   '<li><strong>Jumeirah:</strong> Jumeirah 1, 2 and 3, Al Wasl, Umm Suqeim, Al Safa, City Walk and La Mer.</li>'
   '<li><strong>Downtown and Business Bay:</strong> Downtown Dubai, Business Bay, DIFC, Za\'abeel and Dubai Design District.</li>'
   '<li><strong>Sheikh Zayed Road:</strong> the Sheikh Zayed Road towers, Trade Centre, Satwa and Al Jafiliya.</li>'
   '<li><strong>Karama:</strong> Karama, Al Mankhool, Oud Metha, Bur Dubai and Umm Hurair.</li>'
   '<li><strong>Damac Aykon City:</strong> Aykon City residents, plus Business Bay, Al Wasl and Al Safa.</li></ul>'
   '<p>If your area is not listed, message the team on WhatsApp and ask. Offices are covered too, and many people book a collection from work rather than home. See all <a href="/branches">branch locations</a>.</p>'),
  ('Tips for a smooth pickup',
   '<ul><li><strong>Check pockets.</strong> Pens, coins and tissues can damage clothes in the wash.</li>'
   '<li><strong>Separate the delicate pieces.</strong> Put silk, embellished abayas and anything labelled dry clean only in their own bag and mention them when you book.</li>'
   '<li><strong>Point out stains.</strong> Tell the team what the stain is if you know. Stains are treated before the main clean, and fresh ones come out more easily than old ones.</li>'
   '<li><strong>Leave clear instructions for the building.</strong> If the driver collects from reception or the concierge, let them know a laundry pickup is coming.</li>'
   '<li><strong>Plan around busy weeks.</strong> Demand for abayas and kanduras peaks before Ramadan and Eid, so book a few days early in those weeks.</li>'
   '<li><strong>Confirm the ready time.</strong> For anything you need on a certain day, ask the team to confirm when it will be back before you hand it over.</li></ul>'),
 ],
 'faqs': [
  ('Does Dima Laundry offer pickup and delivery in Dubai?', 'Yes. Dima Laundry collects from homes and workplaces across Dubai, cleans everything in its own Al Quoz centres and delivers it back. Book on WhatsApp, by phone, online or in the Dima app.'),
  ('How much does laundry pickup cost in Dubai?', 'Dima Laundry charges per item from a published price list that is the same at every branch, for example AED 14 for a shirt and AED 48 for a two piece suit. Ask the team when you book if you have a question about your order.'),
  ('Can I set up a weekly laundry pickup?', 'Yes. Choose a fixed day and time and Dima Laundry collects every week.'),
  ('Can I get same day laundry with pickup?', 'Express service is available with pickup. Message the team on WhatsApp for today\'s cut-off time and price, and book as early in the day as you can.'),
 ],
 'links': [('Contact and booking', '/contact'), ('Express laundry', '/services/express-laundry'), ('Full price list', '/prices'), ('Branch locations', '/branches')],
}
]
