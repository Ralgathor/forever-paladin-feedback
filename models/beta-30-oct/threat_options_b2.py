"""Threat options after the development notes of 2 November 2026 (not proposals yet): % of the Warrior at each tier.
Run: python3 threat_options_b2.py

All rows have Redoubt (C-P1). The model gives Holy Shield too many hits, thus each gain over C-P1 is scaled by
CAL (0.55): the ratio of the wowsims gain to the model gain with the same gear (models/wowsims-b2/patches/threat-options.patch).
HS: the Holy Shield threat multiplier (live 1.2). CP9: Holy Shield adds this x block value to each hit (C-P9).
"""
import sys
import os; D = os.path.dirname(os.path.abspath(__file__))
base = sys.argv[1] if len(sys.argv) > 1 else os.path.join(D, "..")
for d in ("mana", "threat", "beta-30-oct"):
    sys.path.insert(0, f"{base}/{d}")
import threat_model as T
import threat_b2 as B

CAL = 0.55
OPTIONS = (("HS +100%", 2.0, 0), ("HS +125%", 2.25, 0), ("HS +150%", 2.5, 0), ("C-P9 100%", 1.2, 1.0),
           ("HS +50%, C-P9 75%", 1.5, 0.75), ("HS +100%, C-P9 100%", 2.0, 1.0))

def run(hs, cp9, g, crusader=True):
    B.HS_THREAT, B.CP9_BV = hs, cp9
    p = ("CP1", "CP9") if cp9 else ("CP1",)
    tps = B.paladin_b2(g, prop=p, crusader=crusader)
    B.HS_THREAT, B.CP9_BV = 1.2, 2.0
    return tps

if __name__ == "__main__":
    print("Tier | C-P1 | " + " | ".join(n for n, _, _ in OPTIONS))
    for t in T.TIERS:
        w, a = T.warrior(t), run(1.2, 0, t)
        cells = [f"{a / w:.0%}"] + [f"{(a + CAL * (run(hs, c, t) - a)) / w:.0%}" for _, hs, c in OPTIONS]
        print(f"{t.name} | " + " | ".join(cells))
