"""Protection Paladin threat and mana on the beta of 30 October 2026 (wowsims Forever, push 113554).
Uses models/threat/threat_model.py of the repo for the gear, the attack table, the Warrior and the Druid.
Run: python3 threat_b2.py <repo>/models

Changes against the beta of 18 October (threat_model.paladin(g, TANK_REF, proposed=False, c14=0)):
- Righteous Fury: x1.33 all threat, and x1.9 more for Holy (multiplicative in wowsims: Holy x2.527).
- Shieldsworn: Holy Strike cooldown 10 -> 6 sec. Each Holy Strike that lands triggers the Holy Shield damage
  (no charge used) and the Shield Specialization mana return (no 3 sec limit).
- Iron Creed 3 ranks: +10/20/30% Holy Strike threat (was 5 ranks of 5%).
- Conviction 3 ranks: 2/4/6% critical chance, attacks and spells.
- One-Handed Weapon Specialization and Improved Seal of Fury removed.
- Shield Specialization 2/2: 100% chance x 4% maximum mana for each block (once each 3 sec), +30% block value.
Tank build B2T 0/38/13: Divine Intellect 2, Redoubt 5, Precision 3, Sacred Duty 1, Templar's Bulwark,
Shield Specialization 2, Toughness 5, Swift Judgement, Improved Righteous Fury 3, Anticipation 5, Holy Shield,
Reckoning 5, Iron Creed 3, Shieldsworn; Benediction 5, Improved Judgement 2, Conviction 3, Sanctified Judgement 3.
"""
import sys
base = sys.argv[1] if len(sys.argv) > 1 else "."
sys.path.insert(0, base + "/threat"); sys.path.insert(0, base + "/mana")
import threat_model as T
from threat_model import table, armor_dr, CRUSADER, NORM_1H, HS_THREAT, CONS_EVERY, HIT_FRAC, SWING, CRIT_SUPP

RF_ALL, RF_HOLY = 1.33, 1.9
B2T = dict(prec=3, red=5, sj=1, reck=5, ic=3, hsh=1, ij=2, conv=3, shs=1, sanj=3, ben=5, ss=2)

def paladin_b2(g, tal=B2T, crusader=True, consecration=False, detail=False, rf_all=RF_ALL):
    t = lambda k: tal.get(k, 0)
    hit = g.hit + 0.01 * t("prec")
    crit = g.crit + 0.02 * t("conv")
    sp = g.sp + (CRUSADER if crusader else 0)
    holy, phys = RF_HOLY * rf_all, rf_all
    seals = 1 + 0.03 * t("is")                        # Improved Seals: 3% each rank now
    hs_cd = 6 if t("shs") else 10
    hs_blocks = (1.5 + t("red") / 5) / 10             # beta rule: 2.5 blocks each 10 sec with Redoubt 5/5
    extra = 1.0 / 10 * t("reck") / 5
    land_a, f_auto = table(hit, crit, auto=True)
    land_s, f_spec = table(hit, crit, auto=False)
    swings = 1 / g.wspeed
    src = {}
    if t("hsh"):
        rate = hs_blocks + (land_s / hs_cd if t("shs") else 0)
        src["Holy Shield"] = (221 + 0.08 * sp) * holy * HS_THREAT * rate
    _, f_jud = table(hit, crit, auto=False, dodge=0.0, parry=0.0)
    jud = (160 + 0.429 * sp) * seals * f_jud
    src["Judgement of Fury"] = jud * holy * (1 / (10 - t("ij")) + t("sj") / 60)
    hstr = 0.5 * (g.weapon(NORM_1H) + 93 + 0.429 * sp) * f_spec
    src["Holy Strike"] = hstr * holy * (1 + 0.10 * t("ic")) * (1 + 0.20 * t("sa")) / hs_cd
    dr = armor_dr(g.armor)
    src["Auto attacks"] = g.weapon() * (1 - dr) * f_auto * swings * phys
    src["Reckoning attacks"] = g.weapon() * (1 - dr) * f_auto * extra * phys
    hits = land_a * swings + land_a * extra
    src["Seal of Fury"] = (35 + 0.10 * sp) * seals * (1 + max(0.0, crit - CRIT_SUPP)) * holy * hits
    if consecration:
        src["Consecration"] = (312 + 0.336 * sp) * 0.85 * (1 + 0.5 * crit) * holy / CONS_EVERY
    total = sum(src.values())
    return (total, src) if detail else total

