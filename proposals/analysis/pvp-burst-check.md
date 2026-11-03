# PvP burst check

**Question.** Do the proposals make the PvP burst of the Paladin too high? This check is for Watch list W6.

"Burst" is the damage that the Paladin does to a player during one Hammer of Justice stun (6 sec). The target cannot act during the stun.

## Short answer

- **The kept proposals do not change the burst.** The Holy Strike Seal trigger (C1) added 3–5%, and it was withdrawn on 2 November 2026.
- **The largest burst** is the "Reckoning bomb" with a two-hand weapon: about 3,630 damage in the live version.
- **Reckoning (C-P12) was withdrawn on 2 November 2026.** It did not change the two-hand bomb. With a shield, it gave the 4 charges 1–3 sec sooner (part 3).
- **No change to the proposals is necessary.** Watch the bomb in the live version (W6, W26).
- **Light's Vigil (C-H7) adds a Holy Shock burst.** With 3 stacks, three Holy Shocks hit in one stun: 1,640–2,160 damage. A fourth one at the end of the stun gives 2,180–2,880. Live: one Holy Shock, 550–720. The burst is ready each 18 sec, with no setup. This is accepted for now: watch it in PvP (W30, part 6).

## 1. Builds

| Build | Points | Main talents |
| --- | --- | --- |
| Reckoning bomb | 0/25/26, two-hand weapon | Reckoning 5/5, Swift Judgement, Improved Hammer of Justice 3/3, Seal of Command, Conviction 3/3, Sacred Arbiter, Two-Handed Weapon Specialization 3/3, Vengeance 3/3 |
| Unsealed Wrath | 0/20/31, two-hand weapon | Swift Judgement, Improved Hammer of Justice 3/3, Unsealed Wrath. No Reckoning |
| Protection | Shield | Reckoning 5/5, Shieldsworn. A one-hand weapon gives a smaller burst |

**What the Reckoning bomb does.** Reckoning stores extra attacks when the Paladin takes a critical hit (or blocks, with a shield). The stored attacks all hit on the next auto attack. With 4 stored attacks, the Paladin does a large burst in one stun.

## 2. Burst in one stun

| Case | Reckoning bomb, no stored attacks | Reckoning bomb, 4 stored attacks | Unsealed Wrath |
| --- | --- | --- | --- |
| Live | 2,070 | 3,630 | 2,400 |
| Proposed | 2,070 | 3,630 | 2,400 |
| With C1 (withdrawn) | 2,180 (+5%) | 3,740 (+3%) | 2,510 (+5%) |

- **Each extra attack** does about 390 damage. 4 stored attacks add about 1,560.
- **C1 (withdrawn)** gave Holy Strike a Seal of Command chance: about +110 damage.
- **Unsealed Wrath** stores 3 copies of Seal of Command. A Seal change releases them: about +330. C1 did not change this, because Unsealed Wrath stores copies only from auto attacks.

## 3. How fast Reckoning stores 4 attacks

Reckoning 5/5, one melee attacker with an attack each 1.5 sec.

| Case | Charges each min | Time to 4 charges |
| --- | --- | --- |
| Two-hand weapon, live | 8.0 | 30 sec |
| Shield, 35% block, live | 13.2 | 18 sec |
| Shield, 35% block, C-P12 (withdrawn) | 16.0 | 15 sec |
| Shield, 60% block (Redoubt, C-P1), live | 16.6 | 14 sec |
| Shield, 60% block (Redoubt, C-P1), C-P12 (withdrawn) | 18.4 | 13 sec |

- **Two-hand weapon:** no shield, thus no blocks. Only critical hits give charges.
- **Shield:** Redoubt (C-P1) gives the 4 charges 4 sec sooner. But 4 stored one-hand attacks add only about 1,050 damage, against 1,560 with a two-hand weapon.
- **C-P12 (withdrawn)** gave the 4 charges 1–3 sec sooner with a shield.

