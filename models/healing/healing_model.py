# Four-class healing model for Forever (level 60), after DoubleZug's framework.
# Same gear, raid buffs and consumables for all. Spell values from the Forever spellbook
# (build 1.60.1.70450). Druid Rejuvenation and Regrowth corrected. Base mana added.
#
# Version 2 (review of 22 October 2026):
# - The cast plan is a linear program: the best mix of all spells for the mana and the time.
# - Cooldowns and consumables count only uses that start early enough to end in the fight.
# - Heals over time can be critical heals in Forever: each tick (HOT_CRIT). Lingering Light (C-H2) too, but a
#   critical tick does not start it again (only non-periodic critical heals do).
# - One tank: a Riptide or a Regrowth can be kept for its full duration, or recast.
# - Talent review (22 October 2026): Druid: Gift of the Earthmother (global cooldown 1 sec for Rejuvenation,
#   Swiftmend, Wild Growth), Nature's Splendor (Rejuvenation 15 sec, Regrowth 27 sec), Genesis on periodic
#   healing only, Swiftmend heals for the full heal over time (Forever text). Priest: no Penance (the DoubleZug
#   build has Prayer of Mending and Binding Heal; Penance needs 20 Discipline points more). Shaman: Healing Way 25%.
#   Inner Focus + Prayer of Healing scales the coefficient the same way as the base heal.
import math
from scipy.optimize import linprog

HPG = 715          # healing power from gear (DoubleZug profile)
CRIT_BASE = 0.143  # 4% gear + 3% aura + 7.3% from 438 Intellect
PAL_CRIT = 0.035   # Paladin base spell critical chance (game files, wowsims Forever)
HOT_CRIT = True    # heals over time can be critical heals in Forever (each tick, x1.5). False: Classic 1.12 rule
MP5 = 117          # 40 gear + 25 Mana Spring + 40 Wisdom + 12 mana oil
POT = 1800         # one major mana potion, 2 min cooldown
TIDE = 1160        # Mana Tide Totem (4 x 290 over 12 sec), 5 min cooldown

def uses(T, cd, dur=0.0):
    """Number of uses of a cooldown in a fight of T sec. The first use is at 0.
    A use counts only if it ends before the end of the fight."""
    return max(0, math.floor((T - dur - 1e-9) / cd) + 1)

def regen_full(cls, spi):   # Classic 1.12 Spirit regeneration, mana per sec, out of the 5-second rule
    return {"pri": (13 + spi/4)/2, "pal": (15 + spi/5)/2, "dru": (15 + spi/5)/2, "sha": (17 + spi/5)/2}[cls]

class Spell:
    """raw/eff: healing for one cast (all targets); tank: share that lands on the tank.
    maxn(T): cast limit. group: (name, weight) pairs for shared limits (see GROUPS)."""
    def __init__(s, name, raw, eff, cost, time, maxn=None, tank=1.0, groups=()):
        s.name, s.raw, s.eff, s.cost, s.time, s.tank = name, raw, eff, cost, time, tank
        s.maxn = maxn; s.groups = groups

def cd_limit(cd, time):
    return lambda T: uses(T, cd, time)

# ---------------------------------------------------------------- Lingering Light (C-H2) pool
def ll_ticks(events):
    """Lingering Light on one target, as its text says. events: (time, amount added) for each non-periodic
    critical heal. The new amount and the healing that remains are added together and spread over a new
    6 sec: one tick each 2 sec. Returns the list of (tick time, tick amount)."""
    ticks = []
    for t, add in sorted(events):
        rem = sum(a for tt, a in ticks if tt > t)
        ticks = [(tt, a) for tt, a in ticks if tt <= t]
        pool = rem + add
        ticks += [(t + 2, pool/3), (t + 4, pool/3), (t + 6, pool/3)]
    return ticks

def ll_spam_history(heal, c, ling, n=20, cast=1.5, rng=None):
    """Events of Flash of Light spam that ends at time 0: n casts, one each 1.5 sec, critical with chance c."""
    import random
    rng = rng or random
    return [(-cast*i, ling*heal*1.5) for i in range(n) if rng.random() < c]

