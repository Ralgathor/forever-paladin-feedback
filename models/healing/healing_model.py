# Four-class healing model for Forever (level 60), after DoubleZug's framework.
# Same gear, raid buffs and consumables for all. Spell values from the Forever spellbook
# (build 1.60.1.70450). Druid Rejuvenation and Regrowth corrected. Base mana added.
import math, itertools, json, sys

HPG = 715          # healing power from gear (DoubleZug profile)
CRIT_BASE = 0.143  # 4% gear + 3% aura + 7.3% from 438 Intellect
MP5 = 117          # 40 gear + 25 Mana Spring + 40 Wisdom + 12 mana oil
POT = 1800         # one major mana potion
TIDE = 1160        # Mana Tide Totem (4 x 290)

def regen_full(cls, spi):   # Classic 1.12 Spirit regeneration, mana per sec, out of the 5-second rule
    return {"pri": (13 + spi/4)/2, "pal": (15 + spi/5)/2, "dru": (15 + spi/5)/2, "sha": (17 + spi/5)/2}[cls]

class Spell:
    def __init__(s, name, raw, cost, time, oh, cd=None, tank=1.0, fixed=False, maxn=None, free=False):
        s.name, s.raw, s.cost, s.time, s.oh, s.cd, s.tank = name, raw, cost, time, oh, cd, tank
        s.maxn = maxn; s.fixed = fixed
    def n_max(s, T):
        if s.maxn is not None: return s.maxn(T)
        return math.floor(T / s.cd) if s.cd else None

# ---------------------------------------------------------------- classes
def paladin(hp_gear=HPG, rev=0.30, illum=0.50, light=1.12, bol=True, ling=0.0, conv=0.0,
            bened=0.10, inf_all=False, hs_heal_mult=1.0, hs_cost_mult=1.0, hs_holy_power=0.0,
            lv=True, lv_cost_mult=1.0, lv_heal_mult=1.0, lv_coef=0.15, lv_illum=True):
    hp = hp_gear
    c = CRIT_BASE + 0.05 + conv            # Holy Power +5% (all spells)
    c_hs = CRIT_BASE + 0.15 + conv         # Holy Power +15% for Holy Shock
    def heal(base, coef, blessing):        # Healing Light multiplies the full heal (beta test)
        return (base + (blessing if bol else 0) + coef * hp) * light
    fol = heal(308, 1.5/3.5, 115); hl = heal(1580, 2.5/3.5, 400)
    hs = (320 + 1.5/3.5 * hp) * light * hs_heal_mult * (1 + hs_holy_power)
    def crit_heal(h, cc): return h * (1 + 0.5*cc) + ling * h * 1.5 * cc   # Lingering Light: 20% of crit as HoT
    def lingpart(h, cc): return ling * h * 1.5 * cc
    sp = {}
    fol_raw = crit_heal(fol, c); hl_raw = crit_heal(hl, c); hs_raw = crit_heal(hs, c_hs)
    fol_cost = 140 - illum*140*c; hl_cost = 660 - illum*660*c
    hs_cost = 325*(1-bened)*hs_cost_mult - illum*325*c_hs
    # effective: FoL 15%, HL 20%, HS 15% overheal; half of Lingering Light overheals
    def eff(raw, h, cc, oh): return (raw - lingpart(h, cc)) * (1-oh) + lingpart(h, cc) * 0.5
    p_inf = 1.0 if inf_all else c          # Infusion of Light trigger chance per Flash of Light
    # Divine Favor: next Holy Light is a critical heal. 2 min cooldown, costs 4% of base mana
    df_raw = hl*1.5 + ling*hl*1.5
    df = Spell("Divine Favor + Holy Light", df_raw, 660 - illum*660 + 0.04*1512, 2.5 if not inf_all else 1.5,
               0.20, maxn=lambda T: math.floor(T/120)+1, fixed=True)
    df.eff = (hl*1.5)*(0.8) + ling*hl*1.5*0.5
    hss = Spell("Holy Shock", hs_raw, hs_cost, 1.5, 0.15, cd=10, fixed=True)
    hss.eff = eff(hs_raw, hs, c_hs, 0.15)
    # Light's Vigil rank 3: 1,340 mana, 1.5 sec cast, 6 sec cooldown. The next Holy Shock on the
    # target has no cooldown and heals the party (5) for 684-724 each. Coefficient assumed 15%.
    # Illumination: one return of 50% of 1,340 if one of the 5 heals is a critical heal.
    lvh = (704 + lv_coef*hp) * lv_heal_mult
    p_any = 1 - (1-c)**5
    lv_raw = 5*crit_heal(lvh, c) + hs_raw
    lv_cost = 1340*lv_cost_mult - (illum*1340*p_any if lv_illum else 0) + hs_cost
    lvs = Spell("Light's Vigil + Holy Shock", lv_raw, lv_cost, 3.0, 0, cd=6, fixed=True,
                tank=(lvh*(1+0.5*c) + hs_raw)/lv_raw)
    lvs.eff = 5*eff(crit_heal(lvh, c), lvh, c, 0.25) + eff(hs_raw, hs, c_hs, 0.15)
    # fillers
    f1 = Spell("Flash of Light", fol_raw, fol_cost, 1.5, 0.15); f1.eff = eff(fol_raw, fol, c, 0.15)
    # Flash of Light, Holy Light only after an Infusion trigger (1.5 sec cast)
    unit_raw = fol_raw + p_inf*hl_raw; unit_cost = fol_cost + p_inf*hl_cost
    f2 = Spell("Flash of Light, Holy Light on Infusion", unit_raw, unit_cost, 1.5 + p_inf*1.5, 0)
    f2.eff = eff(fol_raw, fol, c, 0.15) + p_inf*eff(hl_raw, hl, c, 0.20)
    f3 = Spell("Holy Light", hl_raw, hl_cost, 2.5, 0.20); f3.eff = eff(hl_raw, hl, c, 0.20)
    regen = regen_full("pal", 336)
    pool = 1512 - 280 + 15*438
    return dict(cls="Paladin", pool=pool, regen=regen, castfrac=rev, extra=0,
                fixed=[df, hss] + ([lvs] if lv else []), fillers=[f1, f2, f3], crit=c)

