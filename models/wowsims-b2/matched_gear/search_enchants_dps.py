"""Enchant search for the matched damage sets (18 November 2026).

enchants.json held the wowsims preset enchants. They do not obey the item pool rules for all specs, and the presets
are not equal: Retribution had Lesser Agility (+3) on the cloak and Healing Power (Argent Dawn, Exalted) on the
bracers; the Rogue had Enchant Weapon - Agility (Timbermaw Hold, Revered) on the off hand; the Hunter had no head
enchant and a Zul'Gurub scope; Mage and Warlock had the Molten Core weapon enchant. This search gives each spec the same
rules as the tank enchant search (../tank_gear/search_enchants.py):

- Candidates: the enchants of the database for the slot, with a source, phase 1, no raid source and no Revered or
  Exalted reputation. Scopes only on bows, guns and crossbows.
- Start: enchants.json. Each slot in turn tries all candidates (zzbatch, one job for each process, 1,000 iterations,
  enchants and consumables of the second run, /tmp/zzdump_u). A candidate replaces the enchant only if the DPS is more
  than 0.2% higher. Two passes at most. The result is enchants_fair.json.
- A start enchant that breaks the rules is removed first.

Usage: python3 search_enchants_dps.py <wowsims clone> <Spec>. Needs /tmp/ms/zzbatch and /tmp/zzdump_u (enchants_consumables.py).
"""
import json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

W, spec = sys.argv[1], sys.argv[2]
D = os.path.dirname(os.path.abspath(__file__))
db = json.load(open(os.path.join(W, 'assets/database/db.json')))
items = {i['id']: i for i in db['items']}
name = {e['effectId']: e['name'] for e in db['enchants']}
RAID = {1977, 2717, 2677, 2159, 3428, 3429, 3456}
SLOT_TYPE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 12, 12, 13, 13, 14]
CASTER = spec in ('Fire', 'DemonologyFireBrand')
USEFUL = {3, 5, 6, 7, 8, 11, 17, 18, 19} if CASTER else {0, 1, 14, 15, 17, 18, 19, 20}
PROCS = {1900, 803, 1894, 1898, 1899, 1897, 1896, 963, 8205, 8216, 8217, 8721, 2543, 30, 32, 33, 663, 664, 8720, 2523}

def legal(e):
    srcs = e.get('sources') or []
    if any('drop' in s and s['drop'].get('zoneId') in RAID for s in srcs): return False
    if any('rep' in s and s['rep'].get('repLevel', 0) >= 6 for s in srcs): return False
    if e.get('phase', 1) >= 2: return False
    return bool(srcs)

def useful(e):
    return e['effectId'] in PROCS or any(v and i in USEFUL for i, v in enumerate(e.get('stats', [])))

def fits(e, slot, item):
    types = [e.get('type')] + e.get('extraTypes', [])
    if SLOT_TYPE[slot] not in types: return False
    if SLOT_TYPE[slot] == 14: return item.get('rangedWeaponType') in (1, 2, 3)
    if SLOT_TYPE[slot] != 13: return True
    et, ht, wt = e.get('enchantType', 0), item.get('handType'), item.get('weaponType')
    if wt == 7: return et == 2
    if wt == 5: return et == 5
    if et == 1: return ht == 4
    return et in (0, 4) if wt == 8 else et == 0

SET = json.load(open(os.path.join(D, f'set_{spec}.json')))['items']
E0 = json.load(open(os.path.join(D, 'enchants.json')))[spec]
cur = [int(E0.get(str(s), 0)) if SET[s].get('id') else 0 for s in range(17)]
ok = {e['effectId'] for e in db['enchants'] if legal(e)}
for s in range(17):
    if cur[s] and cur[s] not in ok:
        print('REMOVE', s, name.get(cur[s]), flush=True); cur[s] = 0
os.makedirs('/tmp/ms/solo', exist_ok=True)
def run(ench, iters, tag):
    it = [dict(x, **({'enchant': e} if e and x.get('id') else {})) for x, e in zip(SET, ench)]
    for x in it:
        if not x.get('enchant'): x.pop('enchant', None)
    f = f'/tmp/ms/solo/ench_{spec}_{tag}'
    json.dump([{'spec': spec, 'items': it, 'cons': True, 'iters': iters, 'dir': '/tmp/zzdump_u'}], open(f + '.in', 'w'))
    subprocess.run(['/tmp/ms/zzbatch', f + '.in', f + '.out'], capture_output=True)
    return json.load(open(f + '.out'))[0]['dps']
start = list(cur)
E_ALL = [e for e in db['enchants'] if legal(e) and useful(e)]
ref = run(cur, 1000, 'ref'); print('START', json.dumps(start), round(ref, 1), flush=True)
for p in range(2):
    changed = False
    for s in range(17):
        if not SET[s].get('id'): continue
        cands = sorted({e['effectId'] for e in E_ALL if fits(e, s, items[SET[s]['id']])} | {0, cur[s]})
        if len(cands) < 2: continue
        tries = [cur[:s] + [c] + cur[s + 1:] for c in cands]
        with ThreadPoolExecutor(4) as ex: res = list(ex.map(lambda z: run(z[1], 1000, f'{s}_{z[0]}'), enumerate(tries)))
        rank = sorted(zip(cands, res), key=lambda z: -z[1])
        print('SLOT', s, items[SET[s]['id']]['name'], ' '.join(f'{c}:{round(v, 1)}' for c, v in rank[:5]), flush=True)
        bc, bv = rank[0]; cv = dict(zip(cands, res))[cur[s]]
        if bc != cur[s] and bv > cv * 1.002:
            print('  ->', name.get(cur[s], 'none'), '=>', name.get(bc), flush=True); cur[s], changed = bc, True
    if not changed: break
print('FINAL', json.dumps(cur))
print('ENCHANTS', ' | '.join(f'{s}:{name.get(e)}' for s, e in enumerate(cur) if e))
out = os.path.join(D, 'enchants_fair.json')
allf = json.load(open(out)) if os.path.exists(out) else {}
allf[spec] = {str(s): e for s, e in enumerate(cur) if e}
json.dump(allf, open(out, 'w'))
