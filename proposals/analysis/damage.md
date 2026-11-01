# Damage

This tab compares the single-target damage of Retribution with the other damage classes. The unit is damage per second (DPS) on one level 63 boss. The values use the beta of 30 October 2026 and wowsims Forever of 1 November 2026.

- **Start value:** wowsims Forever (master of 1 November) with the default Retribution set.
- **Increase with gear:** the model models/beta-30-oct/retribution_b2.py. The script damage_tables_b2.py in the same folder calculates all other tables of this tab.
- **Other classes:** the MythicSim values (22 October) and the model of models/damage (Fury, Arms, Combat Rogue).

## Summary

- **Beta.** Retribution does 906 DPS in wowsims, 100% of the pure average at fresh level 60. In Naxxramas, it is 94% (model). The hybrid target is 95%.
- **wowsims update of 1 November.** The new rotation, the Unsealed Wrath fix and new weapon oils give Retribution +7% (848 → 906).
- **Holy Strike Seal trigger (C1).** It gives +5.3% in the model and +5.6% in wowsims. With C1, Retribution is 105% of the pure average at fresh level 60 and 99% in Naxxramas.
- **C1 review.** Keep C1. Without it, Retribution goes below the hybrid target from Naxxramas (part 5).
- **Increase with gear.** Retribution increases ×1.63 to Naxxramas, Fury ×1.73. Fixed base values cause the gap. No talent change closes it.
- **Judgement of the Crusader** gives +9.3% at fresh level 60 and +6.3% in Naxxramas.

## 1. Build and gear

- **Build.** The wowsims default Retribution build of 1 November, 14/6/31 (050250002-501-05233011201301351).
  - Holy 14: Divine Strength 5/5, Reverence 2/2, Improved Seals 5/5, Holy Conduit 2/2.
  - Protection 6: Divine Intellect 5/5, Precision 1/1.
  - Retribution 31: Benediction 5/5, Improved Judgement 2/2, Conviction 3/3, Sanctified Judgement 3/3, Unyielding Faith 1, Seal of Command, Pursuit of Justice 2, Sacred Arbiter, Two-Handed Weapon Specialization 3/3, Repentance, Vengeance 3/3, Champion of the Light 5/5, Unsealed Wrath.
- **Gear.** A fresh level 60 profile: crafted items, dungeon items and quest rewards. Without talents and buffs: 283 Strength, 74 Agility, 5.9% critical hit, 5% hit, 254 spell damage and 87 Intellect.
- **Weapon.** Stormcarver (Blacksmithing, item level 63): 155–233 damage, 3.6 sec, +32 spell damage.
- **With talents and raid buffs.** 1,244 Attack Power, 326 spell damage (Champion of the Light gives 72), 6% hit, 12.6% critical hit and 3,029 mana.

## 2. Model

- **Raid buffs.** Blessing of Kings, Blessing of Might, Battle Shout, Mark of the Wild and Blessing of Wisdom. No consumables. No Judgement of the Crusader (see part 6).
- **Boss.** Level 63. 976 armor after 5 Sunder Armor and Faerie Fire. You attack from behind: no parry and no block.
- **Hit table.** 8% miss before hit. 6.5% dodge. 40% of auto attacks are glancing blows (−35% damage). Critical hit against the boss: −4.8%.
- **Unsealed Wrath.** Each auto attack that lands stores a copy of the active Seal (15 sec, 3 copies). An auto attack with a different Seal consumes the copies. Each copy gives the stored Seal its usual chance.
- **Rotation.** The wowsims rotation casts the other Seal after each swing. Thus, each auto attack gives a Seal of Righteousness hit and a Seal of Command chance.
- **Seal of Command.** 7 procs each minute. Each proc does 70% of weapon damage + 23.3% of spell damage.
- **Seal of Righteousness.** 67.5 + 12% of spell damage for each hit.
- **Judgement.** One each 8 sec: 178.2 + 42.9% of spell damage. The boss cannot dodge it.
- **Holy Strike.** One each 10 sec: 50% of (normalized weapon damage + 93 + 42.9% of spell damage). Sacred Arbiter: +20%.
- **Hammer of Wrath.** One each 6 sec in the last 20% of the fight. Instant with Champion of the Light 5/5: 498 + 42.9% of spell damage.
- **Multipliers.** Improved Seals: ×1.15 (Seals and Judgements). Two-Handed Weapon Specialization: ×1.06, Physical damage only. Conviction: +6% critical hit for all attacks and spells.
- **Vengeance.** A simulation of the stacks (3% each, 3 stacks). The average is +5.7%.
- **Fight.** 2 min. A 5 min fight gives +0.6% (Vengeance). wowsims gives +0.9%.
- **Not in the model.** Exorcism, Consecration and Retribution Aura.

