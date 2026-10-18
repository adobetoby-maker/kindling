#!/usr/bin/env python3
"""Second controlled short-input hypothesis; no publication or canon changes."""
import importlib.util
import json
from pathlib import Path
import re
import sys

spec = importlib.util.spec_from_file_location('diagnostic_base', Path(__file__).with_name('nm-breeze-diagnostic.py'))
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
base.OUT = base.BOOK/'narration/breeze/diagnostic-short-heading-v2'


def prepare():
    directory = base.BOOK/'narration/breeze/chapter-09'
    track = json.loads((directory/'direction.json').read_text())
    source = base.BOOK/'manuscript/chapter-09.md'
    if base.sha(source) != track['sourceSha256']:
        raise ValueError('Stale source')
    ids = ['s252','s253','s254']
    selected = [s for s in track['segments'] if s['id'] in ids]
    if [s['id'] for s in selected] != ids:
        raise ValueError('Unexpected heading window')
    original = ' '.join(s['text'] for s in selected)
    if original.count('How: She stopped.') != 1:
        raise ValueError('Heading wording changed')
    text = original.replace('How: She stopped.', '“How.” She stopped.')
    words = lambda t: re.findall(r"[^\W_]+(?:'[^\W_]+)*", t.lower().replace('’', "'"))
    if words(text) != words(original):
        raise ValueError('Punctuation trial changed ordered words')
    return [{'name':'heading-with-preceding-context','chapter':9,
             'sourceSha256':base.sha(source), 'directionSha256':base.sha(directory/'direction.json'),
             'segmentIds':ids, 'original':original, 'text':text,
             'instruct':selected[0]['instruct']+' Read the written notebook heading How clearly as a label, once. Then fully return to base narrator for She stopped and the following narration. No added explanation.',
             'transformation':'Include preceding context, expose written heading with quotation/period punctuation only; exact ordered source words unchanged. Audition only.'}]


base.prepare = prepare
if __name__ == '__main__':
    {'render':base.render, 'verify':base.verify}[sys.argv[1]]()
