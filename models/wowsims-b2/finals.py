"""builds/: the 3,000 iteration check of the search builds, and the stat weights (same random seed for all runs).
Run: python3 finals.py > logs/finals.log. With codes as arguments, only those builds run (append to logs/finals.log). Needs /tmp/bin/rettest and /tmp/bin/prottest (see run.sh).
The shock builds (wowsims Holy Shock set and rotation): python3 finals.py shock > logs/finals_shock.log."""
import os
from concurrent.futures import ThreadPoolExecutor
import search as S

RB1 = "050250002-501-05233011201301351"
BS2 = "-05302102313501531-52233000001"  # live tank with Sacred Arbiter
BUILDS = [
    ("ret", "raid", "beta", RB1), ("ret", "raid", "beta", "050150001-503-15233011101301351"),
    ("ret", "raid", "prop", RB1), ("ret", "raid", "prop", "050150002-502-05233011201301351"),
    ("ret", "fresh", "beta", RB1), ("ret", "fresh", "beta", "050150001-503-15233011101301351"),
    ("ret", "fresh", "prop", RB1), ("ret", "fresh", "prop", "050050002-503-15233011101301351"),
    ("prot", "raid", "beta", "050050002-05302102213301531-502"), ("prot", "raid", "beta", "05005-05302102213201531-5023"),
    ("prot", "raid", "beta", BS2),
    ("prot", "raid", "prop", "-3530110213501531-54233"), ("prot", "raid", "prop", "-3530110213501531-53233000001"),
]
SB1 = "05025210221021--0523330110130033"  # the wowsims Holy Shock build (HolyShockTalents)
SB2 = "05025211222021051--052323010013"   # 31 Holy points with Light's Vigil (C-H7)
SB3 = "15325210222121201--052330002013"   # 32/0/19 hybrid healer: Light's Vigil, Oath of Light, Boundless Light, no Holy Power
SF1 = "0502521022102--0523330110130034"    # fresh 60 climb, live trees: no Holy Shock, Champion of the Light 4
SF2 = "0502520122102--0523330110130034"    # fresh 60 climb, proposed trees: also Illumination 1 for Divine Favor
SHOCK_BUILDS = [("shock", case, mode, code) for case in ("raid", "fresh") for mode in ("beta", "prop")
                for code in (SB1, SB2, SB3, SF1, SF2)]
SHOCK_WEIGHTS = [("shock", "raid", "beta", SB1), ("shock", "raid", "prop", SB1), ("shock", "fresh", "beta", SB1),
                 ("shock", "raid", "prop", SB2)]
# stat index (proto Stat order): name, amount
RET_STATS = [(0, "Strength", 20), (1, "Agility", 20), (3, "Intellect", 20), (5, "Spell damage", 40),
             (14, "Attack power", 40), (17, "Hit rating", 10), (18, "Crit rating", 10), (19, "Haste rating", 10),
             (21, "Expertise rating", 10)]
PROT_STATS = [(0, "Strength", 20), (1, "Agility", 20), (2, "Stamina", 20), (5, "Spell damage", 40),
              (17, "Hit rating", 10), (21, "Expertise rating", 10), (22, "Defense rating", 10),
              (23, "Block rating", 10), (24, "Block value", 20), (25, "Dodge rating", 10), (26, "Parry rating", 10),
              (28, "Armor", 200)]
WEIGHTS = [("ret", "raid", "beta", RB1), ("ret", "raid", "prop", RB1), ("ret", "fresh", "beta", RB1),
           ("prot", "raid", "beta", "050050002-05302102213301531-502"), ("prot", "raid", "beta", BS2), ("prot", "raid", "prop", "-3530110213501531-54233")]

def go(spec, case, mode, code, bonus=None):
    return S.run(spec, case, S.decode(code, mode), mode, it=3000, extra={"FEEDBACK_BONUS": bonus} if bonus else None)

if __name__ == "__main__":
    import sys
    if sys.argv[1:] == ["shock"]:
        BUILDS, WEIGHTS = SHOCK_BUILDS, SHOCK_WEIGHTS
    elif sys.argv[1:]:
        BUILDS = [b for b in BUILDS if b[3] in sys.argv[1:]]
        WEIGHTS = [b for b in WEIGHTS if b[3] in sys.argv[1:]]
    with ThreadPoolExecutor(4) as ex:
        res = list(ex.map(lambda b: go(*b), BUILDS))
    for b, r in zip(BUILDS, res):
        print("BUILD", *b, {k: r[k] for k in ("dps", "tps", "dtps", "tmi", "oom", "crush", "std") if k in r}, flush=True)
    for spec, case, mode, code in WEIGHTS:
        st = PROT_STATS if spec == "prot" else RET_STATS
        jobs = [None] + [f"{i}:{n}" for i, _, n in st]
        with ThreadPoolExecutor(4) as ex:
            rr = list(ex.map(lambda j: go(spec, case, mode, code, j), jobs))
        base = rr[0]
        print(f"WEIGHTS {spec} {case} {mode} {code} base={ {k: base[k] for k in ('dps', 'tps', 'dtps', 'tmi') if k in base} }")
        for (i, name, n), r in zip(st, rr[1:]):
            d = {k: (r[k] - base[k]) / n for k in ("dps", "tps", "dtps", "tmi") if k in base}
            print(f"  {name}: " + " ".join(f"{k}={v:+.3f}" for k, v in d.items()), flush=True)
