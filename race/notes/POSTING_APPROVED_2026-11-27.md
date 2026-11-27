# Posting approved (2026-11-27)

Owner approved, in the project thread on 2026-11-26:
1. Publish the content bank to DEV and Mastodon under the existing accounts (dev.to/sprintshelf, mastodon.social/@sprintshelf). Each post names its business. Pace it: no bursts, respect platform rate limits, one DEV article per business per run at most, and at most 2 Mastodon posts per business per day.
2. Replace "Sprint Shelf" in product copy with each business's own name.

This supersedes the "posting is OFF" hold in RUN_STATUS_2026-11-26.md. The 12-hour routine may post under the existing accounts from now on, subject to the rules above and the original guardrails (original work only, no fake reviews or engagement, no spam, and an AI-content label flagged to the owner where a platform requires one).

Done in this change:
- Product asset copy (race/assets/B01-B15.md): "Sprint Shelf" replaced with the business name for each product.

Still open:
- Site builder (race/tools/build_site.py) still brands the site "Sprint Shelf". It needs per-business branding before the business sites are rebuilt.
- Gumroad product descriptions are updated on Gumroad itself, not from this repo.
- Guide links that point to sprintshelf.netlify.app are blocked by Netlify credit limits. Point them at each business's GitHub Pages home.
