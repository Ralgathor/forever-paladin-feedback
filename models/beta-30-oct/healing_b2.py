"""Holy Paladin on the beta of 30 October 2026 (wowsims Forever, branch paladin/hotfix-113554-port, push 113554).
Uses models/healing/healing_model.py of the repo for the Priest, the Druid, the Shaman and the solver.
Run from the repo: python3 healing_b2.py <repo>/models/healing

Changes against the beta of 18 October (healing_model.paladin defaults):
- No Blessing of Light. Oath of Light on one ally: Holy Light +400, Flash of Light +115, Holy Shock +229 (only there).
- Holy Power 5/5: no critical chance. The critical heal multiplier x1.5: 150% -> 225% (wowsims and the server rule,
  aura A_MOD_CRITICAL_HEALING_AMOUNT). The low case reads the text as +50% of the bonus: 175%.
- Boundless Light 2/2: Holy Shock +30% critical chance on an ally with no Oath of Light. bl_fol: the same for Flash of Light (a withdrawn idea, see Withdrawn ideas).
- Build 38/5/8: Holy (no Divine Strength, no Divine Precision, Purifying Power 1), Divine Intellect 5/5,
  Benediction 5/5, Conviction 3/3 (+6% critical chance, all spells). Reverence 2/2 = 30% (as before).
- Light's Vigil rank 3: no change in cost or heal (only the range, 20 -> 40 yd).
"""
import sys
sys.path.insert(0, sys.argv[1] if len(sys.argv) > 1 else ".")
import healing_model as H
from healing_model import Spell, cd_limit, regen_full, solve, priest, druid, shaman, budget, max_hps, HPG, CRIT_BASE, PAL_CRIT

def paladin_b2(hp=HPG, tank=False, oath=None, bonus=1.25, conv=0.06, boundless=0.30, light=1.12, rev=0.30,
               illum=0.50, bened=0.10, lv=True, df_cd=120, bl_fol=0.0):
    """oath: Oath of Light on the healed target (default: True on one tank, False in the raid).
    bonus: critical heal bonus (0.5 = no Holy Power, 1.25 = Holy Power 5/5 with the server rule)."""
    if oath is None: oath = tank
    c = CRIT_BASE + PAL_CRIT + conv
    c_hs = c + (0 if oath else boundless)
    o = (lambda v: v) if oath else (lambda v: 0)
    c_fol = c + (0 if oath else bl_fol)   # Boundless Light for Flash of Light (withdrawn idea)
    fol = (308 + o(115) + 1.5/3.5*hp) * light
    hl = (1580 + o(400) + 2.5/3.5*hp) * light
    hs = (320 + o(229) + 1.5/3.5*hp) * light
    def direct(h, cc, oh):
        r = h*(1 + bonus*cc)
        return r, r*(1-oh)
    fol_r, fol_e = direct(fol, c_fol, 0.15); hl_r, hl_e = direct(hl, c, 0.20); hs_r, hs_e = direct(hs, c_hs, 0.15)
    fol_cost = 140 - illum*140*c_fol
    hl_cost = 660 - illum*660*c
    hs_cost = 325*(1-bened) - illum*325*c_hs
    p_inf_fol = c_fol                 # Flash of Light critical heal: next Holy Light 1 sec faster
    sp = []
    df_r = hl*(1 + bonus)
    sp.append(Spell("Divine Favor + Holy Light", df_r, df_r*0.8, 660 - illum*660 + 0.04*1512, 2.5,
                    maxn=cd_limit(df_cd, 2.5)))
    # Holy Shock, then Holy Light on Infusion of Light (chance c_hs). Shown as one spell with the same cooldown.
    sp.append(Spell("Holy Shock", hs_r, hs_e, hs_cost, 1.5, maxn=cd_limit(10, 1.5)))
    if lv:
        # Light's Vigil rank 3 + Holy Shock. The party heal: 704 + 14.3% of healing power, x5. With no Oath on the
        # Vigil target, Boundless Light applies to the Holy Shock (wowsims: the Oath check is on the Holy Shock).
        lvh = 704 + 0.143*hp
        p_any = 1 - (1-c)**5
        one_r, one_e = direct(lvh, c, 0.25)
        lv_cost = 1340 - illum*1340*p_any + hs_cost
        sp.append(Spell("Light's Vigil + Holy Shock", 5*one_r + hs_r, 5*one_e + hs_e, lv_cost, 3.0,
                        maxn=cd_limit(6, 3.0), tank=(one_r + hs_r)/(5*one_r + hs_r)))
    sp.append(Spell("Flash of Light", fol_r, fol_e, fol_cost, 1.5))
    sp.append(Spell("Flash of Light, Holy Light on Infusion", fol_r + p_inf_fol*hl_r, fol_e + p_inf_fol*hl_e,
                    fol_cost + p_inf_fol*hl_cost, 1.5 + p_inf_fol*1.5))
    sp.append(Spell("Holy Light", hl_r, hl_e, hl_cost, 2.5))
    return dict(cls="Paladin", pool=1512 - 280 + 15*438, regen=regen_full("pal", 336), castfrac=rev,
                extra=None, spells=sp, groups={}, crit=c)

