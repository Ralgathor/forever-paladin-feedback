# Healing

This section compares the Holy Paladin with the three other healers of Forever: Priest, Druid and Shaman. It uses all the Forever heals of each class, not only the big heals. It also checks C3 in PvP. The design goal of Holy is a healer for long fights and the best single-target healer.

## Summary

- **In the beta, the Holy Paladin is the weakest raid healer.** It heals 10–13% less than the lowest other healer, and 35–42% less than the Priest (part 4).
- **The cooldown heals cause the difference.** For the other healers, a cooldown heal is the most efficient spell: Prayer of Mending, Riptide, Swiftmend and Tranquility. For the Paladin, Holy Shock and Light's Vigil are the least efficient spells (part 3).
- **The Paladin also has the least mana.** Reverence keeps 30% of the Spirit regeneration during casts. Meditation, Reflection and Mindfulness keep 50% (part 2).
- **The Druid talents make the Druid strong.** Nature's Splendor makes Rejuvenation and Regrowth last longer. Swiftmend heals for the full heal over time and does not remove it (player test). Gift of the Earthmother gives a global cooldown of 1 sec.
- **With the proposals, the Paladin is about equal to the Shaman in raids** (−2% to +5%). It is 7–19% below the Druid and 27–32% below the Priest. C1 gives the mana. C2, C19 and Conviction give larger heals (part 4).
- **On one tank, the proposed Paladin is first by a small margin.** It is 1–9% above the Druid, and 14–32% above the Shaman and the Priest. Thus, the proposals make the Paladin the best single-target healer, as the design goal says. In the beta, the Paladin is 5–13% below the Druid (part 5).
- **After a large hit on one tank, the Druid is first.** The proposed Paladin is 14–18% below it after 3 sec, and 3–4% below after 6 sec. It is 9% or more above the Shaman and the Priest. In the beta, the Paladin is 18–22% below the Druid (part 5).
- **Heals over time can be critical heals in Forever.** This helps the Priest, the Druid and the Shaman. The Paladin has almost no heals over time. With the Classic rule, the proposed Paladin is 1–4% higher against each healer (part 8).
- **We withdrew C20.** With C20, the Paladin is first on one tank by 9–15%, and 10–14% above the Shaman in raids. Healing Light at 35% gives +5% to +13% on one tank (part 6, W14).
- **A stronger Holy Shock or Light's Vigil is not necessary in raids.** The raid healing is already at the level of the Shaman (part 6).

## 1. Model

