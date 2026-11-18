# Damage

**Question.** How much damage does Retribution do on one boss, against the other damage classes?

All values are DPS on one level 63 boss. The start values come from wowsims (master commit ad6b13af8 of 18 November 2026, hotfixes of 16 and 17 November). Judgement of Righteousness and Judgement of Fury are ranged attacks, as in the hotfixes of 11 November. Judgement of Command is a melee attack, as in the late hotfix of 13 November. wowsims now has these rules itself. The increase with gear comes from the damage model.

"Pure average" is the average DPS of the best spec of each pure damage class (Warrior, Rogue, Hunter, Mage, Warlock) in wowsims. Each spec uses the best set from the same pre-raid item pool (part 7). The six sets open in wowsims from the [item pool sets](https://ralgathor.github.io/forever-paladin-feedback/sets/) page. The design target for a hybrid class is 95% of the pure average. Players report this target from developer comments. No official text gives the number.

## Short answer

- **The live Retribution is at the target or above it at all gear levels.** It does 910 DPS in wowsims with the item pool set: 98% of the pure average at fresh 60. In Blackwing Lair and Naxxramas, it is 95% (model). In Naxxramas, the exact value is 94.6%.
- **Build 70755 gives Retribution +3.5% in wowsims (default set: 906 → 938).** Vengeance stacks up to 5 times, and Two-Handed Weapon Specialization also increases Holy damage. The pure classes lose 0–5% in the same update (part 7).
- **The hotfix 113578 ports of 4 November give the pure classes +5–17% in wowsims.** Fury +6%, Combat Rogue +5%, Hunter +17%. The pure average goes from 770 to 812, and Retribution from 118% to 112% (part 7).
- **wowsims master 8298ab833 (4 November, later) changes the pure classes by −3.5% to +1.4%.** Hunter −3.5% (new reaction times), Demonology Warlock +1.4% (patch of 3 November and new elixirs), Combat Rogue +0.8%, Fury +0.3%. The pure average goes from 812 to 809. Retribution stays at 112%.
- **wowsims master 9a8624af9 (4 November, evening) changes only Fury: +0.2%** (839 → 841, one Reckless Swings before the pull). The pure average stays at 809.6 (809.3 before), and Retribution at 112.2%.
- **wowsims master df57e2571 (6 November) adds 2,447 items. A new item search gives the pure average +0.9%** (809.6 → 817.1). The same commit halves the Natural flasks. Combat Rogue +5.2%, Hunter +2.0%, Demonology Warlock +0.7%, Fury −1.5%, Fire Mage −1.0%. Retribution does not change. It then had 111% of the pure average (part 7).
- **wowsims master ae9b8c23a (8 November) adds 362 pool items for a Paladin, for example Hand of Justice and Cape of the Black Baron. A new item search gives the pure average +5.4%** (817.1 → 861.1). Fire Mage +8.9%, Demonology Warlock +6.9%, Fury +4.3%, Combat Rogue +3.4%, Hunter +3.3%. Retribution +3.1% (908 → 937). It then had 109% of the pure average (part 7).
- **wowsims master 9f254e8d8 (9 November) changes the Windfury Totem rule: Retribution −9.9% (937 → 844).** Windfury now procs only from auto attacks and from main-hand or next-swing abilities. Holy Strike and Judgement of Command do not proc it. Fury loses 2.6%, and the other pure specs do not change. A new item search after 262 new items gives the pure average +1.4% (856.9 → 868.6). Retribution then had 97% of the pure average (part 7).
- **wowsims master 3633d376a (11 November) adds 464 items, 335 of them pool items for a Paladin. A new item search with all proc items that wowsims implements gives the pure average +3.4%** (868.6 → 897.8). Fury +8.7% with Ironfoe and Flurry Axe, Combat Rogue +3.4%, Fire Mage +1.9%, Hunter +1.6%, Demonology Warlock +1.5%. Retribution does not change. It then had 94% of the pure average (part 7).
- **wowsims master 52471a100 (12 November) adds 69 items. A new item search gives the pure average +0.3%** (897.8 → 900.1). Fury +0.6% with Death Grips and Highborne Research Tablet, Fire Mage +0.3%, Demonology Warlock +0.3%, Combat Rogue +0.1%, Hunter +0.0%. Retribution +0.5% (843.5 → 847.7) with Warblade of Caer Darrow, a new item in the database. It then had 94% of the pure average (part 7).
- **wowsims master 129fcd89e (12 November, evening) decreases the Hand of Justice and Ironfoe procs. A new item search gives the pure average −1.3%** (900.1 → 888.0). Fury −5.4%, Combat Rogue −1.8%, Hunter +0.6%. The Fire Mage and Demonology Warlock do not change. Retribution −1.2% (847.7 → 837.8), with Demonshear in place of Warblade of Caer Darrow. It then had 94% of the pure average, and 93% of Fury (part 7).
- **wowsims master 8c7b5a5f5 (13 November) with the judgement hotfixes: Retribution −0.6%** (837.8 → 832.6). Judgement of Righteousness and Judgement of Fury are now ranged attacks, thus they no longer trigger melee weapon procs. The late hotfix of 13 November makes Judgement of Command a melee attack again, thus it still triggers them. With all three judgements ranged, the loss was −1.5%.

  A new item search gave Fury −0.3% (Gauntlets of Heroism), and the other sets did not change. The pure average went from 888.0 to 887.4. Retribution then had 94% of the pure average, and 93% of Fury (part 7).
- **wowsims master 6084403a9 (15 November): Retribution +6.0% (832.6 → 882.6).** The Seals of Command, Fury and Righteousness now proc from the Windfury Totem strike. With lean buffs (no Windfury Totem), Retribution loses 0.4%. The Windfury Totem now also rolls on each main-hand melee ability: Fury +7.6%, Combat Rogue +1.9%. The casters do not change.

  A new item search after 98 new items gave Fury +1.2%, Combat Rogue +1.0%, Fire Mage +0.6% and Retribution +0.2%. The pure average went from 887.4 to 910.1. Retribution then had 97% of the pure average, and 91% of Fury (part 7).
- **wowsims master ad6b13af8 (18 November) changes the proc rates of many items.** With the sets of 15 November, Combat Rogue gains 10.1% (776.1 → 854.5). Retribution loses 0.2%, and the other specs change by −0.9% to +0.3%.

  A new item search gives Retribution +3.7% with Destiny: wowsims now implements its proc. Fury, Combat Rogue and Hunter gain 1.1–1.4%. The pure average goes from 910.1 to 931.4. Retribution then had 98% of the pure average, and 93% of Fury (part 7).
- **The same enchant rules for all specs (18 November evening).** No enchant from a raid, from a reputation at Revered or Exalted, or from a later phase. A search sets the enchants of each spec (part 7). The pure average goes from 931.4 to 935.0, and Retribution from 914.8 to 919.5. Retribution stays at 98% of the pure average and 93% of Fury. The test run value of Retribution goes from 905 to 910.
- **The wowsims update of 1 November** gives Retribution +7% (848 → 906): a new rotation, the Unsealed Wrath fix and new weapon oils.
- **The Holy Strike Seal trigger (C1) gives +5.2–5.7%.** With C1, Retribution has 103% of the pure average at fresh 60 and 99% in Naxxramas.
- **C1 is withdrawn (2 November 2026).** On 2 November, it put Retribution 15–20 points above the target. On 9 November, the decision was to keep C1 withdrawn after the Windfury Totem rule. The C1 rows below stay for reference.
- **Retribution increases less with gear than Fury:** ×1.65 against ×1.73 to Naxxramas. Fixed base values in the Paladin spells cause this. No talent change can fix it.
- **Judgement of the Crusader** adds +9.0% at fresh 60 and +6.0% in Naxxramas.

## 1. Against the pure average

wowsims values with the same item pool, enchants and consumables for each spec (part 7). Fury Warrior 989, Combat Rogue 866, Hunter 951, Fire Mage 927, Demonology Warlock 943. The pure average is 935. Without the Rogue, it is 952. Retribution does 920 in the same runs.

- **At fresh 60,** the live Retribution is 98% of the pure average and 93% of Fury. With C1 (withdrawn), it is 104% and 98%.
- **Without the Rogue,** the live version is 96.5%. C1 gives 102%.
- **The tables use ratios.** Retribution (910, item pool set, full buffs and consumables, 2 min) is the start value. The other classes keep their ratio to Retribution in the same item pool runs.

The increase of Hunter, Mage and Warlock with gear is not known. The table uses ×1.75 to Naxxramas. The method part gives ×1.60 and ×1.90.

| Build | Fresh 60 | Pre-raid | Molten Core | Blackwing Lair | Naxxramas |
| --- | --- | --- | --- | --- | --- |
| **Live** | **98%** | **98%** | **97%** | **95%** | **95%** |
| C1 (withdrawn) | 104% | 103% | 103% | 101% | 100% |
| C1 (withdrawn), Sacred Arbiter +10% | 103% | 102% | 101% | 100% | 99% |
| C1 (withdrawn), Sacred Arbiter +0% | 102% | 101% | 100% | 98% | 98% |
| Live, no more spell damage on plate after fresh 60 | 98% | 96% | 93% | 89% | 87% |
| C1 (withdrawn), no more spell damage on plate after fresh 60 | 104% | 101% | 98% | 95% | 92% |

- **The live version is at the target or above it at all gear levels.** It is 3 points above at fresh 60, and at the target in Blackwing Lair and Naxxramas (94.6%). Before the enchant rules of 18 November evening, it was 1 point below in Naxxramas. On 13 November, it was below the target at all gear levels (94–90%). wowsims master 6084403a9 (15 November) gave most of the change: the Seals now proc from the Windfury Totem strike. Destiny (18 November) gives the rest.
- **C1 puts Retribution above the target at all gear levels** (5–9 points). At fresh 60, Retribution with C1 is 2% below Fury.
- **Spell damage on plate gear is important.** Without new spell damage on plate items, the live Paladin has only 87% in Naxxramas.
- **Why C1 is withdrawn.** It gave one Seal rule for all melee attacks and +2.6% tank threat. On 2 November, Retribution reached the target without it. The decision of 9 November keeps C1 withdrawn. Now the live version is 2–3 points above the target up to Molten Core, and at the target in Blackwing Lair and Naxxramas (model). Righteous Fury (C25) already gives the tank the Warrior threat (see Threat).
- **Do not decrease Sacred Arbiter (W15) now.** At +10%, Retribution loses 0.8% in wowsims (910 → 903). The live version is only at the target in Naxxramas (94.6%).
- **Check again later.** The pure average uses the item pool sets of wowsims master ad6b13af8 of 18 November (part 7). The searches of 11, 12, 13, 15 and 18 November also tested all proc items that wowsims implements. The Warrior, Rogue and Hunter have the changes of hotfix 113578, and the Warlock has the patch of 3 November. The Mage changes of the development notes are not in wowsims yet (W15).

**DPS of each class.** The start values keep the ratio to Retribution of the same item pool runs (part 7), with Retribution at 910. The increase comes from the model. Hunter, Mage and Warlock use ×1.75.

| Spec | Fresh 60 | Pre-raid | Molten Core | Blackwing Lair | Naxxramas |
| --- | --- | --- | --- | --- | --- |
| Fury Warrior | 979 (106%) | 1,113 (107%) | 1,273 (106%) | 1,467 (107%) | 1,693 (106%) |
| Hunter | 941 (102%) | 1,063 (102%) | 1,241 (103%) | 1,418 (103%) | 1,647 (103%) |
| Demonology Warlock | 933 (101%) | 1,054 (101%) | 1,230 (102%) | 1,406 (102%) | 1,633 (103%) |
| **Pure average** | **925** | **1,045** | **1,205** | **1,376** | **1,591** |
| Fire Mage | 918 (99%) | 1,037 (99%) | 1,210 (100%) | 1,383 (100%) | 1,606 (101%) |
| **Retribution, live** | **910 (98%)** | **1,019 (98%)** | **1,170 (97%)** | **1,310 (95%)** | **1,505 (95%)** |
| Combat Rogue | 857 (93%) | 956 (92%) | 1,073 (89%) | 1,208 (88%) | 1,378 (87%) |

- **Retribution is fifth at all gear levels.** Only the Rogue is below it. At fresh 60, it has 93% of Fury and 98% of the Warlock. In Naxxramas, it has 89% of Fury and 92% of the Warlock.
- **The Rogue decreases the pure average.** Without the Rogue, the pure average is 943 at fresh 60.
- **The calculator Damage cards show these values.**

## 2. Where the damage comes from

Fresh 60, raid buffs, 2 min fight, wowsims rotation (plan 1 + 3, model).

| Source | Live | Share | With C1 (withdrawn) | Share |
| --- | --- | --- | --- | --- |
| Auto attacks | 115 | 35% | 116 | 33% |
| Seal of Command | 81 | 25% | 96 | 27% |
| Judgement | 51 | 15% | 51 | 15% |
| Holy Strike | 45 | 14% | 45 | 13% |
| Seal of Righteousness | 18 | 5% | 21 | 6% |
| Hammer of Wrath (last 20% of the fight) | 22 | 7% | 22 | 6% |
| **Total** | **332** | | **351 (+5.6%)** | |

- **About 65% of the damage is Holy damage** (67% with C1). Boss armor does not decrease it.
- **C1 let Holy Strike trigger the active Seal.** This gave about one extra Seal hit each 10 sec, with no mana cost.

## 3. Increase with gear

The five gear levels of Threat, part 2. Each level gives 17.5% more stats from gear. Retribution, Fury, Arms and Combat Rogue have the same gear and buffs.

| Gear level | Retribution | Retribution, no more spell damage on plate | Fury | Arms | Combat Rogue |
| --- | --- | --- | --- | --- | --- |
| Fresh 60 | ×1.00 | ×1.00 | ×1.00 | ×1.00 | ×1.00 |
| Pre-raid best | ×1.12 | ×1.10 | ×1.14 | ×1.10 | ×1.12 |
| Molten Core | ×1.29 | ×1.23 | ×1.30 | ×1.25 | ×1.25 |
| Blackwing Lair | ×1.44 | ×1.35 | ×1.50 | ×1.40 | ×1.41 |
| Naxxramas | ×1.65 | ×1.53 | ×1.73 | ×1.59 | ×1.61 |

**Retribution as a % of Fury**

| Gear level | Live | Live, no more spell damage on plate | Live, flatter gear | C1 (withdrawn) | C1 (withdrawn), no more spell damage on plate | C1 (withdrawn), flatter gear |
| --- | --- | --- | --- | --- | --- | --- |
| Fresh 60 | 93% | 93% | 93% | 98% | 98% | 98% |
| Pre-raid best | 92% | 90% | 92% | 97% | 95% | 97% |
| Molten Core | 92% | 88% | 92% | 97% | 93% | 97% |
| Blackwing Lair | 89% | 84% | 90% | 94% | 89% | 95% |
| Naxxramas | 89% | 82% | 89% | 94% | 87% | 94% |

**Why Retribution increases less**

| Source | Increase to Naxxramas |
| --- | --- |
| Seal of Command | ×1.79 |
| Auto attacks | ×1.71 |
| Holy Strike | ×1.68 |
| Judgement | ×1.51 |
| Seal of Righteousness | ×1.44 |
| Hammer of Wrath | ×1.30 |
| **Retribution** | **×1.65** |
| Fury Warrior | ×1.73 |

- **About 19% of the damage is fixed base values.** Gear does not change them. Examples: Judgement 178.2, Seal of Righteousness 67.5 for each hit, Hammer of Wrath 498.
- **About 17% comes from spell damage,** with small coefficients (12–43%).
- **Only about 65% increases with the weapon and Attack Power.** For Fury and Rogue, it is almost 100%.
- **Hit.** Retribution has 6% hit at fresh 60, near the 8% cap. The classes with two weapons start at 27% miss. Thus, each hit point helps them until Naxxramas.
- **Fury is the outlier.** In Naxxramas, the live Retribution is 117% of Arms (same gear, model) and 109% of Combat Rogue.

## 4. Judgement of the Crusader

Judgement of the Crusader adds 161 Holy damage taken. Each hit receives 161 × its spell damage coefficient. The other parts do not include it.

| Build | Fresh 60 | Naxxramas |
| --- | --- | --- |
| Live | +30 (+9.0%) | +33 (+6.0%) |
| C1 (withdrawn) | +32 (+9.2%) | +35 (+6.1%) |

- **The +161 does not increase with gear.** Thus, its percentage decreases in raids.
- **Personal Judgement of the Crusader (C2)** lets each Retribution Paladin keep its own Crusader.

## 5. Mana and the Seal plans

The wowsims rotation uses plan 1 + 3: 1 swing with Seal of Righteousness, then 3 swings with Seal of Command. The first swing with the new Seal releases the stored copies. The copies of Seal of Command ignore the 1 sec cooldown of the proc. The mana pool is 3,029 (fresh 60, Blessing of Wisdom).

| Seal plan | wowsims: live, full buffs, 2 min | Model: damage | Model: mana each sec | Model: mana empty after |
| --- | --- | --- | --- | --- |
| 1 + 3 (wowsims rotation) | 910 DPS | 100% | 27.8 | 3 min 43 sec |
| 1 + 2 | −0.6% | 99.2% | 35.6 | 2 min 21 sec |
| 2 + 2 | −1.9% | 97.5% | 27.8 | 3 min 43 sec |
| 1 + 1 (a Seal change after each swing) | −3.0% | 97.5% | 51.2 | 1 min 21 sec |
| 3 + 1 | −5.3% | 94.9% | 27.8 | 3 min 43 sec |
| Seal of Command only | — | 85.7% | 10.2 | No limit |

- **Plan 1 + 3 is the best plan.** A copy of Seal of Command has more value than a copy of Seal of Righteousness.
- **At fresh 60, plan 1 + 3 lasts for a 3 min fight.** In a 5 min fight, plan 3 + 3 is the best (−2.5%). In Naxxramas, plan 1 + 3 lasts 5 min.
- **In wowsims, the mana lasts 5 min,** because the consumables include Major Mana Potion.
- **A 20% Seal cost decrease on Unsealed Wrath (W29)** gives 0% in a 2 min fight and +2.6% in a 5 min fight (model). In wowsims, it gives 0%.
- **The model tables of this tab use plan 1 + 3 and no mana limit.** The start value (910) comes from wowsims with the same plan.

## 6. Stat values

Live, raid buffs, 5 min fight (model).

| Stat | DPS for each point |
| --- | --- |
| 1 spell damage | 0.17 |
| 1 Attack Power | 0.11 |
| 1 Strength | 0.26 |
| 1 Intellect | 0.12 |
| 1% critical hit | 4.9 |
| 1% hit (up to the cap) | 4.7 |

- **1 spell damage is worth about 1.5 Attack Power.** Plate items with spell damage are good for Retribution, and Warriors do not want them.
- **Two-Handed Weapon Specialization 3/3** gives +6.5 DPS (+2.0%) in the model, on physical damage only. Build 70755 also gives it Holy damage (part 7).
- For the wowsims stat weights, see builds/retribution.md.

## 7. Check with wowsims

Item pool Retribution set (part 7) with the enchants of 18 November evening (part 7), and the default rotation and consumables. Fury and Arms: the wowsims pre-raid sets. One level 63 boss, 3,000 iterations. "Lean buffs" is a small set of buffs.

| Case | 2 min | 5 min |
| --- | --- | --- |
| Live, full buffs | 910 | 925 |
| C1 (withdrawn), full buffs | 958 (+5.2%) | 974 (+5.3%) |
| Live, lean buffs | 692 | 705 |
| C1 (withdrawn), lean buffs | 732 (+5.7%) | 744 (+5.5%) |
| Fury Warrior, pre-raid gear | 925 | 908 |
| Arms Warrior, pre-raid gear | 841 | 828 |

- **C1 (withdrawn):** +5.2–5.7% in wowsims, +5.6–5.7% in the model. On commit 6084403a9, it gave +5.2–5.6%. On commit 8c7b5a5f5, it gave +4.9–5.6%. With all three judgements ranged, it gave +4.8–5.5%. On commit 129fcd89e, it gave +4.7–5.7%. With Warblade of Caer Darrow (commit 52471a100), it gave +3.8–4.8%.
- **Almost no run is out of mana.** Only the 5 min runs with lean buffs have no mana, for less than 2 sec.
- **Master commit 9f254e8d8 (9 November).** The Windfury Totem rule gives Retribution −10% with full buffs (939 → 841). The lean buffs have no Windfury Totem, thus they do not change. In the wowsims pre-raid sets, Fury has 804 and Arms 779 (865 and 826 on commit 8298ab833).
- **Master commit 3633d376a (11 November).** The Paladin values do not change. In the wowsims pre-raid sets, Fury does not change (804) and Arms has +0.1% (780).
- **Master commit 52471a100 (12 November).** With the set of 11 November, the Paladin values do not change. The new set gives the live Retribution +0.8% (841 → 848). In the wowsims pre-raid sets, Fury has +0.2% (806), because the Whirlwind off-hand strike now starts Flurry. Arms does not change (780).
- **Master commit 129fcd89e (12 November, evening).** Hand of Justice and Ironfoe proc less. With the set of 12 November, the live Retribution loses 2.1% (848 → 831). The new set with Demonshear gives back +0.9% (838). wowsims also gives new Fury and Arms pre-raid sets with the new dungeon items: Fury +4.3% (806 → 840) and Arms +4.2% (780 → 813).
- **Master commit 8c7b5a5f5 (13 November) with the judgement hotfixes.** The Retribution set does not change. The live Retribution loses 0.9% (838 → 831). Judgement of Righteousness and Judgement of Fury are ranged (hotfixes of 11 November), and Judgement of Command is melee again (late hotfix of 13 November). With all three judgements melee, the value is 835.

  With all three ranged, it was 825. The Two-Handed Weapon Specialization fix gives the rest. In the wowsims pre-raid sets, Fury has +0.4% (840 → 844) and Arms +0.4% (813 → 816).
- **Master commit 6084403a9 (15 November).** With the set of 13 November, the live Retribution gains 6.1% with full buffs (831 → 882). The Seals of Command, Fury and Righteousness now proc from the Windfury Totem strike. With lean buffs (no Windfury Totem), it loses 0.4% (680 → 677). wowsims now makes Judgement of Righteousness and Judgement of Fury ranged attacks itself, thus `judgement-ranged.patch` is no longer necessary.

  The new set (Counterattack Lodestone in place of Hand of Justice) gives the same value in this run (882). In the wowsims pre-raid sets, Fury has +10.8% (844 → 935) and Arms +2.8% (816 → 839). The Windfury Totem now rolls on each main-hand melee ability.
- **Master commit ad6b13af8 (18 November).** The commit changes the proc rates of many items. With the set of 15 November, the live Retribution loses 0.2% (part 7). The new set with Destiny gives +2.7% in the test run (882 → 905), and +1.9% with lean buffs (677 → 690). In the wowsims pre-raid sets, Fury has −1.1% (935 → 925) and Arms +0.2% (839 → 841).
- **The wowsims update of 1 November,** step by step: 836 → 852 (Unsealed Wrath fix) → 889 (new rotation and presets) → 901 (new weapon oils), in the wowsims test suite.
- **Build 70755 (master commit d97252f2a, 3 November).** With the default set, the live Retribution increases from 906 to 938 (+3.5%). The two test flags on master of 1 November gave 981 (+8.3%), thus the game data gives less. wowsims now also uses the trainer ranks of Strength of Earth Totem and Grace of Air Totem in the raid buffs. With the Ruins of Ahn'Qiraj book ranks, Retribution has 949 (item pool set: 920).
- **Master commit 6ee3c30f35 (4 November).** The Paladin values do not change. The hotfix 113578 ports give Fury +7% in the wowsims pre-raid set (807 → 865) and Arms +5% (773 → 814).
- **Master commit 8298ab833 (4 November, later).** The Paladin values do not change. Fury stays at 865 in the wowsims pre-raid set, and Arms goes to 826 (+1.5%).
- **wowsims Fury.** Against the wowsims Fury pre-raid set, the item pool Retribution is 98% of Fury (6084403a9: 94%; 8c7b5a5f5: 98%; 129fcd89e: 100%; 52471a100: 105%). But the two sets have different quality. With the same item pool, enchants and consumables, it is 93% of Fury (see below).

**Same item pool for each spec (searches on 2, 6, 8, 9, 11, 12, 13, 15 and 18 November 2026, two on 12 November).** This run gives the pure average of parts 1 and 3. All specs take their items from one pre-raid pool. The first search ran in wowsims of 1 November. On 4 November, the same sets ran again on master commits 6ee3c30f35, 8298ab833 and 9a8624af9. On 6 November, master commit df57e2571 adds 2,447 items.

241 of them obey the pool rules for a Paladin and have item level 45 or higher. The search ran again on this commit for all six specs, from the sets of 4 November, with the same rules and steps. On 8 November, master commit ae9b8c23a adds the items of the hotfixes of 7 and 8 November. 362 of them obey the pool rules for a Paladin, for example Hand of Justice, Blackhand's Breadth and Cape of the Black Baron. The search ran again for all six specs, from the sets of 6 November.

On 9 November, master commit 9f254e8d8 adds 262 items and changes the Windfury Totem rule. The search ran again for all six specs, from the sets of 8 November. On 11 November, master commit 3633d376a adds 464 items. 335 of them obey the pool rules for a Paladin, for example Ironfoe, Dal'Rend's Sacred Charge and Blackhand Doomsaw. The search ran again for all six specs, from the sets of 9 November. On 12 November, master commit 52471a100 adds 69 items, and the search ran again from the sets of 11 November.

Later on 12 November, master commit 129fcd89e decreases the Hand of Justice and Ironfoe procs and adds Blackhand's Breadth. The search ran again from the sets of 12 November. On 13 November, master commit 8c7b5a5f5 adds 46 items, for example Gauntlets of Heroism, and the judgements become ranged attacks. The search ran again from the sets of 12 November, evening. On 15 November, master commit 6084403a9 adds 98 items, for example Sorcerer's Crown and Darkmantle Footpads. The Seals and the Windfury Totem also proc from more attacks. The search ran again from the sets of 13 November. On 18 November, master commit ad6b13af8 changes the proc rates of many items, and wowsims implements more item effects, for example Destiny. The search ran again from the sets of 15 November. The values below come from commit ad6b13af8.

- **Item pool.** Uncommon, rare and epic items of item level 63 or lower, for level 60 or lower. Only content of the game start and Dire Maul: no Classic items of patch 1.6 or later (item ids 19000–23999). Thus, no Zul'Gurub, Ahn'Qiraj or Naxxramas era items, no dungeon set 2 and no battleground rewards. No raid drops, no world boss drops and no PvP items. No items that need Revered or Exalted reputation. Items with random enchantments are not in the pool. Each spec keeps its armor and weapon types, and its weapon setup (two-handed weapon, two weapons, or weapon and off-hand item).
- **Search.** The start is the wowsims test set, without the items outside the pool. For each slot, the search tests the best items for the stat values of the spec, and all items with an effect. Since 11 November, the candidates also include all items of the slot with an effect that wowsims implements. There are 368 such items on commit ad6b13af8, for example Ironfoe, Flurry Axe and Destiny. It keeps the best item, and repeats until no slot changes.
- **Same conditions for all.** The full wowsims test raid buffs and debuffs, the same for all specs: melee and caster buffs, totems, auras, and all debuffs with Judgement of the Crusader. Level 63 boss, 2 min, 10,000 iterations. The class weapon items stay (oils, stones, poisons). With the buffs and debuffs of the own wowsims preset of each spec, all six values stay the same.
- **Enchants (18 November evening).** The same rules for all specs, as for the tanks (Analysis, Threat, part 6). An enchant must have a source in the game data. No raid source, no Revered or Exalted reputation source, phase 1 only. A search sets the enchant of each slot, one slot at a time, 1,000 iterations each. A new enchant must give more than 0.2% DPS. The search starts from the wowsims preset enchants and removes the enchants that break the rules (`search_enchants_dps.py`, `enchants_fair.json`). Mage and Warlock start from the Balance Druid caster enchants.

  Before, the presets were not equal. Retribution had Healing Power (Argent Dawn, Exalted) on the wrists. The Rogue had the off-hand Agility enchant of Timbermaw Hold (Revered). The Hunter had no head enchant and a Zul'Gurub scope. Mage and Warlock had the Molten Core weapon enchant. Now Retribution and Fury have Superior Strength on the wrists and +15 Strength on the gloves. The Rogue has Greater Stats, Greater Agility boots and Crusader on the off hand. The Hunter has Lesser Arcane Amalgamation on the head and legs, Greater Agility gloves, Revelation and a phase 1 scope. Mage and Warlock have Revelation and armor kits on the gloves.
- **Consumables.** Each spec keeps its wowsims flask, food and potions. All specs use the same elixirs and extra items: all of those in the six presets. The Hunter preset has no flask, thus the Hunter uses the Fury flask. Fury, Rogue and Hunter use Flask of Natural Aggression. Commit df57e2571 halves this flask. The Fire Mage keeps its own elixirs, because the full list stops the sim. Physical elixirs do not help a caster: the Warlock changes by 0.2%.

| Spec | No enchants, no consumables | Enchants | Consumables | Enchants and consumables | Average item level | Epic items | Set |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Fury Warrior | 751 | 838 | 895 | 989 | 60.8 | 7 | [Fury Warrior set](https://ralgathor.github.io/forever-paladin-feedback/sets/fury-warrior.html) |
| Hunter | 778 | 847 | 881 | 951 | 60.6 | 3 | [Hunter set](https://ralgathor.github.io/forever-paladin-feedback/sets/hunter.html) |
| Demonology Warlock | 667 | 719 | 884 | 943 | 59.9 | 4 | [Demonology Warlock set](https://ralgathor.github.io/forever-paladin-feedback/sets/demonology-warlock.html) |
| Fire Mage | 681 | 734 | 871 | 927 | 60.2 | 5 | [Fire Mage set](https://ralgathor.github.io/forever-paladin-feedback/sets/fire-mage.html) |
| Combat Rogue | 710 | 754 | 818 | 866 | 59.6 | 6 | [Combat Rogue set](https://ralgathor.github.io/forever-paladin-feedback/sets/combat-rogue.html) |
| **Pure average** | **717** | **778** | **870** | **935** | | | |
| **Retribution, live** | **682 (95%)** | **735 (94%)** | **862 (99%)** | **920 (98%)** | **60.6** | **6** | [Retribution set](https://ralgathor.github.io/forever-paladin-feedback/sets/retribution.html) |
| Retribution, % of Fury | 91% | 88% | 96% | 93% | | | |

- **Set links.** Each link opens the final set of the spec in wowsims, with enchants, consumables, raid buffs and the fight. Select Simulate to run it. A later wowsims version can give a different DPS. All six links: [item pool sets](https://ralgathor.github.io/forever-paladin-feedback/sets/).
- **Enchant rules (18 November evening).** Against the wowsims preset enchants (both columns): Hunter +0.9% (942.7 → 950.8), Fury +0.8% (980.8 → 988.9), Retribution +0.5% (914.8 → 919.5), Combat Rogue +0.2% (863.6 → 865.5), Fire Mage +0.2% (925.8 → 927.3), Demonology Warlock −0.1% (944.0 → 942.7). The pure average goes from 931.4 to 935.0, and Retribution from 98.2% to 98.3%. Retribution against Fury goes from 93.3% to 93.0%. The values with the preset enchants: `ec_results_ad6b13af8_preset_enchants.json`.
- **Master commit ad6b13af8 (18 November) and the new search.** Against commit 6084403a9 (both columns): Combat Rogue +11.3% (776.1 → 863.6), Retribution +3.5% (884.0 → 914.8), Hunter +1.1% (932.2 → 942.7) and Fury +0.4% (976.6 → 980.8). The Fire Mage (+0.3%) and the Demonology Warlock (+0.1%) almost do not change. The pure average goes from 910.1 to 931.4, and Retribution from 97.1% to 98.2%.
- **Two causes (18 November).** With the sets of 15 November on commit ad6b13af8, Combat Rogue gains 10.1% (776.1 → 854.5), and Fury loses 0.9%. Retribution loses 0.2%, and the other specs change by less than 0.3%. The commit changes the proc rates of many items. The cause of the Rogue gain is not known. The pure average is then 924.8, and Retribution 95.4%. The new sets give the rest: Retribution +3.7%, Fury +1.4%, Hunter +1.2%, Combat Rogue +1.1%.
- **New items in the sets (18 November).** Retribution: Destiny in place of Demonshear, and Soulforge Warboots in place of Hippogryph Hide Boots. wowsims now implements the Destiny proc. Fury: Ironfoe and Bashguuder in place of Sword of Zeal and Flurry Axe. Combat Rogue: two Felstriker in place of Ironfoe and Talon of Tor'Rel. Hunter: The Blackrock Slicer in place of Arcanite Reaper. The Fire Mage and Demonology Warlock sets do not change. The sets of 15 November are in `sets_6084403a9/`.
- **Master commit 6084403a9 (15 November) and the new search.** Against commit 8c7b5a5f5 (both columns): Fury +8.8% (897.2 → 976.6), Retribution +6.2% (832.6 → 884.0) and Combat Rogue +2.9% (754.1 → 776.1). Hunter +0.8% (925.2 → 932.2) and Fire Mage +0.6% (917.8 → 923.1). The Demonology Warlock does not change. The pure average goes from 887.4 to 910.1, and Retribution from 93.8% to 97.1%.
- **Two causes (15 November).** With the sets of 13 November on commit 6084403a9, Fury gains 7.6%, Retribution 6.0% and Combat Rogue 1.9%. The Seals now proc from the Windfury Totem strike, and the Windfury Totem rolls on each main-hand melee ability. The pure average is then 905.3, and Retribution 97.5%. The new sets give the rest: Fury +1.2%, Combat Rogue +1.0%, Fire Mage +0.6%, Retribution +0.2%.
- **New items in the sets (15 November).** Retribution: Counterattack Lodestone in place of Hand of Justice. Fury: Battleboots of Heroism, Blackhand's Breadth, Counterattack Lodestone and Sword of Zeal, in place of Windreaver Greaves, Hand of Justice, Highborne Research Tablet and Ironfoe. Combat Rogue: Darkmantle Footpads (new in the database) and Counterattack Lodestone. Fire Mage: Sorcerer's Crown and Sorcerer's Sandals (new in the database). The Hunter and Demonology Warlock sets do not change. The sets of 13 November are in `sets_8c7b5a5f5/`.
- **Master commit 8c7b5a5f5 (13 November) and the new search.** Against commit 129fcd89e (both columns): Retribution −0.6% (837.8 → 832.6), Fury −0.3% (900.3 → 897.2). The other specs do not change. The pure average goes from 888.0 to 887.4, and Retribution from 94.3% to 93.8%. With all three judgements ranged, Retribution had 825.2 (93.0%).
- **Ranged judgements (hotfixes of 11 November, late hotfix of 13 November).** The hotfixes of 11 November make the Paladin judgements ranged attacks. Thus, they no longer trigger melee weapon procs. The late hotfix of 13 November makes Judgement of Command a melee attack again. Judgement of Righteousness and Judgement of Fury stay ranged.

  wowsims master 8c7b5a5f5 did not have these changes, thus this repository added them (`models/wowsims-b2/patches/judgement-ranged.patch`). With the sets of 12 November, evening on commit 8c7b5a5f5, only Retribution changes: −0.6% in the test run (835.3 → 830.6, 2 min, full buffs). With all three judgements ranged, it was −1.2%.
- **New items in the sets (13 November).** Fury: Gauntlets of Heroism (new in the database) in place of Death Grips. Without enchants and consumables, the new set gives +0.5%. With both, it gives −0.3%. The rules keep the result of the search. The other five sets do not change. The sets of 12 November, evening are in `sets_129fcd89e/`.
- **Master commit 129fcd89e (12 November, evening) and the new search.** Against commit 52471a100 (both columns): Fury −5.4% (951.7 → 900.3), Combat Rogue −1.8% (768.0 → 754.1), Retribution −1.2% (847.7 → 837.8). Hunter +0.6% (920.1 → 925.2). The Fire Mage and Demonology Warlock do not change. The pure average goes from 900.1 to 888.0, and Retribution from 94.2% to 94.3%.
- **The Hand of Justice and Ironfoe change (12 November, evening).** Hand of Justice has its full proc chance (3%) only against Dwarves, and 1% against other targets. Ironfoe has 6% against Orcs and 3% against other targets. With the sets of 12 November on commit 129fcd89e, Fury loses 5.8%, Combat Rogue 4.1% and Retribution 1.8%. The pure average is then 882.7, and Retribution 94.3%.
- **New items in the sets (12 November, evening).** Fury: Cloudkeeper Legplates. Combat Rogue: Devilsaur Leggings and Blackhand's Breadth (new in the database). With Devilsaur Gauntlets, the Rogue now has the 2-piece bonus of Devilsaur Armor (+2% hit): wowsims now gives the bonuses of 113 item sets. Hunter: Blackhand's Breadth.

  Retribution: Demonshear in place of Warblade of Caer Darrow. The Fire Mage and Demonology Warlock sets do not change. The sets of 12 November are in `sets_52471a100/`.
- **Master commit 52471a100 (12 November) and the new search.** Against commit 3633d376a (both columns): Fury +0.6% (946.2 → 951.7), Retribution +0.5% (843.5 → 847.7), Fire Mage +0.3% (915.5 → 917.8), Demonology Warlock +0.3% (940.3 → 942.7). Combat Rogue +0.1% (767.0 → 768.0), Hunter +0.0% (919.8 → 920.1). The pure average goes from 897.8 to 900.1, and Retribution from 94.0% to 94.2%.
- **The commit alone changes little (12 November).** With the sets of 11 November on commit 52471a100, the pure average is 898.5, and Retribution 93.9%. Fury has +0.1% (Whirlwind off-hand strike and Flurry). The Fire Mage has +0.3% (new spell resistance rule).
- **New items in the sets (12 November).** Fury: Death Grips and Highborne Research Tablet. Combat Rogue and Hunter: Highborne Research Tablet. Demonology Warlock: Eye of Orgrimmar. Retribution: Battleborn Armbraces, Highborne Research Tablet and Warblade of Caer Darrow (new in the database). The Fire Mage set does not change. The sets of 11 November are in `sets_3633d376a/`.
- **Master commit 3633d376a (11 November) and the new search.** Against commit 9f254e8d8 (both columns): Fury +8.7% (870.7 → 946.2), Combat Rogue +3.4% (742.1 → 767.0), Fire Mage +1.9% (898.7 → 915.5). Hunter +1.6% (905.4 → 919.8), Demonology Warlock +1.5% (926.0 → 940.3). Retribution does not change (843.5). The pure average goes from 868.6 to 897.8, and Retribution from 97.1% to 94.0%.
- **Only the new sets cause the change (11 November).** With the sets of 9 November on commit 3633d376a, no spec changes by more than 0.1%. The pure average is then 868.7, and Retribution 97.1%.
- **Proc items (11 November).** The search before 11 November took only the items with an effect and good stat values. A proc weapon has low stat values, thus the search did not test some of them. Now the search tests all 266 items with an effect that wowsims implements. Items with an effect that wowsims does not implement are not candidates, for example Destiny before 18 November.
- **New items in the sets (11 November).** Fury: Ironfoe in the main hand and Flurry Axe in the off hand (+6.2% in the search, without enchants and consumables). Also Mark of Fordring, Truestrike Shoulders, Battleborn Armbraces and Windreaver Greaves. Combat Rogue: Mark of Fordring, Ironfoe and Talon of Tor'Rel. Hunter: Mark of Fordring, Truestrike Shoulders and Windreaver Greaves. Fire Mage: Eye of Flame, Burial Shawl, Sublime Wristguards, Omnicast Boots and Witchblade.

  Demonology Warlock: Eye of Flame, Royal Seal of Eldre'Thalas, Witchblade and Bonecreeper Stylus. All these items are new in the database, except Flurry Axe and Talon of Tor'Rel. The search tested 28 two-handed weapons for Retribution, all proc weapons that wowsims implements among them. The Retribution set does not change. The sets of 9 November are in `sets_9f254e8d8/`.
- **Master commit 9f254e8d8 (9 November) and the new search.** Against commit ae9b8c23a (both columns): Retribution −9.9% (936.6 → 843.5). Combat Rogue +1.6% (730.4 → 742.1), Fire Mage +1.2% (888.2 → 898.7), Fury +0.8% (863.8 → 870.7), Demonology Warlock +0.5% (921.6 → 926.0), Hunter +0.4% (901.6 → 905.4). The pure average goes from 861.1 to 868.6, and Retribution from 108.8% to 97.1%.
- **Two causes (9 November).** With the sets of 8 November on commit 9f254e8d8, the Windfury Totem rule gives Retribution −9.9% and Fury −2.6%. The other specs do not change. The pure average is then 856.9, and Retribution 98.4%. The new items give the rest: Fury +3.5%, Combat Rogue +1.4%, Fire Mage +1.2%.
- **Windfury Totem (9 November).** Windfury now procs only from auto attacks and from main-hand or next-swing abilities. In the Forever logs, Holy Strike (0 of 78) and Judgement of Command (0 of 105) never proc it. In the Retribution test raid, Windfury gave +22% damage before this commit and +10% now.
- **New items in the sets (9 November).** Fury: Bloodmail Boots, Sword of Zeal and Satyr's Bow. Combat Rogue: Imperial Jewel, Flamebreak Talisman and Sword of Zeal. Hunter: Star of Mystaria, Bloodmail Boots, Flamebreak Talisman and Deep Jungle Rifle. Fire Mage: Star of Mystaria and Skyshroud Leggings. Demonology Warlock: Star of Mystaria and Mind Carver. All these items are new in the database. The Retribution set does not change. The sets of 8 November are in `sets_ae9b8c23a/`.
- **Master commit ae9b8c23a (8 November) and the new search.** Against commit df57e2571 (both columns): Fire Mage +8.9% (815.6 → 888.2), Demonology Warlock +6.9% (862.5 → 921.6), Fury +4.3% (828.5 → 863.8), Combat Rogue +3.4% (706.2 → 730.4), Hunter +3.3% (872.7 → 901.6). Retribution +3.1% (908.3 → 936.6). The pure average goes from 817.1 to 861.1, and Retribution from 111.2% to 108.8%.
- **Two causes (8 November).** With the sets of 6 November on commit ae9b8c23a, only the Hunter changes: +1.8% (872.7 → 888.5). Attack Power on gear now also gives ranged Attack Power. The pure average is then 820.4, and Retribution 110.7%. The new items give the rest.
- **New items in the sets (8 November).** Hand of Justice and Cape of the Black Baron: Fury, Combat Rogue, Hunter and Retribution. Fury also takes Sentimental Locket, Warpwood Bracers, Magni's Will and Mirah's Song. Combat Rogue: Blackstone Ring and Precisely Calibrated Boomstick. Hunter: Hermit's Pauldron and Tarnished Elven Ring. Fire Mage and Demonology Warlock: Crimson Felt Hat, Songstone of Ironforge, Maiden's Circle, Eye of the Beast, Second Wind, Arbiter's Blade and Lord Sakrasis' Scepter. The Fire Mage also takes Rotgrip Mantle and Magister's Leggings. Hermit's Pauldron and Magister's Leggings were in the pool before. All other items are new in the database. The sets of 6 November are in `sets_df57e2571/`.
- **Master commit df57e2571 (6 November) and the new search.** Against commit 9a8624af9 (both columns): Combat Rogue +5.2% (671.6 → 706.2), Hunter +2.0% (855.6 → 872.7), Demonology Warlock +0.7% (856.3 → 862.5), Fury −1.5% (840.7 → 828.5), Fire Mage −1.0% (823.9 → 815.6). The Retribution set does not change: 908.3. The pure average goes from 809.6 to 817.1, and Retribution from 112.2% to 111.2%.
- **Two causes (6 November).** With the sets of 4 November on commit df57e2571, the flask change alone gives Fury −1.9%, Hunter −1.9% and Rogue −1.2%. The pure average is then 801.7, and Retribution 113.3%. The new sets give +1.9% to the pure average.
- **New items in the sets (6 November).** Fury: Timbermaw Tunic, Deepfury Bracers (new), Bagh Nakh, Skypierce Javelin (new). Combat Rogue: Bagh Nakh in the main hand. Hunter: Flawless Arcanite Rifle. Fire Mage: Lapidis Tankard of Tidesippe (new) and Red Mageweave Headband. Demonology Warlock: Lapidis Tankard of Tidesippe. Bagh Nakh, Flawless Arcanite Rifle, Timbermaw Tunic and Red Mageweave Headband were in the pool before. The first search stopped at a local best set.
- **Fire Mage (6 November).** The search runs without enchants and consumables. There, Lapidis Tankard of Tidesippe was better (+0.6%). With both, the Fire Mage lost 1.0%. The rules keep the result of the search.
- **Master commit 8298ab833 (later on 4 November) changes the pure classes again.** Against commit 6ee3c30f35 (both columns): Hunter −3.5% (new reaction times), Demonology Warlock +1.4% (patch of 3 November and the elixirs of its new preset), Combat Rogue +0.8%, Fury +0.3%, Mage 0%. Retribution +0.2% (the new elixirs). On commit 6ee3c30f35, the pure average was 812 and Retribution 906 (112%).
- **Master commit 9a8624af9 (evening of 4 November).** Fury +0.2% (839.2 → 840.7): Fury casts one Reckless Swings before the pull. The other specs and Retribution do not change. The pure average was 809.6, and Retribution 112.2% (108.0% of Fury).
- **The hotfix 113578 ports of 4 November change the pure classes.** Against the run of 3 November (both columns): Fury +6.2%, Combat Rogue +5.0%, Hunter +16.5%, Mage and Warlock 0%. Retribution 0%. On 3 November, the pure average was 770 and Retribution 906 (118%).
- **Build 70755 changed the pure classes too (3 November).** Against the run of 1 November (both columns): Fury −2.1%, Hunter −4.8%, Combat Rogue −1.7%, Mage and Warlock 0%. Retribution +3.7%. wowsims now uses the trainer ranks of the totems and of the Hunter spells, not the Ruins of Ahn'Qiraj book ranks. On 1 November, the pure average was 784 and Retribution 874 (112%).
- **Parts 1 and 3 use the last column.** The start value of the model (910, the same set with the Retribution test buffs) has full buffs and consumables. Thus, the other classes need the same.
- **Enchants decrease the Retribution ratio by 1 point.** The physical enchants help Fury most.
- **Consumables increase the Retribution ratio by 4 points.** Retribution uses physical elixirs and spell elixirs. A pure class uses only one of the two groups.
- **The two together give +3 points:** 98% of the pure average, and 93% of Fury.
- **The wowsims presets are not the same for each class.** With each preset as it is, Retribution had 116% on 1 November (9 elixirs). The Rogue preset has no elixir. Thus, this run gives the same elixirs to all specs.
- **The Rogue is low in this sim.** Without the Rogue, the pure average is 952, and Retribution is 96.5%. On 1 November, the six wowsims Rogue talent presets gave 315–657 DPS on the same set. The best one (Combat Backstab) gave only +2%. With a Rogue at the Fury level, Retribution is 96%.

  The wowsims Rogue is not complete. Issue 13 has the stat values and the gear effects open. Issue 28 has 40 of 100 items open, among them Coup de Grace and Occult Poison. A rerun is due when issue 13 closes.
- **Fight length (1 November).** At 3 min, Retribution was 114% of the pure average. At 5 min, it was 115%. The casters and the Rogue lose DPS in longer fights, and Retribution gains a little.
- **The later items helped the pure classes more.** With the first pool (ZG, AQ, battleground and dungeon set 2 items), Retribution had 108% and Fury 102%. Retribution keeps Forever items (Vindicator's Belt, Timbermaw Tunic) and Arcanite Reaper.
- **Limits.** Many Forever items have no source in the game data. They stay in the pool. The same rule applies to all specs. The search can stop at a local best set.
- **Files.** `models/wowsims-b2/matched_gear/` (search scripts, sets and logs).

**All damage specs with the wowsims test sets (2 November 2026).** Each spec uses its wowsims test character with pre-raid gear: dungeon, quest, craft and early reputation items. No raid or PvP items. The same raid buffs for all, no consumables (poisons and weapon stones from the class stay). 2 min, 3,000 iterations. The pure average is the best spec of each pure class: 600 DPS.

| Spec | DPS | % of the pure average |
| --- | --- | --- |
| Fury Warrior | 703 | 117% |
| Hunter | 643 | 107% |
| Demonology Warlock | 576 | 96% |
| Rogue | 566 | 94% |
| Fire Mage | 515 | 86% |
| Feral Druid | 674 | 112% |
| **Retribution, live** | **672** | **112%** |
| Shadow Priest | 597 | 99% |
| Enhancement Shaman | 525 | 87% |
| Balance Druid | 496 | 83% |
| Elemental Shaman | 405 | 67% |

- **The gear is not the same for each class.** The sets have different quality: Retribution has 7 epic items, the Hunter and the Warlock have 1. Ret in the Warrior armor does 571 (−15%), and the Warrior in the Ret armor does 562 (−20%). Thus, parts 1 and 3 use the same item pool run above.
- **Retribution and Feral are 12% above the pure average.** The other hybrids are at 67–99%. In this sim, no hybrid group is at 95%.
- **Changes to the test sets.** Fury uses the wowsims pre-raid Fury set, with Dark Iron Destroyer in place of Annihilator (a world drop). The raid and PvP items of the Mage set are replaced with the Warlock choices. The new blue items of Forever (for example Adaptive Combat Assistant) have no source in the game data. All sets keep them.
- **Files.** `models/wowsims-b2/go/allspecs_main.go` and `logs/allspecs.log`.

## 8. Options that were not kept

- **Burning Zeal (C-R4).** +0.8% at fresh 60 to +1.4% in Naxxramas. Withdrawn on 31 October: the live Retribution was above the target.
- **Measure for Measure (C-R5).** About +1% at all gear levels. Withdrawn.
- **Holy Strike Seal trigger (C1).** +5.3–5.7% at all gear levels. Withdrawn on 2 November 2026: Retribution was above the target. The decision of 9 November keeps it withdrawn.
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

- Unsealed Wrath: each auto attack that lands stores a copy of the active Seal (3 copies). A swing with the other Seal releases them. Seal of Command copies ignore the 1 sec cooldown of the proc.
- Seal plan 1 + 3, the wowsims rotation: 1 swing with Seal of Righteousness, then 3 swings with Seal of Command.
- Seal of Command: 7 procs each min, 70% of weapon damage + 23.3% of spell damage.
- Seal of Righteousness: 67.5 + 12% of spell damage for each hit.
- Judgement: one each 8 sec, 178.2 + 42.9% of spell damage.
- Holy Strike: one each 10 sec, 50% of (weapon damage + 93 + 42.9% of spell damage). Sacred Arbiter +20%.
- Hammer of Wrath: one each 6 sec in the last 20% of the fight, 498 + 42.9% of spell damage.
- Improved Seals ×1.15 (Seals and Judgements). Two-Handed Weapon Specialization ×1.06 (physical only). Conviction +6% critical hit. Vengeance: average +5.4%.
- Not in the model: Exorcism, Consecration, Retribution Aura.

**Other gear growth cases (live / C1 withdrawn, Naxxramas):** ×1.60 gives 100% / 106%. ×1.90 gives 90% / 95%.

## 10. Method and limits

- **Scripts.** `models/beta-30-oct/retribution_b2.py` (model) and `damage_tables_b2.py` (tables). wowsims tests in `models/wowsims-b2`. Other classes: wowsims with the same item pool (part 7) and `models/damage` (increase with gear of Fury, Arms and Combat Rogue).
- The model calculates averages. It is not a full simulation.
- The model keeps the rules of 30 October: Vengeance 3 stacks, and Two-Handed Weapon Specialization on physical damage only. The start value (910) has the changes of build 70755 and the Windfury Totem rule of 9 November. It also has the Seal procs from the Windfury Totem strike (15 November). It also has the ranged Judgement of Righteousness and Judgement of Fury (hotfixes of 11 November). Judgement of Command is melee (late hotfix of 13 November). Thus, the increase with gear is an estimate.
- Not confirmed: the critical hit decrease against a boss, and the Seal of Righteousness value with a 3.6 sec weapon.
- The Fury and Combat Rogue rotations and talents are assumptions. Arms uses the wowsims rotation.
- The gear levels are estimates with Classic steps. The Forever raid items are not known.
