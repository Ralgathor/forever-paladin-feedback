"""builds/: the 3,000 iteration check of the search builds, and the stat weights (same random seed for all runs).
Run: python3 finals.py > finals.log. With codes as arguments, only those builds run (append to finals.log). Needs /tmp/bin/rettest and /tmp/bin/prottest (see run.sh)."""
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
    if sys.argv[1:]:
        BUILDS = [b for b in BUILDS if b[3] in sys.argv[1:]]
        WEIGHTS = [b for b in WEIGHTS if b[3] in sys.argv[1:]]
    with ThreadPoolExecutor(4) as ex:
        res = list(ex.map(lambda b: go(*b), BUILDS))
    for b, r in zip(BUILDS, res):
        print("BUILD", *b, {k: r[k] for k in ("dps", "tps", "dtps", "tmi", "oom", "crush", "std") if k in r}, flush=True)
    for spec, case, mode, code in WEIGHTS:
        st = RET_STATS if spec == "ret" else PROT_STATS
        jobs = [None] + [f"{i}:{n}" for i, _, n in st]
        with ThreadPoolExecutor(4) as ex:
            rr = list(ex.map(lambda j: go(spec, case, mode, code, j), jobs))
        base = rr[0]
        print(f"WEIGHTS {spec} {case} {mode} {code} base={ {k: base[k] for k in ('dps', 'tps', 'dtps', 'tmi') if k in base} }")
        for (i, name, n), r in zip(st, rr[1:]):
            d = {k: (r[k] - base[k]) / n for k in ("dps", "tps", "dtps", "tmi") if k in base}
            print(f"  {name}: " + " ".join(f"{k}={v:+.3f}" for k, v in d.items()), flush=True)
