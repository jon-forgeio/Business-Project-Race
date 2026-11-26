# Business sites on GitHub Pages (2026-11-26)

Netlify is retired for these sites (account credit blocked deploys; owner chose no spending).

## URLs
- Second Draft Careers: https://jon-forgeio.github.io/Business-Project-Race/second-draft-careers/
- Hearth & Host: https://jon-forgeio.github.io/Business-Project-Race/hearth-and-host-race/
- Solo Ops Studio: https://jon-forgeio.github.io/Business-Project-Race/solo-ops-studio/
- Classroom & Family Desk: https://jon-forgeio.github.io/Business-Project-Race/classroom-and-family-desk/
- Game Night Co: https://jon-forgeio.github.io/Business-Project-Race/game-night-co-race/

## One-time setup (owner)
Repo Settings > Pages > Source: Deploy from a branch > branch `claude/project-thread-bq2kcb`, folder `/docs`. The repo must be public for free Pages.

## Routine deploy steps
1. Edit or regenerate pages with `race/tools/gen.py` (writes to `race/sites/<slug>/`).
2. Copy each `race/sites/<slug>/*` into `docs/<slug>/`, and replace any `https://<slug>.netlify.app/` with the GitHub Pages base above.
3. Commit and push to `claude/project-thread-bq2kcb`. Pages rebuilds on push.
4. Never commit tokens. Pages content is public.
