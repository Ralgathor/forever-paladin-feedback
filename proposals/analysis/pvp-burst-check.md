# PvP burst check

## Beta of 30 October 2026

This check is for Watch list W6. The model is models/beta-30-oct/pvp_burst_b2.py. The values are estimates, not a simulation.

**Builds**

- **0/25/26, two-handed weapon (the Reckoning bomb).** Protection 25: Reckoning 5/5, Swift Judgement, Improved Hammer of Justice 3/3. Retribution 26: Seal of Command, Conviction 3/3, Sacred Arbiter, Two-Handed Weapon Specialization 3/3, Vengeance 3/3.
- **0/20/31, two-handed weapon (Unsealed Wrath).** Protection 20 gives Swift Judgement and Improved Hammer of Justice. This build cannot take Reckoning.
- **Protection with a shield.** Reckoning 5/5 and Shieldsworn. A one-handed weapon gives a smaller burst.

**Changes against the check of 18 October**

- Two-Handed Weapon Specialization now increases only physical damage. Thus, it does not increase Seals, Judgements and the Holy damage of Holy Strike.
- Conviction 3/3 gives +6% critical chance (26% in the model).
- Improved Hammer of Justice 3/3 gives a 45 sec cooldown.
- Reckoning (C-P12) replaces Reckoning (C-P6). The release stays as in the beta: the stored attacks occur on the next auto attack.

**Burst in one 6 sec Hammer of Justice stun**

| Case | 0/25/26, no stored attacks | 0/25/26, 4 stored attacks | 0/20/31, Unsealed Wrath |
| --- | --- | --- | --- |
| Beta | 2,070 | 3,630 | 2,400 |
| Proposed (C1, C-P12) | 2,180 (+5%) | 3,740 (+3%) | 2,510 (+5%) |

- Each extra attack does about 390 damage. 4 stored attacks add about 1,560.
- Holy Strike Seal trigger (C1) adds one Seal of Command chance to Holy Strike: about +110. This is the only change from the proposals.
- Unsealed Wrath gives 3 stored Seal of Command copies. A Seal change consumes them: about +330. C1 does not change Unsealed Wrath, because Unsealed Wrath triggers only on auto attacks.

**Reckoning charges (5/5, one melee attacker, an attack each 1.5 sec)**

| Case | Charges each min | Time to 4 charges |
| --- | --- | --- |
| Two-handed weapon, beta and C-P12 | 8.0 | 30 sec |
| Shield, 35% block, beta | 13.2 | 18 sec |
| Shield, 35% block, C-P12 | 16.0 | 15 sec |
| Shield, 60% block (with Redoubt, C-P1), beta | 16.6 | 14 sec |
| Shield, 60% block (with Redoubt, C-P1), C-P12 | 18.4 | 13 sec |

- **Two-handed weapon.** There is no block without a shield. Thus, only the critical hit trigger works, and C-P12 does not change the bomb.
- **Shield.** With C-P12, 4 charges come 1–3 sec sooner. But a one-handed weapon does less damage: 4 stored attacks add about 1,050 (estimate), against 1,560 with a two-handed weapon.

**Result**

- The proposals increase the PvP burst by 3–5%. All of it comes from Holy Strike Seal trigger (C1).
- Reckoning (C-P12) does not change the largest burst (two-handed weapon). It makes the smaller shield burst a little more frequent.
- Thus, W6 needs no change to the proposals. Monitor the bomb in the beta (W6, W26).

## Beta of 18 October 2026 (earlier check)

This check is for Reckoning (C-P6). The build is 0/26/25 with a two-handed weapon. It is the build v5p-532300210215002-5005031211331 in the calculator (RB5):

- Protection 26: Reckoning 5/5, Swift Judgement, Improved Hammer of Justice 2/3.
- Retribution 25: Seal of Command, Sacred Arbiter, Two-Handed Weapon Specialization 3/3, Vengeance 3/3, Conviction 5/5.
- Toughness and Divine Strength removal (C-P3) deletes Divine Strength from this build. The model uses a fixed 300 damage for each swing. Thus, the values do not change. Without +10% Strength, the real burst is about 2% lower.

The values are estimates, not a simulation.

**Assumptions**

- One 6 sec Hammer of Justice stun. Hammer of Justice has a 50 sec cooldown in this build (60 sec, −10 sec at 2/3).
- Two-handed weapon: 3.5 sec speed, 300 damage for each swing, with Attack Power. About 1.7 auto attacks occur during the stun.
- Two-Handed Weapon Specialization (+6%) applies to melee attacks, Seals, Judgements and Holy Strike.
- 25% critical hit chance. A critical hit does two times the damage. Armor removes 30% of physical damage. Vengeance is not in the model.
- Seal of Command: 7 procs each minute (41% chance for each swing). Each proc does 70% of weapon damage as Holy damage.
- Holy Strike rank 8: 50% of weapon damage plus 81–105, all Holy damage.
- Judgement of Command on a stunned target: 388–422 (in-game tooltip with gear; the base value is 339–373). Swift Judgement gives a second Judgement in the same stun.
- In the beta, Holy Strike does not trigger Seal of Command. Extra attacks are the same as auto attacks, with Seal of Command procs.

| Part of the burst | Proposed | Beta, no stored attacks | Beta, 4 stored attacks |
| --- | --- | --- | --- |
| Holy Strike | 500 (+20%, and Seal of Command on 41% of Holy Strikes, Holy Strike Seal trigger, C1) | 390 (+20% damage, no Seal effect) | 390 |
| Extra attacks (about 390 each) | 2: 780 | 0 | 4: 1,570 |
| Auto attacks (about 1.7) | 670 | 670 | 670 |
| Two Judgements on a stunned target (about 535 each) | 1,070 | 1,070 | 1,070 |
| **Total** | **3,020** | **2,130** | **3,700** |

All values are approximate.

- **Result.** The proposal is about 42% above the usual beta burst. It is about 18% below the best beta burst (the Classic bomb with 4 stored attacks).
- **Uncertainty.** About ±25%: 2,270–3,780.
- **Swift Judgement** gives about 18% of the burst. When Swift Judgement is on cooldown (60 sec, and 50 sec for Hammer of Justice), the proposed total is about 2,490. It is on the watch list (W6).
