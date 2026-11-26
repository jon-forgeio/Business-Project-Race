import html, os, json
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'sites')
CONTACT = 'jon.business.race@gmail.com'

SITES = [
 dict(slug='second-draft-careers', name='Second Draft Careers', tag='Job search and career tools for the next step',
  hero='Get your next job search moving, one clear task at a time.',
  sub='Practical plans, resume bullets and outreach templates for people rebuilding their career after a layoff or a career change.',
  cta='See the tools', font="Georgia, 'Times New Roman', serif", accent='#b45309', accent2='#92400e', ink='#0f1f3d', bg='#f7f5f0', dark='#0f1f3d',
  about='Second Draft Careers makes short, usable career documents: a restart plan for the first week after a layoff, resume bullet rewrites, podcast pitch emails and LinkedIn templates. Each one is a fixed-scope product you can use right away.',
  faq=[('Is this career advice or a guarantee of results?', 'No. These are templates and plans to help you organize your own search. They do not promise interviews or offers.'),
       ('How do I get my files?', 'Checkout and delivery run through Gumroad. You receive the download link there after purchase.'),
       ('Do you write my resume for me?', 'The resume bullet rewrite is a fixed-scope service. Send your existing bullets and the result comes back within the stated turnaround.')],
  products=[
   ('B03', 'Layoff Week One: The 7-Day Job Search Restart Plan', 'A seven-day plan for restarting a job search after a layoff, with one clear task per day.', 'https://businessrace.gumroad.com/l/nhxmzf', '$9'),
   ('B05', 'Resume Bullet Rewrite: 10 Bullets, Back in 48 Hours', 'Ten rewritten resume bullets that lead with what you did and what changed because of it.', 'https://businessrace.gumroad.com/l/coiyeb', '$19'),
   ('B10', 'Podcast Guest Pitch Email Pack (6 Templates and a Tracker)', 'Six pitch templates and a simple tracker, so you are not starting from a blank page each time.', 'https://businessrace.gumroad.com/l/dtmjky', '$9'),
   ('B15', 'LinkedIn Headline and About Section Template Kit', 'Headline and About section templates written to be easy to scan and search.', 'https://businessrace.gumroad.com/l/vlbte', '$12')]),
 dict(slug='hearth-and-host-race', name='Hearth & Host', tag='Templates for hosting and home life',
  hero='Warm, ready-to-use templates for hosting, moving and home life.',
  sub='Toasts, guest messages, pet sitter forms, moving checklists and a first-month household planner, written so you can adapt them in minutes.',
  cta='Browse the kits', font="'Trebuchet MS', 'Segoe UI', sans-serif", accent='#c2410c', accent2='#9a3412', ink='#2b1d14', bg='#fdf6ec', dark='#3b2316',
  about='Hearth & Host makes home-focused documents: wedding toast structures, short-term rental guest messages, pet sitter client packs, moving checklists and a non-medical newborn household schedule. Everything is a fixed-scope digital product.',
  faq=[('Is the newborn schedule medical advice?', 'No. It is a non-medical household planner. For health questions, talk to a qualified clinician.'),
       ('Can I edit the templates?', 'Yes. Every template is meant to be adapted to your own names, places and details.'),
       ('How do I get my files?', 'Checkout and delivery run through Gumroad. Your download link arrives there after purchase.')],
  products=[
   ('B01', 'The 10-Minute Wedding Toast Kit', 'A simple toast structure with prompts that help you find and tell your own stories.', 'https://businessrace.gumroad.com/l/rtbyanv', '$7'),
   ('B04', 'Short-Term Rental Guest Message Pack (21 Templates)', 'Twenty-one guest messages for booking, check-in, check-out and house rules.', 'https://businessrace.gumroad.com/l/upakjg', '$9'),
   ('B09', 'Pet Sitter Client Pack: Intake, Care Sheet, Daily Updates', 'An intake form, care sheet and daily update messages for pet sitting clients.', 'https://businessrace.gumroad.com/l/btanaj', '$10'),
   ('B12', 'Moving-Day Checklist and 8-Week Timeline', 'A room-by-room moving checklist and an eight-week countdown of what to do when.', 'https://businessrace.gumroad.com/l/sditqz', '$7'),
   ('B13', 'Newborn First-Month Household Schedule (Non-Medical)', 'A household routine planner for the first month. Not medical advice.', 'https://businessrace.gumroad.com/l/fehfmm', '$8')]),
 dict(slug='solo-ops-studio', name='Solo Ops Studio', tag='Systems and templates for small shops and freelancers',
  hero='Run your shop or freelance work with fewer loose ends.',
  sub='Standard operating checklists, listing rewrites and client onboarding packs for one-person businesses.',
  cta='See the packs', font="'Segoe UI', Roboto, Helvetica, Arial, sans-serif", accent='#0d9488', accent2='#0f766e', ink='#111827', bg='#f3f4f6', dark='#111827',
  about='Solo Ops Studio builds operating documents for one-person businesses: checklists for running a digital product shop, rewritten product listings and client onboarding templates. Each product is a fixed-scope digital item.',
  faq=[('Do you guarantee more sales?', 'No. The packs make routine work faster and more consistent. Results depend on your own shop and market.'),
       ('Are the listing rewrites custom?', 'Yes. The listing rewrite is a fixed-scope service covering five of your products, delivered within the stated turnaround.'),
       ('How do I get my files?', 'Checkout and delivery run through Gumroad. Your download link arrives there after purchase.')],
  products=[
   ('B02', 'Etsy Digital Product Shop SOP Pack (12 Checklists)', 'Twelve repeatable checklists for running a digital product shop week after week.', 'https://businessrace.gumroad.com/l/ovfudt', '$12'),
   ('B06', 'Shop Listing Rewrite: 5 Product Listings, Back in 48 Hours', 'Rewritten titles, descriptions and tags for five of your product listings.', 'https://businessrace.gumroad.com/l/apfxk', '$24'),
   ('B08', 'Freelancer Client Onboarding Pack (Intake, Kickoff, Handoff)', 'Intake, kickoff and handoff templates that start client work cleanly.', 'https://businessrace.gumroad.com/l/stcfjq', '$11')]),
 dict(slug='classroom-and-family-desk', name='Classroom & Family Desk', tag='Prompts and planners for teachers and families',
  hero='Clear, kind messages and plans for teachers and families.',
  sub='Ready-to-adapt prompts for parent emails and progress notes, plus a step-by-step outliner for scholarship essays.',
  cta='See the resources', font="'Gill Sans', 'Trebuchet MS', sans-serif", accent='#2563eb', accent2='#1d4ed8', ink='#172033', bg='#f5f9ff', dark='#1e3a8a',
  about='Classroom & Family Desk makes practical writing resources for teachers, parents and students: prompt sets for parent communication and a scholarship essay outliner. Each product is a digital download.',
  faq=[('Are the prompts suitable for any school?', 'They are general starting points. Adapt them to your school’s policies and your own voice.'),
       ('Is the scholarship outliner a guarantee of an award?', 'No. It is a method for organizing your own essay. It does not promise results.'),
       ('How do I get my files?', 'Checkout and delivery run through Gumroad. Your download link arrives there after purchase.')],
  products=[
   ('B07', '23 Teacher Prompts for Parent Emails and Progress Notes', 'Twenty-three prompts for parent emails and progress notes, ready to adapt.', 'https://businessrace.gumroad.com/l/sotpbv', '$8'),
   ('B11', 'Scholarship Essay Outliner: 8 Prompt Types, Step by Step', 'A step-by-step outline method for eight common scholarship essay prompt types.', 'https://businessrace.gumroad.com/l/qotlkq', '$8')]),
 dict(slug='game-night-co-race', name='Game Night Co', tag='Tools for league commissioners and game nights',
  hero='A commissioner kit that keeps your league running smoothly.',
  sub='Rules, draft-night planning and a payouts tracker text for fantasy league commissioners.',
  cta='Get the kit', font="'Helvetica Neue', Arial, sans-serif", accent='#f59e0b', accent2='#d97706', ink='#f8fafc', bg='#1e1b4b', dark='#140f36',
  about='Game Night Co makes tools for the people who run the game: a fantasy league commissioner kit with rules, a draft-night plan and a payouts tracker text. It is a single digital product.',
  faq=[('Does the kit replace my league’s rules?', 'No. It is a starting template. Edit the rules to fit your league and agree them with your members.'),
       ('Does this handle real money?', 'No. The payouts tracker is a text template. Handling payments is up to you and your league.'),
       ('How do I get my files?', 'Checkout and delivery run through Gumroad. Your download link arrives there after purchase.')],
  products=[
   ('B14', 'Fantasy League Commissioner Kit: Rules, Draft Night, Payouts', 'Rules, a draft-night plan and a payouts tracker text to run your league cleanly.', 'https://businessrace.gumroad.com/l/pdklnr', '$7')]),
]