## 3. Damage sources

Fresh level 60, raid buffs, 2 min fight:

| Source | Beta | Share | With C1 | Share |
| --- | --- | --- | --- | --- |
| Auto attacks | 116 | 36% | 116 | 34% |
| Seal of Command | 54 | 17% | 64 | 19% |
| Judgement | 51 | 16% | 51 | 15% |
| Holy Strike | 45 | 14% | 45 | 13% |
| Seal of Righteousness | 36 | 11% | 42 | 12% |
| Hammer of Wrath (last 20% of the fight) | 22 | 7% | 22 | 7% |
| **Total** | **324** |  | **341 (+5.3%)** |  |

- About 64% of the damage is Holy damage (66% with C1). Armor does not decrease it.
- **Holy Strike Seal trigger (C1).** Holy Strike triggers the active Seal. Thus, it gives about one extra Seal of Righteousness hit or Seal of Command chance each 10 sec.
- **Mana.** C1 does not change the mana cost: 51.2 mana each sec.

## 4. Mana and the Seal plans

The model uses 3,029 mana. The income is 6.2 mana each sec from Reverence 2/2 and 8 from Blessing of Wisdom.

| Seal plan | Damage | Mana each sec | Mana empty after |
| --- | --- | --- | --- |
| A Seal change after each swing (n = 1) | 100% | 51.2 | 1 min 21 sec |
| n = 2 | 98.2% | 35.6 | 2 min 21 sec |
| n = 3 | 97.4% | 27.8 | 3 min 43 sec |
| n = 4 | 94.5% | 23.1 | 5 min 40 sec |
| Seal of Command only | 88% | 10.2 | No limit |

- **n** is the number of swings with Seal of Righteousness before one swing with Seal of Command.
- **The best plan in the fight** costs 2% damage in a 2 min fight and 4% in a 5 min fight at fresh level 60. From Molten Core, n = 1 is possible for 2 min.
- **wowsims.** The wowsims consumables now include Major Mana Potion. With it, the mana lasts for 5 min with full and lean buffs.
- **A Seal cost decrease of 20% on Unsealed Wrath (W29)** gives +0.7% in a 2 min fight and +2.6% in a 5 min fight (model). In wowsims, it gives 0% because the mana lasts.
- **The pure average tables use no mana limit.**

## 5. Against the pure average

The pure average is the best spec of each pure damage class in MythicSim (22 October 2026): Warrior 929, Rogue 702, Hunter 1,175, Mage 860 and Warlock 879. The average is 909. Without Combat Rogue, it is 961.

- **Fresh level 60.** The beta Retribution (906) is 100% of the pure average and 98% of Fury. With C1 (954), it is 105% and 103%. Without Combat Rogue, the beta is 94% and C1 is 99%.
- **Higher tiers.** Fury and Combat Rogue use the increase of the model. The increase of Hunter, Mage and Warlock is not known. The table uses three cases: ×1.60, ×1.75 and ×1.90 in Naxxramas.

| Build | Fresh level 60 | Pre-raid | Molten Core | Blackwing Lair | Naxxramas |
| --- | --- | --- | --- | --- | --- |
| Beta, ×1.60 | 100% | 100% | 100% | 100% | 100% |
| **Beta, ×1.75** | **100%** | **98%** | **97%** | **95%** | **94%** |
| Beta, ×1.90 | 100% | 97% | 94% | 91% | 89% |
| C1, ×1.60 | 105% | 105% | 106% | 105% | 105% |
| **C1, ×1.75** | **105%** | **104%** | **102%** | **100%** | **99%** |
| C1, ×1.90 | 105% | 102% | 99% | 96% | 94% |

