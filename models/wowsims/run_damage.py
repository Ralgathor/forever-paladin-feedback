"""Retribution against the other damage specs (Analysis, Damage, part 7). Run: python3 run_damage.py"""
import copy, json, os
from concurrent.futures import ThreadPoolExecutor
from wowsims import *
from builds import *

def P(name, gearpath=None, talents=None):
    p = load(name)
    if gearpath: p["equipment"] = gear(gearpath)
    if talents: p["talentsString"] = talents
    return p


SPECS = {
    "Retribution, beta": (P(RET), ""),
    "Retribution, proposed (RB1)": (P(RET, talents=RB1), RET_PROP),
    "Fury Warrior (prebis gear)": (P("ClassWarrior__p1_fury__default__fury__Fury", "warrior/dps/gear_sets/prebis_fury"), ""),
    "Arms Warrior (prebis gear)": (P("ClassWarrior__p1_arms__Arms__arms__Fury", "warrior/dps/gear_sets/prebis_arms"), ""),
    "Rogue (Combat gear)": (P("ClassRogue__p1_muti__default__default__Rogue", "rogue/dps/gear_sets/p1_bscombat"), ""),
    "Enhancement Shaman": (P("shaman_enhancement/ClassShaman__testing__default__testing__Windfury"), ""),
    "Feral Druid": (P("druid_feralcat/ClassDruid__default__default__default__Standard"), ""),
    "Hunter (Marksmanship)": (P("ClassHunter__p1__default__default__Default"), ""),
    "Mage (Fire)": (P("ClassMage__p1Arcane__default__deepFire__Default"), ""),
    "Warlock (Destruction)": (P("ClassWarlock__preraid__default__destro__Destruction"), ""),
    "Shadow Priest": (P("ClassPriest__testing__default__default__Shadow"), ""),
    "Balance Druid (prebis gear)": (P("druid_balance/ClassDruid__prebis__default__default__Standard"), ""),
    "Elemental Shaman": (P("shaman_elemental/ClassShaman__testing__default__default__Standard"), ""),
}
PURE = ("Fury Warrior (prebis gear)", "Rogue (Combat gear)", "Hunter (Marksmanship)", "Mage (Fire)", "Warlock (Destruction)")
SCENS = ("raid", "raid_nocons", "solo")

def run(jobs):
    return dict(ThreadPoolExecutor(4).map(lambda j: (j[0], metrics(sim(request(j[1], j[2]), j[3]))), jobs))

def classes():
    r = run([((n, s), p, s, f) for n, (p, f) in SPECS.items() for s in SCENS])
    pure = {s: sum(r[(n, s)]["dps"] for n in PURE) / len(PURE) for s in SCENS}
    return r, pure

def proposals():
    """Each proposal alone on RB1, raid and solo."""
    cases = [("RB1, no proposals", ""), ("Twist of Light (C-R2)", "C17"), ("Holy Strike Seal trigger (C1)", "C16"),
             ("Conviction (C-R1)", "C15"), ("Reverence (C-H1)", "C1"), ("Sanctified Judgement (C-R3)", "C26"),
             ("All", RET_PROP), ("All, Sacred Arbiter +10%", RET_PROP + ",SA10"), ("All, Echo 6 sec", RET_PROP + ",ECHO6")]
    return run([((l, s), P(RET, talents=RB1), s, f) for l, f in cases for s in ("raid", "solo")]), [c[0] for c in cases]

# Analysis, Damage, part 11 and Builds, parts 4 and 5: the new Retribution talents (flags BZ<n>, MFM<n>) and
# Shock-Retribution with Divine Precision in Holy row 4 (M-H5). The Holy Shock rotation casts Holy Shock above 40% mana.
# Builds without Holy Shock give the same result with it as with the preset rotation (within 0.3%).
SHOCK_APL = json.load(open(os.path.join(HERE, "data", "shock_ret.apl.json")))
NEW = RET_PROP + ",VIN5"
NEW_BUILDS = [("RB2", RB2, NEW), ("RB2, Burning Zeal 2/2", RB2, NEW + ",BZ2"),
              ("RB2, Measure for Measure 3/3", RB2, NEW + ",MFM3"), ("RB2, both", RB2, NEW + ",BZ2,MFM3"),
              ("RB6 (5/8/38)", RB6, NEW + ",BZ2,MFM3"), ("Shock-Retribution (26/0/25)", SHOCK_RET, NEW),
              ("Shock-Retribution with Divine Precision (28/0/23)", SHOCK_RET_DP, NEW)]