CSS_BASE = """*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:var(--font);color:var(--ink);background:var(--bg);font-size:17px;line-height:1.6;-webkit-font-smoothing:antialiased}
img{max-width:100%}a{color:var(--accent2)}
.w{max-width:1040px;margin:0 auto;padding:0 16px}
header{position:sticky;top:0;z-index:5;background:var(--dark);color:#fff}
header .w{display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:60px;flex-wrap:wrap}
.brand{font-weight:800;font-size:19px;color:#fff;text-decoration:none;letter-spacing:.2px}
nav a{color:#e5e7eb;text-decoration:none;margin-left:18px;font-size:15px}nav a:hover{color:#fff;text-decoration:underline}
.hero{padding:64px 0 48px}
.eyebrow{text-transform:uppercase;letter-spacing:.14em;font-size:13px;font-weight:700;color:var(--accent2);margin:0 0 10px}
h1{font-size:clamp(32px,5vw,50px);line-height:1.12;margin:0 0 16px;letter-spacing:-.5px;color:var(--ink);font-family:var(--heading)}
h2{font-size:clamp(24px,3vw,32px);line-height:1.2;margin:0 0 18px;font-family:var(--heading);color:var(--ink)}
h3{font-size:19px;margin:0 0 8px;color:var(--ink)}
.lead{font-size:19px;max-width:640px;margin:0 0 26px;opacity:.9}
.btn{display:inline-block;background:var(--accent);color:#fff;padding:13px 22px;border-radius:10px;text-decoration:none;font-weight:700;border:0;cursor:pointer;font-size:16px}
.btn:hover{background:var(--accent2);color:#fff}
.btn.ghost{background:transparent;color:var(--ink);border:2px solid var(--accent)}
.btn.ghost:hover{background:var(--accent);color:#fff}
section{padding:48px 0}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:22px;display:flex;flex-direction:column;gap:10px}
.card p{margin:0;opacity:.85;font-size:15.5px;flex:1}
.price{font-weight:800;font-size:22px;color:var(--ink)}
.card .btn{text-align:center}
.steps{counter-reset:s}.steps li{list-style:none;padding-left:0;margin:0 0 14px}
ol.steps{padding:0;margin:0}
.step{display:flex;gap:14px;align-items:flex-start}.num{flex:0 0 36px;height:36px;border-radius:50%;background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800}
.panel{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:26px}
details{border-bottom:1px solid var(--line);padding:14px 0}summary{cursor:pointer;font-weight:700;font-size:17px}details p{margin:10px 0 0;opacity:.88}
footer{background:var(--dark);color:#d1d5db;padding:36px 0 44px;font-size:14px}footer a{color:#fff}
.note{font-size:13.5px;opacity:.8;margin-top:12px}
@media (max-width:640px){.hero{padding:40px 0 32px}nav a{margin-left:12px}section{padding:36px 0}}
"""

