# Run log (2026-11-25T00:54:42Z)
- B01-B10 are LIVE on Gumroad with checkout (links in race/scoreboard.csv). Gumroad payout method is set.
- Gumroad caps product CREATION at 10 per rolling day. B11-B15 content is written (race/assets/B11-B15.md). Create+publish them after 2026-11-26T00:38Z: POST /v2/products (name, price, published=false) -> PUT description/custom_receipt/tags[] -> PUT rich_content (JSON body) -> PUT /enable. Verify short URL 200. Updating existing products is not capped.
- Every run: check Gumroad /v2/sales and race Gmail for orders first. Services B05, B06 (and B15 when live) are fulfilled by email within 48h from the race Gmail.
- Then work distribution for all 15; no spam, no fake reviews; only explicit public requests and channels with an account.

## Channels (updated)
- DEV article 1 live (B08). Mastodon post 1 live (B03). Both credentials are proxy-injected and verified.
- Next: one new DEV article per run (rotate B03, B05, B07, B10, B02, B15) and up to 3 Mastodon posts per day, spread across the other products. Check race/actions.jsonl so topics never repeat.
- Pending: B11-B15 Gumroad creation after 2026-11-26T00:38Z (daily product cap).

## Update (setup session, 2026-11-25T02:12:50Z)
- Mastodon avatar and header set. Designed covers attached to B01-B10 on Gumroad. race/tools/metrics.py added; follow the Daily optimization loop in RACE_BRIEF.md.
- Still pending: B11-B15 creation after 2026-11-26T00:38Z, with covers (extend the cover template), then post free content for them.
- DEV profile picture must be uploaded manually by the owner (no API); Gumroad profile picture/cover likewise.

## Handover (setup session end, 2026-11-25T02:20:59Z)
- LIVE: B01-B10 on Gumroad with designed covers and upgraded descriptions. Content so far: DEV article (B08), Mastodon posts (B03, B02).
- B11-B15: content in race/assets, covers already rendered in race/assets/covers. Create+publish after 2026-11-26T00:38Z, then attach covers (Mastodon media upload -> Gumroad /covers url=) and upgrade descriptions like B01-B10.
- Next content ideas (not yet used): DEV articles for B03 (job search after layoff, #career), B05 (rewriting resume bullets, #career), B07 (AI for teachers, #ai), B10 (podcast pitch, #career), B02 (Etsy SOPs, #productivity). Mastodon: B04 host messages, B07, B09, B10, B12, B14. At most 3 Mastodon posts/day, 1 DEV article/run.
- Run the metrics tool every run and apply the Daily optimization loop in RACE_BRIEF.md.

## Netlify site (2026-11-25T02:46:25Z)
- Site sprintshelf.netlify.app deployed (19 pages: home, 10 products, 5 free guides, about, sitemap). Rebuild/deploy any time: sh race/tools/deploy_site.sh /tmp/dist (token is proxy-injected). Add new live products and guides under race/site/content/guides/.
- BLOCKER: the site returns 401 (Netlify team login required for visitors). Do NOT try to change account security settings; the owner must switch this off in Netlify. Until then do not link to the site from posts. Each run: curl the home page; if 200, start linking it and submit sitemap links in posts.
- Hashnode dropped (API needs paid Pro). GitHub Pages dropped (token collides with the repo credential).
