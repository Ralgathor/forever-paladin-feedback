# PvP burst check

This check is for C11 (Reckoning). The build is 0/26/25 with a two-handed weapon. It is the build p-5532000210215-50005031211331 in the calculator:

- Protection 26: Reckoning 5/5, Swift Judgement, Improved Hammer of Justice 2/3.
- Retribution 25: Seal of Command, Sacred Arbiter, Two-Handed Weapon Specialization 3/3, Vengeance 3/3, Conviction 5/5.

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
| Holy Strike | 500 (+20%, and Seal of Command on 41% of Holy Strikes, C16) | 390 (+20% damage, no Seal effect) | 390 |
| Extra attacks (about 390 each) | 2: 780 | 0 | 4: 1,570 |
| Auto attacks (about 1.7) | 670 | 670 | 670 |
| Two Judgements on a stunned target (about 535 each) | 1,070 | 1,070 | 1,070 |
| **Total** | **3,020** | **2,130** | **3,700** |

All values are approximate.

- **Result.** The proposal is about 42% above the usual beta burst. It is about 18% below the best beta burst (the Classic bomb with 4 stored attacks).
- **Uncertainty.** About ±25%: 2,270–3,780.
- **Swift Judgement** gives about 18% of the burst. When Swift Judgement is on cooldown (60 sec, and 50 sec for Hammer of Justice), the proposed total is about 2,490. It is on the watch list (W6).
