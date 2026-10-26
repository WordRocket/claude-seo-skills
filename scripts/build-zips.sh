#!/bin/sh
# Builds one .zip per skill into dist/ for uploading to claude.ai (Settings › Capabilities › Skills).
set -e
cd "$(dirname "$0")/.."
rm -rf dist && mkdir dist
cd plugins/seo/skills
for s in */; do
  s=${s%/}
  zip -qr "../../../dist/$s.zip" "$s" -x '*.DS_Store'
done
cd ../../..
ls -1 dist