- **Source.** The model uses the method of the DoubleZug sheets for the four Forever healers (early beta). All classes use the same gear, buffs and fight. We compared each spell value with the Forever spellbook. Three reviews corrected the model (22 October 2026). They examined the first version, the recovery model and the talents of the Druid, the Priest and the Shaman. A check against the game files in wowsims Forever (23 October 2026) corrected the Paladin base critical chance, the Regrowth coefficients and Chain Heal.
- **Gear.** 715 healing power, 315 Intellect, 249 Spirit, 40 mana each 5 sec, 4% spell critical chance. Parts 4 and 5 also use 900 healing power (raids).
- **Raid buffs.** Arcane Intellect, Mark of the Wild, Blessing of Kings and Divine Spirit give stats. Blessing of Wisdom, Mana Spring Totem and a mana oil give mana. An aura gives +3% spell critical chance. Thus, each healer has 117 mana each 5 sec.
- **Consumables and other healers.** Each healer uses one major mana potion each 2 min (1,800 mana). Each healer also receives one Mana Tide Totem each 5 min (1,160 mana). A potion or a cooldown counts only if it ends before the end of the fight. Thus, the healer uses 2 potions in 3 min and 5 potions in 10 min.
- **Mana pool.** Classic base mana at level 60, plus 15 mana for each point of Intellect. The DoubleZug sheets do not add the base mana.
- **Spirit regeneration.** The model uses the Classic 1.12 formula of each class. Forever did not publish a formula. The DoubleZug tests do not agree with the Classic formula or the TBC formula.
- **Talents.** Each class uses the healer build of its DoubleZug sheet. The Paladin has a base spell critical chance of 3.5% (game files). The beta Paladin has Divine Intellect, Healing Light 3/3, Reverence 3/3, Illumination 5/5 and Infusion of Light 2/2. It also has Divine Favor, Holy Shock, Holy Power 5/5, Light's Vigil and Benediction 5/5. Blessing of Light is on the target.
- **Talents of the other healers.** Druid: Gift of Nature, Improved Rejuvenation, Genesis (+5% periodic healing), Improved Regrowth. The Druid also has Gift of the Earthmother and Nature's Splendor (Rejuvenation 15 sec, Regrowth 27 sec). Priest: Prayer of Mending and Binding Heal, no Penance (the build has no points for it). Shaman: Purification, Healing Way (25%) and Tidal Mastery.
- **Proposed Paladin.** C1, C2, C3, C19, Benediction 5/5 (M11) and Conviction (C15, M8), as in build HB1. Illumination stays at 50% (we withdrew C20).
- **Cast plan.** A linear program finds the best mix of casts for the mana and the time of the fight. The mix can use all heals of the class. After 5 sec with no cast, the full Spirit regeneration starts. The model counts 2/3 of the time with no cast as full regeneration. Instant spells use a global cooldown of 1.5 sec. Gift of the Earthmother gives 1 sec to Rejuvenation, Swiftmend and Wild Growth.
- **Critical heals.** Direct heals can be critical heals. In Forever, each tick of a heal over time can also be a critical heal ([Warcraft Tavern](https://www.warcrafttavern.com/forever/guides/restoration-druid/)). The model gives each tick the critical chance of the class (×1.5). The ticks of Lingering Light (C2) can also be critical heals, but a critical tick does not start Lingering Light again. Lingering Light follows its text: a direct critical heal adds to the healing that stays, and the total ticks over a new 6 sec. The model removes the healing that stays at the end of the fight.
- **Raid and one tank.** "Raid" counts all heals on all targets. "One tank" counts only the heals on the tank: one target of Prayer of Mending, Tranquility, Healing Stream Totem and Light's Vigil. Only one Rejuvenation and one Renew can be active at a time. A Riptide or a Regrowth stays for its full duration, or the healer casts it again before the end.
- **Overhealing (DoubleZug values).** Flash of Light 15%, Holy Light 20%, Holy Shock 15%, Light's Vigil 25%, the Lingering Light heal (C2) 50%. Prayer of Mending 15%. Renew, Greater Heal and Binding Heal 25%. Regrowth and Rejuvenation 25%, Swiftmend 20%, Tranquility 40%, Wild Growth 50%. Riptide and Chain Heal 25%, Healing Wave 20%, Healing Stream Totem 50%.
- **Light's Vigil.** Rank 3: 1,340 mana. The next Holy Shock heals each party member for 684–724. The Illumination text names Light's Vigil. The model uses one Illumination return for each cast if one of the 5 heals is critical. It uses a coefficient of 15%, and no Holy Power or Healing Light bonus. No player test gives these values.
- **Other rules.** Binding Heal: 2 casts each min, because half of it heals the Priest (DoubleZug). Swiftmend heals for the full heal over time of the Rejuvenation (one tank) or the Regrowth (raid). In raids, the plan casts Regrowth. This agrees with the Forever text of Swiftmend. It does not remove the heal over time (player test).
- **Corrections to the DoubleZug sheets.**
  - Druid: Rejuvenation rank 11 heals 776 in 12 sec, and 970 in 15 sec with Nature's Splendor (sheet: 812). Regrowth heals 994 over 21 sec, and 1,278 over 27 sec (the same as the sheet). The healing power bonus also increases with the duration. The Regrowth coefficients are 28.6% (direct) and 49.7% (over 21 sec), from the game files.
  - Druid: the sheet gives 6 free Wild Growth casts from Omen of Clarity. The model gives none, because Omen of Clarity needs melee hits (part 8).
  - Priest: Prayer of Mending can also be a critical heal. Druid: Swiftmend can also be a critical heal.
  - Shaman: one Mana Tide Totem (sheet: two) and 715 healing power (sheet: 700). Chain Heal rank 3 heals 506.5 at level 60 (game files; sheet: 490).
  - Paladin: Holy Light 1,580 and Flash of Light 308 (sheet: 1,609 and 316).
- **Not in the model.** Power Word: Shield and Divine Aegis absorbs, the armor from Inspiration and Ancestral Healing, Lay on Hands and Nature's Swiftness.

## 2. Mana for each healer

Mana for the full fight: mana pool, mana each 5 sec, Spirit regeneration during casts, potions, Mana Tide Totem and class tools. Time with no cast gives more.

| Healer | Mana pool | Spirit regeneration during casts (mana per sec) | 3 min | 5 min | 10 min |
| --- | --- | --- | --- | --- | --- |
| Priest | 7,486 | 24.2 | 20,823 | 28,341 | 47,396 |
| Druid (Innervate on itself) | 7,534 | 23.1 | 24,804 | 32,178 | 55,022 |
| Shaman | 7,810 | 21.1 | 20,571 | 27,705 | 45,800 |
| Paladin, beta | 7,802 | 12.3 | 18,993 | 25,081 | 40,560 |
| Paladin, proposed (C1) | 7,802 | 20.6 | 20,473 | 27,547 | 45,492 |

- In the beta, the Paladin has the least mana: 9% less than the Priest and 23% less than the Druid in fights of 3 min.
- The cause is Reverence (30%). Meditation, Reflection and Mindfulness keep 50%. With C1, the Paladin has about the same mana as the Priest and the Shaman.
- The Druid casts Innervate on itself (4,149 mana each 6 min). In raids, Druids often give it to a Priest.
- Water Shield (Shaman), Litany of Light (Priest), Illumination and Divine Favor (Paladin) are in the spell costs of part 3.

## 3. Healing per mana of each spell

715 healing power. Raw healing per mana · healing per mana after overhealing. The values include critical heals and mana returns.

| Healer | Cooldown heals | Other heals |
| --- | --- | --- |
| Priest | Prayer of Mending (5 targets, 10 sec): 18.5 · 15.7 | Binding Heal 8.2 · 6.1. Renew 7.2 · 5.4. Greater Heal 6.0 · 4.5. Prayer of Healing 5.2 · 3.4. Flash Heal 4.1 · 3.1 |
| Druid | Tranquility (2 min): 11.9 · 7.2. Swiftmend (15 sec, full Regrowth): 8.8 · 7.0. Wild Growth (6 sec): 5.1 · 2.5 | Regrowth 7.6 · 5.7. Rejuvenation 6.8 · 5.1. Healing Touch 4.7 · 3.8 |
| Shaman | Healing Stream Totem: 160 · 80. Riptide (6 sec): 7.8 · 5.8 | Chain Heal (2.5 targets, on a Riptide target) 7.5 · 5.6. Healing Wave 6.0 · 4.8. Lesser Healing Wave 4.1 · 3.5 |
| Paladin, beta | Divine Favor and Holy Light (2 min): 10.7 · 8.6. Light's Vigil and Holy Shock (6 sec): 4.9 · 3.7. Holy Shock (10 sec): 3.4 · 2.9 | Flash of Light 7.3 · 6.2. Holy Light 5.3 · 4.3 |
| Paladin, proposed | Divine Favor and Holy Light: 12.8 · 9.5. Light's Vigil and Holy Shock: 5.9 · 4.4. Holy Shock: 4.6 · 3.7 | Flash of Light 8.2 · 6.7. Holy Light 5.9 · 4.6 |

- The filler heals are about equal: Flash of Light (beta) 7.3, Renew 7.2, Regrowth 7.6 and Chain Heal 7.5 raw healing per mana.
- The other healers cast their cooldown heals each time that they are ready. In fights of 3 min, Prayer of Mending gives 43% of the Priest healing. Riptide gives 47% of the Shaman healing. Swiftmend and Tranquility give 21% of the Druid healing.
- Holy Shock and Light's Vigil are the least efficient Paladin spells, in the beta and with the proposals. The best cast plan does not use them.
- With the proposals, Flash of Light (8.2) is the most efficient Paladin heal after Divine Favor. Divine Favor is available only one time each 2 min.

## 4. Raid healing

Healing per sec after overhealing, all targets.

| Healer | 715: 3 min | 715: 5 min | 715: 10 min | 900: 3 min | 900: 5 min | 900: 10 min |
| --- | --- | --- | --- | --- | --- | --- |
| Priest | 948 | 846 | 769 | 1,053 | 938 | 852 |
| Druid | 855 | 689 | 604 | 903 | 729 | 639 |
| Shaman | 709 | 599 | 517 | 779 | 654 | 562 |
| Paladin, beta | 616 | 532 | 449 | 674 | 588 | 496 |
| Paladin, proposed | 694 | 605 | 526 | 769 | 677 | 592 |

- The Priest, the Druid and the Shaman spend all their mana before the end of the fight. Thus, their healing per mana and their mana decide the result.
- In the beta, the Paladin is 10–13% below the lowest other healer.
- With the proposals, the Paladin is −2% to +5% against the Shaman and 7–19% below the Druid. It is still 27–32% below the Priest. The cause is Prayer of Mending (part 8).
- After the Priest, the Druid heals the most. Swiftmend on a Regrowth of 27 sec is its most efficient heal after Tranquility. It also casts Innervate on itself.
- The proposed Paladin casts Flash of Light, Holy Light when Infusion of Light is active, and Divine Favor. It does not cast Holy Shock or Light's Vigil. In fights of 10 min, it also uses all its mana before the end.

## 5. One tank

Healing per sec after overhealing, on one tank. "Maximum" is the raw healing per sec for 30 sec, with no mana limit and all cooldowns ready.

| Healer | 715: 3 min | 715: 5 min | 715: 10 min | 900: 3 min | 900: 5 min | 900: 10 min | Maximum, 715 | Maximum, 900 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Priest | 568 | 481 | 416 | 611 | 518 | 450 | 1,202 | 1,288 |
| Druid | 681 | 573 | 518 | 737 | 622 | 563 | 1,320 | 1,423 |
| Shaman | 607 | 509 | 437 | 654 | 548 | 470 | 1,278 | 1,377 |
| Paladin, beta | 616 | 532 | 449 | 674 | 588 | 496 | 1,279 | 1,347 |
| Paladin, proposed | 694 | 605 | 526 | 769 | 677 | 592 | 1,531 | 1,647 |

- In the beta, the Paladin is 5–13% below the Druid, and 1–13% above the Shaman and the Priest. Its maximum is about equal to the Shaman.
- With the proposals, the Paladin is 1–9% above the Druid, and 14–32% above the Shaman and the Priest. Its maximum is 16% above the Druid and 20% above the Shaman.
- The proposals give more mana (C1) and larger heals (C2, C19, Conviction). The lead over the Shaman and the Priest increases with the fight length.
- The design goal of Holy is the best single-target healer. The proposals reach it by 1–9%. With C20 (withdrawn), the lead is 9–15%. With Healing Light at 35%, it is 5–13% (part 6, W14).

**Holy Light in the model.** The values above count all healing on the tank as equal. Thus, the model casts Holy Light only after Infusion of Light or with Divine Favor. Holy Light gives about 30% of the healing in fights of 3 min and 6% in fights of 10 min. The other heals are Flash of Light, because it gives more healing for each mana point (8.2 against 5.9). In a real fight, a Paladin casts more Holy Light after a large hit. The table below shows this value.

**Recovery after a large hit.** The table gives the healing on the tank in the first 3 and 6 sec after the hit, at 715 healing power. There is no overhealing. The long cooldowns are Divine Favor, Nature's Swiftness and Inner Focus.

The rules of the recovery model:

- Before the hit, each healer heals the tank as in its cast plan for one tank. Thus, its heals over time are on the tank at the hit. These are Renew (Priest), Rejuvenation and Regrowth (Druid), Riptide and Healing Stream Totem (Shaman), and Lingering Light (Paladin, C2).
- Their ticks after the hit count. A new cast of the same spell replaces the old one. A heal over time cast after the hit ticks each 3 sec.
- Swiftmend heals for the full Rejuvenation. If no Rejuvenation is on the tank, Swiftmend uses the Regrowth.
- Before the hit, the Paladin casts Flash of Light. Then Infusion of Light can be active: always with C3, and 88% of the time in the beta. It stays active until a Holy Light uses it.
- Lingering Light follows its text. It ticks each 2 sec. A direct critical heal adds the healing that stays to the new heal over time. A simulation of the critical heals gives the Paladin values.

| Healer | 3 sec | 6 sec | 3 sec, no long cooldown | 6 sec, no long cooldown | Best casts (6 sec, no long cooldown) |
| --- | --- | --- | --- | --- | --- |
| Priest | 3,663 | 6,906 | 3,327 | 6,570 | Greater Heal, Greater Heal |
| Druid | 6,293 | 10,041 | 4,898 | 8,686 | Swiftmend, Regrowth, Healing Touch |
| Shaman | 4,750 | 8,054 | 3,361 | 6,664 | Healing Wave, Healing Wave |
| Paladin, beta | 5,024 | 8,232 | 3,947 | 7,155 | Holy Light (Infusion of Light), Holy Shock, Holy Light, Flash of Light |
| Paladin, proposed | 5,188 | 9,695 | 4,217 | 8,449 | Holy Light (1.5 sec), Flash of Light, Holy Light (1.5 sec), Holy Shock |

- The heals over time at the hit give the other healers 300–670 in the first 3 sec: Druid 669, Priest 383, Shaman 301. The Lingering Light pool of the Paladin gives 179.
- The Druid is first in all cases. Its heals over time are on the tank, and Swiftmend heals for a full Rejuvenation in a global cooldown of 1 sec. The proposed Paladin is 14–18% below the Druid after 3 sec, and 3–4% below after 6 sec.
- The proposed Paladin is 9% or more above the Shaman and the Priest in all cases.
- In the beta, the Paladin is 18–22% below the Druid.
- C3 makes each Holy Light after a Flash of Light or Holy Shock a 1.5 sec cast. Without C3, the proposed Paladin heals 1–2% less after 3 sec, and 7–8% less after 6 sec. The beta often has Infusion of Light active at the hit. Thus, C3 adds little in the first 3 sec.
- Lingering Light ticks each 2 sec. Thus, a critical heal after the hit gives its first tick 2 sec later. In the first 3 sec, Lingering Light adds little.
- With only the heals cast after the hit, the proposed Paladin is 4–11% below the Druid after 3 sec. After 6 sec, it is 7–8% above.
- At 900 healing power, the result is almost the same.
- Power Word: Shield is not in the table. It absorbs about 1,100 damage and uses one global cooldown.

## 6. Options and changes examined

**The lead on one tank.** Each value range covers 715 and 900 healing power, and fights of 3, 5 and 10 min.

| Option | Raid, against the Shaman | Raid, against the Druid | Raid, against the Priest | One tank, against the best other healer |
| --- | --- | --- | --- | --- |
| The proposals (Healing Light 30%, Illumination 50%) | −2% to +5% | −7% to −19% | −27% to −32% | +1% to +9% |
| Healing Light 35% (withdrawn) | +2% to +9% | −4% to −16% | −24% to −29% | +5% to +13% |
| Healing Light 25% | −6% to +1% | −11% to −22% | −30% to −34% | −2% to +5% |
| Healing Light 20% | −9% to −3% | −14% to −25% | −32% to −37% | −6% to +1% |
| C20: Illumination 75% (withdrawn) | +10% to +14% | −7% to +1% | −17% to −26% | +9% to +15% |

- In raids, the proposals put the Paladin at the level of the Shaman, and 7–19% below the Druid. On one tank, it is first by 1–9%.
- C20 adds 8–14% in raids and 6–8% on one tank. With C20, the Paladin is first on one tank by 9–15%.
- Healing Light at 35% gives +5% to +13% on one tank. At 25% or 20%, the Paladin is about level with the Druid on one tank (−6% to +5%).

**Changes to Holy Shock and Light's Vigil.** With the proposals.

| Change | Raid, against the Shaman | Raid, against the Priest | One tank, against the best other healer |
| --- | --- | --- | --- |
| None | −2% to +5% | −27% to −32% | +1% to +9% |
| Holy Shock heals ×2 | +7% to +12% | −20% to −28% | +7% to +17% |
| Holy Shock heals ×2.5 | +14% to +20% | −14% to −22% | +15% to +25% |
| Holy Shock costs 50% less | +3% to +10% | −23% to −28% | +5% to +12% |
| Light's Vigil heals ×1.25 | +1% to +5% | −24% to −32% | +1% to +9% |
| Light's Vigil heals ×2 | +27% to +38% | −16% to +3% | +1% to +9% |
| Light's Vigil costs 50% less | +51% to +72% | +11% to +16% | +1% to +9% |
| Illumination returns mana for each critical heal of Light's Vigil (up to 5 for each cast) | +13% to +19% | −11% to −26% | +1% to +9% |
| The same, with Illumination at 75% (C20) | +75% to +114% | +29% to +44% | +15% to +20% |
| Light's Vigil coefficient 0% or 30% | −2% to +5% | −26% to −32% | +1% to +9% |

- A change to Holy Shock or Light's Vigil is not necessary in raids: the raid healing is already at the level of the Shaman.
- A Holy Shock change also increases the result on one tank. With Holy Shock ×2, the Paladin is first on one tank by 7–17%.
- With one Illumination return for each cast, the best cast plan does not use Light's Vigil. With one return for each critical heal, it uses Light's Vigil in all fight lengths. This gives +22% raid healing in fights of 3 min and +14% in fights of 10 min. The coefficient changes the result by less than 1%.
- The cost of Light's Vigil has a large effect: at 50% less, the Paladin is 51–72% above the Shaman.
- Two other values with no test can make Light's Vigil stronger. They are the Holy Power bonus (+15% critical chance for Holy Shock) and the Healing Light bonus.

## 7. C3 in PvP

Assumptions:

- Retribution Paladin, level 60, 300 healing power. No healing talents (Healing Light is in row 6). No Blessing of Light on the Paladin.
- Holy Strike: 10 sec cooldown, about 95% chance to hit a player.
- Other classes: Classic base values −10%.

| Heal | Healing | Cast | Limit |
| --- | --- | --- | --- |
| Flash of Light (Paladin) | 437 | 1.5 sec | — |
| Holy Light (Paladin) | 1,794 | 2.5 sec | — |
| Holy Light after Holy Strike (C3 rank 2) | 1,794 | 1.5 sec | One time each 10 sec |
| Lesser Healing Wave (Enhancement Shaman) | About 930 | 1.5 sec | — |
| Flash Heal (Priest) | About 925 | 1.5 sec | — |

| In 30 sec | Beta (Holy Strike critical hits, about 25%) | C3 (all Holy Strike hits) |
| --- | --- | --- |
| Fast Holy Light casts | About 0.75 | About 3 |
| Healing | About 1,350 | About 5,400 |
| Mana | About 500 | About 1,980 |

- **Without C3, the hybrid Paladin has no good fast heal.** Flash of Light heals half as much as Lesser Healing Wave. A 2.5 sec Holy Light is easy to interrupt.
- **With C3, the Paladin heals about 2,230 in 3 sec** (Holy Light after Holy Strike, then Flash of Light). Two Lesser Healing Waves heal about 1,860. The Paladin cannot do this again before the next Holy Strike.
- **Mana is the main limit.** A Retribution Paladin with about 4,000 mana can cast 5–6 Holy Light. Then it has no mana for Seals and Judgement. A 7-point dip with Infusion of Light has no points for Reverence.
- **Players can stop it.** Kick, Pummel and Earth Shock interrupt the cast. Mortal Strike and Wound Poison decrease the heal by 50%. Spiritual Focus is in row 2. Concentration Aura gives only 35% pushback resistance.
- **It costs damage.** Each heal uses a global cooldown. During it, the Paladin does not attack.
- **Combinations.** Hammer of Justice or Repentance, then Holy Strike, then a 1.5 sec Holy Light gives a free heal of about 1,800. In the beta, the Paladin can already cast Holy Light during Divine Shield.

## 8. Limits

The values in brackets are for a raid fight of 3 min at 715 healing power.

- **Prayer of Mending.** The model gives it 5 targets with 15% overhealing. It gives 43% of the Priest healing. With 3 targets, the Priest gives 786, not 948. The Priest is then below the Druid (855).
- **Omen of Clarity.** With 2 free Wild Growth casts each minute, the Druid gives 940, not 855.
- **Mana Tide Totem.** With two Mana Tide Totems, the Shaman gives 742, not 709.
- **Swiftmend.** A player test shows that it does not remove the heal over time. If Swiftmend removes the heal over time, the Druid gives 833 in raids (not 855) and 616 on one tank (not 681).
- **Nature's Splendor.** It needs 11 Balance points. The DoubleZug sheet values use it. Without it, the Druid gives 747 in raids and 626 on one tank. The model also increases its healing power bonus with the duration. Without this, the Druid gives 826 and 656.
- **Critical heals over time.** The values use critical ticks for all heals over time, as in Forever. With the Classic rule (no critical ticks), the proposed Paladin is −1% to +6% against the Shaman and 4–16% below the Druid in raids. On one tank, it is 4–11% above the best other healer.
- **Spirit regeneration.** The Classic formulas give the Priest the most regeneration. Forever can use a different formula (see Open questions).
- **Overhealing.** The values are estimates. They change with the raid, the damage and the healer assignments.
- **Light's Vigil.** Only one Light's Vigil for each party can be active. The model gives the Paladin a full party of 5. With fewer players near the target, the heal is less.
- **Builds.** Analysis, Builds uses the first version of this model (with the Classic big heals of the other classes). Its values compare Paladin builds only. Thus, this comparison with the other healers does not change them.
