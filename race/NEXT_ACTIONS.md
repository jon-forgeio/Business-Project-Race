# Run log (2026-11-25T00:54:42Z)
- B01-B10 are LIVE on Gumroad with checkout (links in race/scoreboard.csv). Gumroad payout method is set.
- Gumroad caps product CREATION at 10 per rolling day. B11-B15 content is written (race/assets/B11-B15.md). Create+publish them after 2026-11-26T00:38Z: POST /v2/products (name, price, published=false) -> PUT description/custom_receipt/tags[] -> PUT rich_content (JSON body) -> PUT /enable. Verify short URL 200. Updating existing products is not capped.
- Every run: check Gumroad /v2/sales and race Gmail for orders first. Services B05, B06 (and B15 when live) are fulfilled by email within 48h from the race Gmail.
- Then work distribution for all 15; no spam, no fake reviews; only explicit public requests and channels with an account.
