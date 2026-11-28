"""Enchant search for the item pool tank sets (18 November 2026).

The wowsims default sets of the Protection Paladin and the Bear Druid have no enchants. FEEDBACK_ITEMS keeps the
enchants of the default set on their slots, thus the Paladin and Druid item pool sets ran with no enchants, and the
Warrior set with 9 enchants. This search gives the three tanks the same enchant rules:

- Each slot with an item takes the enchant that gives the best score (the score of search_tank.py: threat score for
  the threat sets, survival score for the survival sets).
- Candidates: the enchants of the wowsims database for the slot, with a source in the game data, and no source in a raid
  (Zul'Gurub, Molten Core, Blackwing Lair, Onyxia, Ahn'Qiraj, Naxxramas), not at Revered or Exalted reputation, and phase 1
  in the database (phase 2 holds the Zul'Gurub and later enchants, for example Core Armor Kit). These are the item pool rules.
  Enchants for resistance, Spirit, mana, healing only, skills and speed are not candidates.
- Start: the enchants of the default set (Warrior: the prebis set; Paladin and Druid: none). Each slot in turn tries all
  candidates (1,000 iterations, the same seed). A candidate replaces the enchant only if the score is more than 0.2%
  better. Two passes at most. Final: 3,000 iterations.
- Consumables: FEEDBACK_CONSUMES=full (threat sets) or fullsurv (survival sets, with Greater Stoneshield Potion).

Usage: [ENCH_START='[...]'] python3 search_enchants.py <wowsims clone> <prot|war|bear> [surv]. Needs the test binaries of run_pool.sh in /tmp/bin.
Output: enchants_<tank>[_surv].json (17 enchant ids) and the log on stdout (log_ench_<tank>[_surv].txt).
"""
import json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

W, tank = sys.argv[1], sys.argv[2]
surv = len(sys.argv) > 3 and sys.argv[3] == 'surv'
D = os.path.dirname(os.path.abspath(__file__))
db = json.load(open(os.path.join(W, 'assets/database/db.json')))
items = {i['id']: i for i in db['items']}
BIN = {'prot': ('/tmp/bin/prottest', 'sim/paladin/protection', 'TestFeedbackRun', 'set_prot', 'paladin/protection', 'default'),
       'war': ('/tmp/bin/wartest', 'sim/warrior/protection', 'TestFeedbackRun', 'set_war', 'warrior/protection', 'prebis'),
       'bear': ('/tmp/bin/beartest', 'sim/druid/feralbear', 'TestFeedbackBear', 'set_bear', 'druid/feralbear', 'default')}
b, cwd, test, setf, spec, gear = BIN[tank]
SET = json.load(open(os.path.join(D, setf + ('_surv' if surv else '') + '.json')))
RAID = {1977, 2717, 2677, 2159, 3428, 3429, 3456}
SLOT_TYPE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 12, 12, 13, 13, 14]
USEFUL = {0, 1, 2, 14, 16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 28}  # Str, Agi, Sta, AP, Feral AP, hit, crit, haste, defense, block, block value, dodge, parry, armor
if tank == 'prot':
    USEFUL |= {3, 5, 9}  # Intellect, spell damage, Holy damage
PROCS = {1900, 803, 1894, 1898, 1899, 1897, 1896, 8216, 8217, 8721, 2543, 2545, 863, 1704, 463}
if tank == 'prot':
    # 19 November 2026: no Protection ability procs Revelation (8217) in game. In wowsims, only the heal of Judgement
    # of Light procs it, and the next Judgement of Fury then crits (+2% threat). Thus the Paladin tank sets do not use it.
    PROCS.discard(8217)

def legal(e):
    srcs = e.get('sources') or []
    if any('drop' in s and s['drop'].get('zoneId') in RAID for s in srcs): return False  # also the Zul'Gurub quest enchants
    if any('rep' in s and s['rep'].get('repLevel', 0) >= 6 for s in srcs): return False  # Revered or Exalted
    if e.get('phase', 1) >= 2: return False  # later content (Zul'Gurub patch and later, Molten Core formulas)
    return bool(srcs)

def useful(e):
    st = e.get('stats', [])
    return e['effectId'] in PROCS or any(v and i in USEFUL for i, v in enumerate(st))

