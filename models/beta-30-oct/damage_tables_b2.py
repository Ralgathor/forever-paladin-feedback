"""Analysis, Damage, on the beta of 30 October 2026: the tables that retribution_b2.py does not print.
Run: python3 damage_tables_b2.py ../damage
Build: the wowsims default Retribution build of 1 November, 14/6/31 (retribution_b2.py). Fury, Arms and Combat Rogue: damage_model.py.
"""
import sys
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else "../damage"]
sys.path.insert(0, sys.argv[1]); sys.path.insert(0, ".")
import damage_model as M
from retribution_b2 import retribution_b2, stats_b2, PURE, RET_SIM
from damage_model import gear, TIER_NAMES, fury, arms, rogue

g = gear(0)
s = stats_b2(g)
print(f"## Stats with talents and raid buffs: Attack Power {s['ap']:.0f}, spell damage {s['sd']:.0f} "
      f"(Champion of the Light {s['sd'] - g['sd']:.0f}), hit {s['hit']:.0%}, critical hit {s['crit']:.1%}, "
      f"Intellect {s['int']:.0f}")

for lab, kw in (("beta", {}), ("C1", dict(c1=True))):
    tot, src, V, mana = retribution_b2(g, detail=True, **kw)
    holy = tot - src["Auto attacks"]
    print(f"## Sources, {lab}, 2 min: " + ", ".join(f"{k} {v:.0f} ({v / tot:.0%})" for k, v in src.items())
          + f"; total {tot:.0f}; Holy {holy / tot:.0%}; spend {mana['spend']:.1f}")
b0 = retribution_b2(g)
print(f"## 5 min fight: {retribution_b2(g, fight=300) / b0 - 1:+.1%}")

print("\n## Against the pure average (wowsims, same item pool for each spec) at fresh level 60")
avg = sum(PURE.values()) / len(PURE)
c1 = RET_SIM * retribution_b2(g, c1=True) / b0
no_rogue = (avg * 5 - PURE["Rogue"]) / 4
print(f"  pure average {avg:.0f}; beta {RET_SIM} ({RET_SIM / avg:.0%}, Fury {RET_SIM / PURE['Warrior']:.0%}); "
      f"C1 {c1:.0f} ({c1 / avg:.0%}, Fury {c1 / PURE['Warrior']:.0%}); without Rogue {no_rogue:.0f}: beta "
      f"{RET_SIM / no_rogue:.0%}, C1 {c1 / no_rogue:.0%}")
print(f"  same gear (model): beta Retribution {b0:.0f}, Fury {fury(g):.0f}, Arms {arms(g):.0f}, Combat Rogue {rogue(g):.0f}")

print("\n## Increase from fresh level 60: Retribution | spell damage stays | Fury | Arms | Combat Rogue")
R = [retribution_b2(gear(t)) for t in range(5)]
R254 = [retribution_b2(gear(t, sd_fixed=True)) for t in range(5)]
RF = [retribution_b2(gear(t, flat=True)) for t in range(5)]
RF254 = [retribution_b2(gear(t, flat=True, sd_fixed=True)) for t in range(5)]
F = [fury(gear(t)) for t in range(5)]
FF = [fury(gear(t, flat=True)) for t in range(5)]
A = [arms(gear(t)) for t in range(5)]
C = [rogue(gear(t)) for t in range(5)]
for t, n in enumerate(TIER_NAMES):
    print(f"  {n} | x{R[t] / R[0]:.2f} | x{R254[t] / R254[0]:.2f} | x{F[t] / F[0]:.2f} | x{A[t] / A[0]:.2f} | x{C[t] / C[0]:.2f}")
start_b, start_c = RET_SIM / PURE["Warrior"], c1 / PURE["Warrior"]
print("## Retribution as a % of Fury (wowsims start, same item pool), beta | C1: Classic steps, spell damage stays, flatter, flatter + stays")
for t, n in enumerate(TIER_NAMES):
    row = []
    for st in (start_b, start_c):
        row.append(f"{st * R[t] / R[0] / (F[t] / F[0]):.0%}/{st * R254[t] / R254[0] / (F[t] / F[0]):.0%}/"
                   f"{st * RF[t] / RF[0] / (FF[t] / FF[0]):.0%}/{st * RF254[t] / RF254[0] / (FF[t] / FF[0]):.0%}")
    print(f"  {n} | " + " | ".join(row))