def priest(hp_gear=HPG, tank=False):
    hp = hp_gear + 84    # Spiritual Guidance 5/5: 25% of 336 Spirit
    d = hp - 799
    c = 0.1903
    def S(name, J, I, K_J, cost, time, oh, **kw):
        raw = (J + I*d) * K_J
        s = Spell(name, raw, cost, time, oh, **kw); s.eff = raw*(1-oh); return s
    pom = S("Prayer of Mending (5 hits)", 5*869.105, 5*0.491, 1.0, 257, 1.5, 0.15, cd=10, fixed=True, tank=0.2)
    pen = S("Penance", 1887.3, 0.623, 2069/1887.3, 289, 2.0, 0.25, cd=12, fixed=True)
    bh  = S("Binding Heal", 2544.9, 0.934, 2790/2544.9, 342, 1.5, 0.25, tank=0.5, fixed=True, maxn=lambda T: round(2*T/60))
    gh  = S("Greater Heal", 2688.8, 0.934, 2948/2688.8, 491, 2.5, 0.25, fixed=True, maxn=lambda T: round(2*T/60))
    inf = S("Inner Focus + Prayer of Healing", 5416.5, 5*0.315*1.1, 1.0, 0, 3.0, 0.35, maxn=lambda T: math.floor(T/180)+1, fixed=True, tank=0.2)
    ren = S("Renew", 1941.2, 1.316, 2129/1941.2, 296, 1.5, 0.25)
    ren_up = S("Renew (kept on the tank)", 1941.2, 1.316, 2129/1941.2, 296, 1.5, 0.25, fixed=True, maxn=lambda T: math.floor(T/15))
    poh = S("Prayer of Healing (5 hits)", 5*886.9, 5*0.315, 972/886.9, 927, 3.0, 0.35, tank=0.2)
    fh  = S("Flash Heal", 1272.4, 0.467, 1395/1272.4, 342, 1.5, 0.25)
    gh2 = S("Greater Heal", 2688.8, 0.934, 2948/2688.8, 491, 2.5, 0.25)
    regen = regen_full("pri", 336)
    pool = 1436 - 280 + 15*422
    return dict(cls="Priest", pool=pool, regen=regen, castfrac=0.5, extra=0,
                fixed=[pom, pen, bh, gh, inf] + ([ren_up] if tank else []),
                fillers=([gh2, fh] if tank else [ren, gh2, fh, poh]), crit=c)

