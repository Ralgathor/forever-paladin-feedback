"""Holy proposals on the beta of 30 October: Reverence 50% (C-H1) and Lingering Light (C-H2, withdrawn on 31 October).
Run: python3 holy_proposals_b2.py"""
import sys
import os; D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(D, "..", "healing")); sys.path.insert(0, D)
import healing_model as H
from healing_model import Spell, cd_limit, regen_full, solve, priest, druid, shaman, max_hps, HPG, CRIT_BASE, PAL_CRIT, HOT_CRIT, ll_end_pool
import healing_b2 as B

def pal(hp=HPG, tank=False, oath=None, bonus=1.25, conv=0.06, boundless=0.30, light=1.12, rev=0.30, illum=0.50, bened=0.10, ling=0.0, df_cd=120, infall=False):
    if oath is None: oath = tank
    c = CRIT_BASE + PAL_CRIT + conv
    c_hs = c + (0 if oath else boundless)
    o = (lambda v: v) if oath else (lambda v: 0)
    fol = (308 + o(115) + 1.5/3.5*hp) * light
    hl = (1580 + o(400) + 2.5/3.5*hp) * light
    hs = (320 + o(229) + 1.5/3.5*hp) * light
    kt = (1 + bonus*c) if HOT_CRIT else 1.0
    def direct(h, cc, oh):
        ll = ling * h*(1+bonus) * cc * kt      # 10/20% of the full critical heal, ticks can crit
        r = h*(1 + bonus*cc)
        return r + ll, r*(1-oh) + ll*0.5
    fol_r, fol_e = direct(fol, c, 0.15); hl_r, hl_e = direct(hl, c, 0.20); hs_r, hs_e = direct(hs, c_hs, 0.15)
    fol_cost = 140 - illum*140*c; hl_cost = 660 - illum*660*c; hs_cost = 325*(1-bened) - illum*325*c_hs
    p_inf = 1.0 if infall else c
    sp = []
    df = hl*(1+bonus); dfl = ling*df*kt
    sp.append(Spell("Divine Favor + Holy Light", df+dfl, df*0.8+dfl*0.5, 660 - illum*660 + 0.04*1512, 2.5, maxn=cd_limit(df_cd, 2.5)))
    sp.append(Spell("Holy Shock", hs_r, hs_e, hs_cost, 1.5, maxn=cd_limit(10, 1.5)))
    lvh = 704 + 0.143*hp; p_any = 1 - (1-c)**5
    one_r, one_e = direct(lvh, c, 0.25)
    sp.append(Spell("Light's Vigil + Holy Shock", 5*one_r + hs_r, 5*one_e + hs_e, 1340 - illum*1340*p_any + hs_cost, 3.0, maxn=cd_limit(6, 3.0), tank=(one_r + hs_r)/(5*one_r + hs_r)))
    sp.append(Spell("Flash of Light", fol_r, fol_e, fol_cost, 1.5))
    sp.append(Spell("Flash of Light, Holy Light on Infusion", fol_r + p_inf*hl_r, fol_e + p_inf*hl_e, fol_cost + p_inf*hl_cost, 1.5 + p_inf*1.5))
    sp.append(Spell("Holy Light", hl_r, hl_e, hl_cost, 2.5))
    end = ll_end_pool(fol*(1+bonus)/1.5, c, ling) * kt if ling else 0.0
    return dict(cls="Paladin", pool=1512 - 280 + 15*438, regen=regen_full("pal", 336), castfrac=rev, extra=None, spells=sp, groups={}, crit=c, end_loss=(end, end*0.5))

# sanity: equal to healing_b2 with ling=0
assert abs(solve(pal(715,False),180,False)["eff"]-solve(B.paladin_b2(715,False),180,False)["eff"])<1
TS=(180,300,600)
cases=[("Beta 30 Oct",{}),("+ Lingering Light 1/2",dict(ling=0.10)),("+ Lingering Light 2/2",dict(ling=0.20)),
       ("+ Reverence 50%",dict(rev=0.50)),("+ Rev 50% + LL 2/2",dict(rev=0.50,ling=0.20)),("+ Rev 50% + LL 1/2",dict(rev=0.50,ling=0.10)),
       ("+ Rev 50% + LL 2/2 + Infusion all",dict(rev=0.50,ling=0.20,infall=True)),
       ("175%: beta",dict(bonus=0.75)),("175%: + Rev 50% + LL 2/2",dict(bonus=0.75,rev=0.50,ling=0.20))]
for hp in (715,900):
  for tank in (False,True):
    O={T:B.others(hp,T,tank) for T in TS}
    print(f"## {'tank' if tank else 'raid'} {hp}: Druid "+" | ".join(f"{O[T]['Druid']:.0f}" for T in TS)+"  Shaman "+" | ".join(f"{O[T]['Shaman']:.0f}" for T in TS)+"  Priest "+" | ".join(f"{O[T]['Priest']:.0f}" for T in TS))
    for n,kw in cases:
      v={T:solve(pal(hp,tank,**kw),T,tank)["eff"] for T in TS}
      print(f"  {n:36s} "+" | ".join(f"{v[T]:4.0f} (Dru {v[T]/O[T]['Druid']-1:+4.0%})" for T in TS))
  print("  max raw HPS tank:", {n:round(max_hps(pal(hp,True,**kw))) for n,kw in cases[:5]}, "Druid", round(max_hps(druid(hp,tank=True))))