def shock_player(t):
    p = P(RET, talents=t); p["rotation"] = SHOCK_APL; return p

def righteous_fury(p):
    p = copy.deepcopy(p)
    p["rotation"]["prepullActions"].insert(0, {"action": {"castSpell": {"spellId": {"spellId": 25780}}},
                                               "doAtValue": {"const": {"val": "-25s"}}})
    return p

def front(p):
    """From the front: request(tank=True) keeps the preset buffs. Use the same raid buffs as the other columns."""
    p = copy.deepcopy(p); p["buffs"] = load(REF)["buffs"]; return p

def new_talents():
    jobs = [((l, s), shock_player(t), s, f) for l, t, f in NEW_BUILDS for s in SCENS]
    jobs += [((l, "front"), (front(shock_player(t)), "raid", True), None, f) for l, t, f in NEW_BUILDS[:5]]
    jobs += [((l, "tank"), (front(righteous_fury(shock_player(t))), "raid", True), None, f) for l, t, f in NEW_BUILDS
             if l in ("RB2", "RB6 (5/8/38)")]
    def one(j):
        if j[2] is None:
            p, s, tank = j[1]
            return j[0], metrics(sim(request(p, s, tank=tank), j[3]))
        return j[0], metrics(sim(request(j[1], j[2]), j[3]))
    return dict(ThreadPoolExecutor(4).map(one, jobs))

if __name__ == "__main__":
    r, pure = classes()
    print("| Spec | Raid | Raid, no consumables | Solo |\n| --- | --- | --- | --- |")
    for n in SPECS:
        print(f"| {n} | " + " | ".join(f"{r[(n, s)]['dps']:,.0f}" for s in SCENS) + " |")
    print("| Pure average | " + " | ".join(f"{pure[s]:,.0f}" for s in SCENS) + " |")
    for n in ("Retribution, beta", "Retribution, proposed (RB1)"):
        print(f"| {n}, % of the pure average / of Fury | " + " | ".join(
            f"{r[(n, s)]['dps'] / pure[s]:.0%} / {r[(n, s)]['dps'] / r[('Fury Warrior (prebis gear)', s)]['dps']:.0%}" for s in SCENS) + " |")
    same = run([(("beta", "raid"), P(RET, "warrior/dps/gear_sets/prebis_arms"), "raid", ""),
                (("prop", "raid"), P(RET, "warrior/dps/gear_sets/prebis_arms", RB1), "raid", RET_PROP)])
    arms = r[("Arms Warrior (prebis gear)", "raid")]["dps"]
    print(f"\nSame gear (Arms prebis): beta {same[('beta', 'raid')]['dps']:.0f} ({same[('beta', 'raid')]['dps'] / arms:.0%} of Arms), "
          f"proposed {same[('prop', 'raid')]['dps']:.0f} ({same[('prop', 'raid')]['dps'] / arms:.0%})")
    pr, labels = proposals()
    base = {s: pr[("RB1, no proposals", s)]["dps"] for s in ("raid", "solo")}
    print("\n| Case (RB1) | Raid | Solo |\n| --- | --- | --- |")
    for l in labels:
        print(f"| {l} | " + " | ".join(f"{pr[(l, s)]['dps']:.0f} ({pr[(l, s)]['dps'] / base[s] - 1:+.1%})" for s in ("raid", "solo")) + " |")

    n = new_talents()
    rb2 = {s: n[("RB2", s)]["dps"] for s in SCENS + ("front",)}
    print("\n| Build (Holy Shock rotation) | Raid | Raid, no consumables | Solo | From the front | Raid, % of the pure average |")
    print("| --- | --- | --- | --- | --- | --- |")
    for l, _, _ in NEW_BUILDS:
        cols = [f"{n[(l, s)]['dps']:.0f} ({n[(l, s)]['dps'] / rb2[s] - 1:+.1%})" for s in SCENS]
        cols.append(f"{n[(l, 'front')]['dps']:.0f} ({n[(l, 'front')]['dps'] / rb2['front'] - 1:+.1%})" if (l, "front") in n else "—")
        print(f"| {l} | " + " | ".join(cols) + f" | {n[(l, 'raid')]['dps'] / pure['raid']:.0%} |")
    for l in ("RB2", "RB6 (5/8/38)"):
        t = n[(l, "tank")]
        print(f"Retribution tank, {l}, Righteous Fury, from the front: {t['tps']:.0f} TPS, {t['dtps']:.0f} damage taken per sec")
