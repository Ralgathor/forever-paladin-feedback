# Open tank search (16 November 2026): each slot tries the 12 pool items with the best tank stat sum, the pool items with an
# implemented effect and, for the Paladin, the items with spell damage and Defense. Up to 3 passes over the 17 slots, from the set_<tank>[SUF].json set.
# Usage: [TANK_SCORE=survival SUF=_surv] [EFFECTS=<zzeffects list>] python3 search_open.py <prot|war|bear> <dump> pool  (relax: looser rules, test only)
import json, os, sys, time
TG=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TG+'/../matched_gear')
from opt import d, by, pre_raid, ok_class, ilvl, st, SLOT_TYPE, ARMOR, WEAP, RANGED, RAIDISH, PVP, PVPREP, RAID_ZONES, WORLD_BOSS, atl
ARMOR[11] = {1, 2}; WEAP[11] = {2, 3, 4, 8}; RANGED[11] = {9}
WEAP[1] = WEAP[1] | {7}; WEAP[2] = WEAP[2] | {7}
import importlib.util
src = open(TG+'/search_tank.py').read()
head = src.split("tank, dump = sys.argv[1], sys.argv[2]")[0]
exec(head)
tank, dump, mode = sys.argv[1], sys.argv[2], sys.argv[3]
c = CLS[tank]
def why(it):
    r=[]
    if 19000<=it['id']<24000: r.append('id')
    if ilvl(it)>63: r.append('ilvl')
    for s in (it.get('sources') or [])+atl.get(it['id'],[]):
        if (s.get('rep') or {}).get('repLevel',0)>=7: r.append('rep'); break
    return r
def relaxed(it):
    if ilvl(it)>66 or it['id'] in RAIDISH or it.get('quality',0)>4 or it.get('quality',0)<2: return False
    if it.get('reqLvl',0)>60: return False
    if any(p in it['name'] for p in PVP): return False
    if it.get('factionRestriction')==2: return False
    for s in (it.get('sources') or [])+atl.get(it['id'],[]):
        if 'pvp' in s or (s.get('rep') or {}).get('repFactionId') in PVPREP: return False
        dr=s.get('drop')
        if dr and (dr.get('zoneId') in RAID_ZONES or dr.get('npcId') in WORLD_BOSS): return False
    return True
P = pre_raid if mode=='pool' else relaxed
req = json.load(open(dump))
start = [x.get('id', 0) for x in (req['raid']['parties'][0]['players'][0]['equipment']['items'] + [{}] * 17)[:17]]
twoh = by.get(start[14], {}).get('handType') == 4
pool = [it for it in d['items'] if P(it) and ok_class(it, c) and 'randomSuffixOptions' not in it and ilvl(it) >= 45]
EFF = set(int(x) for x in open(os.environ.get('EFFECTS', TG+'/effects_6084403a9.txt')))
exec(src.split("def fits(it, s):")[1].split("def name(i)")[0].join(["def fits(it, s):",""]) if False else "def fits(it, s):"+src.split("def fits(it, s):")[1].split("def name(i)")[0])
def name(i): return by[i]['name'] if i in by else '-'
ref = run([start], 1000)[0]
SUF=os.environ.get('SUF','')
cur = json.load(open(TG+f'/set_{tank}{SUF}.json'))
base = run([cur], 1000)[0]
print('REF', json.dumps(ref)); print('BASE', round(score(base, ref),4), json.dumps(base), flush=True)
def spdef(it):
    x=st(it); return tank=='prot' and (x.get(5,0)+x.get(9,0))>0 and x.get(22,0)>0
for ps in range(3):
    changed=False
    print('PASS', ps, flush=True)
    for s in range(17):
        if not cur[s]: continue
        used = set(cur)
        L = sorted([it for it in pool if fits(it, s) and it['id'] not in used], key=lambda it: -val(it))[:12]
        L += [it for it in pool if fits(it, s) and it['id'] not in used and it['id'] in EFF and it.get('itemEffects') and it not in L]
        L += [it for it in pool if fits(it, s) and it['id'] not in used and spdef(it) and it not in L]
        if not L: continue
        res = run([[*cur[:s], it['id'], *cur[s+1:]] for it in L], 1000)
        best = max(zip(L, res), key=lambda z: score(z[1], ref))
        if score(best[1], ref) > score(base, ref) * 1.002:
            print('SLOT', s, name(cur[s]), '->', best[0]['name'], best[0]['id'], ilvl(best[0]), why(best[0]), round(score(base, ref),4), '->', round(score(best[1], ref),4), flush=True)
            cur[s] = best[0]['id']; base = best[1]; changed=True
    
    if not changed: break
fin = run([json.load(open(TG+f'/set_{tank}{SUF}.json')), cur], 3000)
print('FINAL old', json.dumps(fin[0]), round(score(fin[0], ref),4)); print('FINAL new', json.dumps(fin[1]), round(score(fin[1], ref),4))
print('SET', json.dumps(cur)); print('SETNAMES', ' ; '.join(name(i) for i in cur))
