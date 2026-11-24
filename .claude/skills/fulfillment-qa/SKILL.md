---
name: fulfillment-qa
description: Deliver paid orders and handle inbound buyers first each run.
---
1. List sales via Gumroad API /v2/sales; match to business.
2. Instant-delivery products: confirm delivery worked. Services: deliver via race Gmail connector within promised time.
3. Reply to urgent inbound; no unsupported promises.
4. Log order ID, delivery status, issues in race/ledger.csv (no customer PII in public files).