**C1 review (×1.75)**

| Build | Fresh level 60 | Pre-raid | Molten Core | Blackwing Lair | Naxxramas |
| --- | --- | --- | --- | --- | --- |
| Beta | 100% | 98% | 97% | 95% | 94% |
| C1 | 105% | 104% | 102% | 100% | 99% |
| C1, Sacred Arbiter +10% | 104% | 103% | 101% | 99% | 98% |
| C1, Sacred Arbiter +0% | 103% | 101% | 100% | 98% | 97% |
| Beta, spell damage on plate stays at 254 | 100% | 96% | 93% | 89% | 86% |
| C1, spell damage on plate stays at 254 | 105% | 101% | 98% | 94% | 91% |

- **The beta is now near the target.** With the wowsims update, the beta Retribution is at or above 95% until Blackwing Lair. In Naxxramas, it is 1 point below.
- **C1 is 4–10 points above the target.** At fresh level 60, Retribution with C1 is 3% above Fury.
- **Without spell damage on plate items,** the beta goes to 86% in Naxxramas. C1 keeps 91%.
- **Recommendation: keep C1.** It gives one Seal rule for all melee attacks. It also gives the tank threat (Analysis, Threat). Without it, Retribution goes below the target in Naxxramas.
- **The balance lever is Sacred Arbiter (W15).** If raid logs confirm the wowsims level, decrease Sacred Arbiter to +10%. Then C1 gives +4.1%. At +0%, C1 gives +2.9%.
- **The MythicSim values are from 22 October.** The wowsims update can also change the other classes. Check the pure average again with new MythicSim values.

## 6. Judgement of the Crusader

Judgement of the Crusader adds 161 Holy damage taken. Each hit receives 161 × its spell damage coefficient. Seal of Command receives 29%. Parts 3–5 do not include it.

| Build | Fresh level 60 | Naxxramas |
| --- | --- | --- |
| Beta | +30 (+9.3%) | +33 (+6.3%) |
| C1 | +33 (+9.5%) | +36 (+6.4%) |

- **By source (beta, fresh level 60).** Judgement +11.1, Seal of Righteousness +6.4, Seal of Command +6.0, Holy Strike +4.3 and Hammer of Wrath +2.4.
- **The +161 does not increase with gear.** Thus, its % decreases in raids.
- **Personal Judgement of the Crusader (C2).** Each Retribution Paladin keeps its own Judgement of the Crusader. Holy Strike refreshes it (Sacred Arbiter).

## 7. Increase with gear

The five gear tiers of Analysis, Threat, part 2. Each tier gives 17.5% more Strength, Agility, Attack Power, critical hit, spell damage and Intellect from gear. Retribution, Fury, Arms and Combat Rogue use the same gear and raid buffs.

| Tier | Retribution | Retribution, spell damage stays at 254 | Fury | Arms | Combat Rogue |
| --- | --- | --- | --- | --- | --- |
| Fresh level 60 | ×1.00 | ×1.00 | ×1.00 | ×1.00 | ×1.00 |
| Pre-raid best in slot | ×1.12 | ×1.09 | ×1.14 | ×1.10 | ×1.12 |
| Molten Core | ×1.27 | ×1.22 | ×1.30 | ×1.25 | ×1.25 |
| Blackwing Lair | ×1.42 | ×1.33 | ×1.50 | ×1.40 | ×1.41 |
| Naxxramas | ×1.63 | ×1.49 | ×1.73 | ×1.59 | ×1.61 |

**Retribution as a % of Fury** (start: MythicSim Fury 929)

| Tier | Beta | Beta, spell damage stays | Beta, flatter gear | C1 | C1, spell damage stays | C1, flatter gear |
| --- | --- | --- | --- | --- | --- | --- |
| Fresh level 60 | 98% | 98% | 98% | 103% | 103% | 103% |
| Pre-raid best in slot | 96% | 94% | 96% | 101% | 98% | 101% |
| Molten Core | 96% | 91% | 95% | 101% | 96% | 100% |
| Blackwing Lair | 93% | 87% | 93% | 98% | 91% | 98% |
| Naxxramas | 92% | 84% | 92% | 97% | 89% | 97% |