def ll_end_pool(heal, c, ling, samples=4000, seed=1):
    """Lingering Light healing that remains after the last cast (expected value). At the end of a fight it is lost."""
    import random
    rng = random.Random(seed); tot = 0.0
    for _ in range(samples):
        tot += sum(a for t, a in ll_ticks(ll_spam_history(heal, c, ling, rng=rng)) if t > 0)
    return tot / samples

# ---------------------------------------------------------------- Paladin
# tank: not used (the Paladin has the same spells for raid and one tank)
def paladin(hp=HPG, tank=False, rev=0.30, illum=0.50, light=1.12, bol=True, ling=0.0, conv=0.0,
            bened=0.10, inf_all=False, hs_heal_mult=1.0, hs_cost_mult=1.0,
            lv=True, lv_cost_mult=1.0, lv_heal_mult=1.0, lv_coef=0.15, lv_per_crit=False):
    c = CRIT_BASE + PAL_CRIT + 0.05 + conv            # Holy Power +5% (all spells)
    c_hs = CRIT_BASE + PAL_CRIT + 0.15 + conv         # Holy Power +15% for Holy Shock
    def heal(base, coef, blessing):        # Healing Light multiplies the full heal (beta test)
        return (base + (blessing if bol else 0) + coef * hp) * light
    fol = heal(308, 1.5/3.5, 115); hl = heal(1580, 2.5/3.5, 400)
    hs = (320 + 1.5/3.5 * hp) * light * hs_heal_mult
    # direct heal with critical heals; Lingering Light (C-H2): 20% of a critical heal as a heal over time.
    # Its ticks can be critical heals (chance c). A critical tick does not start Lingering Light again.
    kt = (1 + 0.5*c) if HOT_CRIT else 1.0
    def direct(h, cc, oh):
        ll = ling * h * 1.5 * cc * kt
        return h*(1 + 0.5*cc) + ll, h*(1 + 0.5*cc)*(1-oh) + ll*0.5   # half of Lingering Light overheals
    fol_r, fol_e = direct(fol, c, 0.15); hl_r, hl_e = direct(hl, c, 0.20); hs_r, hs_e = direct(hs, c_hs, 0.15)
    fol_cost = 140 - illum*140*c
    hl_cost = 660 - illum*660*c
    hs_cost = 325*(1-bened)*hs_cost_mult - illum*325*c_hs
    p_inf = 1.0 if inf_all else c          # chance that a Flash of Light triggers Infusion of Light
    sp = []
    # Divine Favor: the next Holy Light is a critical heal. 2 min cooldown, 4% of base mana
    t_df = 1.5 if inf_all else 2.5
    df_r = hl*1.5 + ling*hl*1.5*kt
    sp.append(Spell("Divine Favor + Holy Light", df_r, hl*1.5*0.8 + ling*hl*1.5*kt*0.5,
                    660 - illum*660 + 0.04*1512, t_df, maxn=cd_limit(120, t_df)))
    sp.append(Spell("Holy Shock", hs_r, hs_e, hs_cost, 1.5, maxn=cd_limit(10, 1.5)))
    if lv:
        # Light's Vigil rank 3: 1,340 mana, 1.5 sec cast, 6 sec cooldown. The next Holy Shock on the
        # target has no cooldown and heals the party (5) for 684-724 each. Coefficient assumed 15%.
        # Illumination names Light's Vigil: one return for each cast if one of the 5 heals is critical
        # (or, with lv_per_crit, one return for each critical heal).
        lvh = (704 + lv_coef*hp) * lv_heal_mult
        p_any = 1 - (1-c)**5
        one_r, one_e = direct(lvh, c, 0.25)
        lv_cost = 1340*lv_cost_mult - illum*1340*(5*c if lv_per_crit else p_any) + hs_cost
        sp.append(Spell("Light's Vigil + Holy Shock", 5*one_r + hs_r, 5*one_e + hs_e, lv_cost, 3.0,
                        maxn=cd_limit(6, 3.0), tank=(one_r + hs_r)/(5*one_r + hs_r)))
    sp.append(Spell("Flash of Light", fol_r, fol_e, fol_cost, 1.5))
    sp.append(Spell("Flash of Light, Holy Light on Infusion", fol_r + p_inf*hl_r, fol_e + p_inf*hl_e,
                    fol_cost + p_inf*hl_cost, 1.5 + p_inf*1.5))
    sp.append(Spell("Holy Light", hl_r, hl_e, hl_cost, 2.5))
    # Lingering Light carries over the remaining healing at each refresh: no healing is lost, but the healing
    # that remains at the end of the fight does not land.
    end = ll_end_pool(fol, c, ling) * kt if ling else 0.0
    return dict(cls="Paladin", pool=1512 - 280 + 15*438, regen=regen_full("pal", 336), castfrac=rev,
                extra=None, spells=sp, groups={}, crit=c, end_loss=(end, end*0.5))

