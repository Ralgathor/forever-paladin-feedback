# Damage

**Question.** How much damage does Retribution do on one boss, against the other damage classes?

All values are DPS on one level 63 boss. The start values come from wowsims (master of 1 November 2026). The increase with gear comes from the damage model.

"Pure average" is the average DPS of the best spec of each pure damage class (Warrior, Rogue, Hunter, Mage, Warlock) in MythicSim. The design target for a hybrid class is 95% of the pure average.

## Short answer

- **The live Retribution is near the target.** It does 906 DPS in wowsims: 100% of the pure average at fresh 60. In Naxxramas, it is 94% (model), 1 point below the target.
- **The wowsims update of 1 November** gives Retribution +7% (848 → 906): a new rotation, the Unsealed Wrath fix and new weapon oils.
- **The Holy Strike Seal trigger (C1) gives +5.3–5.6%.** With C1, Retribution is 105% of the pure average at fresh 60 and 99% in Naxxramas.
- **Keep C1.** Without it, Retribution is below the target in Naxxramas. If C1 is too strong, decrease Sacred Arbiter to +10% (W15).
- **Retribution increases less with gear than Fury:** ×1.63 against ×1.73 to Naxxramas. Fixed base values in the Paladin spells cause this. No talent change can fix it.
- **Judgement of the Crusader** adds +9.3% at fresh 60 and +6.3% in Naxxramas.

## 1. Against the pure average

MythicSim values (22 October): Warrior 929, Rogue 702, Hunter 1,175, Mage 860, Warlock 879. The pure average is 909. Without the Rogue, it is 961.

- **At fresh 60,** the live Retribution (906) is 100% of the pure average and 98% of Fury. With C1 (954), it is 105% and 103%.
- **Without the Rogue,** the live version is 94% and C1 is 99%.

The increase of Hunter, Mage and Warlock with gear is not known. The table uses ×1.75 to Naxxramas. The method part gives ×1.60 and ×1.90.

| Build | Fresh 60 | Pre-raid | Molten Core | Blackwing Lair | Naxxramas |
| --- | --- | --- | --- | --- | --- |
| **Live** | **100%** | **98%** | **97%** | **95%** | **94%** |
| **C1** | **105%** | **104%** | **102%** | **100%** | **99%** |
| C1, Sacred Arbiter +10% | 104% | 103% | 101% | 99% | 98% |
| C1, Sacred Arbiter +0% | 103% | 101% | 100% | 98% | 97% |
| Live, no more spell damage on plate after fresh 60 | 100% | 96% | 93% | 89% | 86% |
| C1, no more spell damage on plate after fresh 60 | 105% | 101% | 98% | 94% | 91% |

- **The live version reaches the target until Blackwing Lair.** In Naxxramas, it is 1 point below.
- **C1 is 4–10 points above the target.** At fresh 60, Retribution with C1 is 3% above Fury.
- **Spell damage on plate gear is important.** Without new spell damage on plate items, the live Paladin reaches only 86% in Naxxramas. C1 keeps 91%.
- **Why keep C1.** It gives one Seal rule for all melee attacks. It also gives the tank threat (see Threat). Without it, Retribution is below the target in Naxxramas.
- **The balance lever is Sacred Arbiter (W15).** If raid logs confirm the wowsims level, decrease it to +10%. C1 then gives +4.1%. At +0%, it gives +2.9%.
- **Check again later.** The MythicSim values are from 22 October. The wowsims update can also change the other classes.

## 2. Where the damage comes from

Fresh 60, raid buffs, 2 min fight (model).

| Source | Live | Share | With C1 | Share |
| --- | --- | --- | --- | --- |
| Auto attacks | 116 | 36% | 116 | 34% |
| Seal of Command | 54 | 17% | 64 | 19% |
| Judgement | 51 | 16% | 51 | 15% |
| Holy Strike | 45 | 14% | 45 | 13% |
| Seal of Righteousness | 36 | 11% | 42 | 12% |
| Hammer of Wrath (last 20% of the fight) | 22 | 7% | 22 | 7% |
| **Total** | **324** | | **341 (+5.3%)** | |

- **About 64% of the damage is Holy damage** (66% with C1). Boss armor does not decrease it.
- **C1 lets Holy Strike trigger the active Seal.** This gives about one extra Seal hit each 10 sec.
- **C1 costs no mana.**

## 3. Increase with gear

The five gear levels of Threat, part 2. Each level gives 17.5% more stats from gear. Retribution, Fury, Arms and Combat Rogue have the same gear and buffs.

