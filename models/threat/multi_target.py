"""Threat against several targets: Paladin (PB1) against the Warrior (Thunder Clap, Cleave) and the Druid (Swipe).
Analysis, Threat, part 8. Uses the builds and rotations of threat_model.py. Area spell values: wowsims Forever spell
data (28 October 2026). Run: python3 multi_target.py"""
from threat_model import (DRU_WOWSIMS, TIERS, PB1, paladin, table, armor_dr, rage_taken, GCD, HIT_FRAC, BOSS_MISS,
                          SWING, RAGE_SWING, CRIT_SUPP, RAGE_THREAT, RAGE_ALL, WAR, WAR_STANCE, DRU, BEAR)

TRASH_ARMOR = 3731      # no Sunder Armor or Faerie Fire on the extra targets
MOB_SHARE = 1 / 3       # each mob hits for 1/3 of a boss hit of the tier (assumption)

# Warrior: Thunder Clap rank 6: 103 + 7% AP, 4 targets, 6 sec, 20 rage, spell hit table, threat x1 (wowsims: not
# verified). Cleave rank 5: weapon + 50, 2 targets, 20 rage, 91.8 flat threat (split). wowsims Forever: Revenge 10 casts
# each min and Rend on the main target at 1, 3 and 5 targets.
TC = dict(base=103, ap=0.07, targets=4, cd=6, cost=20 - 3)
CLEAVE = dict(bonus=50, targets=2, flat=91.8, cost=20 - 3)
# Druid: Swipe rank 5 (threat_model.DRU), 3 targets. wowsims Forever: Lacerate on 1 target, Swipe on 2 or more.
SWIPE_TARGETS = 3
# Paladin: Consecration rank 5: 96 Holy damage to all enemies. The 216 bonus damage and the spell power go to the first
# 4 enemies only (wowsims Forever). Holy Shield: damage only on a block, to the attacker, 4 charges. With 2 or more
# attackers, all 4 charges are used each 10 sec (wowsims Forever: 3.7-3.9 at 3 and 5 targets).
CONS_TARGETS = 4
HS_CHARGES = 4 / 10

def tier(g, n):
    return g.but(armor=TRASH_ARMOR, boss_hit=g.boss_hit * MOB_SHARE * n)

def pal(g, n, tal=PB1, proposed=True, cons=True):
    """Returns (threat per sec on all targets, threat per sec on one extra target)."""
    gg = g.but(armor=TRASH_ARMOR)
    c14 = 2.0 if proposed else 0.0
    tot, src = paladin(gg, tal, proposed=proposed, c14=c14, consecration=cons, detail=True)
    if n == 1:
        return tot, 0.0
    hs1 = ((2.0 if proposed else 1.5) + tal.get("red", 0) / 5) / 10     # blocks per sec on one boss
    _, s0 = paladin(gg, tal, proposed=proposed, c14=c14, consecration=cons, crusader=False, detail=True)
    hs_block = (s0["Holy Shield, base"] + s0["Holy Shield, block value"]) / hs1          # extra target: no Crusader
    hs_main = (src["Holy Shield, base"] + src["Holy Shield, block value"]) / hs1
    single = tot - src["Holy Shield, base"] - src["Holy Shield, block value"]
    hs_total = hs_main * HS_CHARGES / n + hs_block * HS_CHARGES * (n - 1) / n
    cons_near = s0.get("Consecration", 0.0)
    cons_far = cons_near * 96 / (312 + 0.336 * gg.sp)
    cons_extra = cons_near * min(n - 1, CONS_TARGETS - 1) + cons_far * max(0, n - CONS_TARGETS)
    return single + hs_total + cons_extra, hs_block * HS_CHARGES / n + cons_extra / (n - 1)

