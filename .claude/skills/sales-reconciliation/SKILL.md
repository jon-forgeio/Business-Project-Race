---
name: sales-reconciliation
description: Reconcile verified net sales into the scoreboard.
---
1. Pull transactions from provider; dedupe by transaction ID; one business each.
2. Net = payment - fees - refunds/chargebacks, excl. tax, within start..cutoff.
3. Update race/ledger.csv and race/scoreboard.md (one row per business).
4. Pending, quotes, views score $0.