| Gear level | Retribution | Retribution, no more spell damage on plate | Fury | Arms | Combat Rogue |
| --- | --- | --- | --- | --- | --- |
| Fresh 60 | ×1.00 | ×1.00 | ×1.00 | ×1.00 | ×1.00 |
| Pre-raid best | ×1.12 | ×1.09 | ×1.14 | ×1.10 | ×1.12 |
| Molten Core | ×1.27 | ×1.22 | ×1.30 | ×1.25 | ×1.25 |
| Blackwing Lair | ×1.42 | ×1.33 | ×1.50 | ×1.40 | ×1.41 |
| Naxxramas | ×1.63 | ×1.49 | ×1.73 | ×1.59 | ×1.61 |

**Retribution as a % of Fury**

| Gear level | Live | Live, no more spell damage on plate | Live, flatter gear | C1 | C1, no more spell damage on plate | C1, flatter gear |
| --- | --- | --- | --- | --- | --- | --- |
| Fresh 60 | 98% | 98% | 98% | 103% | 103% | 103% |
| Pre-raid best | 96% | 94% | 96% | 101% | 98% | 101% |
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

- **About 23% of the damage is fixed base values.** Gear does not change them. Examples: Judgement 178.2, Seal of Righteousness 67.5 for each hit, Hammer of Wrath 498.
- **About 18% comes from spell damage,** with small coefficients (12–43%).
- **Only about 59% increases with the weapon and Attack Power.** For Fury and Rogue, it is almost 100%.
- **Hit.** Retribution has 6% hit at fresh 60, near the 8% cap. The classes with two weapons start at 27% miss. Thus, each hit point helps them until Naxxramas.
- **Fury is the outlier.** In Naxxramas, the live Retribution is 116% of Arms and 131% of Combat Rogue.

## 4. Judgement of the Crusader

Judgement of the Crusader adds 161 Holy damage taken. Each hit receives 161 × its spell damage coefficient. The other parts do not include it.

| Build | Fresh 60 | Naxxramas |
| --- | --- | --- |
| Live | +30 (+9.3%) | +33 (+6.3%) |
| C1 | +33 (+9.5%) | +36 (+6.4%) |

- **The +161 does not increase with gear.** Thus, its percentage decreases in raids.
- **Personal Judgement of the Crusader (C2)** lets each Retribution Paladin keep its own Crusader.

## 5. Mana and the Seal plans

The wowsims rotation uses plan 1 + 3: 1 swing with Seal of Righteousness, then 3 swings with Seal of Command. The first swing with the new Seal releases the stored copies. The copies of Seal of Command ignore the 1 sec cooldown of the proc. The mana pool is 3,029 (fresh 60, Blessing of Wisdom).

| Seal plan | wowsims: C1, full buffs, 2 min | Model: damage | Model: mana each sec | Model: mana empty after |
| --- | --- | --- | --- | --- |
| 1 + 3 (wowsims rotation) | 956 DPS | 100% | 27.8 | 3 min 43 sec |
| 1 + 2 | −0.7% | 99.2% | 35.6 | 2 min 21 sec |
| 2 + 2 | −2.4% | 97.5% | 27.8 | 3 min 43 sec |
| 1 + 1 (a Seal change after each swing) | −3.4% | 97.5% | 51.2 | 1 min 21 sec |
| 3 + 1 | −6.4% | 94.9% | 27.8 | 3 min 43 sec |
| Seal of Command only | — | 85.7% | 10.2 | No limit |

- **Plan 1 + 3 is the best plan.** A copy of Seal of Command has more value than a copy of Seal of Righteousness.
- **At fresh 60, plan 1 + 3 lasts for a 3 min fight.** In a 5 min fight, plan 3 + 3 is the best (−2.5%). In Naxxramas, plan 1 + 3 lasts 5 min.
- **In wowsims, the mana lasts 5 min,** because the consumables include Major Mana Potion.
- **A 20% Seal cost decrease on Unsealed Wrath (W29)** gives 0% in a 2 min fight and +2.6% in a 5 min fight (model). In wowsims, it gives 0%.
- **The model tables of this tab use plan 1 + 1 and no mana limit.** Plan 1 + 1 is 2.5% below plan 1 + 3 in the model. The start value (906) comes from wowsims with plan 1 + 3.

## 6. Stat values

Live, raid buffs, 5 min fight (model).

| Stat | DPS for each point |
| --- | --- |
| 1 spell damage | 0.18 |
| 1 Attack Power | 0.10 |
| 1 Strength | 0.23 |
| 1 Intellect | 0.13 |
| 1% critical hit | 4.7 |
| 1% hit (up to the cap) | 4.3 |

- **1 spell damage is worth about 2 Attack Power.** Plate items with spell damage are good for Retribution, and Warriors do not want them.
- **Two-Handed Weapon Specialization 3/3** gives +6.6 DPS (+2.1%). It now increases only physical damage.
- For the wowsims stat weights, see builds/retribution.md.