def druid(hp_gear=HPG, ooc_wg=0, tank=False):
    hp = hp_gear; d = hp - 715
    def S(name, J, I, K_J, cost, time, oh, **kw):
        raw = (J + I*d) * K_J
        s = Spell(name, raw, cost, time, oh, **kw); s.eff = raw*(1-oh); return s
    # Rejuvenation rank 11: 776 over 12 sec, 360 mana. Coefficient 12/15 = 0.8. Talents x1.328
    rej_J = (776 + 0.8*715)*1.328
    # Regrowth rank 9: 965-1077 direct, 994 over 21 sec, 525 mana. Coefficients 0.3 / 0.621 (DoubleZug)
    reg_J = (1021 + 994 + 0.921*715)*1.114
    reg_K = reg_J + 440 + 0.0915*(994 + 0.621*715)*1.114
    sm_val = ((rej_J*1.0915) + (994 + 0.621*715)*1.114*1.0915) / 2
    tranq = S("Tranquility", 9115.6, 1.8, 9950/9115.6, 833, 10.0, 0.40, maxn=lambda T: math.floor(T/120)+1, fixed=True, tank=0.2)
    sm  = S("Swiftmend", sm_val, 0.877, 1.0, 249, 1.0, 0.20, cd=15, fixed=True)
    wg  = S("Wild Growth", 4854.4, 1.305, 5299/4854.4, 1050, 1.0, 0.50, cd=6, tank=0.2)
    rej = S("Rejuvenation", rej_J, 1.0624, 1.0915, 360, 1.0, 0.25)
    rgw = S("Regrowth", reg_J, 1.026, reg_K/reg_J, 525, 2.0, 0.25)
    ht  = S("Healing Touch", 2934.8, 1.1, 3203/2934.8, 680, 3.0, 0.20)
    # one target: one Rejuvenation at a time; a new Regrowth replaces the old heal over time
    rej_up = S("Rejuvenation (kept on the tank)", rej_J, 1.0624, 1.0915, 360, 1.0, 0.25, fixed=True, maxn=lambda T: math.floor(T/12))
    hot_part = (994 + 0.621*715)*1.114*1.0915
    rgw_t = S("Regrowth (recast on one target)", reg_K - hot_part + hot_part*2.0/21, 1.026*0.4, 1.0, 525, 2.0, 0.25)
    fixed = [tranq, sm] + ([rej_up] if tank else [])
    if ooc_wg:
        w = S("Wild Growth (free, Omen of Clarity)", 4854.4, 1.305, 5299/4854.4, 0, 1.0, 0.50,
              maxn=lambda T: round(ooc_wg*T/60), fixed=True, tank=0.2); fixed.append(w)
    regen = regen_full("dru", 386)
    pool = 1244 - 280 + 15*438
    innerv = lambda T: (math.floor(T/360)+1) * 20 * (5*regen - 0.5*regen)
    return dict(cls="Druid", pool=pool, regen=regen, castfrac=0.5, extra=innerv,
                fixed=fixed, fillers=([rgw_t, ht] if tank else [rgw, rej, ht, wg]), crit=0.183)

def shaman(hp_gear=HPG, T=180, tank=False):
    hp = hp_gear
    k = 1.1215   # crit factor at 24.3%
    def S(name, raw, cost, time, oh, **kw):
        s = Spell(name, raw, cost, time, oh, **kw); s.eff = raw*(1-oh); return s
    rt_full = (1646 + 0.7*hp)*1.1*k
    rt_tank = ((841 + 0.2*hp) + (805 + 0.5*hp)*6/15)*1.1*k   # recast each 6 sec replaces the heal over time
    rt = S("Riptide", rt_tank if tank else rt_full, 341, 1.5, 0.25, cd=6, fixed=True)
    n_hst = math.floor(T/300)+1
    hst = S("Healing Stream Totem", (11 + 0.02*hp)*(T/2)*5/n_hst, 80, 1.5, 0.50, maxn=lambda TT: n_hst, fixed=True, tank=0.2)
    hw = S("Healing Wave", (1371.5 + 3/3.5*hp)*1.1*1.24*k, 507, 2.5, 0.20, fixed=True, maxn=lambda T: round(2*T/60))
    ch_j = (490 + 2.5/3.5*hp)*1.1
    ch = S("Chain Heal (2.5 targets, into Riptide)", 2431.2*ch_j/1089.0, 333.7, 2.5, 0.25, tank=1.25/2.232)
    hw2 = S("Healing Wave", (1371.5 + 3/3.5*hp)*1.1*1.24*k, 507, 2.5, 0.20)
    lhw = S("Lesser Healing Wave", (820 + 1.5/3.5*hp)*1.1*k, 380*0.95 - 24.7, 1.5, 0.15)
    regen = regen_full("sha", 336)
    pool = 1520 - 280 + 15*438
    return dict(cls="Shaman", pool=pool, regen=regen, castfrac=0.5, extra=0,
                fixed=[hst, rt, hw], fillers=[ch, hw2, lhw], crit=0.243)