# ---------------------------------------------------------------- Priest
def priest(hp_gear=HPG, tank=False):
    hp = hp_gear + 84          # Spiritual Guidance 5/5: 25% of 336 Spirit
    d = hp - 799
    c = 0.1903; k = 1 + 0.5*c; k_if = 1 + 0.5*(c + 0.25)
    def S(name, J, I, crit, cost, time, oh, **kw):
        raw = (J + I*d) * (k if crit else 1.0)
        return Spell(name, raw, raw*(1-oh), cost, time, **kw)
    sp = [
      # Prayer of Mending: direct heal, 5 targets, 10 sec cooldown. The tank gets one of the 5 heals.
      S("Prayer of Mending (5 targets)", 5*869.105, 5*0.491, True, 257, 1.5, 0.15, maxn=cd_limit(10, 1.5), tank=0.2),
      # Binding Heal: half heals the Priest. The DoubleZug sheet casts it 2 times each min.
      S("Binding Heal", 2544.9, 0.934, True, 342, 1.5, 0.25, maxn=lambda T: round(2*T/60), tank=0.5),
      # Inner Focus: no cost, +25% critical chance. Both the base heal and the coefficient use this multiplier.
      S("Inner Focus + Prayer of Healing", 5*886.9*k_if/k, 5*0.315*k_if/k, True, 0, 3.0, 0.35, maxn=cd_limit(180, 3.0), tank=0.2),
      S("Greater Heal", 2909.2, 0.943, True, 491, 2.5, 0.25),
      S("Flash Heal", 1272.4, 0.467, True, 342, 1.5, 0.25),
    ]
    renew = S("Renew", 1941.2, 1.316, HOT_CRIT, 296, 1.5, 0.25)       # heal over time: critical ticks in Forever
    if tank: renew.maxn = lambda T: math.floor(T/15); renew.name = "Renew (one at a time)"
    sp.append(renew)
    if not tank:
        sp.append(S("Prayer of Healing (5 targets)", 5*886.9, 5*0.315, True, 927, 3.0, 0.35, tank=0.2))
    return dict(cls="Priest", pool=1436 - 280 + 15*422, regen=regen_full("pri", 336), castfrac=0.5,
                extra=None, spells=sp, groups={}, crit=c)