def beta1(g, **kw):
    return T.paladin(g, T.TANK_REF, proposed=False, c14=0, **kw)

# ---------------------------------------------------------------- mana (mana_model.py costs)
import mana_model as M
def mps_b2(mana, mp5, tal=B2T, cons=False, wisdom=False, hit=True, block=0.40):
    """block: share of the boss swings that are blocks (beta: about 40% with Holy Shield and Redoubt)."""
    t = lambda k: tal.get(k, 0)
    b = 1 - 0.02 * t("ben")
    hs_cd = 6 if t("shs") else 10
    judgements = 1 / (10 - t("ij"))
    cost = (M.HOLY_SHIELD / 10 + M.HOLY_STRIKE / hs_cd + M.JUDGEMENT * judgements + M.SEAL_OF_FURY / M.SEAL_TIME) * b
    if cons:
        cost += M.CONSECRATION * b / M.CONS_EVERY
    income = mp5 / 5 + (M.WISDOM if wisdom else 0)
    chance = 0.5 * t("ss")
    if hit:
        # blocks: once each 3 sec at most; the boss swings each 2 sec, so at most one block in 2 swings
        income += mana * 0.04 * chance * min(block / M.SWING, 1 / 3)
    if t("shs"):
        income += mana * 0.04 * chance * 0.85 / hs_cd     # 85% of the Holy Strikes land
    income += M.SEAL_OF_FURY * (2 - b) * 0.2 * t("sanj") * (judgements + t("sj") / 60)
    return income - cost

if __name__ == "__main__":
    g = T.PART1
    print("## Part 1 gear: TPS")
    w, d = T.warrior(g), T.druid(g)
    b1, b2 = beta1(g), paladin_b2(g)
    p = T.paladin(g)
    print(f"Warrior {w:.0f} | Druid {d:.0f} | Paladin beta 18 Oct {b1:.0f} ({b1/w:.0%} of Warrior, {b1/d:.0%} of Druid) | "
          f"beta 30 Oct {b2:.0f} ({b2/w:.0%}, {b2/d:.0%}) | proposed (18 Oct base) {p:.0f} ({p/w:.0%}, {p/d:.0%})")
    _, s = paladin_b2(g, detail=True)
    print("  30 Oct sources: " + ", ".join(f"{k} {v:.0f}" for k, v in s.items()))
    _, s1 = beta1(g, detail=True)
    print("  18 Oct sources: " + ", ".join(f"{k} {v:.0f}" for k, v in s1.items()))
    print(f"  30 Oct without Shieldsworn: {paladin_b2(g, dict(B2T, shs=0)):.0f}; without the +33%: {paladin_b2(g, rf_all=1.0):.0f}; "
          f"with Consecration: {paladin_b2(g, consecration=True):.0f}")
    print("\n## Gear progression: Warrior | Druid | beta 18 Oct | beta 30 Oct | beta 30 Oct + Consecration | proposed (18 Oct base)")
    for t in T.TIERS:
        w, d = T.warrior(t), T.druid(t)
        cols = (beta1(t), paladin_b2(t), paladin_b2(t, consecration=True), T.paladin(t))
        print(f"{t.name} | {w:.0f} | {d:.0f} | " + " | ".join(f"{v:.0f} ({v/w:.0%} W, {v/d:.0%} D)" for v in cols))
    print("\n## Mana (MPS), B2T, Blessing of Wisdom: fresh level 60 | Naxxramas, no Consecration / Consecration")
    for name, kw in (("hit", {}), ("not hit", dict(hit=False))):
        cols = []
        for _, m, p5 in (M.TIERS[0], M.TIERS[-1]):
            for cons in (False, True):
                v = mps_b2(m, p5, cons=cons, wisdom=True, **kw)
                cols.append(f"{v:+.1f}" + ("" if v >= 0 else f" ({M.lasts(m, v)})"))
        print(f"30 Oct, {name}: " + " | ".join(cols))
        cols = []
        for _, m, p5 in (M.TIERS[0], M.TIERS[-1]):
            for cons in (False, True):
                v = M.mps(m, p5, sanj=3, ij=2, cons=cons, wisdom=True, beta=True, hit=(name == "hit"))
                cols.append(f"{v:+.1f}" + ("" if v >= 0 else f" ({M.lasts(m, v)})"))
        print(f"18 Oct (PB1 talents, beta rules), {name}: " + " | ".join(cols))
