# Healing

This section compares the Holy Paladin with the three other healers of Forever: Priest, Druid and Shaman. It uses the beta trees of 30 October 2026. It uses all the Forever heals of each class, not only the big heals. The design goal of Holy is a healer for long fights and the best single-target healer. It does not need to be the best raid healer.

No Holy talent proposal stays. Thus, the proposed Holy Paladin is the beta Holy Paladin. The spell changes (C1, C2, C4, C5) do not change the healing values.

## Summary

- **On one tank, the Paladin is first.** With Oath of Light on the tank, it is 3–12% above the Druid, and 21–28% above the Shaman and the Priest (part 5). In the beta of 18 October, it was 5–13% below the Druid.
- **After a large hit, the Paladin is first.** With all cooldowns, it heals 18% more than the Druid in the first 3 sec, and 11% more in 6 sec. With short cooldowns only, it is 2% below the Druid (part 6).
- **In raids, the Paladin is still the weakest healer.** It is 18–26% below the Druid, 8–13% below the Shaman and 34–41% below the Priest (part 4). This is accepted, because Holy is not a raid healer first.
- **The cause in raids.** Oath of Light helps only one ally. In raids, almost all casts go to other targets. The other healers have efficient cooldown heals for the raid: Prayer of Mending, Riptide, Swiftmend and Tranquility (part 3).
- **The Paladin has the least mana.** Reverence keeps 30% of the Spirit regeneration during casts. Meditation, Reflection and Mindfulness keep 50% (part 2).
- **Holy Power decides the one-tank result.** The values use a 225% critical heal (wowsims). At 175%, the Paladin is 7% below to 1% above the Druid on one tank (part 7). Open items gives the test.

## 1. Model