def war(g, n):
    w = WAR; gg = tier(g, n); dr = armor_dr(TRASH_ARMOR)
    land_a, f_auto = table(gg.hit, gg.crit, auto=True)
    land_s, f_spec = table(gg.hit, gg.crit, auto=False)
    rate = 1 / gg.wspeed
    swing_rage = RAGE_SWING * gg.wspeed * (land_a + max(0.0, gg.crit - CRIT_SUPP))
    events = ((1 - HIT_FRAC - BOSS_MISS) + HIT_FRAC * w["blocked"]) * n
    talent = w["event_rage"] * events / SWING + w["bloodrage"]
    taken = rage_taken(gg, w["crush"]) + talent
    spare = (taken + rate * swing_rage - w["slam_cost"] / w["slam_cd"] - w["revenge_cost"] * w["revenge_rate"]
             - w["block_cost"] / w["block_cd"] - w["rend_cost"] / w["rend_dur"])
    gcd_left = 1 / GCD - 1 / w["slam_cd"] - w["revenge_rate"] - 1 / w["rend_dur"]
    phys = (1 - dr) * w["dmg"]
    src = {}
    if n > 1:
        tcs = min(1 / TC["cd"], max(0.0, spare / TC["cost"]), gcd_left)
        spare -= tcs * TC["cost"]; gcd_left -= tcs
        src["Thunder Clap"] = (TC["base"] + TC["ap"] * gg.ap) * phys * 0.94 * min(n, TC["targets"]) * tcs
    sunders = max(0.0, min(gcd_left, spare / w["sunder_cost"]))
    spare -= sunders * w["sunder_cost"]
    if n > 1:      # spare rage: Cleave on 2 or more targets, Heroic Strike on 1
        q = max(0.0, min(1.0, spare / (rate * (CLEAVE["cost"] + swing_rage))))
        k = min(n, CLEAVE["targets"])
        src["Cleave"] = ((gg.weapon() + CLEAVE["bonus"]) * phys * f_spec * k + CLEAVE["flat"] * land_s) * rate * q
    else:
        q = max(0.0, min(1.0, spare / (rate * (w["hs_cost"] + swing_rage))))
        src["Heroic Strike"] = ((gg.weapon() + w["hs_bonus"]) * phys * f_spec + w["hs_threat"] * land_s) * rate * q
    src["Auto attacks"] = gg.weapon() * phys * f_auto * rate * (1 - q)
    src["Shield Slam"] = (w["slam"] + gg.bv) * phys * f_spec / w["slam_cd"]
    src["Revenge"] = ((w["revenge"] + w["revenge_ap"] * gg.ap) * w["revenge_mult"] * phys * f_spec * 2.25
                      * w["revenge_rate"])
    src["Rend"] = (w["rend"] + w["rend_ap"] * gg.ap) * w["rend_ticks"] * w["dmg"] * land_s / w["rend_dur"]
    src["Sunder Armor"] = (w["sunder"] + w["sunder_ap"] * gg.ap) * land_s * sunders
    src["Rage"] = RAGE_THREAT * ((taken + rate * swing_rage * (1 - q)) if RAGE_ALL else talent)
    src = {kk: v * WAR_STANCE for kk, v in src.items()}
    extra = 0.0
    if n > 1:      # Thunder Clap and rage on each target, the second Cleave target is one of the extra targets
        extra = (src["Thunder Clap"] / min(n, TC["targets"]) + src["Rage"] / n + src["Cleave"] / 2 / (n - 1))
    return sum(src.values()), extra