## 4. Changes since the check of 18 October

- Two-Handed Weapon Specialization increases only physical damage in this check (beta of 30 October). Build 70755 also gives it Holy damage.
- Conviction 3/3 gives +6% critical chance (26% in the model).
- Improved Hammer of Justice 3/3 gives a 45 sec cooldown.
- Reckoning (C-P12) replaced the withdrawn Reckoning proposal (C-P6). C-P12 was also withdrawn on 2 November 2026. Reckoning now works as in the live version.

## 5. Earlier check: Reckoning (C-P6), beta of 18 October

This check was for the withdrawn proposal C-P6. C-P6 released the stored attacks with Holy Strike. The build was 0/26/25 with a two-hand weapon ([`v5p-532300210215002-5005031211331`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#v5p-532300210215002-5005031211331), RB5).

| Part of the burst | C-P6 | Beta, no stored attacks | Beta, 4 stored attacks |
| --- | --- | --- | --- |
| Holy Strike | 500 | 390 | 390 |
| Extra attacks (about 390 each) | 2: 780 | 0 | 4: 1,570 |
| Auto attacks (about 1.7) | 670 | 670 | 670 |
| Two Judgements on a stunned target | 1,070 | 1,070 | 1,070 |
| **Total** | **3,020** | **2,130** | **3,700** |

- C-P6 was about 42% above the usual beta burst, and about 18% below the best beta burst.
- The error of this estimate is about ±25%: 2,270–3,780.
- Swift Judgement gave about 18% of the burst. When it was on cooldown, the C-P6 total was about 2,490.

## 6. Light's Vigil (C-H7) on an enemy

On an enemy, Light's Vigil removes the Holy Shock cooldown. It does not change the Holy Shock damage. Thus each stack gives one more Holy Shock in a burst.

| Case | Holy Shocks in one stun | Holy Shock damage |
| --- | --- | --- |
| Live (10 sec cooldown) | 1 | 550–720 |
| C-H7, 3 stacks | 3 | 1,640–2,160 |
| C-H7, 3 stacks, a fourth Holy Shock as the stun ends | 4 | 2,180–2,880 |

- **Inputs.** Holy Shock: 348 + 42.9% of spell damage, 400 to 715 spell damage, 10–20% critical hit chance, ×1.5 damage on a critical hit. Holy Power changes only heals.
- **Order.** Hammer of Justice uses the first global cooldown. Then three Holy Shocks land in the stun. The first Holy Shock gives a fourth stack when the 6 sec limit is over.
- **Against the Retribution bursts.** The Reckoning bomb does 3,630, Unsealed Wrath 2,400 and the bomb with no stored attacks 2,070. Four Holy Shocks with auto attacks and a Judgement reach the level of the Reckoning bomb.
- **Differences.** The Holy Shock burst has no setup. It is ready each 18 sec (3 stacks), and Holy Shock has a range of 20 yd. The Reckoning bomb needs 4 stored attacks.
- **Decision of 3 November.** Light's Vigil keeps its effect on enemies. Watch the burst in PvP (W30). If it is too strong, the next Holy Shock incurs no cooldown only when cast on allies. This change gives no healing loss.
- **Model.** `models/beta-30-oct/light_vigil_ch7.py` gives the healing burst. The damage values are estimates.

## 7. Method and limits

- **Model.** `models/beta-30-oct/pvp_burst_b2.py`. The values are estimates, not a simulation.
- **Inputs of the earlier check.** Two-hand weapon: 3.5 sec, 300 damage for each swing. About 1.7 auto attacks during the stun. 25% critical hit chance, ×2 damage. Armor removes 30% of physical damage. Vengeance is not in the model. Seal of Command: 7 procs each min (41% for each swing), each 70% of weapon damage as Holy damage. Judgement of Command on a stunned target: 388–422.
- **Real fights** also have PvP gear, trinkets and other players. The model does not include them.
