"""Blog drafts waiting for review. Same fields as POSTS in blog_posts.py, plus "date" (YYYY-MM-DD).

Drafts build at /preview/<slug>: noindex, not in the sitemap, blog list, footer or llms.txt.
To publish: move the dict to the TOP of POSTS in blog_posts.py (newest first) and remove it here.
"""

DRAFTS = [
{'slug': 'carpet-cleaning-price-dubai',
 'short': 'Carpet cleaning prices',
 'date': '2026-11-09',
 'title': 'Carpet Cleaning Prices in Dubai: What Affects the Cost',
 'desc': 'What carpet and rug cleaning costs in Dubai per square metre, how to work out the price for your rug, what changes the cost and how to keep it down.',
 'h1': 'Carpet Cleaning Prices in Dubai: What Affects the Cost',
 'answer': 'Carpet cleaning in Dubai is priced by size and material. At Dima Laundry a standard machine made carpet costs AED 30 per square metre, handmade and wool rugs AED 40 per square metre, and '
           'leather rugs AED 50 per square metre. A 2 by 3 metre machine made rug is 6 square metres, so it costs AED 180 to clean.',
 'sections': [('Carpet and rug cleaning prices',
               "<p>Carpets are priced per square metre, not per piece, so a small bedside rug costs far less than a large living room carpet. These are Dima Laundry's published "
               'rates:</p><ul><li>Carpet, machine made: AED 30 per sq m</li><li>Carpet, handmade: AED 40 per sq m</li><li>Carpet, wool: AED 40 per sq m</li><li>Carpet, leather: AED 50 per sq '
               'm</li></ul><p>Carpets are cleaned on a single standard service. There is no separate premium tier for rugs, so the rate above is the rate you pay for that type of carpet. You can see '
               'these alongside curtains and other home fabrics on the full <a href="/prices">price list</a>.</p>'),
              ('How to work out the cost of your rug',
               '<p>The sum is simple: length in metres, times width in metres, times the rate for your type of carpet.</p><ol><li>Measure the length and width of the rug in metres.</li><li>Multiply '
               "them to get the area in square metres.</li><li>Multiply the area by the rate for the material.</li></ol><p>Some examples using Dima Laundry's rates:</p><ul><li>A 1.5 by 2 metre "
               'machine made rug is 3 sq m. At AED 30, that is AED 90.</li><li>A 2 by 3 metre machine made rug is 6 sq m. At AED 30, that is AED 180.</li><li>A 2 by 3 metre handmade or wool rug is 6 '
               'sq m. At AED 40, that is AED 240.</li><li>A 2 by 3 metre leather rug is 6 sq m. At AED 50, that is AED 300.</li></ul><p>Round, oval and odd shaped rugs are less obvious to measure. '
               'If yours is not a rectangle, send the measurements or a photo on WhatsApp and ask the team how they will measure it before you book.</p>'),
              ('What affects the price',
               '<p>Two things set the price of carpet cleaning: how big the carpet is and what it is made of.</p><p><strong>Size.</strong> Because the rate is per square metre, doubling the area '
               'doubles the price. A runner for a hallway and a large carpet for a majlis are priced on the same rate, but the larger one costs more because there is more of it to '
               'clean.</p><p><strong>Material and construction.</strong> Machine made carpets are the most common in Dubai apartments and are at the lowest rate, AED 30. Handmade rugs, including '
               'Persian rugs, and wool rugs are AED 40, because they need a more careful hand. Leather rugs are AED 50.</p><p>If you are not sure what your rug is made of, check the label on the '
               'back or ask the team when they collect it. If a rug has heavy stains, damage or fragile areas, mention it when you book so the team can tell you what to expect.</p>'),
              ('What the price covers',
               '<p>Dima Laundry cleans carpets at its own centres in Al Quoz rather than on your floor. That matters in Dubai, where fine sand and dust work their way deep into the pile and are hard '
               'to lift out with a vacuum alone. Each carpet is:</p><ul><li>Dusted to remove sand from deep in the pile</li><li>Deep washed and stain treated</li><li>Handled with care if it is '
               'handmade or wool</li><li>Fully dried before it comes back to you</li></ul><p>Pickup and delivery are available across Dubai, so you do not need to fit a rolled up rug into a taxi. '
               'Book online, on WhatsApp, by phone on 800 DIMA (3462) or in the Dima app.</p><p>If you would rather have a sofa or mattress cleaned at home, that is a different service, and you can '
               'find it on the <a href="/services/sofa-cleaning">sofa and mattress cleaning</a> page.</p>'),
              ('How long it takes and when to book',
               '<p>Rugs need time to dry fully, so carpet cleaning is not an express service. Carpets, curtains, leather and similar items always go through standard turnaround because they cannot '
               'be rushed safely. The team confirms the return date when they collect your carpet.</p><p>That means it pays to plan ahead. If you need a carpet back for guests, for Eid or before '
               'handing back an apartment, book well before the date rather than in the last few days.</p><p>As for how often: every 6 to 12 months suits most Dubai homes. Clean more often if you '
               'have children or pets, or if your balcony doors are open a lot and sand blows in.</p>'),
              ('How to keep the cost down',
               '<ul><li>Measure before you book so you know the price in advance and there are no surprises.</li><li>Vacuum regularly between cleans. It slows down the build up of sand in the '
               'pile.</li><li>Deal with spills quickly by blotting, not rubbing, and point out any stains when the rug is collected.</li><li>Send several rugs in one pickup, and add curtains or '
               'other home fabrics to the same order if they are due too.</li><li>Use a rug under heavy traffic areas, such as the entrance or under a dining table, so your larger carpet needs '
               'cleaning less often.</li></ul><p>For any rug that is unusual, very old or very valuable, ask the team before you book. They will tell you whether it can be cleaned and which rate '
               'applies.</p>')],
 'faqs': [('How much is carpet cleaning per square metre in Dubai?', 'At Dima Laundry, machine made carpets are AED 30 per square metre, handmade and wool rugs AED 40, and leather rugs AED 50.'),
          ('How much does it cost to clean a 2 by 3 metre rug?',
           'A 2 by 3 metre rug is 6 square metres. At Dima Laundry that is AED 180 for a machine made rug, AED 240 for a handmade or wool rug and AED 300 for a leather rug.'),
          ('Can I get my carpet cleaned the same day?', 'No. Carpets need time to dry fully, so they go through standard turnaround. The team confirms the return date when they collect it.'),
          ('Do you collect carpets from home?', 'Yes. Dima Laundry offers pickup and delivery across Dubai. Book online, on WhatsApp, by phone or in the Dima app.')],
 'links': [('Carpet and rug cleaning', '/services/carpet-cleaning'), ('Full price list', '/prices'), ('Curtain cleaning', '/services/curtain-cleaning'), ('Contact and booking', '/contact')]},
]
