"""PvP burst check on the beta of 30 October 2026 (W6). Estimates, not a simulation.
Run: python3 pvp_burst_b2.py

Burst in one 6 sec Hammer of Justice stun. Same assumptions as Analysis, PvP burst check (beta of 18 October):
- Two-handed weapon, 3.5 sec, 300 damage for each swing. Armor removes 30% of physical damage. 1.7 auto attacks in the stun.
- Critical hit: two times the damage. 26% chance (Conviction 3/3 now gives +6%).
- Two-Handed Weapon Specialization 3/3: +6% physical damage only (beta of 30 October). Thus, not on Seals, Judgements
  and the Holy damage of Holy Strike.
- Seal of Command: 41% chance on each swing, 70% of weapon damage as Holy damage.
- Holy Strike: 150 + 109 Holy damage, Sacred Arbiter +20%. Holy Strike Seal trigger (C1): also Seal of Command.
- Judgement of Command on a stunned target: 405 (tooltip with gear). Swift Judgement gives a second Judgement.
- Unsealed Wrath (Retribution 31 points): 3 stored Seal of Command copies, consumed by a Seal change.
Reckoning charge rate: a melee attacker hits each 1.0-2.0 sec. 20% of the attacks that are not blocked are critical hits.
"""
import random

C = 0.26; ARM = 0.70; THS = 1.06; W = 300.0; SOC = 0.41*0.70*W*(1 + C)

def auto(n): return n*(W*ARM*THS*(1 + C) + SOC)
def holy_strike(c1): return (150 + 109)*1.2*(1 + C) + (SOC if c1 else 0)
def judgements(n): return n*405*(1 + C)

def bursts():
    extra = auto(1)
    rows = []
    for name, c1 in (("Beta", False), ("Proposed (C1)", True)):
        base = holy_strike(c1) + auto(1.7) + judgements(2)
        uw = holy_strike(c1) + auto(1.7) + judgements(2) + 3*SOC
        rows.append((name, base, base + 4*extra, uw))
    return extra, rows

def reckoning(p_block, chance, icd, crit=0.20, shield=True, T=600000, seed=1):
    rnd = random.Random(seed); t = 0; last = -99; n = 0; charges = 0; t0 = 0; full = []
    while t < T:
        t += rnd.uniform(1.0, 2.0)
        r = rnd.random()
        if shield and r < p_block:
            if t - last >= icd and rnd.random() < chance:
                last = t; n += 1; charges += 1
        elif r < (p_block if shield else 0) + crit:
            n += 1; charges += 1
        if charges >= 4:
            full.append(t - t0); charges = 0; t0 = t
    return n/(T/60), sum(full)/len(full)

if __name__ == "__main__":
    extra, rows = bursts()
    print(f"Extra attack: {extra:.0f}")
    print("Case | 0/25/26, no stored attacks | 0/25/26, 4 stored attacks | 0/20/31 Unsealed Wrath")
    for r in rows:
        print(f"{r[0]} | {r[1]:.0f} | {r[2]:.0f} | {r[3]:.0f}")
    print("Reckoning 5/5: charges each min, time to 4 charges")
    print("Two-handed (crit trigger only, beta = C-P12): %.1f, %.0f sec" % reckoning(0, 0, 0, shield=False))
    for p in (0.35, 0.60):
        for name, c, i in (("beta", 0.40, 1.5), ("C-P12 (withdrawn)", 1.0, 4.0)):
            print(f"Shield, {p:.0%} block, {name}: " + "%.1f, %.0f sec" % reckoning(p, c, i))