def fits(e, slot, item):
    types = [e.get('type')] + e.get('extraTypes', [])
    if SLOT_TYPE[slot] not in types: return False
    if SLOT_TYPE[slot] != 13: return True
    et, ht, wt = e.get('enchantType', 0), item.get('handType'), item.get('weaponType')
    if wt == 7: return et == 2
    if slot == 15: return et == 5
    if et == 1: return ht == 4
    return et in (0, 4) if wt == 8 else et == 0

def default_enchants():
    gs = os.path.join(W, 'ui/specs', spec, 'gear_sets')
    f = [x for x in os.listdir(gs) if x.startswith(gear + '.gear')][0]
    if f.endswith('.json'):
        return [x.get('enchant', 0) for x in json.load(open(os.path.join(gs, f)))['items']] + [0] * 17
    return None  # the siml default sets of the Paladin and the Druid have no enchants (checked)

def run(ench, iters):
    env = dict(os.environ, FEEDBACK_DUR='180', FEEDBACK_ITER=str(iters), FEEDBACK_ITEMS=','.join(map(str, SET)),
               FEEDBACK_CONSUMES='fullsurv' if surv else 'full', FEEDBACK_ENCHANTS=','.join(map(str, ench)))
    out = subprocess.run([b, '-test.run', test, '-test.v'], cwd=os.path.join(W, cwd), env=env, capture_output=True, text=True).stdout
    r = {}
    for l in out.splitlines():
        if l.startswith('TMI avg='): r['tmi'] = float(l.split()[1].split('=')[1])
        if l.startswith('RESULT'):
            for kv in l.split():
                if '=' in kv:
                    k, v = kv.split('=', 1)
                    try: r[k] = float(v.rstrip('%'))
                    except ValueError: pass
    if 'dps' not in r: r['dps'] = 1.0
    return r

def score(r, ref):
    if surv: return 0.4 * r['tps'] / ref['tps'] + 0.3 * ref['dtps'] / r['dtps'] + 0.3 * ref['tmi'] / r['tmi']
    return 0.4 * r['tps'] / ref['tps'] + 0.2 * r['dps'] / ref['dps'] + 0.2 * ref['dtps'] / r['dtps'] + 0.2 * ref['tmi'] / r['tmi']

E_ALL = [e for e in db['enchants'] if legal(e) and useful(e)]
name = {e['effectId']: e['name'] for e in db['enchants']}
# 28 November 2026: wowsims dc09e002f0 has no Warrior prebis file (now prebis_balanced and prebis_offensive). ENCH_START
# gives the start enchants as a JSON list, for example the START line of the earlier log.
de = json.loads(os.environ['ENCH_START']) if os.environ.get('ENCH_START') else default_enchants()
cur = [(de[s] if de and SET[s] else 0) for s in range(17)]
start = list(cur)
ref = run(cur, 1000)
print('START', json.dumps(cur), json.dumps(ref), flush=True)
base = ref
for p in range(2):
    changed = False
    for s in range(17):
        if not SET[s]: continue
        cands = sorted({e['effectId'] for e in E_ALL if fits(e, s, items[SET[s]])} | {0})
        if len(cands) < 2: continue
        tries = [cur[:s] + [c] + cur[s + 1:] for c in cands]
        with ThreadPoolExecutor(4) as ex: res = list(ex.map(lambda x: run(x, 1000), tries))
        rank = sorted(zip(cands, res), key=lambda z: -score(z[1], ref))
        print('SLOT', s, items[SET[s]]['name'], ' '.join(f"{c}:{round(score(r, ref), 4)}" for c, r in rank[:5]), flush=True)
        bc, br = rank[0]
        cr = dict(zip(cands, res))[cur[s]]
        if bc != cur[s] and score(br, ref) > score(cr, ref) * 1.002:
            print('  ->', name.get(cur[s], 'none'), '=>', name.get(bc), flush=True)
            cur[s], changed = bc, True
    if not changed: break
fin_old, fin_new = run(start, 3000), run(cur, 3000)
print('FINAL start', json.dumps(start), json.dumps(fin_old))
print('FINAL new', json.dumps(cur), json.dumps(fin_new), 'score', round(score(fin_new, fin_old), 4))
print('ENCHANTS', ' | '.join(f"{s}:{name.get(e)}" for s, e in enumerate(cur) if e))
json.dump(cur, open(os.path.join(D, f"enchants_{tank}{'_surv' if surv else ''}.json"), 'w'))