- **Source.** The model uses the method of the DoubleZug sheets for the four Forever healers (early beta). All classes use the same gear, buffs and fight. A check compared each spell value with the Forever spellbook. Three reviews corrected the model (22 October 2026). A check against the game files in wowsims Forever (23 October 2026) corrected the Paladin base critical chance, the Regrowth coefficients and Chain Heal.
- **Scripts.** models/healing/healing_model.py gives the Priest, the Druid, the Shaman and the solver. models/beta-30-oct/healing_b2.py gives the Paladin of the beta of 30 October. models/beta-30-oct/recovery_b2.py gives part 6. models/beta-30-oct/holy_proposals_b2.py gives part 8.
- **Gear.** 715 healing power, 315 Intellect, 249 Spirit, 40 mana each 5 sec, 4% spell critical chance. Parts 4 and 5 also use 900 healing power (raids).
- **Raid buffs.** Arcane Intellect, Mark of the Wild, Blessing of Kings and Divine Spirit give stats. Blessing of Wisdom, Mana Spring Totem and a mana oil give mana. An aura gives +3% spell critical chance. Thus, each healer has 117 mana each 5 sec.
- **Consumables and other healers.** Each healer uses one major mana potion each 2 min (1,800 mana). Each healer also receives one Mana Tide Totem each 5 min (1,160 mana). A potion or a cooldown counts only if it ends before the end of the fight.
- **Mana pool.** Classic base mana at level 60, plus 15 mana for each point of Intellect.
- **Spirit regeneration.** The model uses the Classic 1.12 formula of each class. Forever did not publish a formula.
- **Paladin build.** 38/5/8: Holy with no Divine Strength and no Divine Precision, Purifying Power 1. Divine Intellect 5/5, Benediction 5/5 and Conviction 3/3 (+6% critical chance with all spells). Healing Light 3/3 (+12%), Reverence 2/2 (30%), Illumination 5/5, Divine Favor, Holy Shock, Holy Power 5/5, Boundless Light 2/2 and Light's Vigil. The Paladin base spell critical chance is 3.5% (game files).
- **Oath of Light.** On one ally: Holy Light +400, Flash of Light +115, Holy Shock +229. In the one-tank values, the tank has the Oath. In the raid values, the heals go to other targets and have no Oath.
- **Holy Power 5/5.** The critical heal heals for 225% (×1.5 on the 150% critical heal). This is the wowsims value. Part 7 gives 200% and 175%.
- **Boundless Light 2/2.** Holy Shock has +30% critical chance on an ally with no Oath of Light.
- **Talents of the other healers.** Druid: Gift of Nature, Improved Rejuvenation, Genesis (+5% periodic healing), Improved Regrowth, Gift of the Earthmother and Nature's Splendor (Rejuvenation 15 sec, Regrowth 27 sec). Priest: Prayer of Mending and Binding Heal, no Penance. Shaman: Purification, Healing Way (25%) and Tidal Mastery.
- **Cast plan.** A linear program finds the best mix of casts for the mana and the time of the fight. After 5 sec with no cast, the full Spirit regeneration starts. The model counts 2/3 of the time with no cast as full regeneration. Instant spells use a global cooldown of 1.5 sec. Gift of the Earthmother gives 1 sec to Rejuvenation, Swiftmend and Wild Growth.
- **Critical heals.** Direct heals can be critical heals. In Forever, each tick of a heal over time can also be a critical heal ([Warcraft Tavern](https://www.warcrafttavern.com/forever/guides/restoration-druid/)). The model gives each tick the critical chance of the class (×1.5).
- **Raid and one tank.** "Raid" counts all heals on all targets. "One tank" counts only the heals on the tank: one target of Prayer of Mending, Tranquility, Healing Stream Totem and Light's Vigil.
- **Overhealing (DoubleZug values).** Flash of Light 15%, Holy Light 20%, Holy Shock 15%, Light's Vigil 25%. Prayer of Mending 15%. Renew, Greater Heal and Binding Heal 25%. Regrowth and Rejuvenation 25%, Swiftmend 20%, Tranquility 40%, Wild Growth 50%. Riptide and Chain Heal 25%, Healing Wave 20%, Healing Stream Totem 50%.
- **Light's Vigil.** Rank 3: 1,340 mana. The next Holy Shock heals each party member for 684–724. The beta of 30 October changes only its range (40 yd). The model uses one Illumination return for each cast if one of the 5 heals is critical. No player test gives these values.
- **Not in the model.** Power Word: Shield and Divine Aegis absorbs, the armor from Inspiration and Ancestral Healing, Lay on Hands and Nature's Swiftness.

## 2. Mana for each healer

Mana for the full fight: mana pool, mana each 5 sec, Spirit regeneration during casts, potions, Mana Tide Totem and class tools. Time with no cast gives more.

| Healer | Mana pool | Spirit regeneration during casts (mana per sec) | 3 min | 5 min | 10 min |
| --- | --- | --- | --- | --- | --- |
| Priest | 7,486 | 24.2 | 20,823 | 28,341 | 47,396 |
| Druid (Innervate on itself) | 7,534 | 23.1 | 24,804 | 32,178 | 55,022 |
| Shaman | 7,810 | 21.1 | 20,571 | 27,705 | 45,800 |
| Paladin | 7,802 | 12.3 | 18,993 | 25,081 | 40,560 |

- The Paladin has the least mana: 9% less than the Priest and 23% less than the Druid in fights of 3 min.
- The cause is Reverence (30%). Meditation, Reflection and Mindfulness keep 50%. The beta of 30 October does not change Reverence (2 ranks, 15/30%).
- The Druid casts Innervate on itself (4,149 mana each 6 min). In raids, Druids often give it to a Priest.

## 3. Healing per mana of each spell

715 healing power. Raw healing per mana · healing per mana after overhealing. The values include critical heals and mana returns.

| Healer | Cooldown heals | Other heals |
| --- | --- | --- |
| Priest | Prayer of Mending (5 targets, 10 sec): 18.5 · 15.7 | Binding Heal 8.2 · 6.1. Renew 7.2 · 5.4. Greater Heal 6.5 · 4.9. Prayer of Healing 5.2 · 3.4. Flash Heal 4.1 · 3.1 |
| Druid | Tranquility (2 min): 11.9 · 7.2. Swiftmend (15 sec, full Regrowth): 8.8 · 7.0. Wild Growth (6 sec): 5.1 · 2.5 | Regrowth 7.6 · 5.7. Rejuvenation 6.8 · 5.1. Healing Touch 4.7 · 3.8 |
| Shaman | Healing Stream Totem: 160 · 80. Riptide (6 sec): 7.8 · 5.8 | Chain Heal (2.5 targets, on a Riptide target) 7.5 · 5.6. Healing Wave 6.0 · 4.8. Lesser Healing Wave 4.1 · 3.5 |
| Paladin, raid (no Oath of Light) | Divine Favor and Holy Light (2 min): 13.5 · 10.8. Light's Vigil and Holy Shock (6 sec): 6.1 · 4.7. Holy Shock (10 sec): 5.7 · 4.9 | Flash of Light 7.2 · 6.2. Holy Light 5.2 · 4.2 |
| Paladin, tank with Oath of Light | Divine Favor and Holy Light: 16.1 · 12.9. Light's Vigil and Holy Shock: 5.9 · 4.5. Holy Shock: 4.9 · 4.2 | Flash of Light 8.6 · 7.3. Holy Light 6.2 · 5.0 |

- On the tank with Oath of Light, Flash of Light (8.6) is the most efficient filler heal of all healers. Renew gives 7.2, Regrowth 7.6 and Chain Heal 7.5.
- In raids, Flash of Light (7.2) is equal to the filler heals of the other healers. But the other healers also cast their cooldown heals each time that they are ready. In fights of 3 min, Prayer of Mending gives 43% of the Priest healing. Riptide gives 47% of the Shaman healing. Swiftmend and Tranquility give 21% of the Druid healing.
- Holy Power makes Divine Favor and Holy Light the most efficient Paladin heal. It is available only one time each 2 min.
- Boundless Light makes Holy Shock better in raids (5.7 raw healing per mana) than on the tank (4.9). It is still below Flash of Light.

## 4. Raid healing

Healing per sec after overhealing, all targets.

| Healer | 715: 3 min | 715: 5 min | 715: 10 min | 900: 3 min | 900: 5 min | 900: 10 min |
| --- | --- | --- | --- | --- | --- | --- |
| Priest | 948 | 846 | 769 | 1,053 | 938 | 852 |
| Druid | 855 | 689 | 604 | 903 | 729 | 639 |
| Shaman | 709 | 599 | 517 | 779 | 654 | 562 |
| Paladin, beta of 18 October | 616 | 532 | 449 | 674 | 588 | 496 |
| Paladin, beta of 30 October | 629 | 533 | 450 | 697 | 599 | 506 |

- The Paladin is 18–26% below the Druid, 8–13% below the Shaman and 34–41% below the Priest.
- The beta of 30 October gives +0–3% in raids. Holy Power gives larger critical heals, but Blessing of Light is gone. Oath of Light helps only one ally.
- The Paladin casts Flash of Light, and Divine Favor with Holy Light each 2 min. In fights of 3 min, it also casts about 5 Light's Vigil. It spends all its mana before the end of the fights of 3 and 5 min.
- **Upper limit.** With Oath of Light on all heals, the Paladin is 3–7% above the Shaman. This is not possible in the game. It shows that Oath of Light alone is not a raid tool.

## 5. One tank

Healing per sec after overhealing, on one tank with Oath of Light. "Maximum" is the raw healing per sec for 30 sec, with no mana limit and all cooldowns ready.

| Healer | 715: 3 min | 715: 5 min | 715: 10 min | 900: 3 min | 900: 5 min | 900: 10 min | Maximum, 715 | Maximum, 900 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Priest | 606 | 511 | 441 | 649 | 549 | 475 | 1,289 | 1,375 |
| Druid | 681 | 573 | 518 | 737 | 622 | 563 | 1,320 | 1,423 |
| Shaman | 607 | 509 | 437 | 654 | 548 | 470 | 1,278 | 1,377 |
| Paladin, beta of 18 October | 616 | 532 | 449 | 674 | 588 | 496 | 1,279 | 1,347 |
| Paladin, beta of 30 October | 732 | 633 | 534 | 801 | 699 | 590 | 1,536 | 1,618 |

- The Paladin is 3–12% above the Druid, and 21–28% above the Shaman and the Priest. Its maximum is 14–16% above the Druid.
- The design goal of Holy is the best single-target healer. The beta of 30 October reaches it (single-target goal, W14). A lead of more than 20% is too strong.
- The lead is smallest in fights of 10 min (+3% at 715). Then the mana of the Paladin is the limit.
- The cast plan is almost only Flash of Light, with Divine Favor and Holy Light each 2 min. In fights of 3 min, a Holy Light also follows a critical Flash of Light (Infusion of Light).

## 6. Recovery after a large hit

The table gives the healing on the tank in the first 3 and 6 sec after the hit. There is no overhealing. The long cooldowns are Divine Favor, Nature's Swiftness and Inner Focus.

The rules of the recovery model:

- Before the hit, each healer heals the tank as in its cast plan for one tank. Thus, its heals over time are on the tank at the hit: Renew (Priest), Rejuvenation and Regrowth (Druid), Riptide and Healing Stream Totem (Shaman).
- Their ticks after the hit count. A new cast of the same spell replaces the old one.
- Swiftmend heals for the full Rejuvenation. If no Rejuvenation is on the tank, Swiftmend uses the Regrowth.
- The Paladin has Oath of Light on the tank. Infusion of Light can be active at the hit after a critical Flash of Light.

| Healer | 715: 3 sec | 715: 6 sec | 715: 3 sec, no long cooldown | 715: 6 sec, no long cooldown | 900: 3 sec | 900: 6 sec |
| --- | --- | --- | --- | --- | --- | --- |
| Priest | 3,932 | 7,416 | 3,569 | 7,052 | 4,193 | 7,905 |
| Druid | 6,293 | 10,041 | 4,898 | 8,686 | 6,839 | 10,860 |
| Shaman | 4,750 | 8,054 | 3,361 | 6,664 | 5,119 | 8,689 |
| Paladin, beta of 18 October | 5,024 | 8,232 | 3,947 | 7,155 | 5,337 | 8,745 |
| Paladin, beta of 30 October | 7,441 | 11,183 | 4,784 | 8,526 | 7,882 | 11,839 |

- With all cooldowns, the Paladin is 18% above the Druid after 3 sec and 11% above after 6 sec. Divine Favor with Holy Power and Oath of Light gives a Holy Light of about 4,900.
- With short cooldowns only, the Paladin is 2% below the Druid after 3 and 6 sec. The heals over time of the Druid are on the tank at the hit, and Swiftmend heals for a full Rejuvenation.
- The Paladin is 39% or more above the Shaman and the Priest after 6 sec with all cooldowns.
- At 900 healing power, the result is almost the same.
- Power Word: Shield is not in the table. It absorbs about 1,100 damage and uses one global cooldown.

## 7. Holy Power: 225%, 200% or 175%

The Holy Power text says that it increases the critical heal bonus of Holy spells by 50%. wowsims and the server rule (aura A_MOD_CRITICAL_HEALING_AMOUNT) multiply the full critical heal by 1.5: 225%. The Classic rule of Ice Shards and Ruin adds 50% of the bonus: 175%.

| Case (715) | Raid, 3 / 5 / 10 min, against the Druid | One tank, 3 / 5 / 10 min, against the Druid |
| --- | --- | --- |
| 225% | −26% / −23% / −26% | +8% / +10% / +3% |
| 200% | −30% / −27% / −29% | +2% / +5% / −2% |
| 175% | −34% / −31% / −33% | −3% / −1% / −7% |

- At 225%, the Paladin is the best healer on one tank in all cases.
- At 175%, the Druid is first on one tank in fights of 3 and 10 min. The design goal is then not reached.
- Open items gives the test. Take Holy Power 5/5, cast Divine Favor, then Holy Light on a target with no Oath of Light. Compare the heal with the average of the tooltip.

## 8. Options examined on the beta of 30 October

These options are withdrawn (see Withdrawn ideas). The table gives their values for a decision after the Holy Power test.

| Option (715) | Raid against the Druid, 3 / 5 / 10 min | One tank against the Druid, 3 / 5 / 10 min |
| --- | --- | --- |
| Beta of 30 October | −26% / −23% / −26% | +8% / +10% / +3% |
| Lingering Light 2/2 (C-H2) | −21% / −17% / −20% | +15% / +18% / +10% |
| Reverence 50% (C-H1) | −22% / −18% / −19% | +13% / +17% / +12% |
| Reverence 50% and Lingering Light 2/2 | −17% / −12% / −14% | +21% / +25% / +20% |
| Boundless Light also +15% critical chance for Flash of Light | −16% / −8% / −10% | +8% / +10% / +3% |
| Boundless Light for Flash of Light, critical heal 200% | −21% / −15% / −16% | +2% / +5% / −2% |
| Flash of Light +30% critical chance, critical heal 200% | −13% / −3% / 0% | +2% / +5% / −2% |

- Lingering Light and Reverence 50% add 5–12 points to the one-tank lead at 225%. Together, they give 20–25% above the Druid, past the 20% limit.
- Boundless Light for Flash of Light changes only the raid values, because the tank has the Oath of Light. It is the best option if the Holy Power test gives 175–200%.
- Infusion of Light on all hits (C-H3) adds nothing in the model. The cast plan is almost only Flash of Light.

## 9. Limits

The values in brackets are for a raid fight of 3 min at 715 healing power.

- **Holy Power.** The values use 225%. Part 7 gives the other cases. This is the largest open question of this tab.
- **Prayer of Mending.** The model gives it 5 targets with 15% overhealing. It gives 43% of the Priest healing. With 3 targets, the Priest gives 786, not 948.
- **Omen of Clarity.** With 2 free Wild Growth casts each minute, the Druid gives 940, not 855.
- **Mana Tide Totem.** With two Mana Tide Totems, the Shaman gives 742, not 709.
- **Swiftmend.** A player test shows that it does not remove the heal over time. If Swiftmend removes the heal over time, the Druid gives 833 in raids (not 855) and 616 on one tank (not 681).
- **Nature's Splendor.** It needs 11 Balance points. Without it, the Druid gives 747 in raids and 626 on one tank.
- **Critical heals over time.** The values use critical ticks for all heals over time, as in Forever. With the Classic rule (no critical ticks), the Paladin is 7–9% below the Shaman and 19–23% below the Druid in raids. On one tank, it is 6–14% above the Druid.
- **Spirit regeneration.** The Classic formulas give the Priest the most regeneration. Forever can use a different formula (see Open items).
- **Overhealing.** The values are estimates. They change with the raid, the damage and the healer assignments.
- **Oath of Light.** The model puts all tank heals on the Oath target. A Paladin who heals two tanks has the Oath on one of them only.
- **Light's Vigil.** Only one Light's Vigil for each party can be active. The model gives the Paladin a full party of 5.
- **wowsims.** wowsims Forever has no heal rotation for the Holy Paladin now (a gear planner only). The Druid and the Shaman have no heal spells in wowsims. Thus, this tab has no wowsims check on the beta of 30 October. The earlier check (beta of 18 October) found the Paladin model within −4.3% to +5.3% of wowsims. It is in the history of the repository.
