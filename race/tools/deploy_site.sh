#!/bin/sh
# Rebuild and deploy the Sprint Shelf Netlify site. Run from repo root. Token is proxy-injected.
set -e
OUT=${1:-/tmp/sprintshelf-dist}
rm -rf "$OUT" "$OUT.zip"
python3 -I race/tools/build_site.py "$OUT"
(cd "$OUT" && python3 -I -c "import shutil;shutil.make_archive('$OUT','zip','.')")
curl -s -m 120 -X POST -H 'Authorization: Bearer proxy-injected' -H 'Content-Type: application/zip' --data-binary @"$OUT.zip" "https://api.netlify.com/api/v1/sites/1f4c2caf-93e8-44c7-87d8-0a7f5d60ea51/deploys"
