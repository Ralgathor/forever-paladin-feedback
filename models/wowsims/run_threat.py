"""Protection against the Warrior and the Druid (Analysis, Threat, part 7). Run: python3 run_threat.py"""
from concurrent.futures import ThreadPoolExecutor
from wowsims import *
from builds import *

PROP_GEAR = json.load(open(os.path.join(HERE, "data", "prebis_proposed_gear.json")))
GEARS = {"Julien gear": julien()["equipment"], "Proposed pre-raid gear": PROP_GEAR}
VARIANTS = [("All proposals", PROT_PROP), ("Holy Shield 150%", PROT_PROP + ",HSBV150"),
            ("Holy Shield 100%", PROT_PROP + ",HSBV100"), ("Iron Creed 6%", PROT_PROP + ",IC6"),
            ("Crushing blow fix only (C-P1)", "C6")]
SCENS = ("raid", "raid_nocons")

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
    return dict(ThreadPoolExecutor(4).map(lambda j: (j[0], tank(j[1], j[2], j[3])), jobs))

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