# ---------------------------------------------------------------- Druid
def druid(hp=HPG, tank=False, ooc_wg=0, sm_consumes=False):
    c = 0.183; k = 1 + 0.5*c
    kh = k if HOT_CRIT else 1.0                 # heals over time: critical ticks in Forever
    # Talents (DoubleZug build): Gift of Nature +10% healing, Improved Rejuvenation +15%, Genesis +5% periodic
    # healing, Improved Regrowth +50% critical chance, Gift of the Earthmother (global cooldown 1 sec for
    # Rejuvenation, Swiftmend and Wild Growth), Nature's Splendor (Rejuvenation +3 sec, Regrowth +6 sec).
    # Rejuvenation rank 11: 776 over 12 sec, 360 mana, coefficient 0.8. With Nature's Splendor: 15 sec, the
    # same ticks: 970 and coefficient 1.0.
    rej0 = (776*15/12 + 1.0*hp)*1.1*1.15*1.05
    rej = rej0*kh
    # Regrowth rank 9: 965-1077 direct (coefficient 0.286), 994 over 21 sec (0.497), 525 mana (game files).
    # With Nature's Splendor: 27 sec, 1,278 and coefficient 0.798.
    rg_dir = (1021 + 0.286*hp)*1.1; rg_hot0 = (994 + 0.497*hp)*27/21*1.1*1.05; rg_hot = rg_hot0*kh
    rg_dir_c = rg_dir*(1 + 0.5*(c + 0.5))
    rg = rg_dir_c + rg_hot
    # Swiftmend (Forever text): heals for the full periodic value of the Rejuvenation or Regrowth on the target.
    # A direct heal (can be critical). One tank: a Rejuvenation is always on the tank. Raid: the plan casts Regrowth.
    sm = rej0*k if tank else rg_hot0*k
    if sm_consumes: sm -= 0.5*(rej if tank else rg_hot)  # if it removes the heal over time (half of it is left)
    sp = [
      Spell("Tranquility", (9115.6 + 1.8*(hp-715))*kh, (9115.6 + 1.8*(hp-715))*kh*0.6, 833, 10.0, maxn=cd_limit(120, 10.0), tank=0.2),
      Spell("Swiftmend", sm, sm*0.8, 249, 1.0, maxn=cd_limit(15, 1.0)),
      Spell("Healing Touch", (2934.8 + 1.1*(hp-715))*k, (2934.8 + 1.1*(hp-715))*k*0.8, 680, 3.0),
    ]
    wg = (4854.4 + 1.305*(hp-715))*kh           # heal over time: critical ticks in Forever
    if tank:
        sp.append(Spell("Rejuvenation (one at a time)", rej, rej*0.75, 360, 1.0, maxn=lambda T: math.floor(T/15)))
        # Regrowth kept for 27 sec, or recast: the new one replaces the heal over time after 2 sec
        sp.append(Spell("Regrowth (kept 27 sec)", rg, rg*0.75, 525, 2.0, groups=(("rg_slot", 27),)))
        rr = rg_dir_c + rg_hot*2/27
        sp.append(Spell("Regrowth (recast)", rr, rr*0.75, 525, 2.0, groups=(("rg_slot", 2),)))
        groups = {"rg_slot": lambda T: T}
    else:
        sp += [Spell("Regrowth", rg, rg*0.75, 525, 2.0),
               Spell("Rejuvenation", rej, rej*0.75, 360, 1.0),
               Spell("Wild Growth", wg, wg*0.5, 1050, 1.0, maxn=cd_limit(6, 1.0), tank=0.2)]
        groups = {}
    if ooc_wg:
        sp.append(Spell("Wild Growth (free, Omen of Clarity)", wg, wg*0.5, 0, 1.0,
                        maxn=lambda T: round(ooc_wg*T/60), tank=0.2))
    regen = regen_full("dru", 386)
    innerv = lambda T: uses(T, 360, 20) * 20 * (5*regen - 0.5*regen)   # Innervate on itself
    return dict(cls="Druid", pool=1244 - 280 + 15*438, regen=regen, castfrac=0.5, extra=innerv,
                spells=sp, groups=groups, crit=c)