def others(hp, T, tank):
    out = {}
    for n, f in (("Priest", priest), ("Druid", druid), ("Shaman", shaman)):
        k = shaman(hp, tank=tank, T=T) if f is shaman else f(hp, tank=tank)
        out[n] = solve(k, T, tank)["eff"]
    return out

TS = (180, 300, 600)
CASES = (("Paladin, beta 18 Oct", lambda hp, tank: H.paladin(hp, tank=tank)),
         ("Paladin, beta 30 Oct", lambda hp, tank: paladin_b2(hp, tank)),
         ("Paladin, beta 30 Oct, crit 175%", lambda hp, tank: paladin_b2(hp, tank, bonus=0.75)),
         ("Paladin, beta 30 Oct, crit 200%", lambda hp, tank: paladin_b2(hp, tank, bonus=1.0)),
         ("Paladin, Boundless Light for Flash of Light +15%, crit 225%", lambda hp, tank: paladin_b2(hp, tank, bl_fol=0.15)),
         ("Paladin, Boundless Light for Flash of Light +15%, crit 200%", lambda hp, tank: paladin_b2(hp, tank, bonus=1.0, bl_fol=0.15)),
         ("Paladin, Boundless Light for Flash of Light +15%, crit 175%", lambda hp, tank: paladin_b2(hp, tank, bonus=0.75, bl_fol=0.15)),
         ("Paladin, Flash of Light +30%, crit 200%", lambda hp, tank: paladin_b2(hp, tank, bonus=1.0, bl_fol=0.30)),
         ("Paladin, beta 30 Oct, no Conviction", lambda hp, tank: paladin_b2(hp, tank, conv=0.0)),
         ("Paladin, beta 30 Oct, raid with Oath on all heals (upper limit)", lambda hp, tank: paladin_b2(hp, tank, oath=True)))

if __name__ == "__main__":
    for hp in (715, 900):
        for tank in (False, True):
            print(f"## {'One tank' if tank else 'Raid'}, healing power {hp}: HPS after overhealing, 3 | 5 | 10 min")
            O = {T: others(hp, T, tank) for T in TS}
            for n in ("Priest", "Druid", "Shaman"):
                print(f"  {n:62s} " + " | ".join(f"{O[T][n]:5.0f}" for T in TS))
            for n, f in CASES:
                if tank and "upper" in n: continue
                v = {T: solve(f(hp, tank), T, tank)["eff"] for T in TS}
                print(f"  {n:62s} " + " | ".join(
                    f"{v[T]:5.0f} (Dru {v[T]/O[T]['Druid']-1:+.0%}, Pri {v[T]/O[T]['Priest']-1:+.0%}, "
                    f"Sha {v[T]/O[T]['Shaman']-1:+.0%})" for T in TS))
        print(f"## Maximum raw HPS on one tank, 30 sec, {hp}: Paladin 18 Oct {max_hps(H.paladin(hp)):.0f}, "
              f"30 Oct {max_hps(paladin_b2(hp, True)):.0f}, Druid {max_hps(druid(hp, tank=True)):.0f}, "
              f"Shaman {max_hps(shaman(hp, tank=True, T=30)):.0f}, Priest {max_hps(priest(hp, tank=True)):.0f}")
    for tank in (False, True):
        r = solve(paladin_b2(715, tank), 300, tank)
        print(f"## Cast plan 30 Oct, {'tank' if tank else 'raid'}, 5 min: " +
              ", ".join(f"{a} {b:.0f}" for a, b in r["casts"].items()) + f"; idle {r['idle']:.0f} sec")
