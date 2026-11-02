"""Enchants and consumables on the matched sets (2 November 2026).

1. Writes /tmp/zzdump_u: the dumped test requests, with the same elixirs and extra consumables for each spec
   (all elixirs and extras of the six test presets). Each spec keeps its own flask, food and potions.
   The Hunter preset has no flask: it takes the physical flask of Fury and Rogue (274274).
2. Writes ec_jobs.json for zzbatch: for each spec, base / enchants / consumables / both.
   Enchants: enchants.json (wowsims preset enchants by slot; Mage and Warlock: Balance pre-raid caster
   enchants, 2504 Weapon Spell Power on the main hand).
Fire Mage crashes with the full elixir list in wowsims 895cd67f9. It keeps its own preset consumables
(the physical elixirs do not help a caster: Demonology Warlock 862.8 with its own, 861.2 with the full list).
Run: python3 enchants_consumables.py; zzbatch ec_jobs.json ec_out.json
"""
import json, os
S = ['DpsWarrior', 'Rogue', 'Hunter', 'Retribution', 'Fire', 'DemonologyFireBrand']
D = {s: json.load(open(f'/tmp/zzdump/Test{s}-Average-Default.json')) for s in S}
cons = lambda d: d['raid']['parties'][0]['players'][0].setdefault('consumables', {})
el, ex = set(), set()
for d in D.values():
    el |= set(cons(d).get('elixirIds', [])); ex |= set(cons(d).get('extraIds', []))
os.makedirs('/tmp/zzdump_u', exist_ok=True)
for s, d in D.items():
    c = cons(d)
    if s != 'Fire':
        c['elixirIds'], c['extraIds'] = sorted(el), sorted(ex)
    if s == 'Hunter':
        c['flaskId'] = 274274
    json.dump(d, open(f'/tmp/zzdump_u/Test{s}-Average-Default.json', 'w'))
E = json.load(open('enchants.json'))
jobs = []
for s in S:
    items = json.load(open(f'set_{s}.json'))['items']
    e = E[s]
    ie = [dict(x, **({'enchant': e[str(k)]} if str(k) in e and x.get('id') else {})) for k, x in enumerate(items)]
    for lab, it, c in (('base', items, False), ('ench', ie, False), ('cons', items, True), ('both', ie, True)):
        jobs.append({'spec': s, 'items': it, 'cons': c, 'iters': 10000, 'label': lab, 'dir': '/tmp/zzdump_u'})
json.dump(jobs, open('ec_jobs.json', 'w'))