# ---------------------------------------------------------------- Shaman
def shaman(hp=HPG, tank=False, T=180):
    c = 0.243; k = 1 + 0.5*c
    kh = k if HOT_CRIT else 1.0                 # heals over time: critical ticks in Forever
    # Riptide rank 3: direct 799-883 (coefficient 0.2), 805 over 15 sec (0.5). Purification x1.1.
    rt_dir = (841 + 0.2*hp)*1.1*k; rt_hot = (805 + 0.5*hp)*1.1*kh
    hw = (1371.5 + 3/3.5*hp)*1.1*1.25*k        # Purification +10%, Healing Way +25% (Forever text)
    ch_j = (506.5 + 2.5/3.5*hp)*1.1             # Chain Heal rank 3: 506.5 average (game files)
    ch = 2431.2*ch_j/1089.0                     # 2.5 targets, 90% on a Riptide target (DoubleZug)
    n_hst = uses(T, 300, 0)
    hst = (11 + 0.02*hp)*(T/2)*5/n_hst*kh       # Healing Stream Totem: 5 min, 5 targets, each 2 sec
    sp = [Spell("Healing Stream Totem", hst, hst*0.5, 80, 1.5, maxn=lambda TT: n_hst, tank=0.2),
          Spell("Healing Wave", hw, hw*0.8, 507, 2.5),
          Spell("Lesser Healing Wave", (820 + 1.5/3.5*hp)*1.1*k, (820 + 1.5/3.5*hp)*1.1*k*0.85, 380*0.95 - 24.7, 1.5)]
    if tank:
        # Riptide on one tank: kept 15 sec (full heal over time), or recast each 6 sec (6/15 of it)
        r1 = rt_dir + rt_hot; r2 = rt_dir + rt_hot*6/15
        sp += [Spell("Riptide (kept 15 sec)", r1, r1*0.75, 341, 1.5, groups=(("rt_cd", 1), ("rt_slot", 15))),
               Spell("Riptide (recast)", r2, r2*0.75, 341, 1.5, groups=(("rt_cd", 1), ("rt_slot", 6)))]
        groups = {"rt_cd": lambda T: uses(T, 6, 1.5), "rt_slot": lambda T: T}
    else:
        r = rt_dir + rt_hot
        sp += [Spell("Riptide", r, r*0.75, 341, 1.5, maxn=cd_limit(6, 1.5)),
               Spell("Chain Heal (2.5 targets, on a Riptide target)", ch, ch*0.75, 333.7, 2.5)]
        groups = {}
    return dict(cls="Shaman", pool=1520 - 280 + 15*438, regen=regen_full("sha", 336), castfrac=0.5,
                extra=None, spells=sp, groups=groups, crit=c)

# ---------------------------------------------------------------- fight
def budget(k, T):
    b = (k["pool"] + MP5/5*T + k["castfrac"]*k["regen"]*T
         + uses(T, 120, 0)*POT + uses(T, 300, 12)*TIDE)
    if k["extra"]: b += k["extra"](T)
    return b

def solve(k, T=180, tank=False, metric="eff", mana_limit=True):
    """Best mix of casts (linear program). Constraints: cast time + idle time = T;
    mana spent <= budget + regeneration from idle time; cast limits; shared limits.
    Idle time gives full Spirit regeneration after 5 sec: the model counts 2/3 of it."""
    sp = k["spells"]; n = len(sp)
    w = [(s.tank if tank else 1.0) for s in sp]
    val = [(s.eff if metric == "eff" else s.raw) * wi for s, wi in zip(sp, w)]
    c = [-v for v in val] + [0.0]
    A_eq = [[s.time for s in sp] + [1.0]]; b_eq = [T]
    A_ub, b_ub = [], []
    if mana_limit:
        r5 = (1 - k["castfrac"]) * k["regen"] * (2/3)
        A_ub.append([s.cost for s in sp] + [-r5]); b_ub.append(budget(k, T))
    for g, lim in k["groups"].items():
        A_ub.append([dict(s.groups).get(g, 0) for s in sp] + [0.0]); b_ub.append(lim(T))
    bounds = [(0, s.maxn(T) if s.maxn else None) for s in sp] + [(0, None)]
    r = linprog(c, A_ub=A_ub or None, b_ub=b_ub or None, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs")
    assert r.status == 0, r.message
    casts = {s.name: x for s, x in zip(sp, r.x[:-1]) if x > 1e-6}
    raw = sum(s.raw*wi*x for s, wi, x in zip(sp, w, r.x[:-1]))
    eff = sum(s.eff*wi*x for s, wi, x in zip(sp, w, r.x[:-1]))
    spent = sum(s.cost*x for s, x in zip(sp, r.x[:-1]))
    el_raw, el_eff = k.get("end_loss", (0.0, 0.0))     # Lingering Light healing still in the pool at the end
    raw -= el_raw; eff -= el_eff
    return dict(eff=eff/T, raw=raw/T, casts=casts, idle=r.x[-1], spent=spent)

def max_hps(k, T=30):
    """Raw healing per sec on one tank for 30 sec, with no mana limit and all cooldowns ready."""
    return solve(k, T, tank=True, metric="raw", mana_limit=False)["raw"]

if __name__ == "__main__":
    for f in (paladin, priest, druid, shaman):
        kk = f(); r = solve(kk, 180)
        print(kk["cls"], round(budget(kk, 180)), round(r["eff"]), {a: round(b, 1) for a, b in r["casts"].items()}, "idle", round(r["idle"]))
