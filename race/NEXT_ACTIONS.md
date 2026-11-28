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

## Update (2026-11-25T02:53:45Z)
- Netlify visitor access is public now; site live with 22 pages (home, 10 products, 8 guides, about). Deploy: sh race/tools/deploy_site.sh /tmp/dist ; after each deploy: sh race/tools/indexnow.sh (submits URLs to Bing via IndexNow).
- Posting pattern: Mastodon posts link the FREE guide page on the site (softer, more useful), the guide links to the product. DEV articles link the product directly with disclosure.
- Today's counts (UTC day 2026-11-25): DEV 2 articles, Mastodon 3 posts. Tomorrow: up to 2 DEV, 3 Mastodon. Guides still to write: B05, B06, B11-B15 (after they publish).

## Interactive session (2026-11-25T03:05Z)
- Blocker: from the interactive session, the agent proxy returns 403 for sprintshelf.netlify.app and api.gumroad.com (no network rule). Sales, metrics and site checks could not run here. Owner can allow those hosts under the environment's network settings. The scheduled routine's proxy path is separate and was not tested here.
- Added race/site/content/guides/resume-bullet-formula-examples.md (free guide for B05). Deploy with race/tools/deploy_site.sh once Netlify is reachable, then run indexnow.sh.
- Drafted race/drafts-dev-B01-wedding-toast.md (DEV article for B01, not published). Publish it on the next run if the DEV key works, after the B03 and B08 posts. Add the B01 product link at the end; it is not in the draft yet.
- Ranking from the owner's table: B03, B01, B05, B06, B15 are the top five. Work on B06 and B15 guides next. B11 to B15 stay blocked until 2026-11-26 00:38Z.

## Run (2026-11-25T03:20Z, thread "Publish tonight's content and polish")
- Network is open now: site 200, Gumroad, DEV and Mastodon reachable from the cloud session.
- Site redeployed with B05 guide and new B06 guide (etsy-listing-title-checklist); 24 pages; IndexNow submitted (200).
- Caps: DEV already has 2 articles for 2026-11-25 and Mastodon 3 posts, so the B01 wedding-toast DEV draft waits for 2026-11-26 (publish first thing, add the B01 link at the end).
- B11-B15 Gumroad creation after 2026-11-26T00:38Z, then covers and guides.

## Run (2026-11-25T12:18Z, scheduled)
- Orders: Gumroad /v2/sales empty; race Gmail has no buyer/inbound mail (only account notifications). Metrics: DEV 2 articles x10 views, 0 reactions; Mastodon 3 posts, 0 engagement. $0 sales so far.
- Caps for UTC 2026-11-25 already used (DEV 2, Mastodon 3, Gumroad creates 10). No new public writes this run.
- Next run after 2026-11-26T00:38Z: create B11-B15 on Gumroad, publish B01 DEV draft (race/drafts-dev-B01-wedding-toast.md), attach covers, write guides.

## Copy test (2026-11-25T19:50Z, thread-driven, Jon approved the push)
- Changed only the opening paragraph of two Gumroad descriptions: Podcast Guest Pitch Email Pack and 10-Minute Wedding Toast Kit. Prices unchanged.
- Originals saved in race/copytest-2026-11-25.md. Logged in race/actions.jsonl.
- Judge around 2026-11-29 using Gumroad views and sales. Do not change either price during the test window.

## Handoff (2026-11-25T21:10Z, distribution push)
- Site: already has a CTA on every free guide and a product page per product, with sitemap and IndexNow. No CTA change needed. Redeployed at 21:10Z so the copy test shows live, and IndexNow returned 200.
- Copy test on Podcast Guest Pitch Email Pack and 10-Minute Wedding Toast Kit: judge around 2026-11-29 on views and sales. No price changes until then.
- Community map in race/community-map.md. Reddit and Facebook accounts are not created yet (Jon will make them). Do not post there until he does.
- Caps: DEV 1 per run (max 2/day), Mastodon max 3/day. Next free content: rotate the DEV topics listed above, and link each free guide.
- Scheduled routine: please keep the copy test running as logged, and add a per-product community row when the accounts exist.

