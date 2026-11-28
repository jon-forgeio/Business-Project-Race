#!/usr/bin/env python3
"""Read-only metrics snapshot for the race. Run: python3 -I race/tools/metrics.py > race/metrics/latest.json
Credentials are injected by the egress proxy; the placeholders below are intentional."""
import json, subprocess, time

def get(url, hdr):
    out = subprocess.run(['curl', '-s', '-m', '40', '-H', hdr, url], capture_output=True, text=True).stdout
    try:
        return json.loads(out)
    except Exception:
        return None

snap = {"generated_utc": time.strftime('%FT%TZ', time.gmtime())}
# Gumroad pages at 10 products; follow next_page_url so every product is counted.
gum, nxt, pages = [], '/v2/products', 0
while nxt and pages < 10:
    g = get('https://api.gumroad.com' + nxt if nxt.startswith('/') else nxt, 'Authorization: Bearer proxy-injected') or {}
    gum.extend(g.get("products", []))
    nxt, pages = g.get("next_page_url"), pages + 1
snap["gumroad_products"] = [{"name": p.get("name"), "published": p.get("published"), "price": p.get("formatted_price"),
                             "sales_count": p.get("sales_count"), "sales_usd_cents": p.get("sales_usd_cents"), "url": p.get("short_url")}
                            for p in gum]
s = get('https://api.gumroad.com/v2/sales', 'Authorization: Bearer proxy-injected') or {}
snap["gumroad_sales_listed"] = len(s.get("sales", []))
d = get('https://dev.to/api/articles/me/all', 'api-key: proxy-injected') or []
snap["dev_articles"] = [{"id": a.get("id"), "title": a.get("title"), "views": a.get("page_views_count"),
                         "reactions": a.get("public_reactions_count"), "comments": a.get("comments_count"), "url": a.get("url")} for a in d] if isinstance(d, list) else []
me = get('https://mastodon.social/api/v1/accounts/verify_credentials', 'Authorization: Bearer proxy-injected') or {}
snap["mastodon"] = {"followers": me.get("followers_count"), "statuses": me.get("statuses_count")}
if me.get("id"):
    st = get(f'https://mastodon.social/api/v1/accounts/{me["id"]}/statuses?limit=40', 'Authorization: Bearer proxy-injected') or []
    snap["mastodon_posts"] = [{"id": x.get("id"), "url": x.get("url"), "favourites": x.get("favourites_count"),
                               "boosts": x.get("reblogs_count"), "replies": x.get("replies_count")} for x in st] if isinstance(st, list) else []
print(json.dumps(snap, indent=1))