def esc(s): return html.escape(s, quote=True)

def build(s):
    url = f"https://{s['slug']}.netlify.app/"
    title = f"{s['name']}: {s['tag']}"
    desc = s['sub']
    theme = (f":root{{--font:{s['font']};--heading:{s['font']};--accent:{s['accent']};--accent2:{s['accent2']};"
             f"--ink:{s['ink']};--bg:{s['bg']};--dark:{s['dark']};--card:#ffffff;--line:rgba(0,0,0,.12)}}")
    if s['slug']=='game-night-co-race':
        theme = theme.replace('--card:#ffffff', '--card:#2a2566').replace('--line:rgba(0,0,0,.12)', '--line:rgba(255,255,255,.14)')
    cards = []
    for bid, name, blurb, link, price in s['products']:
        cards.append(f'<article class="card"><h3>{esc(name)}</h3><p>{esc(blurb)}</p><div class="price">{esc(price)}</div><a class="btn" href="{esc(link)}" rel="noopener">Buy on Gumroad</a></article>')
    faq = ''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q,a in s['faq'])
    ld = {"@context":"https://schema.org","@graph":[
        {"@type":"Organization","name":s['name'],"url":url,"email":"mailto:"+CONTACT,"description":desc},
        {"@type":"WebSite","name":s['name'],"url":url}] + [
        {"@type":"Product","name":n,"description":b,"brand":{"@type":"Brand","name":s['name']},
         "offers":{"@type":"Offer","url":l,"priceCurrency":"USD","price":p.replace('$',''),"availability":"https://schema.org/InStock"}}
        for _,n,b,l,p in s['products']]}
    body = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary">
