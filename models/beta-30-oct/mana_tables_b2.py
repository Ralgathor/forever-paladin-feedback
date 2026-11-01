"""Analysis, Mana, on the beta of 30 October 2026: the Protection tables.
Run: python3 mana_tables_b2.py ..   (the models folder of the repository)

Tank build B2T 0/38/13 (threat_b2.py). Proposed: the same talents with Redoubt (C-P1): 61.6% block (wowsims).
Sanctified Judgement (C-R3) does not change the return at 3/3. Costs and gear tiers: models/mana/mana_model.py.
"""
import sys
base = sys.argv[1] if len(sys.argv) > 1 else ".."
sys.argv = [sys.argv[0], base]
sys.path.insert(0, base + "/threat"); sys.path.insert(0, base + "/mana"); sys.path.insert(0, base + "/beta-30-oct")
import mana_model as M
import threat_model as T
from threat_b2 import mps_b2, B2T, BLOCK_B2, BLOCK_CP1

def fmt(m, v):
    return f"{v:+.1f}" + ("" if v >= 0 else f": {M.lasts(m, v)}")

def flat_tiers():
    """Analysis, Threat, part 3: from Molten Core, maximum mana at half the rate."""
    out = list(M.TIERS[:2]); pre = M.TIERS[1]
    for name, m, p5 in M.TIERS[2:]:
        out.append((name, pre[1] + (m - pre[1]) / 2, pre[2] + (p5 - pre[2]) / 2))
    return out

if __name__ == "__main__":
    print("## Income and cost, B2T, fresh level 60 (2,897) | Naxxramas (4,900), hit, no Consecration, no Wisdom")
    for lab, blk in (("beta", BLOCK_B2), ("C-P1", BLOCK_CP1)):
        for name, m, p5 in (M.TIERS[0], M.TIERS[-1]):
            v, inc, cost = mps_b2(m, p5, block=blk, detail=True)
            print(f"  {lab}, {name}: " + ", ".join(f"{k} {x:.1f}" for k, x in inc.items()) + f"; cost {cost:.1f}; result {v:+.1f}")
    _, _, c1 = mps_b2(2897, 3, cons=True, detail=True)
    print(f"  cost with Consecration {c1:.1f}")
    print("\n## Tiers, hit, no Consecration: beta | C-P1 | C-P1 flatter | beta + Wisdom | C-P1 + Wisdom")
    for (name, m, p5), (_, fm, fp5) in zip(M.TIERS, flat_tiers()):
        print(f"  {name} ({m}) | {mps_b2(m, p5):+.1f} | {mps_b2(m, p5, block=BLOCK_CP1):+.1f} | "
              f"{mps_b2(fm, fp5, block=BLOCK_CP1):+.1f} | {mps_b2(m, p5, wisdom=True):+.1f} | {mps_b2(m, p5, wisdom=True, block=BLOCK_CP1):+.1f}")
    print("\n## Other cases: fresh beta | fresh C-P1 | Naxx beta | Naxx C-P1")
    cases = (("Consecration on cooldown", dict(cons=True)), ("Consecration, Wisdom", dict(cons=True, wisdom=True)),
             ("Not hit", dict(hit=False)), ("Not hit, Wisdom", dict(hit=False, wisdom=True)),
             ("Not hit, Consecration", dict(hit=False, cons=True)),
             ("No Shieldsworn", dict(tal=dict(B2T, shs=0))),
             ("No Sanctified Judgement", dict(tal=dict(B2T, sanj=0))),
             ("No Benediction", dict(tal=dict(B2T, ben=0))))
    for lab, kw in cases:
        cols = []
        for name, m, p5 in (M.TIERS[0], M.TIERS[-1]):
            for blk in (BLOCK_B2, BLOCK_CP1):
                cols.append(fmt(m, mps_b2(m, p5, block=blk, **kw)))
        print(f"  {lab}: " + " | ".join(cols))
    print("\n## Sanctified Judgement by rank (8.5 Judgements each min): beta | C-R3")
    j = 1 / 8 + 1 / 60
    for r in (1, 2, 3):
        beta = M.SEAL_OF_FURY * (r / 3) * 0.2 * r * j
        print(f"  {r}/3: {beta:.1f} | {M.SEAL_OF_FURY * 0.2 * r * j:.1f}")
    print(f"\n## Reverence 2/2 (30%) at 130 Spirit: {0.30 * (15 + 130 / 5) / 2:.1f} MPS")
    print("\n## Lay on Hands at full mana, time until the mana is back (hit, Wisdom): beta drain all | Devoted Sacrifice 2/2")
    for name, m, p5 in (M.TIERS[0], M.TIERS[-1]):
        v = mps_b2(m, p5, wisdom=True)
        s = lambda x: f"{int(x // 60)} min {int(x % 60)} sec"
        print(f"  {name}: {v:+.1f} per sec | {s(m / v)} | {m / 2:.0f}: {s(m / 2 / v)}")
