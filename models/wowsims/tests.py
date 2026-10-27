"""One check for each proposal in the sim patch: the sim result must show the effect of the proposal text.
Run: python3 tests.py (about 1 min). Each line shows PASS or FAIL, the value and the limits."""
import re, sys
from wowsims import *
from builds import *
import run_healing as RH

N = 300
HOLY_SHIELD = 20928
results = []

def action(o, sid):
    """All entries of one spell (the sim can split a spell by tag), as one action."""
    a = [x for x in player_metrics(o)["actions"] if x["id"].get("spellId") == sid]
    if not a: raise KeyError(sid)
    return {"targets": [t for x in a for t in x["targets"]]}

def S(a, k):
    return sum(t.get(k, 0) for t in a["targets"])

def hit_avg(a):
    """Average heal of a hit that is not critical."""
    return (S(a, "healing") - S(a, "critHealing")) / S(a, "hits")

def crit_rate(a):
    return S(a, "crits") / max(1, S(a, "crits") + S(a, "hits"))

def check(name, value, lo, hi):
    ok = lo <= value <= hi
    results.append(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}: {value:.3f} (limits {lo} to {hi})")

def holy(rot, flags, talents=HOLY_PROP_TALENTS):
    return RH.heal_sim(RH.paladin(talents, rot, False), flags, iters=N)

if __name__ == "__main__":
    # C-H4 Healing Light 10/20/30%: the beta talent gives 12%. Thus, a Holy Light hit is x1.30 / 1.12.
    a, b = (hit_avg(action(holy("Holy Light", f), RH.HL)) for f in ("C15", "C15,HL30"))
    check("Healing Light 30% (C-H4): Holy Light hit, HL30 / beta", b / a, 1.30 / 1.12 - 0.01, 1.30 / 1.12 + 0.01)
    # C-R1 Conviction 5/5 on heals: +5% critical heal chance.
    a, b = (crit_rate(action(holy("Holy Light", f), RH.HL)) for f in ("C15", "C15,C15H"))
    check("Conviction on heals (C-R1): Holy Light critical heals, points added", 100 * (b - a), 4.0, 6.0)
    # C-H2 Lingering Light 20%: 20% of each critical heal, in 3 ticks. Ticks can be critical (x1.5).
    o = holy("Holy Light", HOLY_PROP)
    crit_heal = S(action(o, RH.HL), "critHealing")
    check("Lingering Light 20% (C-H2): its healing / critical Holy Light healing", S(action(o, RH.LINGERING), "healing") / crit_heal, 0.19, 0.27)
    # C-H3 Infusion of Light: each Flash of Light gives a fast Holy Light, so the casts alternate.
    o = holy("FoL then HL", HOLY_PROP)
    check("Infusion of Light (C-H3): Holy Light casts / Flash of Light casts", S(action(o, RH.HL), "casts") / S(action(o, RH.FOL), "casts"), 0.9, 1.1)
    o = holy("FoL then HL", "", HOLY_BETA)
    check("Infusion of Light, beta (critical Flash of Light only): Holy Light casts / Flash of Light casts", S(action(o, RH.HL), "casts") / S(action(o, RH.FOL), "casts"), 0.0, 0.5)

    p = with_talents(julien(), PB1)
    tank = lambda f: sim(request(p, "raid", tank=True, iters=N), f)
    # C-P1 Redoubt: no crushing blows at the defense of Julien's gear.
    check("Crushing blow fix (C-P1): crushing blows, % of boss swings", boss_swings(tank("C6"))["crushes"], 0.0, 1.0)
    check("Beta: crushing blows, % of boss swings", boss_swings(tank(""))["crushes"], 5.0, 20.0)
    # C-P9 Holy Shield: base damage + n% of block value. The damage must be linear in n.
    d = [S(action(tank(f"C6,C14,HSBV{n}"), HOLY_SHIELD), "damage") for n in (0, 100, 200)]
    check("Holy Shield block value (C-P9): (200% - 100%) / (100% - 0%)", (d[2] - d[1]) / (d[1] - d[0]), 0.97, 1.03)
    # C-P8 Shield Specialization: each block restores 6% of maximum mana (3/3), one time each 2 sec.
    # The debug log of one fight gives each mana gain and the maximum mana.
    rq = request(p, "raid", tank=True, iters=1, dur=120); rq["simOptions"]["debug"] = True
    gains = [(float(t), float(g) / float(m)) for t, g, m in re.findall(
        r"\[([\d.]+)\] \[Player \(#1\)\] Gained ([\d.]+) mana from \{SpellID: 1310925[^}]*\} .* of ([\d.]+) total",
        sim(rq, "C6,C13")["logs"])]
    check("Shield Specialization (C-P8): mana of each block / maximum mana", min(g for _, g in gains), 0.0599, 0.0601)
    check("Shield Specialization (C-P8): largest mana of each block / maximum mana", max(g for _, g in gains), 0.0599, 0.0601)
    check("Shield Specialization (C-P8): shortest time between two mana gains, sec",
          min(b[0] - a[0] for a, b in zip(gains, gains[1:])), 2.0, 60.0)

    print(f"\n{sum(results)} of {len(results)} checks pass")
    sys.exit(0 if all(results) else 1)
