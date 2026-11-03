#!/usr/bin/env python3
"""Generate one image with GPT Image 2 on kie.ai (standard library only).

  export KIE_API_KEY=...            (set it yourself; never paste it into chat)
  python3 kie_generate.py --prompt-file prompt.txt --out thumb.png [--resolution 1K|2K|4K] [--aspect 16:9] [--image URL]

Creates a task (POST https://api.kie.ai/api/v1/jobs/createTask), polls it
(GET https://api.kie.ai/api/v1/jobs/recordInfo?taskId=...) and downloads the first result.
--image switches to image-to-image (input_urls). If kie.ai renames a field, see docs.kie.ai › Market › GPT Image 2.
"""
import argparse
import json
import os
import sys
import time
import urllib.request

API = 'https://api.kie.ai/api/v1/jobs'

ap = argparse.ArgumentParser()
ap.add_argument('--prompt-file', required=True)
ap.add_argument('--out', required=True)
ap.add_argument('--resolution', default='2K', choices=['1K', '2K', '4K'])
ap.add_argument('--aspect', default='16:9')
ap.add_argument('--image', action='append', help='reference image URL (image-to-image); repeatable')
a = ap.parse_args()

key = os.environ.get('KIE_API_KEY')
if not key:
    sys.exit('Set KIE_API_KEY in your environment first (kie.ai › API Keys).')
H = {'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'}


def call(url, body=None):
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body is not None else None, headers=H, method='POST' if body is not None else 'GET')
    with urllib.request.urlopen(req, timeout=60) as r:
        d = json.load(r)
    if d.get('code') != 200:
        sys.exit(f"kie.ai error {d.get('code')}: {d.get('msg')}")
    return d['data']


prompt = open(a.prompt_file, encoding='utf-8').read().strip()
inp = {'prompt': prompt, 'aspect_ratio': a.aspect, 'resolution': a.resolution}
model = 'gpt-image-2-text-to-image'
if a.image:
    model = 'gpt-image-2-image-to-image'
    inp['input_urls'] = a.image
task = call(f'{API}/createTask', {'model': model, 'input': inp})['taskId']
print(f'task {task} ({model}, {a.resolution})')
for _ in range(120):
    time.sleep(5)
    d = call(f'{API}/recordInfo?taskId={task}')
    if d.get('state') == 'success':
        url = json.loads(d['resultJson'])['resultUrls'][0]
        urllib.request.urlretrieve(url, a.out)
        print(f'✓ {a.out}')
        break
    if d.get('state') == 'fail':
        sys.exit(f"generation failed: {d.get('failMsg')}")
else:
    sys.exit('timed out waiting for kie.ai')
