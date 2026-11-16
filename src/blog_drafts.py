"""Blog drafts waiting for review. Same fields as POSTS in blog_posts.py, plus "date" (YYYY-MM-DD).

Drafts build at /preview/<slug>: noindex, not in the sitemap, blog list, footer or llms.txt.
To publish: move the dict to the TOP of POSTS in blog_posts.py (newest first) and remove it here.
"""

DRAFTS = [
{'slug': 'curtain-cleaning-dubai-home-or-laundry',
 'short': 'Curtain cleaning: home or laundry',
 'date': '2026-11-16',
 'title': 'Curtain Cleaning in Dubai: At Home or at the Laundry?',
 'desc': 'Should you get your curtains cleaned at home or sent to the laundry? Prices per square metre in Dubai, how to work out the cost, and which option suits which curtains.',
 'h1': 'Curtain Cleaning in Dubai: At Home or at the Laundry?',
 'answer': 'Both work. Cleaning at the laundry suits curtains that are very dirty, stained or easy to take down, while on-site cleaning at home costs less and means the curtains stay up. '
           'Dima Laundry prices curtains per square metre: chiffon AED 12, standard AED 15 and blackout AED 20 at the centre, or AED 8, AED 12 and AED 15 on site.',
 'sections': [('Why curtains in Dubai need regular cleaning',
               '<p>Curtains are one of the largest areas of fabric in a home, and in Dubai they work hard.</p><ul><li><strong>Dust and sand.</strong> Fine dust comes in through windows, balcony '
               'doors and the air conditioning, and the folds of a curtain hold on to it.</li><li><strong>Sun.</strong> Curtains and blackouts sit between the room and strong sunlight most of the '
               'year, which dries out fabric and linings.</li><li><strong>Humidity and cooking.</strong> On humid days and in open plan kitchens, smells cling to curtain fabric and stay '
               'there.</li></ul><p>A good rule for most homes is a professional clean every 6 to 12 months. Go for the shorter gap if your windows face a busy road or construction, you cook with '
               'strong spices near the curtains, or someone in the house has a lot of dust sensitivity.</p>'),
              ('Curtain cleaning prices in Dubai',
               "<p>Curtains are priced by the square metre of fabric, so the size and type of curtain decide the cost. These are Dima Laundry's published rates:</p><ul><li>Chiffon and sheer: AED 12 "
               'per sq m at the centre, AED 8 per sq m on site</li><li>Standard curtains: AED 15 per sq m at the centre, AED 12 per sq m on site</li><li>Blackout curtains: AED 20 per sq m at the '
               'centre, AED 15 per sq m on site</li><li>Chair covers: AED 20 at the centre, AED 15 on site</li><li>Frills: AED 50 at the centre, AED 25 on site</li></ul><p><strong>A worked '
               'example.</strong> A blackout curtain panel that is 2 metres wide and 2.5 metres long is 5 square metres. At the centre that is AED 100 to clean. On site it is AED 75.</p><p>If you '
               'have a sheer and a blackout on the same window, they are two separate curtains, each priced at its own rate. Before you book, send the team the sizes or a photo of each window '
               'on WhatsApp and ask them to confirm how they will measure, so you know the total up front.</p>'),
              ('When to send curtains to the laundry',
               '<p>Cleaning at the centre is the more thorough option and the better choice when:</p><ul><li>The curtains have visible stains, water marks or a strong smell.</li><li>They have not been '
               'cleaned in more than a year.</li><li>You can take them down easily, for example curtains on a rod or with simple hooks.</li><li>You are moving out of an apartment or villa and want '
               'everything fresh for handover.</li><li>You also need repairs or new tape fitted, which can be done in the same order.</li></ul><p>Fabric and lining are checked before cleaning, and '
               'cleaning at the facility takes a few days. If you rely on blackout curtains to sleep, plan for a few nights without them, or send one room at a time.</p><p>Dima Laundry can also fit '
               'new curtain tape: fixing tape on curtains is AED 50, and tape is charged at AED 20 per metre. This is useful when old tape has gone brittle or the hooks no longer sit straight.</p>'),
              ('When on-site cleaning makes more sense',
               '<p>On-site cleaning is done at your home, by appointment. It is the better fit when:</p><ul><li>Your curtains are very long, heavy or on a motorised or ceiling track that is hard to '
               'take down.</li><li>The curtains are dusty and tired rather than badly stained.</li><li>You do not want to be without curtains for a few days, especially in bedrooms.</li><li>You want '
               'the lower rate. On site, chiffon is AED 8 instead of AED 12 per sq m, standard is AED 12 instead of AED 15, and blackout is AED 15 instead of AED 20.</li></ul><p>A common approach in '
               'Dubai homes is to have curtains cleaned on site most of the time, and send them to the laundry for a deeper clean when they are stained or before moving out.</p><p>If you are not sure '
               'which suits your curtains, send a photo and the fabric type to the team and ask what they recommend.</p>'),
              ('How to keep curtains clean for longer',
               '<ul><li><strong>Vacuum them every few weeks.</strong> Use the soft brush tool from top to bottom, and do not forget the top of the curtain and the folds, where most dust '
               'sits.</li><li><strong>Shake out sheers.</strong> Light chiffon curtains collect dust quickly. A gentle shake when you open them helps.</li><li><strong>Keep the windows clean.</strong> '
               'Dirty glass and tracks transfer dust to the fabric every time the curtain moves.</li><li><strong>Check the care label.</strong> Many curtains, especially blackouts and lined curtains, '
               'should not go in a home washing machine. Linings can shrink at a different rate from the face fabric, and blackout coatings can crack.</li><li><strong>Deal with marks early.</strong> '
               'Blot a fresh mark with a clean white cloth. Do not rub, and do not soak the fabric while it is hanging.</li></ul>'),
              ('How to book curtain cleaning',
               '<p>Message the team on WhatsApp on <a href="https://wa.me/971506398093">+971 50 639 8093</a> or call 800 DIMA (3462). It helps to send:</p><ul><li>A photo of each window with the '
               'curtains closed.</li><li>Rough sizes, width and length, for each curtain.</li><li>The type: sheer, standard or blackout.</li><li>Whether you want them cleaned at the centre or on '
               'site.</li><li>Your area and building.</li></ul><p>For cleaning at the centre, ask the team about taking down, collection and rehanging when you book. If your carpets or sofa are '
               'due at the same time, see <a href="/services/carpet-cleaning">carpet and rug cleaning</a> and <a href="/services/sofa-cleaning">on-site sofa cleaning</a>.</p>')],
 'faqs': [('How much is curtain cleaning in Dubai?',
           'Dima Laundry charges per square metre: chiffon AED 12, standard AED 15 and blackout AED 20 at the centre, or AED 8, AED 12 and AED 15 when cleaned on site at your home.'),
          ('Is on-site curtain cleaning as good as sending them to the laundry?',
           'On-site cleaning suits curtains that are dusty and need a refresh, and it costs less. For stains, strong smells or a long gap since the last clean, cleaning at the centre is the better choice.'),
          ('How long does curtain cleaning at the laundry take?', 'Cleaning at the facility takes a few days. The team confirms the ready date when you book.'),
          ('How often should curtains be cleaned in Dubai?', 'Every 6 to 12 months, because of dust and humidity.'),
          ('Can you replace the tape on my curtains?', 'Yes. Fixing tape on curtains is AED 50, and tape is AED 20 per metre.')],
 'links': [('Curtain cleaning', '/services/curtain-cleaning'), ('Full price list', '/prices'), ('Carpet and rug cleaning', '/services/carpet-cleaning'), ('Contact and booking', '/contact')]},
]