## 7. Check with wowsims

Default Retribution gear, rotation and consumables. One level 63 boss, 3,000 iterations. "Lean buffs" is a small set of buffs.

| Case | 2 min | 5 min |
| --- | --- | --- |
| Live, full buffs | 906 | 914 |
| C1, full buffs | 956 (+5.6%) | 962 (+5.3%) |
| Live, lean buffs | 653 | 660 |
| C1, lean buffs | 690 (+5.6%) | 696 (+5.5%) |
| Fury Warrior, pre-raid gear | 826 | 821 |
| Arms Warrior, pre-raid gear | 729 | 723 |

- **C1:** +5.3–5.6% in wowsims, +5.3% in the model. They agree.
- **No run is out of mana.**
- **The wowsims update of 1 November,** step by step: 836 → 852 (Unsealed Wrath fix) → 889 (new rotation and presets) → 901 (new weapon oils), in the wowsims test suite.
- **wowsims Fury.** The live Retribution is 110% of the wowsims Fury, but the two specs have different gear. Thus, this tab compares with the MythicSim Fury.

## 8. Options that were not kept

- **Burning Zeal (C-R4).** +0.8% at fresh 60 to +1.3% in Naxxramas. Withdrawn: with C1, Retribution is already above the target.
- **Measure for Measure (C-R5).** About +1% at all gear levels. Withdrawn.
- **Twist of Light (C-R2).** The live version removes it. Unsealed Wrath takes its place.

## 9. Inputs of the model

**Build.** The wowsims default Retribution build, 14/6/31 ([`b2050250002-501-05233011201301351`](https://ralgathor.github.io/forever-paladin-feedback/calculator/#b2050250002-501-05233011201301351)).

- Holy: Divine Strength 5/5, Reverence 2/2, Improved Seals 5/5, Holy Conduit 2/2.
- Protection: Divine Intellect 5/5, Precision 1/1.
- Retribution: Benediction 5/5, Improved Judgement 2/2, Conviction 3/3, Sanctified Judgement 3/3, Unyielding Faith 1, Seal of Command, Pursuit of Justice 2, Sacred Arbiter, Two-Handed Weapon Specialization 3/3, Repentance, Vengeance 3/3, Champion of the Light 5/5, Unsealed Wrath.

**Gear.** Fresh 60 gear (crafted, dungeon and quest items). Weapon: Stormcarver, 155–233 damage, 3.6 sec, +32 spell damage. With talents and raid buffs: 1,244 Attack Power, 326 spell damage, 6% hit, 12.6% critical hit, 3,029 mana.

**Fight**

- Raid buffs: Blessing of Kings, Blessing of Might, Battle Shout, Mark of the Wild, Blessing of Wisdom. No consumables, no Judgement of the Crusader.
- Boss: level 63, 976 armor after debuffs. The Paladin attacks from behind: no parry and no block.
- 8% miss, 6.5% dodge, 40% glancing blows (−35% damage), critical hit −4.8%.
- 2 min fight. A 5 min fight gives +0.6%.

**Spells**

- Unsealed Wrath: each auto attack that lands stores a copy of the active Seal (3 copies). A swing with the other Seal releases them.
- Seal of Command: 7 procs each min, 70% of weapon damage + 23.3% of spell damage.
- Seal of Righteousness: 67.5 + 12% of spell damage for each hit.
- Judgement: one each 8 sec, 178.2 + 42.9% of spell damage.
- Holy Strike: one each 10 sec, 50% of (weapon damage + 93 + 42.9% of spell damage). Sacred Arbiter +20%.
- Hammer of Wrath: one each 6 sec in the last 20% of the fight, 498 + 42.9% of spell damage.
- Improved Seals ×1.15 (Seals and Judgements). Two-Handed Weapon Specialization ×1.06 (physical only). Conviction +6% critical hit. Vengeance: average +5.7%.
- Not in the model: Exorcism, Consecration, Retribution Aura.

**Other gear growth cases (live / C1, Naxxramas):** ×1.60 gives 100% / 105%. ×1.90 gives 89% / 94%.

## 10. Method and limits

- **Scripts.** `models/beta-30-oct/retribution_b2.py` (model) and `damage_tables_b2.py` (tables). wowsims tests in `models/wowsims-b2`. Other classes: MythicSim (22 October) and `models/damage` (Fury, Arms, Combat Rogue).
- The model calculates averages. It is not a full simulation.
- Not confirmed: the critical hit decrease against a boss, and the Seal of Righteousness value with a 3.6 sec weapon.
- The Fury and Combat Rogue rotations and talents are assumptions. Arms uses the wowsims rotation.
- The gear levels are estimates with Classic steps. The Forever raid items are not known.
