#!/usr/bin/env python3
"""Build the Sprint Shelf static site from live Gumroad products + race/site/content/guides/*.md.
Usage: python3 -I race/tools/build_site.py <outdir>   (then zip and deploy, see race/tools/deploy_site.sh)"""
import json, os, re, subprocess, sys, html, glob, datetime
BASE = 'https://sprintshelf.netlify.app'
out = sys.argv[1]
os.makedirs(out, exist_ok=True)

def get(url):
    return json.loads(subprocess.run(['curl', '-s', '-m', '40', '-H', 'Authorization: Bearer proxy-injected', url], capture_output=True, text=True).stdout)

prods = [p for p in get('https://api.gumroad.com/v2/products')['products'] if p.get('published')]
state = json.load(open('race/state.json'))
bid = {b['gumroad_product_id']: b['id'] for b in state['businesses'] if b.get('gumroad_product_id')}
for p in prods:
    p['bid'] = bid.get(p['id'], '')
prods.sort(key=lambda p: p['bid'])
by_bid = {p['bid']: p for p in prods}

def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')[:70]

def md(body):
    out_h, items = [], []
    def flush():
        nonlocal items
        if items:
            out_h.append('<ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'); items = []
    def inline(t):
        t = html.escape(t)
        return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    for l in body.split('\n'):
        l = l.rstrip()
        if not l: continue
        if l.startswith('- '): items.append(inline(l[2:])); continue
        flush()
        if l.startswith('# '): out_h.append(f'<h2>{inline(l[2:])}</h2>')
        else: out_h.append(f'<p>{inline(l)}</p>')
    flush(); return '\n'.join(out_h)

CSS = """:root{--ink:#0f172a;--mut:#475569;--bg:#f8fafc;--card:#fff;--acc:#0f766e;--acc2:#115e59}*{box-sizing:border-box}body{margin:0;font:17px/1.65 -apple-system,Segoe UI,Inter,Arial,sans-serif;color:var(--ink);background:var(--bg)}a{color:var(--acc2)}
header{background:#fff;border-bottom:1px solid #e2e8f0}.w{max-width:960px;margin:0 auto;padding:0 20px}nav{display:flex;gap:22px;align-items:center;height:64px}nav .b{font-weight:800;font-size:20px;color:var(--ink);text-decoration:none;margin-right:auto}nav a{text-decoration:none;color:var(--mut);font-size:15px}
.hero{padding:56px 0 24px}.hero h1{font-size:40px;line-height:1.15;margin:0 0 12px;letter-spacing:-1px}.hero p{color:var(--mut);max-width:620px;margin:0}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:20px;margin:28px 0 48px}.card{background:var(--card);border:1px solid #e2e8f0;border-radius:14px;overflow:hidden;display:flex;flex-direction:column}.card img{width:100%;aspect-ratio:16/9;object-fit:cover;display:block}.card div{padding:14px 16px 16px}.card h3{margin:0 0 6px;font-size:17px;line-height:1.3}.card p{margin:0;color:var(--mut);font-size:14px}.card a.t{text-decoration:none;color:inherit}
.btn{display:inline-block;background:var(--acc);color:#fff!important;padding:12px 22px;border-radius:10px;text-decoration:none;font-weight:700}.btn:hover{background:var(--acc2)}
main article{background:#fff;border:1px solid #e2e8f0;border-radius:14px;padding:28px 28px 20px;margin:28px 0}article h1{font-size:32px;line-height:1.2;margin:0 0 6px;letter-spacing:-.5px}article h2{font-size:22px;margin:28px 0 6px}article img.cover{width:100%;border-radius:12px;margin:12px 0}.note{color:var(--mut);font-size:14px}.cta{background:#f0fdfa;border:1px solid #99f6e4;border-radius:12px;padding:16px 18px;margin:26px 0}
footer{color:var(--mut);font-size:14px;padding:28px 0 48px}ul{padding-left:22px}li{margin:4px 0}"""

