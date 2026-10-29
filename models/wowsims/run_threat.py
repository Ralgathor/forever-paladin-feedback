"""Protection against the Warrior and the Druid (Analysis, Threat, parts 7 and 8). Run: python3 run_threat.py"""
import copy
from concurrent.futures import ThreadPoolExecutor
from wowsims import *
from builds import *

PROP_GEAR = json.load(open(os.path.join(HERE, "data", "prebis_proposed_gear.json")))
PATH = json.load(open(os.path.join(HERE, "data", "tank_path_gear.json")))
GEARS = {"Julien gear": julien()["equipment"], "Proposed pre-raid gear": PROP_GEAR}
VARIANTS = [("All proposals", PROT_PROP), ("Holy Shield 150%", PROT_PROP + ",HSBV150"),
            ("Holy Shield 100%", PROT_PROP + ",HSBV100"), ("Iron Creed 6%", PROT_PROP + ",IC6"),
            ("Crushing blow fix only (C-P1)", "C6")]
SCENS = ("raid", "raid_nocons")

# Part 7: the best builds and the pre-raid path gear of builds/protection.md
def path_player(talents, gear):
    p = with_talents(julien(), talents); p["equipment"] = PATH[gear]["equipment"]; return p

PATH_RUNS = [("Beta BT4b", BT4b, "beta", ""), ("Proposed PT3", PT3, "proposed", PROT_ALL),
             ("Beta BT4b, proposed gear", BT4b, "proposed", ""), ("Proposed PT3, beta gear", PT3, "beta", PROT_ALL),
             ("PT3, no proposals", PT3, "proposed", ""),
             ("PT3, Holy Shield 150%", PT3, "proposed", PROT_ALL + ",HSBV150"),
             ("PT3, Holy Shield 100%", PT3, "proposed", PROT_ALL + ",HSBV100"),
             ("PT3, Iron Creed 6%", PT3, "proposed", PROT_ALL + ",IC6")]
PATH_RUNS += [(f"PT3 without {f}", PT3, "proposed", ",".join(x for x in PROT_ALL.split(",") if x != f))
              for f in ("C6", "C7", "C11", "C13", "C14", "C15", "C16")]

def tank(p, s, f=""):
    o = sim(request(p, s, tank=True), f)
    return dict(metrics(o), crush=boss_swings(o)["crushes"])

def run():
    jobs = [(("Paladin beta (Julien)", "Julien gear", s), julien(), s, "") for s in SCENS]
    jobs += [(("Warrior", "", s), load(WARRIOR_TANK), s, "") for s in SCENS]
    jobs += [(("Druid", "", s), load(BEAR), s, "") for s in SCENS]
    for g, eq in GEARS.items():
        for l, f in VARIANTS:
            p = with_talents(julien(), PB1); p["equipment"] = eq
            jobs += [((l, g, s), p, s, f) for s in SCENS]
    for l, t, g, f in PATH_RUNS:
        jobs += [((l, "Path gear", s), path_player(t, g), s, f) for s in SCENS]
    return dict(ThreadPoolExecutor(4).map(lambda j: (j[0], tank(j[1], j[2], j[3])), jobs))

# Part 8: groups of 3 and 5 enemies. Each enemy hits for 1/3 of the boss. The Druid uses Swipe on 2 or more targets.
def druid_multi(p):
    p = copy.deepcopy(p); apl = p["rotation"]
    multi = {"cmp": {"op": "OpGt", "lhs": {"numberTargets": {}}, "rhs": {"const": {"val": "1"}}}}
    for g in apl["groups"]:
        if g["name"] == "Damage":
            g["actions"].insert(1, {"action": {"condition": multi, "castSpell": {"spellId": {"spellId": 9908}}}})
    for a in apl["priorityList"]:
        if a.get("action", {}).get("castSpell", {}).get("spellId", {}).get("spellId") == 9881:
            rage = lambda v: {"cmp": {"op": "OpGe", "lhs": {"currentRage": {}}, "rhs": {"const": {"val": v}}}}
            one = {"cmp": {"op": "OpEq", "lhs": {"numberTargets": {}}, "rhs": {"const": {"val": "1"}}}}
            a["action"]["condition"] = {"or": {"vals": [{"and": {"vals": [one, rage("20")]}}, rage("45")]}}
    return p

GROUP_TANKS = {"Paladin beta (BT4b)": (path_player(BT4b, "beta"), ""),
               "Paladin proposed (PT3)": (path_player(PT3, "proposed"), PROT_ALL),
               "Warrior": (load(WARRIOR_TANK), ""), "Druid": (druid_multi(load(BEAR)), "")}

def group(p, f, n, share=1 / 3, iters=2000):
    rq = request(p, "raid", tank=True, iters=iters)
    t0 = rq["encounter"]["targets"][0]; t0["minBaseDamage"] *= share
    rq["encounter"]["targets"] = [dict(copy.deepcopy(t0), name=f"Mob {i + 1}") for i in range(n)]
    pl = player_metrics(sim(rq, f)); per = [0.0] * n
    for a in pl["actions"]:
        for x in a["targets"]:
            if x.get("unitIndex", 0) < n: per[x.get("unitIndex", 0)] += x.get("threat", 0)
    return [v / iters / rq["encounter"]["duration"] for v in per]

def run_groups():
    jobs = [(t, n) for t in GROUP_TANKS for n in (1, 3, 5)]
    return dict(ThreadPoolExecutor(4).map(lambda j: (j, group(*GROUP_TANKS[j[0]], j[1])), jobs))

if __name__ == "__main__":
    r = run()
    print("| Tank | Gear | " + " | ".join(f"{s}: TPS (% Warrior), TMI (% Warrior), crushing blows" for s in SCENS) + " |")
    print("| --- | --- | " + " | ".join("---" for _ in SCENS) + " |")
    for k in sorted({k[:2] for k in r}, key=lambda k: (k[1], k[0])):
        cells = []
        for s in SCENS:
            m, w = r[k + (s,)], r[("Warrior", "", s)]
            cells.append(f"{m['tps']:.0f} ({m['tps'] / w['tps']:.0%}), {m['tmi']:.1f} ({m['tmi'] / w['tmi']:.0%}), {m['crush']:.1f}%")
        print(f"| {k[0]} | {k[1]} | " + " | ".join(cells) + " |")
    g = run_groups()
    print("\n| Tank | 1 target | 3 targets | 5 targets |\n| --- | --- | --- | --- |")
    for t in GROUP_TANKS:
        print(f"| {t} | " + " | ".join(" / ".join(f"{v:,.0f}" for v in g[(t, n)]) for n in (1, 3, 5)) + " |")
