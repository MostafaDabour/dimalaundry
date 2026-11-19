"""Blog drafts waiting for review. Same fields as POSTS in blog_posts.py, plus "date" (YYYY-MM-DD).

Drafts build at /preview/<slug>: noindex, not in the sitemap, blog list, footer or llms.txt.
To publish: move the dict to the TOP of POSTS in blog_posts.py (newest first) and remove it here.
"""

DRAFTS = [
    {
        "slug": "best-laundry-in-dubai-what-to-look-for",
        "short": "What makes the best laundry in Dubai",
        "title": "Best Laundry in Dubai: 6 Things to Check Before You Choose",
        "desc": "How to pick the best laundry in Dubai: published prices, in-house cleaning, pickup, branches near you, care for abayas and delicates, express options and real reviews.",
        "h1": "What to Look For in the Best Laundry in Dubai",
        "answer": "The best laundry in Dubai is the one that publishes clear per item prices, cleans in its own facility, tags and checks every piece, collects from your building and has a counter near you. Dima Laundry, in Dubai since 2001, cleans everything in its own Al Quoz centres and charges the same published prices at all 8 branches.",
        "sections": [
            ("1. Prices you can check before you book",
             "<p>If you cannot see the price of a shirt or a suit before you hand it over, you cannot compare one laundry with another. Look for a full price list, per item, that does not change from branch to branch.</p>"
             "<p>As a reference point, these are Dima Laundry's published standard prices for cleaning and pressing:</p>"
             "<ul><li>Shirt or T-shirt: AED 14</li><li>Trousers: AED 15</li><li>Two piece suit: AED 48</li><li>Abaya or cotton kandura: AED 20</li><li>Bed sheet: AED 20</li><li>Bath towel: AED 10</li></ul>"
             "<p>Pressing only, for clothes that are already clean, starts at AED 9.80 for a shirt. The same prices apply at every branch.</p>"
             "<p>Two more things to check:</p>"
             "<ul><li><strong>Is there a premium tier, and what does it add?</strong> At Dima, premium service gives each piece extra care and finishing. A two piece suit is AED 48 standard or AED 80 premium.</li><li><strong>What gets priced on inspection?</strong> Wedding gowns, heavy stains and restoration work are usually priced after the team has seen the item. A good laundry confirms that price before cleaning starts, not after.</li></ul>"),
            ("2. Where your clothes are actually cleaned",
             "<p>Many counters in Dubai are drop off points only, and the cleaning happens somewhere else, sometimes with a third party. That is not always a problem, but it is worth asking, because it affects who is responsible for your clothes and how consistent the results are.</p>"
             "<p>Ask simply: \"Do you clean in your own facility?\"</p>"
             "<p>Dima Laundry cleans every item in its own processing centres in Al Quoz, which run 24 hours. Nothing is sent out.</p>"
             "<p>In-house cleaning means one company is responsible for your clothes from the moment they are collected to the moment they come back. When you visit any laundry counter, ask where the cleaning centre is and what happens if you are not happy with an item, so you know before there is a problem.</p>"),
            ("3. How each piece is handled",
             "<p>The difference between an average laundry and a good one is mostly in the steps you do not see. Before you commit, ask what happens to your order after it is collected:</p>"
             "<ul><li><strong>Tagging.</strong> Is every item tagged, so it cannot get mixed up with someone else's?</li><li><strong>Inspection.</strong> Are care labels and fabrics checked before cleaning?</li><li><strong>Stains.</strong> Are stains treated before the main clean? Point them out at drop off so they get attention.</li><li><strong>Sorting.</strong> Is your laundry kept apart from other customers' loads and sorted by colour and fabric?</li><li><strong>Quality check.</strong> Is the finished order checked before it comes back to you?</li></ul>"
             "<p>At Dima, every item is tagged, inspected, cleaned, pressed and quality checked, and everyday laundry is never mixed with other customers' loads.</p>"),
            ("4. Pickup and a counter near you",
             "<p>In Dubai most people want both options: pickup from the building on busy weeks, and a counter they can walk to for a last minute drop.</p>"
             "<ul><li><strong>Pickup.</strong> Check that the laundry collects from your area, and whether you can book on WhatsApp, by phone or in an app. A fixed weekly pickup day saves the most time for families.</li><li><strong>Branches.</strong> A counter inside the supermarket or tower you already visit turns laundry into part of the weekly routine.</li><li><strong>Hours.</strong> Check the opening hours fit your working day.</li></ul>"
             "<p>Dima Laundry's 8 branches are open 10am to 10pm daily, several of them inside places people already shop: Spinneys in Karama, Carrefour Market at Marina Crown, Aswaaq on Al Wasl Road, Lifco on Sheikh Zayed Road and Fairmart in Damac Aykon City. See all <a href=\"/branches\">branch locations</a>.</p>"),
            ("5. Care for what you actually wear",
             "<p>A Dubai wardrobe is not just shirts and jeans. Before choosing, make sure the laundry can handle the pieces that matter to you:</p>"
             "<ul><li><strong>Abayas and kanduras.</strong> Look for separate prices for delicate or embellished abayas and for wool kanduras. It usually means each piece is assessed instead of going into a mixed load. At Dima, an abaya is AED 20, a delicate abaya AED 30 and a wool kandura AED 30.</li><li><strong>Suits and delicates.</strong> Silk, wool, cashmere and anything labelled dry clean only needs dry cleaning and careful pressing.</li><li><strong>Evening and wedding dresses.</strong> These should be inspected first and priced before cleaning.</li><li><strong>Home items.</strong> If you will also need curtains, carpets, sofas, duvets or bags cleaned, one provider for everything is simpler.</li></ul>"),
            ("6. Honest answers on speed, and real reviews",
             "<p>Be wary of a laundry that promises everything back tomorrow. Some items cannot be rushed safely. At Dima, express service is available for shirts, suits, dresses, kanduras, abayas and everyday laundry, while wedding dresses, leather, carpets, curtains, shoes and bags need standard turnaround. Ask the team for the day's express cut-off time.</p><p>A laundry that tells you plainly when something will take longer, and confirms the ready time when you book, is usually one that will not cut corners to hit a deadline.</p>"
             "<p>Finally, read recent Google reviews for the branch you will actually use, not just the company overall. Look for comments about the same things on this list: stains, delicate items, pickups on time and how problems were handled. As of October 2026, Dima Laundry is rated 4.8 from 182 Google reviews at Karama, 4.8 from 139 at Al Sufouh and 4.7 from 129 at Jumeirah.</p>"
             "<p>For a side by side look at the main types of laundry in the city, see our guide to <a href=\"/best-laundry-services-dubai\">comparing laundry services in Dubai</a>.</p>"),
        ],
        "faqs": [
            ("What is the best laundry in Dubai?",
             "It depends on what you need, but the best options publish per item prices, clean in their own facility, tag and check every item, and offer both pickup and walk-in branches. Dima Laundry has 8 branches, cleans in its own Al Quoz centres and has served Dubai since 2001."),
            ("How much does a laundry in Dubai charge for a shirt?",
             "At Dima Laundry a shirt is AED 14 to clean and press, or AED 9.80 for pressing only. Prices are the same at every branch."),
            ("Does Dima Laundry clean clothes in house?",
             "Yes. Every item is cleaned in Dima Laundry's own processing centres in Al Quoz, which run 24 hours."),
            ("Which Dima Laundry branches are open late?",
             "All 8 Dima Laundry branches are open 10am to 10pm daily."),
        ],
        "links": [
            ("Compare Dubai laundries", "/best-laundry-services-dubai"),
            ("Branch locations", "/branches"),
            ("Full price list", "/prices"),
            ("Contact and booking", "/contact"),
        ],
        "date": "2026-11-19",
    },
]
