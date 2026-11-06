import json, sys, os
from opt import *
spec=sys.argv[1]; c=CLASS[spec]
req=json.load(open(f'/tmp/zzdump/Test{spec}-Average-Default.json'))
start=req['raid']['parties'][0]['players'][0]['equipment']['items']
if spec=='DpsWarrior': start=json.load(open(f'{W}/ui/specs/warrior/dps/gear_sets/prebis_fury.gear.json'))['items']
start=(start+[{}]*17)[:17]
caster=c in (8,9)
mh=by.get(start[14].get('id'),{}); twoh=mh.get('handType')==4
dual=bool(start[15].get('id'))
pool=[it for it in d['items'] if pre_raid(it) and ok_class(it,c) and 'randomSuffixOptions' not in it and ilvl(it)>=45]
def fits(it,slot):
    t=it.get('type')
    if slot<14: return t==SLOT_TYPE[slot]
    if slot==14: return t==13 and ((it.get('handType')==4) if twoh else it.get('handType') in (1,2)) and it.get('weaponType')!=5
    if slot==15:
        if not dual: return False
        if caster: return t==13 and it.get('weaponType')==5
        return t==13 and it.get('handType') in (2,3) and it.get('weaponType') not in (5,7)
    return t==14
items=[{'id':x['id']} if x.get('id') and x['id'] in by and pre_raid(by[x['id']]) and not x.get('randomSuffix') else {} for x in start]
# SEED=<set file>: start from that set (the run of 6 November 2026 starts from the sets of sets_9a8624af9/)
if os.environ.get('SEED'): items=[{'id':x['id']} if x.get('id') else {} for x in json.load(open(os.environ['SEED']))['items']]
log=open(f'/tmp/ms/log_{spec}.txt','w')
def P(*a):
    print(*a); print(*a,file=log); log.flush()
w,pw=ep(spec,[{'id':x['id']} if x.get('id') else {} for x in start] if os.environ.get('EPFULL') else items); P('EP',{k:round(v,3) for k,v in w.items()},pw)
cand={}
for s in range(17):
    L=[it for it in pool if fits(it,s)]
    L.sort(key=lambda it:-score(it,w,pw,s))
    n=25 if s>=14 else 15
    eff=[it for it in L if it.get('itemEffects')][: (15 if s>=12 else 8)]
    if s in (12,13): eff=[it for it in L if it.get('itemEffects')]
    cand[s]=[it['id'] for it in L[:n]]+[it['id'] for it in eff if it['id'] not in [x['id'] for x in L[:n]]]
P('cands',{s:len(v) for s,v in cand.items()})
# fill empty slots with EP best
for s in range(17):
    if not items[s] and cand[s]:
        for i in cand[s]:
            if s in (11,13) and items[s-1].get('id')==i: continue
            if s in (10,12) and items[s+1].get('id')==i: continue
            items[s]={'id':i}; break
def val(it,iters=1000): return run([{'spec':spec,'items':it,'iters':iters}])[0]['dps']
best=val(items); P('start',round(best,1))
for p in range(3):
    imp=False
    for s in range(17):
        if not cand[s]: continue
        other={10:11,11:10,12:13,13:12}.get(s)
        jobs=[]; ids=[]
        for i in cand[s]:
            if i==items[s].get('id'): continue
            if other is not None and items[other].get('id')==i: continue
            if s==14 and dual and items[15].get('id')==i and by[i].get('unique'): continue
            t=[dict(x) for x in items]; t[s]={'id':i}; jobs.append({'spec':spec,'items':t,'iters':1000}); ids.append(i)
        if not jobs: continue
        r=run(jobs); k=max(range(len(r)),key=lambda k:r[k]['dps'])
        if r[k]['dps']>best*1.002:
            P(f'  pass{p} slot{s}: {by[items[s]["id"]]["name"] if items[s].get("id") else "-"} -> {by[ids[k]]["name"]} {best:.1f}->{r[k]["dps"]:.1f}')
            items[s]={'id':ids[k]}; best=r[k]['dps']; imp=True
    if not imp: break
fin=run([{'spec':spec,'items':items,'iters':10000}])[0]
P('FINAL',spec,round(fin['dps'],1),'+-',round(fin['sd']/100,1))
P('SET',' ; '.join(f"{by[x['id']]['name']}({ilvl(by[x['id']])})" for x in items if x.get('id')))
il=[ilvl(by[x['id']]) for x in items if x.get('id')]; q=[by[x['id']].get('quality') for x in items if x.get('id')]
P('ILVL',round(sum(il)/len(il),1),'epics',q.count(4))
json.dump({'spec':spec,'dps':fin['dps'],'items':items},open(f'/tmp/ms/set_{spec}.json','w'))
