# Tank sets with the rules of the damage item pool (matched_gear/opt.py, pre_raid).
# Each item of the default wowsims tank set that breaks a rule is replaced by an item of the pool
# in the same slot. Candidates: the 12 pool items with the best tank stat sum for the slot.
# No item twice (quest rewards are once only). Each candidate runs in the full set (1,000 iterations); the best score is kept, slot by slot.
# Score (as search.py): 40% threat, 20% damage, 20% damage taken, 20% TMI, each against the default set.
# Usage: python3 search_tank.py <prot|war|bear> <dumped request> ; needs /tmp/zztank (zztank_main.go).
import json, os, subprocess, sys, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'matched_gear'))
from opt import d, by, pre_raid, ok_class, ilvl, st, SLOT_TYPE, ARMOR, WEAP, RANGED
ARMOR[11] = {1, 2}; WEAP[11] = {2, 3, 4, 8}; RANGED[11] = {9}
WEAP[1] = WEAP[1] | {7}; WEAP[2] = WEAP[2] | {7}  # shields for the two shield tanks
CLS = {'prot': 2, 'war': 1, 'bear': 11}
# Tank stat sum for the candidate list only (the sim gives the final choice). Stat ids: sim/core/stats/stats.go.
W = {'prot': {0: .5, 1: .5, 2: 1, 3: .2, 9: .3, 17: .8, 22: 1.2, 23: .8, 24: .3, 25: 1.5, 26: 1.2, 27: .06, 28: .06, 14: .2, 5: .2},
     'war': {0: .6, 1: .6, 2: 1, 17: .8, 18: .6, 22: 1.2, 23: .8, 24: .3, 25: 1.5, 26: 1.2, 27: .06, 28: .06, 14: .3},
     'bear': {0: .8, 1: 1, 2: 1, 17: 1, 18: .8, 22: 1.2, 25: 1.5, 27: .1, 28: .1, 14: .4, 16: .4}}
tank, dump = sys.argv[1], sys.argv[2]
c = CLS[tank]
req = json.load(open(dump))
start = [x.get('id', 0) for x in (req['raid']['parties'][0]['players'][0]['equipment']['items'] + [{}] * 17)[:17]]
twoh = by.get(start[14], {}).get('handType') == 4
pool = [it for it in d['items'] if pre_raid(it) and ok_class(it, c) and 'randomSuffixOptions' not in it and ilvl(it) >= 45]
def fits(it, s):
    t = it.get('type')
    if s < 14: return t == SLOT_TYPE[s]
    if s == 14: return t == 13 and ((it.get('handType') == 4) if twoh else it.get('handType') in (1, 2)) and it.get('weaponType') not in (5, 7)
    if s == 15: return t == 13 and it.get('weaponType') == 7
    return t == 14
def val(it): return sum(W[tank].get(k, 0) * v for k, v in st(it).items())
def run(sets, iters):
    jobs = [{'file': dump, 'items': s, 'iters': iters} for s in sets]
    n = 4; parts = [jobs[i::n] for i in range(n)]; procs = []
    for p in parts:
        if not p: continue
        fi = tempfile.mktemp(suffix='.json'); json.dump(p, open(fi, 'w'))
        procs.append((subprocess.Popen(['/tmp/zztank', fi, fi + '.out']), fi, len(p)))
    res = [None] * len(jobs); k = 0
    for i, (pr, fi, m) in enumerate(procs):
        pr.wait(); r = json.load(open(fi + '.out'))
        for j, x in enumerate(r): res[i + j * n] = x
    return res
def score(r, ref): return 0.4 * r['tps'] / ref['tps'] + 0.2 * r['dps'] / ref['dps'] + 0.2 * ref['dtps'] / r['dtps'] + 0.2 * ref['tmi'] / r['tmi']
def name(i): return by[i]['name'] if i in by else '-'
ref = run([start], 1000)[0]
bad = [s for s, i in enumerate(start) if i and not pre_raid(by[i])]
print('DEFAULT', json.dumps(ref)); print('OUT OF POOL', [(s, name(start[s])) for s in bad])
cur = list(start)
for s in bad: cur[s] = 0
for s in bad:
    used = set(cur)
    L = sorted([it for it in pool if fits(it, s) and it['id'] not in used], key=lambda it: -val(it))[:12]
    sets = []
    for it in L:
        x = list(cur); x[s] = it['id']; sets.append(x)
    res = run(sets, 1000)
    best = max(zip(L, res), key=lambda z: score(z[1], ref))
    cur[s] = best[0]['id']
    print('SLOT', s, name(start[s]), '->', best[0]['name'], ilvl(best[0]), round(score(best[1], ref), 4), [(it['name'], round(score(r, ref), 4)) for it, r in zip(L, res)])
fin = run([start, cur], 3000)
print('FINAL default', json.dumps(fin[0])); print('FINAL pool', json.dumps(fin[1]))
print('SET', json.dumps(cur)); print('SETNAMES', ' ; '.join(name(i) for i in cur))