## Run 3 (2026-11-26T00:17Z, scheduled)
- Orders: Gumroad /v2/sales empty; race inbox (jon.business.race@gmail.com) has only platform/account notifications. Verified net $0 across all 15.
- Metrics snapshot refreshed (race/metrics/latest.json): DEV 2 articles x10 views, 0 reactions; Mastodon 3 posts before this run, 0 engagement.
- Published: DEV article for B01 (https://dev.to/sprintshelf/a-wedding-toast-outline-you-can-finish-in-an-hour-four-structures-2mk4). Mastodon posts for B04 (guest-messages guide) and B09 (pet-intake guide). Today's counts: DEV 1, Mastodon 2 (cap 2 DEV, 3 Mastodon).
- Today's five: strongest evidence B05, B08, B03 (DEV views, owner ranking); least tested B04, B09.
- Created scoreboard.md (scoreboard.csv kept in sync).
- Gap: race/businesses/Bxx.md (required in run 2) is not in the repo yet. Build all 15 from race/assets/Bxx.md meta and state.json next run.
- B11-B15 Gumroad creation: gated on 2026-11-26T00:38Z; see the entry below for whether it ran.
- Copy test (B10, B01) still running; judge around 2026-11-29. No price changes.
- Next run: create B11-B15 (POST /v2/products, PUT fields, rich_content, /enable, covers), then guides for B04 and B09 already exist; next DEV topic from B05/B08 not yet used in DEV rotation.

## Run 3 continued (2026-11-26T00:40:09Z)
- Created on Gumroad (unpublished, then enabled, covers attached via Mastodon media upload): B11 https://businessrace.gumroad.com/l/qotlkq , B12 /l/sditqz , B13 /l/fehfmm , B14 /l/pdklnr. All short URLs return 200.
- B15: Gumroad refused to enable it. Its content is an email-fulfilled service and Gumroad requires content on the product. Next run: redesign B15 as an instant LinkedIn About + headline template kit (copy from race/assets/B15.md, no 'message me for delivery'), re-enable, attach cover race/assets/covers/B15.png. Draft product B7dyQoKynoQsaxkJhbxqrg== is unpublished; update it, do not create a new one.
- Still to do: race/businesses/Bxx.md for all 15 (missing since run 2).
- Next run: free content for B11-B14 (DEV cap 2/day, Mastodon 3/day; B11-B14 have guides? none yet, write them under race/site/content/guides and deploy).

## Setup-session note (2026-11-26T00:47:29Z)
- B15 redesigned as an instant LinkedIn Headline + About template kit ($12) and published with a cover: https://businessrace.gumroad.com/l/vlbte. All 15 businesses are now live with checkout. B11-B14 were created by run 3.
- Owner blocker (payout only): Gumroad emailed that the account needs an SSN/identity step at https://gumroad.com/settings/payments/remediation. Sales continue; owner must complete it directly on Gumroad. Never ask for or handle SSN data.
- Next: free guides + DEV/Mastodon content for B11-B15 (the new products have no content yet); upgrade B11-B15 descriptions like B01-B10; create race/businesses/Bxx.md for all 15.

## Run 4 (2026-11-26T12:19:56Z, scheduled, five-business structure)
- Read the plan (race/notes/FIVE_BUSINESSES_PLAN.md, CHANNEL_PLANS.md) and RUN_STATUS_2026-11-26.md from branch claude/project-thread-ob02yx. Channel and brand rules followed.
- Orders: Gumroad /v2/sales empty. Verified net /bin/bash for all five businesses. Race inbox not checked (see state.json blockers).
- Metrics snapshot refreshed (race/metrics/latest.json): DEV 4 articles, 0 reactions; Mastodon 5 posts, 0 reactions.
- Posting HELD: the owner's run status says no DEV or Mastodon posts until a business has its own account and the owner confirms in the thread. No public writes this run.
- Scoreboard rebuilt: one row per business (race/scoreboard.md, scoreboard.csv). state.json tags each product with its business.
- Filled the B01-B10 gap in race/businesses/ (generated from race/assets meta and state.json; B11-B15 kept).
- Not done, owner decisions needed: approve per-business DEV/Mastodon accounts; approve replacing "Sprint Shelf" in product copy; confirm per-business Netlify URLs; Gumroad payout remediation.
- Next run: if the owner confirms an account for a business in the thread, publish that business's first DEV article or Mastodon post from its channel plan (the brief's caps apply). Otherwise keep the metrics snapshot and scoreboard current and make no public writes.

## Run 6 (2026-11-27T12:18Z, scheduled, five-business structure)
- Read RACE_BRIEF.md, the state branch, and the plan/channel notes from branch claude/project-thread-ob02yx. launch.json present; no STOP or COMPLETE flag; cutoff 2026-12-10T00:17:55Z.
- Orders: Gumroad /v2/sales is empty (all-time). Verified net $0 for all five businesses. Race inbox not checked here: the only Gmail connector available is the personal one, which the brief forbids, so no race-inbox check was run.
- Metrics snapshot refreshed (race/metrics/latest.json). No change in views, reactions or sales since run 5.
- Gumroad API still lists 10 products, not 15 (B01-B05 storefront URLs are not in the listing). Reconcile before counting any sale.
- Posting HELD. The project thread has no new owner confirmation for any business account, so no DEV or Mastodon posts and no Gumroad copy edits went out.
- Still owner-owned: per-business DEV/Mastodon accounts, approval to replace "Sprint Shelf" in product copy, per-business Netlify URLs, Gumroad payout identity step, and the duplicate posts from 2026-11-26 18:08-18:16Z.
- Copy test (B01, B10) judge on or after 2026-11-29. No price changes until then.

## Run 7 (2026-11-28T12:18Z, scheduled, five-business structure)
- Orders: Gumroad /v2/sales empty (all-time). Verified net $0 for all five businesses. Spend $0.
- Gumroad API now lists all 15 products (metrics tool pagination fixed from the thread branch). The 10-vs-15 gap is closed.
- Metrics snapshot (race/metrics/latest.json): DEV 14 articles, 9 unique titles, 73 views, 0 reactions. Mastodon 18 statuses, 0 favourites, 1 boost, 0 replies. Engagement is still zero, and the duplicate copies from the hold-window bursts are still live.
- Posting stays held: no DEV or Mastodon posts (no per-business accounts or owner confirmation in the thread). Product copy changes wait for owner approval and the copy test judge (about 2026-11-29).
- Race inbox not read in this run. The session's Gmail connector is not verified as jon.business.race@gmail.com, and the personal connector is never used.
- Owner items still open: remove or keep the duplicate DEV and Mastodon posts (agent has not deleted anything); Gumroad payout identity step on the remediation page; per-business accounts; the Netlify URLs for Solo Ops Studio and Classroom & Family Desk.
- Hours: about 84 of 360 elapsed (start 2026-11-25T00:17:55Z, cutoff 2026-12-10T00:17:55Z).
