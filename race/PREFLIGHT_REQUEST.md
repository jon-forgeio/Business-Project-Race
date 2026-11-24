# Preflight request (owner-authorized, one time)
Spend $0. Do NOT build businesses, publish, list publicly, send outreach, email anyone, or buy anything. Never create race/launch.json. Report each check PASS/FAIL with evidence in race/preflight-report.md, normal-push (no force) to claude/business-race-6j64nd, then exit.
1. Repo available on branch claude/business-race-6j64nd; race/launch.json absent.
2. Durable state writable: append {"preflight":"<UTC time>"} to race/preflight.log, commit, normal push. Report push result.
3. Gumroad read-only: curl -s -H 'Authorization: Bearer proxy-injected' https://api.gumroad.com/v2/user, /v2/products, /v2/sales (flags/counts only).
4. Polar read-only: curl -s -H 'Authorization: Bearer proxy-injected' 'https://api.polar.sh/v1/products/?limit=1' and '/v1/orders/?limit=1' (counts only).
5. Gmail: only the connector for jon.business.race@gmail.com; call list_labels (read-only), confirm address. FAIL if absent or different address; never use any other Gmail.
6. Gumroad write path without publishing: POST /v2/products with name 'zz-preflight-draft', price 100 -> record id and whether published=false; test whether a file can be attached via API (docs/probe); then DELETE /v2/products/<id> and confirm it is gone.
7. Polar write path without publishing: try creating then deleting/archiving a private draft product, or report why not (scope/sandbox). No public listing.
8. Note the session start type (scheduled vs manual) and which connectors/tools are present.
