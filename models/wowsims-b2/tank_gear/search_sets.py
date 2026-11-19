# Set bonus search (19 November 2026). The open search (search_open.py) changes one slot at a time, thus it cannot find
# a set bonus that needs several pieces. For each item set with pool pieces in 2 or more slots, this search puts k pieces
# of the set in the set_<tank>[SUF].json set (k = 2 to all slots). For each k, it takes the k slots where the set piece
# has the best tank stat sum over the current item. Each candidate runs 1,000 iterations, the best ones 5,000.
# The score is as in search_tank.py, against the current set (1.0 = no change).
# Usage: [TANK_SCORE=survival SUF=_surv] python3 search_sets.py <prot|war|bear> <dumped request of the current set>
import json, os, sys
from collections import defaultdict
TG = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TG + '/../matched_gear')
src = open(TG + '/search_tank.py').read()
exec(src.split("tank, dump = sys.argv[1], sys.argv[2]")[0])
tank, dump = sys.argv[1], sys.argv[2]
c = CLS[tank]
req = json.load(open(dump))
cur = [x.get('id', 0) for x in (req['raid']['parties'][0]['players'][0]['equipment']['items'] + [{}] * 17)[:17]]
SUF = os.environ.get('SUF', '')
assert cur == json.load(open(TG + f'/set_{tank}{SUF}.json')), 'the dump is not the current set'
twoh = by.get(cur[14], {}).get('handType') == 4
pool = [it for it in d['items'] if pre_raid(it) and ok_class(it, c) and 'randomSuffixOptions' not in it and ilvl(it) >= 45]
exec("def fits(it, s):" + src.split("def fits(it, s):")[1].split("def name(i)")[0])
def name(i): return by[i]['name'] if i in by else '-'
base = run([cur], 1000)[0]
sets = defaultdict(list)
for it in pool:
    if it.get('setId'): sets[(it['setId'], it.get('setName'))].append(it)
cands = []
for (sid, sn), L in sets.items():
    best = {}
    for s in range(17):
        if not cur[s]: continue
        F = sorted([it for it in L if fits(it, s)], key=lambda it: -val(it))
        if F: best[s] = F
    if len(best) < 2: continue
    gain = lambda s: val(best[s][0]) - (val(by[cur[s]]) if cur[s] in by else 0)
    order = sorted(best, key=lambda s: -gain(s))
    for k in range(2, len(order) + 1):
        new = list(cur); used = set()
        for s in order[:k]:
            pick = next((it for it in best[s] if it['id'] not in used), None)
            if pick: new[s] = pick['id']; used.add(pick['id'])
        if sum(1 for i in new if by.get(i, {}).get('setId') == sid) < 2 or new == cur: continue
        cands.append((sn, k, new))
print('BASE', json.dumps(base), 'CANDIDATES', len(cands), 'SETS', len(set(x[0] for x in cands)), flush=True)
res = run([x[2] for x in cands], 1000)
rows = sorted(zip(cands, res), key=lambda z: -score(z[1], base))
for (sn, k, new), r in rows[:25]:
    print('C1000', sn, k, round(score(r, base), 4), json.dumps(r), flush=True)
top = [z for z in rows if score(z[1], base) > 0.995][:8]
if top:
    fin = run([cur] + [z[0][2] for z in top], 5000)
    print('BASE5000', json.dumps(fin[0]))
    for ((sn, k, new), _), r in zip(top, fin[1:]):
        print('C5000', sn, k, round(score(r, fin[0]), 4), json.dumps(r), 'SET', json.dumps(new), '|', ' ; '.join(name(i) for i, j in zip(new, cur) if i != j))
