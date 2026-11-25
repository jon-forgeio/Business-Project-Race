#!/bin/sh
# Submit all site URLs (from the deployed sitemap) to IndexNow (Bing etc.). No account needed; key file is served from the site root.
URLS=$(curl -s -m 30 https://sprintshelf.netlify.app/sitemap.xml | grep -o '<loc>[^<]*</loc>' | sed 's/<[^>]*>//g' | python3 -I -c "import sys,json;print(json.dumps([l.strip() for l in sys.stdin if l.strip()]))")
curl -s -m 40 -o /dev/null -w "indexnow http %{http_code}\n" -X POST https://api.indexnow.org/indexnow -H 'Content-Type: application/json; charset=utf-8' -d "{\"host\":\"sprintshelf.netlify.app\",\"key\":\"b7f3c1e94a2d4f6a8c0e5d7b9a1f3c52\",\"keyLocation\":\"https://sprintshelf.netlify.app/b7f3c1e94a2d4f6a8c0e5d7b9a1f3c52.txt\",\"urlList\":$URLS}"