def page(title, desc, path, body, extra=''):
    url = BASE + path
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{url}"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{url}"><meta property="og:type" content="website"><meta name="twitter:card" content="summary"><style>{CSS}</style>{extra}</head><body><header><div class="w"><nav><a class="b" href="/">Sprint Shelf</a><a href="/products/">Products</a><a href="/guides/">Free guides</a><a href="/about/">About</a></nav></div></header><div class="w">{body}<footer>Sprint Shelf. Templates, checklists and prompts. Text written with AI assistance and edited for clarity. Products are sold through Gumroad. Contact: jon.business.race@gmail.com</footer></div></body></html>"""

def write(path, content):
    fp = os.path.join(out, path.lstrip('/'), 'index.html') if path.endswith('/') else os.path.join(out, path.lstrip('/'))
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, 'w').write(content)

urls = ['/']
def card(p):
    cover = (p.get('covers') or [{}])[0].get('url', '')
    sl = f"/products/{slug(p['name'])}/"
    short = re.sub(r'<[^>]+>', '', p['description']).split('.')[0][:140]
    return f'<div class="card"><a class="t" href="{sl}"><img src="{cover}" alt="{html.escape(p["name"])}" loading="lazy"><div><h3>{html.escape(p["name"])}</h3><p>{html.escape(short)}. <strong>{p["formatted_price"]}</strong></p></div></a></div>'

guides = []
for f in sorted(glob.glob('race/site/content/guides/*.md')):
    head, body = open(f).read().split('\n---\n', 1)
    meta = dict(l.split(': ', 1) for l in head.split('\n') if ': ' in l)
    meta['slug'] = os.path.basename(f)[:-3]; meta['body'] = body; guides.append(meta)

# home
home = f'<div class="hero"><h1>Practical templates, checklists and prompts</h1><p>Short, usable documents for specific moments: a toast, a layoff, a new rental guest, a client kickoff. Start with a free guide, buy the full version if it helps.</p></div><div class="grid">{"".join(card(p) for p in prods)}</div><h2>Free guides</h2><ul>{"".join(f"<li><a href=\"/guides/{g[chr(115)+chr(108)+chr(117)+chr(103)]}/\">{html.escape(g[chr(116)+chr(105)+chr(116)+chr(108)+chr(101)])}</a></li>" for g in guides)}</ul>'
write('/', page('Sprint Shelf: practical templates, checklists and prompts', 'Short, usable templates and checklists for weddings, job searches, rentals, teachers, freelancers and small shops.', '/', home))
write('/products/', page('Products | Sprint Shelf', 'All Sprint Shelf templates, checklists and services.', '/products/', f'<div class="hero"><h1>Products</h1></div><div class="grid">{"".join(card(p) for p in prods)}</div>'))
urls.append('/products/')
for p in prods:
    sl = f"/products/{slug(p['name'])}/"; cover = (p.get('covers') or [{}])[0].get('url', '')
    ld = json.dumps({"@context": "https://schema.org", "@type": "Product", "name": p['name'], "image": cover, "brand": {"@type": "Brand", "name": "Sprint Shelf"}, "offers": {"@type": "Offer", "priceCurrency": "USD", "price": str(p['price'] / 100), "url": p['short_url'], "availability": "https://schema.org/InStock"}})
    body = f'<main><article><h1>{html.escape(p["name"])}</h1><p class="note">By Sprint Shelf. {p["formatted_price"]}</p><img class="cover" src="{cover}" alt="{html.escape(p["name"])}">{p["description"]}<div class="cta"><a class="btn" href="{p["short_url"]}">Buy now: {p["formatted_price"]}</a><p class="note">Checkout and delivery are handled by Gumroad.</p></div></article></main>'
    write(sl, page(p['name'] + ' | Sprint Shelf', re.sub(r'<[^>]+>', '', p['description'])[:155], sl, body, f'<script type="application/ld+json">{ld}</script>'))
    urls.append(sl)
write('/guides/', page('Free guides | Sprint Shelf', 'Free, practical guides from Sprint Shelf.', '/guides/', '<div class="hero"><h1>Free guides</h1></div><main><article><ul>' + ''.join(f'<li><a href="/guides/{g["slug"]}/">{html.escape(g["title"])}</a><br><span class="note">{html.escape(g["description"])}</span></li>' for g in guides) + '</ul><h2>Also on DEV</h2><ul><li><a href="https://dev.to/sprintshelf">Articles on DEV</a></li></ul></article></main>'))
urls.append('/guides/')
for g in guides:
    pr = by_bid.get(g['product'])
    cta = f'<div class="cta"><strong>{html.escape(pr["name"])}</strong> ({pr["formatted_price"]})<br><a class="btn" href="/products/{slug(pr["name"])}/">See the full version</a></div>' if pr else ''
    sl = f'/guides/{g["slug"]}/'
    write(sl, page(g['title'] + ' | Sprint Shelf', g['description'], sl, f'<main><article><h1>{html.escape(g["title"])}</h1>{md(g["body"])}{cta}<p class="note">Written with AI assistance and edited for clarity. I run this shop; the link above goes to my own product.</p></article></main>'))
    urls.append(sl)
write('/about/', page('About Sprint Shelf', 'What Sprint Shelf is and how the guides are written.', '/about/', '<main><article><h1>About Sprint Shelf</h1><p>Sprint Shelf makes short, practical documents for specific moments. Each one is a template, checklist, prompt set or fixed-scope writing service.</p><p>The text is written with AI assistance and edited for clarity. Examples are illustrative, not client results, and nothing here is legal, medical or financial advice. Products are sold and delivered through Gumroad.</p><p>Questions: jon.business.race@gmail.com</p></article></main>'))
urls.append('/about/')
today = datetime.date.today().isoformat()
open(os.path.join(out, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>{BASE}{u}</loc><lastmod>{today}</lastmod></url>' for u in urls) + '</urlset>')
open(os.path.join(out, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n')
open(os.path.join(out, '404.html'), 'w').write(page('Page not found | Sprint Shelf', 'Page not found.', '/404.html', '<div class="hero"><h1>Page not found</h1><p><a href="/">Back to the home page</a></p></div>'))
print('pages', len(urls), 'products', len(prods), 'guides', len(guides))
