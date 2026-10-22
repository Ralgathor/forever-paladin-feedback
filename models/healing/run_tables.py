"""Tables of Analysis, Healing (proposals.md). Run: python3 run_tables.py
Raid and one-tank healing per sec after overhealing, for 3, 5 and 10 min fights."""
from healing_model import *
PROP = dict(rev=0.5, illum=0.75, light=1.30, bol=False, ling=0.2, conv=0.05, bened=0.09, inf_all=True)
def mk(cls, hp, T, tank=False, **kw):
    if cls=="sha": return shaman(hp, T=T, tank=tank)
    if cls=="pal": return paladin(hp, **kw)
    return {"pri":priest,"dru":druid}[cls](hp, tank=tank, **kw)
def row(hp, T, tank, **palkw):
    out={}
    for c in ("pri","dru","sha"):
        out[c]=best_over_fixed(mk(c,hp,T,tank),T,tank)["eff"]
    out["pal"]=best_over_fixed(mk("pal",hp,T,**palkw),T,tank)["eff"]
    return out

P=PROP; f=lambda x: f"{x:,.0f}"
cls=[("Priest","pri",{}),("Druid","dru",{}),("Shaman","sha",{}),("Paladin, beta","pal",{}),("Paladin, proposed","pal",P)]
print("## A. Mana (715)")
for n,c,kw in cls:
    k=mk(c,715,180,**kw)
    print(n, "pool",f(k['pool']), "regen while casting/s", round(k['castfrac']*k['regen'],1), "| budget 3/5/10:", " / ".join(f(budget(mk(c,715,T,**kw),T)) for T in (180,300,600)))
print("## B. spells (715, beta talents for Paladin; proposed in brackets)")
for n,c,kw in cls[:4]+[cls[4]]:
    k=mk(c,715,180,**kw); seen=set()
    for s in k['fixed']+k['fillers']:
        if s.name in seen: continue
        seen.add(s.name); print(f"  {n:18s} {s.name:42s} raw {s.raw/max(s.cost,1):5.2f} eff {s.eff/max(s.cost,1):5.2f}  cast {s.time} cd {s.cd}")
for hp in (715,900):
  for tank in (False,True):
    print(f"## {'one tank' if tank else 'raid'} HP {hp}")
    for n,c,kw in cls:
        vals=[best_over_fixed(mk(c,hp,T,tank,**kw) if c!='pal' else mk(c,hp,T,**kw),T,tank) for T in (180,300,600)]
        print(f"  {n:18s} " + " | ".join(f"{v['eff']:5.0f} ({v['filler'][:22]}; {','.join(k_[:10] for k_,x in v['casts'].items() if x)})" for v in vals))
  print("  max HPS one target:", {n: round(max_hps(mk(c,hp,180,True,**kw) if c!='pal' else mk(c,hp,180,**kw),tank=True)) for n,c,kw in cls})
print("## E. options (715): raid 3 min | tank 10 min")
o3=row(715,180,False); o10=row(715,600,True)
for n,kw in {"proposed":P,"HS heal x2":dict(P,hs_heal_mult=2.0),"HS heal x2.5":dict(P,hs_heal_mult=2.5),"HS cost x0.5":dict(P,hs_cost_mult=0.5),
             "LV cost x0.5":dict(P,lv_cost_mult=0.5),"LV heal x2":dict(P,lv_heal_mult=2.0),"LV heal x1.25":dict(P,lv_heal_mult=1.25)}.items():
    r=best_over_fixed(mk('pal',715,180,**kw),180,False)['eff']; t=best_over_fixed(mk('pal',715,600,**kw),600,True)['eff']
    print(f"  {n:14s} raid3 {r:5.0f} vs Pri {r/o3['pri']-1:+.0%} vs lowest {r/min(o3['sha'],o3['dru'])-1:+.0%} | tank10 {t:4.0f} vs best other {t/max(o10['pri'],o10['dru'],o10['sha'])-1:+.0%}")