<meta name="robots" content="index,follow">
<style>{theme}{CSS_BASE}</style>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<header><div class="w"><a class="brand" href="#top">{esc(s['name'])}</a>
<nav><a href="#products">Products</a><a href="#how">How it works</a><a href="#about">About</a><a href="#faq">FAQ</a></nav></div></header>
<main id="top">
<div class="hero"><div class="w">
<p class="eyebrow">{esc(s['tag'])}</p>
<h1>{esc(s['hero'])}</h1>
<p class="lead">{esc(s['sub'])}</p>
<a class="btn" href="#products">{esc(s['cta'])}</a>
</div></div>
<section id="products"><div class="w"><h2>What's inside</h2><div class="grid">{''.join(cards)}</div>
<p class="note">Prices in US dollars. Checkout and download are handled by Gumroad.</p></div></section>
<section id="how"><div class="w"><h2>How it works</h2><div class="grid">
<div class="panel step"><span class="num">1</span><div><h3>Pick a product</h3><p>Choose the one that matches the situation you are in now.</p></div></div>
<div class="panel step"><span class="num">2</span><div><h3>Buy securely</h3><p>Checkout runs on Gumroad. Your download link arrives after purchase.</p></div></div>
<div class="panel step"><span class="num">3</span><div><h3>Adapt and use</h3><p>Edit the templates with your own details, then use them as they fit.</p></div></div>
</div></div></section>
<section id="about"><div class="w"><div class="panel"><h2>About {esc(s['name'])}</h2><p>{esc(s['about'])}</p>
<p>This business is run with AI assistance: drafts are produced with AI tools and then edited for clarity and accuracy. Products are practical templates, not professional advice.</p>
<p>Questions: <a href="mailto:{CONTACT}">{CONTACT}</a></p></div></div></section>
<section id="faq"><div class="w"><h2>Questions</h2>{faq}</div></section>
</main>
<footer><div class="w">
<p><strong>{esc(s['name'])}</strong>. {esc(s['tag'])}.</p>
<p>Run with AI assistance. Products are sold and delivered through Gumroad. Contact: <a href="mailto:{CONTACT}">{CONTACT}</a></p>
<p>&copy; 2026 {esc(s['name'])}</p>
</div></footer>
</body>
</html>
"""
    d = os.path.join(OUT, s['slug']); os.makedirs(d, exist_ok=True)
    open(os.path.join(d,'index.html'),'w',encoding='utf-8').write(body)
    open(os.path.join(d,'robots.txt'),'w').write(f"User-agent: *\nAllow: /\n\nSitemap: {url}sitemap.xml\n")
    open(os.path.join(d,'sitemap.xml'),'w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>{url}</loc></url>\n</urlset>\n')

for s in SITES: build(s)
print('built', [s['slug'] for s in SITES])