_, s0, _, _ = retribution_b2(gear(0), detail=True)
_, s4, _, _ = retribution_b2(gear(4), detail=True)
print("## Increase of each source to Naxxramas: " + ", ".join(f"{k} x{s4[k] / s0[k]:.2f}" for k in s0))
fixed = (0.125 * 178.2 * 1.15 + 0.1 * 0.5 * 93 * 1.2)   # rough: shown as shares below
tot0 = sum(s0.values())
print(f"  shares at fresh level 60: auto attacks and Seal of Command {(s0['Auto attacks'] + s0['Seal of Command']) / tot0:.0%}")
print(f"  Naxxramas: Retribution {retribution_b2(gear(4)) / arms(gear(4)):.0%} of Arms (same gear, model), "
      f"{RET_SIM * R[4] / R[0] / (PURE['Rogue'] * C[4] / C[0]):.0%} of Combat Rogue (beta)")

print("\n## Judgement of the Crusader (fresh level 60 | Naxxramas)")
for lab, kw in (("beta", {}), ("C1", dict(c1=True))):
    a0, a4 = retribution_b2(gear(0), **kw), retribution_b2(gear(4), **kw)
    c0, c4 = retribution_b2(gear(0), crusader=True, **kw), retribution_b2(gear(4), crusader=True, **kw)
    print(f"  {lab}: +{c0 - a0:.0f} ({c0 / a0 - 1:+.1%}) | +{c4 - a4:.0f} ({c4 / a4 - 1:+.1%})")
_, sa_, _, _ = retribution_b2(g, detail=True)
_, sc_, _, _ = retribution_b2(g, detail=True, crusader=True)
print("  by source (beta): " + ", ".join(f"{k} {sc_[k] - sa_[k]:+.1f}" for k in sa_))

print("\n## Stat values (beta, 5 min, DPS for each point)")
base5 = retribution_b2(g, fight=300)
def stat(**d):
    h = dict(g); [h.__setitem__(k, h[k] + v) for k, v in d.items()]
    return retribution_b2(h, fight=300) - base5
print(f"  spell damage {stat(sd=10) / 10:.2f}, Attack Power {stat(ap_items=10) / 10:.2f}, Strength {stat(str=10) / 10:.2f}, "
      f"1% critical hit {stat(crit=0.01):.1f}, 1% hit {stat(hit=0.01):.1f}, Intellect {stat(int=10) / 10:.2f}")
print(f"  hit: gear {g['hit']:.0%} + Precision 1% = {s['hit']:.0%}; cap {M.MISS:.0%}")
thws0 = retribution_b2(g, tal=dict(__import__('retribution_b2').B2, thws=0))
print(f"  Two-Handed Weapon Specialization 3/3: {b0 - thws0:+.1f} DPS ({b0 / thws0 - 1:+.1%})")

print("\n## C1 review: against the pure average, Hunter, Mage and Warlock x1.75 (5 tiers)")
gr = lambda f, **kw: [f(gear(t, **kw)) / f(gear(0, **kw)) for t in range(5)]
F, A, C = gr(fury), gr(arms), gr(rogue)
shape = [(a - 1) / (A[4] - 1) for a in A]
casters = PURE["Hunter"] + PURE["Mage"] + PURE["Warlock"]
pure = [(PURE["Warrior"] * F[t] + PURE["Rogue"] * C[t] + casters * (1 + 0.75 * shape[t])) / 5 for t in range(5)]
cases = (("beta", {}, {}), ("C1", dict(c1=True), {}), ("C1, Sacred Arbiter +10%", dict(c1=True, tal=dict(__import__('retribution_b2').B2, sa=0.5)), {}),
         ("C1, Sacred Arbiter +0%", dict(c1=True, tal=dict(__import__('retribution_b2').B2, sa=0)), {}),
         ("beta, spell damage stays", {}, dict(sd_fixed=True)), ("C1, spell damage stays", dict(c1=True), dict(sd_fixed=True)))
for lab, kw, gk in cases:
    base = [retribution_b2(gear(t, **gk)) for t in range(5)]
    row = [RET_SIM * base[t] / base[0] * retribution_b2(gear(t, **gk), **kw) / base[t] / pure[t] for t in range(5)]
    print(f"  {lab}: " + " | ".join(f"{r:.0%}" for r in row))
