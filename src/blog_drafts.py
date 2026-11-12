"""Blog drafts waiting for review. Same fields as POSTS in blog_posts.py, plus "date" (YYYY-MM-DD).

Drafts build at /preview/<slug>: noindex, not in the sitemap, blog list, footer or llms.txt.
To publish: move the dict to the TOP of POSTS in blog_posts.py (newest first) and remove it here.
"""

DRAFTS = [
{'slug': 'how-often-clean-sofa-dubai',
 'short': 'How often to clean a sofa',
 'date': '2026-11-12',
 'title': 'How Often Should You Clean Your Sofa in Dubai?',
 'desc': 'How often to deep clean a fabric sofa in a Dubai home, the signs it is due, what to do between cleans and what on-site sofa shampooing costs.',
 'h1': 'How Often Should You Clean Your Sofa in Dubai?',
 'answer': 'Most Dubai homes should vacuum a fabric sofa every week and have it deep cleaned once a year, or every six months with children, pets or a lot of sand coming in from the balcony. Clean '
           'it sooner if it smells, looks dull or has stains. Dima Laundry shampoos sofas at your home for AED 70 per seat.',
 'sections': [('Why sofas get dirty faster in Dubai',
               '<p>A sofa does not look dirty until it suddenly does. By then the fabric has been collecting months of things you cannot see.</p><ul><li><strong>Sand and dust.</strong> Fine dust '
               'gets in through balcony doors, windows and on clothes, and settles deep into the fabric and the cushions.</li><li><strong>Sweat and skin oils.</strong> In the hot months people come '
               'in from outside and sit straight down. Arms, headrests and seat fronts take most of it.</li><li><strong>Humidity.</strong> On humid days, damp in the air helps smells cling to '
               'fabric, and an air conditioned room that is closed up all day keeps them there.</li><li><strong>Food and drink.</strong> In many homes the sofa is also where people eat, watch TV and '
               'host guests.</li></ul><p>None of this is a sign of a dirty home. It is what happens to fabric that is used every day in this climate.</p>'),
              ('How often to clean your sofa',
               '<p>There are two kinds of cleaning, and you need both.</p><p><strong>Every week: vacuum.</strong> Use the upholstery tool on the seats, the back, the arms and down the sides of the '
               'cushions, where sand and crumbs collect. Lift the cushions out if they come off. This is the single best thing you can do to make a sofa last.</p><p><strong>Once a year: deep '
               'clean.</strong> For a sofa used by a couple or a small household, one professional shampoo a year is a sensible starting point.</p><p><strong>Every six months: deep clean in busier '
               'homes.</strong> Move to twice a year if any of these apply:</p><ul><li>You have young children or pets.</li><li>The sofa is light coloured.</li><li>It is the main seat in the house '
               'and used every day.</li><li>Your balcony doors are often open and sand blows in.</li><li>Someone in the house smokes, or you cook with strong spices in an open plan '
               'space.</li></ul><p>It is also worth booking a clean before you host guests for Eid or a family visit, and before you hand back a rented apartment with furnished items.</p>'),
              ('Signs your sofa needs a clean now',
               '<p>Do not wait for the calendar if you notice any of these:</p><ul><li>A stale or musty smell when you sit down, even after airing the room.</li><li>Arms and headrests that look '
               'darker or shiny compared with the rest of the fabric.</li><li>Seat cushions that have turned a shade darker than the back.</li><li>Stains from food, drink, makeup or pets that have '
               'not come out with blotting.</li><li>Dust that puffs up when you pat a cushion.</li></ul><p>Older stains are harder to treat than fresh ones, so when you book, tell the team what '
               'caused any marks and roughly how long they have been there.</p>'),
              ('What to do between deep cleans',
               '<ul><li><strong>Blot spills straight away.</strong> Use a clean white cloth and press, do not rub. Rubbing spreads the stain and pushes it deeper.</li><li><strong>Check the care '
               'label first.</strong> Most sofas have a code under a cushion or on the frame. If you are not sure what it means, do not soak the fabric with water or cleaning '
               'sprays.</li><li><strong>Turn and swap cushions.</strong> Flip and rotate them every few weeks so they wear and fade evenly.</li><li><strong>Keep it out of strong sun.</strong> '
               'Afternoon sun through Dubai windows fades fabric quickly. Use blinds or curtains at the hottest time of day.</li><li><strong>Use a throw.</strong> A washable throw on the seat people '
               'use most, or where a pet sleeps, takes much of the daily wear.</li></ul><p>If your sofa has removable covers, you can send just the covers for cleaning between full shampoos.</p>'),
              ('What professional sofa cleaning costs',
               '<p>Dima Laundry cleans fabric sofas and armchairs at your home, so there is no need to move furniture or get a sofa down a tower lift. Stains are pre-treated before the sofa is '
               'shampooed. These are the published prices:</p><ul><li>Sofa shampooing on site: AED 70 per seat</li><li>Removable sofa cover, small: AED 30</li><li>Removable sofa cover, medium: AED '
               '40</li><li>Removable sofa cover, large: AED 50</li></ul><p>Because the price is per seat, a two seater sofa is AED 140 and a three seater AED 210. For corner sofas, chaises and '
               "armchairs, send a photo on WhatsApp and ask the team how many seats they will count, so you know the total before the visit.</p><p>Removable covers are cleaned at Dima's centres "
               'rather than at your home. If your mattress is due too, it can be cleaned on site in the same visit: AED 200 for a single, AED 250 for a queen and AED 300 for a king. All of these are '
               'on the full <a href="/prices">price list</a>.</p>'),
              ('How to book',
               '<p>On-site sofa cleaning is booked by appointment. Message the team on WhatsApp on <a href="https://wa.me/971506398093">+971 50 639 8093</a> or call 800 DIMA (3462) for the next '
               'available slot. When you message, it helps to send:</p><ul><li>A photo of the sofa, so the seat count is clear.</li><li>The fabric, if you know it, or a photo of the care '
               'label.</li><li>Any stains you want the team to look at.</li><li>Your area and building.</li></ul><p>For leather sofas or unusual fabrics, ask the team before you book whether they '
               'can be cleaned on site. If you have rugs that need attention at the same time, see <a href="/services/carpet-cleaning">carpet and rug cleaning</a>, which is done at the Al Quoz '
               'centres with pickup and delivery.</p>')],
 'faqs': [('How often should a sofa be professionally cleaned?',
           'Once a year suits most homes. Every six months is better if you have children, pets, a light coloured sofa or a lot of sand coming in from the balcony.'),
          ('How much is sofa cleaning in Dubai?',
           'Dima Laundry shampoos sofas at your home for AED 70 per seat, so a three seater sofa is AED 210. Removable covers are AED 30 to AED 50 depending on size.'),
          ('Do I need to move my sofa to get it cleaned?', 'No. Dima Laundry shampoos sofas on site, where they sit. Only removable covers are taken to the centre.'),
          ('Can you clean my mattress at the same time?', 'Yes. On-site mattress cleaning is AED 200 for a single, AED 250 for a queen and AED 300 for a king. Mention it when you book.')],
 'links': [('Sofa and mattress cleaning', '/services/sofa-cleaning'), ('Full price list', '/prices'), ('Carpet and rug cleaning', '/services/carpet-cleaning'), ('Contact and booking', '/contact')]},
]