T_GLOBAL = 180

# ---------------------------------------------------------------- simulation
def budget(k, T):
    b = k["pool"] + MP5/5*T + k["castfrac"]*k["regen"]*T + (math.floor(T/120)+1)*POT + (math.floor(T/300)+1)*TIDE
    if callable(k["extra"]): b += k["extra"](T)
    return b

def simulate(k, T=180, tank=False, filler=None, use_fixed=None):
    """Fixed spells first (at most their cast limit), then one filler. Idle time gives
    full Spirit regeneration after 5 sec; idle comes in blocks of 15 sec (2/3 counts)."""
    B = budget(k, T)
    fixed = [s for s in k["fixed"] if (use_fixed is None or s.name in use_fixed)]
    w = (lambda s: s.tank) if tank else (lambda s: 1.0)
    t = m = raw = eff = 0.0; casts = {}
    r5 = (1 - k["castfrac"]) * k["regen"] * (2/3)
    for s in fixed:
        n = s.n_max(T)
        # mana check (allow 5SR from remaining time)
        while n > 0 and m + n*s.cost > B + r5*max(T - t - n*s.time, 0): n -= 1
        while n > 0 and t + n*s.time > T: n -= 1
        t += n*s.time; m += n*s.cost; raw += n*s.raw*w(s); eff += n*s.eff*w(s); casts[s.name] = n
    best = None
    for f in (k["fillers"] if filler is None else [x for x in k["fillers"] if x.name == filler]):
        if tank and f.tank < 0.5: continue
        free_t = T - t
        n_mana = (B - m + r5*free_t) / (f.cost + r5*f.time) if f.cost + r5*f.time > 0 else 1e9
        n = max(0.0, min(n_mana, free_t / f.time))
        R = raw + n*f.raw*w(f); E = eff + n*f.eff*w(f)
        idle = free_t - n*f.time
        res = dict(raw=R/T, eff=E/T, filler=f.name, n=n, casts=dict(casts), idle=idle, budget=B + r5*idle,
                   limited="mana" if n_mana < free_t/f.time else "time")
        if best is None or res["eff"] > best["eff"]: best = res
    return best

def best_over_fixed(k, T=180, tank=False):
    names = [s.name for s in k["fixed"]]
    best = None
    for r in range(len(names)+1):
        for sub in itertools.combinations(names, r):
            res = simulate(k, T, tank, use_fixed=set(sub))
            if best is None or res["eff"] > best["eff"]: best = res
    return best

def max_hps(k, tank=True, T=30):
    """Healing per sec on one target with no mana limit, 30 sec window, cooldowns ready at start."""
    best = 0
    w = (lambda s: s.tank) if tank else (lambda s: 1.0)
    for f in k["fillers"]:
        if tank and f.tank < 0.5: continue
        t = 0; e = 0
        for s in k["fixed"]:
            if tank and s.tank < 0.5: continue
            n = s.n_max(T) if s.cd else 1
            n = min(n, (math.floor(T/s.cd)+1) if s.cd else n)
            if s.raw*w(s)/s.time > f.raw*w(f)/f.time:
                t += n*s.time; e += n*s.raw*w(s)
        e += max(T - t, 0)/f.time * f.raw*w(f)
        best = max(best, e/T)
    return best

if __name__ == "__main__":
    for T in (180,):
        for mk in (paladin, priest, druid, shaman):
            k = mk(); r = best_over_fixed(k, T)
            print(k["cls"], round(budget(k,T)), {kk: (round(v) if isinstance(v,float) else v) for kk,v in r.items()})