def dru(g, n, mults=None):
    d = dict(DRU, **(mults or {})); gg = tier(g, n); dr = armor_dr(TRASH_ARMOR); crit = d["crit"]
    speed = 2.5; ap = gg.ap + d["ap"]; sw = (gg.wdps + ap / 14) * speed
    land_a, f_auto = table(gg.hit, crit, auto=True)
    land_s, f_spec = table(gg.hit, crit, auto=False)
    rate = 1 / speed; ec = max(0.0, crit - CRIT_SUPP)
    swing_rage = RAGE_SWING * speed * 1.3 * (land_a + ec)
    talent = (d["dodge_rage"] * (1 - HIT_FRAC - BOSS_MISS) * n / SWING + d["crit_rage"] * ec * (rate + 1 / d["bite_cd"])
              + d["enrage"])
    taken = rage_taken(gg, d["crush"]) + talent
    spare = taken + rate * swing_rage - d["bite_cost"] / d["bite_cd"]
    phys = 1 - dr
    gcd_left = 1 / GCD - 1 / d["bite_cd"] - 1 / d["ff_cd"]
    src = {}
    k = min(n, SWIPE_TARGETS)
    if n > 1:      # Swipe first, then Maul with the rage that stays
        swipes = max(0.0, min(gcd_left, spare / d["swipe_cost"]))
        spare -= swipes * d["swipe_cost"]
        maul = max(0.0, min(1.0, spare / (rate * (d["maul_cost"] + swing_rage))))
        src["Swipe"] = ((d["swipe"] + d["swipe_ap"] * ap) * d["savage"] * d["swipe_fi"] * phys * f_spec
                        * d["swipe_mult"] * swipes * k)
    else:          # Maul, then Lacerate (threat_model.druid)
        maul = max(0.0, min(1.0, spare / (rate * (d["maul_cost"] + swing_rage))))
        spare -= maul * rate * (d["maul_cost"] + swing_rage)
        lacs = max(0.0, min(gcd_left, spare / d["lac_cost"]))
        stacks = d["lac_stacks"] * min(1.0, lacs * d["lac_dur"])
        src["Lacerate"] = (sw * d["lac_hit"] * stacks * phys * f_spec * lacs
                           + d["lac_tick"] * stacks * d["lac_ticks"] / d["lac_dur"] * land_s)
    src["Auto attacks"] = sw * phys * f_auto * rate * (1 - maul)
    src["Maul"] = (sw + d["maul_bonus"]) * d["savage"] * phys * f_spec * d["maul_mult"] * rate * maul
    src["Primal Bite"] = (sw + d["bite"]) * phys * f_spec * d["bite_mult"] / d["bite_cd"]
    src["Faerie Fire"] = d["ff"] / d["ff_cd"]
    src["Rage"] = RAGE_THREAT * ((taken + rate * swing_rage * (1 - maul)) if RAGE_ALL else talent)
    src = {kk: v * BEAR for kk, v in src.items()}
    extra = 0.0
    if n > 1:      # Swipe on 3 targets: against more, the 2 Swipe targets after the main target are shared
        extra = (src["Swipe"] / k if n <= SWIPE_TARGETS else src["Swipe"] / k * 2 / (n - 1)) + src["Rage"] / n
    return sum(src.values()), extra

if __name__ == "__main__":
    for n in (1, 3, 5):
        print(f"\n## {n} target(s): threat per sec on all targets (on one extra target). Paladin with Consecration")
        print("Tier | Warrior | Druid | Druid, wowsims multipliers | Paladin beta | Paladin proposed | "
              "proposed % of the best of Warrior and Druid (extra target)")
        for g in TIERS:
            w, we = war(g, n); d, de = dru(g, n); dw, dwe = dru(g, n, DRU_WOWSIMS)
            b, be = pal(g, n, proposed=False); p, pe = pal(g, n)
            best = max(w, d)
            line = (f"{g.name} | {w:.0f} ({we:.0f}) | {d:.0f} ({de:.0f}) | {dw:.0f} ({dwe:.0f}) | {b:.0f} ({be:.0f}) | "
                    f"{p:.0f} ({pe:.0f}) | {p / best:.0%}")
            print(line + (f" ({pe / max(we, de):.0%})" if n > 1 else ""))
    print("\n## Paladin proposed without Consecration, % of the best of Warrior and Druid (total)")
    for n in (3, 5):
        r = [pal(g, n, cons=False)[0] / max(war(g, n)[0], dru(g, n)[0]) for g in TIERS]
        print(f"{n} targets: {min(r):.0%}-{max(r):.0%}")