**Why Retribution increases less**

| Source | Increase to Naxxramas |
| --- | --- |
| Seal of Command | ×1.78 |
| Auto attacks | ×1.71 |
| Holy Strike | ×1.68 |
| Judgement | ×1.51 |
| Seal of Righteousness | ×1.44 |
| Hammer of Wrath | ×1.30 |
| **Retribution** | **×1.63** |
| Fury Warrior | ×1.73 |

- **About 23% of the damage is fixed base values.** Gear does not change them: Judgement (178.2), Seal of Righteousness (67.5 for each hit), Hammer of Wrath (498) and the 46.5 of Holy Strike.
- **About 18% comes from spell damage.** The coefficients are small (12–43%).
- **Only about 59% increases with weapon damage and Attack Power.** For Fury and Rogue, it is almost 100%.
- **Hit.** Retribution has 6% hit at fresh level 60 (cap 8%). The two-weapon classes start at 27% miss. Each point of hit helps them until Naxxramas.
- **Fury is the outlier.** In Naxxramas, the beta Retribution is 116% of Arms and 131% of Combat Rogue.

## 8. Stat values

Beta, raid buffs, 5 min fight, DPS for each point:

| Stat | DPS |
| --- | --- |
| 1 spell damage | 0.18 |
| 1 Attack Power | 0.10 |
| 1 Strength | 0.23 |
| 1 Intellect | 0.13 |
| 1% critical hit | 4.7 |
| 1% hit (up to the cap) | 4.3 |

- 1 spell damage is worth about 2 Attack Power. Plate items with spell damage are good for Retribution, and Warriors do not want them.
- **Hit cap.** The build has 6% hit (5% from gear and Precision 1/1). The cap is 8%.
- **Two-Handed Weapon Specialization 3/3** gives +6.6 DPS (+2.1%). It now increases only Physical damage.

## 9. Check with wowsims

wowsims Forever, master of 1 November, with the proposals as flags (models/wowsims-b2). The default Retribution set, rotation and consumables. Level 63 boss, 3,000 iterations.

| Case | 2 min | 5 min |
| --- | --- | --- |
| Beta, full buffs | 906 | 914 |
| C1, full buffs | 956 (+5.6%) | 962 (+5.3%) |
| Beta, lean buffs | 653 | 660 |
| C1, lean buffs | 690 (+5.6%) | 696 (+5.5%) |
| Fury Warrior, pre-raid set | 826 | 821 |
| Arms Warrior, pre-raid set | 729 | 723 |

- **C1.** wowsims gives +5.3–5.6%. The model gives +5.3%.
- **No mana problem.** No run has zero mana. The consumables include Major Mana Potion.
- **The update of 1 November.** The wowsims test suite value goes from 836 to 901 DPS. The Unsealed Wrath fix (stored Seal of Command copies ignore the Seal cooldown) gives 852. The new rotation and presets give 889. The new weapon oils give 901.
- **Against Fury in wowsims.** The beta Retribution is 110% of the wowsims Fury. The two specs use different gear sets. Thus, this tab uses the MythicSim ratio for Fury.

## 10. Options that were not kept

- **Burning Zeal (C-R4).** +0.8% at fresh level 60 to +1.3% in Naxxramas (model). It is withdrawn: with C1, Retribution is already above the target.
- **Measure for Measure (C-R5).** About +1% at all gear levels. It is withdrawn.
- **Twist of Light (C-R2).** The beta removes it. Unsealed Wrath stores up to 3 Seal copies in its place.

## 11. Limits

- The model calculates averages. It is not a full simulation.
- The pure average uses MythicSim values of 22 October. The other classes can change with the wowsims update.
- Not confirmed: the critical hit decrease against a boss and the Seal of Righteousness value at 3.6 sec.
- The Fury and Combat Rogue rotations and talents are assumptions. Arms uses the wowsims Forever rotation.
- The gear tiers are estimates with Classic steps. The Forever raid items are not known.
- Consumables, Consecration and Exorcism are not in the model.
