# Healing

This section compares the Holy Paladin with the three other healers of Forever: Priest, Druid and Shaman. It uses all the Forever heals of each class, not only the big heals. It also checks C3 in PvP. The design goal of Holy is a healer for long fights and the best single-target healer.

## Summary

- **In the beta, the Holy Paladin is the weakest raid healer.** It heals 12–15% less than the lowest other healer, and 37–43% less than the Priest (part 4).
- **The cooldown heals make the difference.** For the other healers, a cooldown heal is the most efficient spell: Prayer of Mending, Riptide, Swiftmend and Tranquility. For the Paladin, Holy Shock and Light's Vigil are the least efficient spells (part 3).
- **The Paladin also has the least mana.** Reverence keeps 30% of the Spirit regeneration while casting. Meditation, Reflection and Mindfulness keep 50% (part 2).
- **On one tank, the beta Paladin is about equal to the best other healer** (−6% to +2%) (part 5).
- **With the proposals, the Paladin is about equal to the Shaman in raids** (−5% to +1%). It is 1–13% below the Druid and 29–34% below the Priest. C1 gives the mana. C2, C19 and Conviction give larger heals (part 4).
- **After a large hit on one tank, the proposed Paladin heals 1–16% more than the best other healer in the first 3–6 sec.** C3 gives most of this result. In the beta, the Paladin is 3–23% below (part 5).
- **On one tank, the proposals put the Paladin 7–17% above the best other healer.** This is below the 20% limit of W14. Its maximum is 18% above the Shaman (part 5).
- **Heals over time can be critical heals in Forever.** This helps the Priest, the Druid and the Shaman. The Paladin has almost no heals over time. With the Classic rule, the proposed Paladin was 3–4% higher against each healer (part 8).
- **We withdrew C20.** Illumination at 75% is not necessary in raids, and it puts the lead on one tank at 13–23% (part 6).
- **A stronger Holy Shock or Light's Vigil is not necessary.** The raid healing is already at the level of the Shaman. A Holy Shock change also increases the lead on one tank (part 6).

## 1. Model

- **Source.** The model uses the method of the DoubleZug sheets for the four Forever healers (early beta). All classes use the same gear, buffs and fight. We compared each spell value with the Forever spellbook. An independent review of the first version found errors. This version corrects them (22 October 2026).
- **Gear.** 715 healing power, 315 Intellect, 249 Spirit, 40 mana each 5 sec, 4% spell critical chance. Parts 4 and 5 also use 900 healing power (raids).
- **Raid buffs.** Arcane Intellect, Mark of the Wild, Blessing of Kings and Divine Spirit give stats. Blessing of Wisdom, Mana Spring Totem and a mana oil give mana. An aura gives +3% spell critical chance. Thus, each healer has 117 mana each 5 sec.
- **Consumables and other healers.** One major mana potion each 2 min (1,800 mana). One Mana Tide Totem each 5 min (1,160 mana) for each healer. A potion or a cooldown counts only if it ends before the end of the fight. Thus, the healer uses 2 potions in 3 min and 5 potions in 10 min.
- **Mana pool.** Classic base mana at level 60, plus 15 mana for each point of Intellect. The DoubleZug sheets do not add the base mana.
- **Spirit regeneration.** The Classic 1.12 formula of each class. Forever did not publish a formula. The DoubleZug tests agree with neither the Classic nor the TBC formula.
- **Talents.** Each class uses the healer build of its DoubleZug sheet. The beta Paladin has Divine Intellect, Healing Light 3/3, Reverence 3/3, Illumination 5/5 and Infusion of Light 2/2. It also has Divine Favor, Holy Shock, Holy Power 5/5, Light's Vigil and Benediction 5/5. Blessing of Light is on the target.
- **Proposed Paladin.** C1, C2, C3, C19, C21 and Conviction (C15, M8), as in build HB1. Illumination stays at 50% (we withdrew C20).
- **Cast plan.** A linear program finds the best mix of casts for the mana and the time of the fight. The mix can use all heals of the class. After 5 sec with no cast, the full Spirit regeneration starts. The model counts 2/3 of the time with no cast as full regeneration.
- **Critical heals.** Direct heals can be critical heals. In Forever, each tick of a heal over time can also be a critical heal ([Warcraft Tavern](https://www.warcrafttavern.com/forever/guides/restoration-druid/)). The model gives each tick the critical chance of the class (×1.5). Lingering Light (C2) cannot be a critical heal (its text). Swiftmend is a direct heal.
- **Raid and one tank.** "Raid" counts all heals on all targets. "One tank" counts only the heals on the tank: one target of Prayer of Mending, Wild Growth, Tranquility, Healing Stream Totem and Light's Vigil. Only one Rejuvenation and one Renew at a time. A Riptide or a Regrowth stays for its full duration, or the healer casts it again before the end.
- **Overhealing (DoubleZug values).** Flash of Light 15%, Holy Light 20%, Holy Shock 15%, Light's Vigil 25%, the Lingering Light heal (C2) 50%. Prayer of Mending 15%. Renew, Greater Heal, Binding Heal and Penance 25%. Regrowth and Rejuvenation 25%, Swiftmend 20%, Tranquility 40%, Wild Growth 50%. Riptide and Chain Heal 25%, Healing Wave 20%, Healing Stream Totem 50%.
- **Light's Vigil.** Rank 3: 1,340 mana. The next Holy Shock heals each party member for 684–724. The Illumination text names Light's Vigil. The model uses one Illumination return for each cast if one of the 5 heals is critical. It uses a coefficient of 15%, and no Holy Power or Healing Light bonus. No player test gives these values.
- **Other rules.** Binding Heal: 2 casts each min, because half of it heals the Priest (DoubleZug). Swiftmend does not remove the heal over time that it uses: the Forever text does not have the word "Consumes" of the Classic text.
- **Corrections to the DoubleZug sheets.**
  - Druid: Rejuvenation rank 11 heals 776 in 12 sec (sheet: 812 in 15 sec). Regrowth heals 994 over time (sheet: 1,278).
  - Druid: the sheet gives 6 free Wild Growth casts from Omen of Clarity. The model gives none, because Omen of Clarity needs melee hits (part 8).
  - Priest: Prayer of Mending can also be a critical heal. Druid: Swiftmend can also be a critical heal.
  - Shaman: one Mana Tide Totem (sheet: two) and 715 healing power (sheet: 700).
  - Paladin: Holy Light 1,580 and Flash of Light 308 (sheet: 1,609 and 316).
- **Not in the model.** Power Word: Shield and Divine Aegis absorbs, the armor from Inspiration and Ancestral Healing, Lay on Hands and Nature's Swiftness.

## 2. Mana for each healer

Mana for the full fight: mana pool, mana each 5 sec, Spirit regeneration while casting, potions, Mana Tide Totem and class tools. Time with no cast gives more.

| Healer | Mana pool | Spirit regeneration while casting (mana per sec) | 3 min | 5 min | 10 min |
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
| Priest | Prayer of Mending (5 targets, 10 sec): 18.5 · 15.7. Penance (12 sec): 7.2 · 5.4 | Binding Heal 8.2 · 6.1. Renew 7.2 · 5.4. Greater Heal 6.0 · 4.5. Prayer of Healing 5.2 · 3.4. Flash Heal 4.1 · 3.1 |
| Druid | Tranquility (2 min): 11.9 · 7.2. Swiftmend (15 sec): 7.4 · 6.0. Wild Growth (6 sec): 5.1 · 2.5 | Regrowth 6.9 · 5.1. Rejuvenation 5.4 · 4.1. Healing Touch 4.7 · 3.8 |
| Shaman | Healing Stream Totem: 160 · 80. Riptide (6 sec): 7.8 · 5.8 | Chain Heal (2.5 targets, on a Riptide target) 7.4 · 5.5. Healing Wave 6.0 · 4.8. Lesser Healing Wave 4.1 · 3.5 |
| Paladin, beta | Divine Favor and Holy Light (2 min): 10.7 · 8.6. Light's Vigil and Holy Shock (6 sec): 4.6 · 3.5. Holy Shock (10 sec): 3.3 · 2.8 | Flash of Light 7.1 · 6.0. Holy Light 5.1 · 4.1 |
| Paladin, proposed | Divine Favor and Holy Light: 12.5 · 9.4. Light's Vigil and Holy Shock: 5.5 · 4.1. Holy Shock: 4.3 · 3.6 | Flash of Light 7.8 · 6.4. Holy Light 5.6 · 4.4 |

- The filler heals are about equal: Flash of Light (beta) 7.1, Renew 7.2, Regrowth 6.9 and Chain Heal 7.4 raw healing per mana.
- The other healers cast their cooldown heals each time that they are ready. In fights of 3 min, Prayer of Mending gives 43% of the Priest healing. Riptide gives 47% of the Shaman healing. Swiftmend and Tranquility give 21% of the Druid healing.
- Holy Shock and Light's Vigil are the least efficient Paladin spells, in the beta and with the proposals. The best play does not cast them.
- With the proposals, Flash of Light (7.8) is the most efficient Paladin heal after Divine Favor. Divine Favor is available only one time each 2 min.

## 4. Raid healing

Healing per sec after overhealing, all targets.

| Healer | 715: 3 min | 715: 5 min | 715: 10 min | 900: 3 min | 900: 5 min | 900: 10 min |
| --- | --- | --- | --- | --- | --- | --- |
| Priest | 948 | 846 | 769 | 1,053 | 938 | 851 |
| Druid | 769 | 620 | 543 | 819 | 660 | 578 |
| Shaman | 703 | 595 | 515 | 773 | 650 | 560 |
| Paladin, beta | 600 | 516 | 436 | 657 | 570 | 481 |
| Paladin, proposed | 669 | 583 | 505 | 742 | 653 | 568 |

- The Priest, the Druid and the Shaman spend all their mana before the end of the fight. Thus, their healing per mana and their mana decide the result.
- In the beta, the Paladin is 12–15% below the lowest other healer.
- With the proposals, the Paladin is −5% to +1% against the Shaman and −13% to −1% against the Druid. It is still 29–34% below the Priest. The cause is Prayer of Mending (part 8).
- After the Priest, the Druid heals the most. It casts Innervate on itself, and its heals over time can be critical heals.
- The proposed Paladin casts Flash of Light, Holy Light after some Infusion of Light triggers, and Divine Favor. It does not cast Holy Shock or Light's Vigil. In fights of 10 min, it also runs out of mana.

## 5. One tank

Healing per sec after overhealing, on one tank. "Maximum" is the raw healing per sec for 30 sec, with no mana limit and all cooldowns ready.

| Healer | 715: 3 min | 715: 5 min | 715: 10 min | 900: 3 min | 900: 5 min | 900: 10 min | Maximum, 715 | Maximum, 900 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Priest | 586 | 499 | 434 | 630 | 537 | 468 | 1,202 | 1,288 |
| Druid | 624 | 516 | 461 | 674 | 558 | 500 | 1,249 | 1,342 |
| Shaman | 604 | 506 | 435 | 650 | 545 | 467 | 1,269 | 1,367 |
| Paladin, beta | 600 | 516 | 436 | 657 | 570 | 481 | 1,261 | 1,328 |
| Paladin, proposed | 669 | 583 | 505 | 742 | 653 | 568 | 1,493 | 1,607 |

- In the beta, the Paladin is about equal to the best other healer (−6% to +2%). Its maximum is about equal to the Shaman.
- With the proposals, the Paladin is first by 7–10% in fights of 3 min, and by 9–17% in fights of 5 and 10 min. Its maximum is 18% above the Shaman.
- The proposals give more mana (C1) and larger heals (C2, C19, Conviction). The lead increases with the fight length. The other healers must stop and wait for more mana.
- This is below the 20% limit of W14. If tests show more than 20%, Healing Light at 25% gives 3–13% (part 6).

**Holy Light in the model.** The values above count all healing on the tank as equal. Thus, the model casts Holy Light only after Infusion of Light or with Divine Favor. Holy Light gives about 30% of the healing in fights of 3 min and 6% in fights of 10 min. The other heals are Flash of Light, because it gives more healing for each mana point (7.8 against 5.6). In play, a Paladin casts more Holy Light after a large hit. The table below shows this value.

**Recovery after a large hit.** Healing that lands on the tank in the first 3 and 6 sec after the hit, at 715 healing power. The healer heals the tank before the hit. Thus, the Paladin cast Flash of Light before the hit. Infusion of Light is then often active: always with C3, and 88% of the time in the beta. The Druid has a Rejuvenation on the tank, and Swiftmend is ready. Only heals cast after the hit count. There is no overhealing. Heals over time count only the ticks in the window. The long cooldowns are Divine Favor, Nature's Swiftness and Inner Focus.

| Healer | 3 sec | 6 sec | 3 sec, no long cooldown | 6 sec, no long cooldown | Best casts (6 sec, no long cooldown) |
| --- | --- | --- | --- | --- | --- |
| Priest | 3,281 | 6,741 | 2,945 | 6,405 | Flash Heal, Greater Heal, Penance |
| Druid | 5,157 | 8,361 | 3,884 | 7,337 | Regrowth, Swiftmend, Healing Touch |
| Shaman | 4,425 | 7,715 | 3,036 | 6,071 | Healing Wave, Healing Wave |
| Paladin, beta | 4,184 | 8,139 | 3,059 | 7,013 | Holy Light (Infusion of Light), Flash of Light, Holy Light |
| Paladin, proposed | 5,235 | 9,678 | 4,052 | 8,186 | Holy Light (1.5 sec), Holy Shock, Holy Light (1.5 sec), Flash of Light |

- In the beta, the Paladin is 19–23% below the best other healer after 3 sec, and 3–6% below after 6 sec. Its first Holy Light is often fast, but the second needs a new critical heal.
- With the proposals, the Paladin is first: +1% to +4% after 3 sec, and +12% to +16% after 6 sec.
- Each Flash of Light or Holy Shock makes the next Holy Light a 1.5 sec cast (C3). Thus, the Paladin opens with Holy Light. Then Holy Shock or Flash of Light prepares the next Holy Light.
- C3 gives most of this result. Without C3, the proposed Paladin heals 10–24% less.
- The Druid is the best other healer: Swiftmend uses the Rejuvenation on the tank, and Nature's Swiftness makes Healing Touch instant.
- At 900 healing power, the result is almost the same.
- Power Word: Shield is not in the table. It absorbs about 1,100 damage and uses one global cooldown.

## 6. Options and changes examined

**The lead on one tank.** Each value range covers 715 and 900 healing power, and fights of 3, 5 and 10 min.

| Option | Raid, against the Shaman | Raid, against the Druid | Raid, against the Priest | One tank, against the best other healer |
| --- | --- | --- | --- | --- |
| The proposals (Healing Light 30%, Illumination 50%) | −5% to +1% | −13% to −1% | −29% to −34% | +7% to +17% |
| Healing Light 35% (withdrawn) | −1% to +5% | −10% to +3% | −27% to −32% | +11% to +22% |
| Healing Light 25% | −9% to −2% | −16% to −5% | −32% to −37% | +3% to +13% |
| Healing Light 20% | −12% to −6% | −20% to −9% | −35% to −39% | −1% to +8% |
| C20: Illumination 75% (withdrawn) | +5% to +9% | −4% to +6% | −22% to −29% | +13% to +23% |

- The proposals put the Paladin at the level of the Shaman in raids, 1–13% below the Druid, and first on one tank by 7–17%.
- C20 adds 8–10% in raids and 6% on one tank. The lead on one tank is then 13–23%: more than the W14 limit in long fights. Thus, C20 stays withdrawn.
- If the lead on one tank is too large in tests, Healing Light at 25% gives 3–13% (W14).

**Changes to Holy Shock and Light's Vigil.** With the proposals.

| Change | Raid, against the Shaman | Raid, against the Priest | One tank, against the best other healer |
| --- | --- | --- | --- |
| None | −5% to +1% | −29% to −34% | +7% to +17% |
| Holy Shock heals ×2 | +3% to +8% | −23% to −31% | +15% to +25% |
| Holy Shock heals ×2.5 | +11% to +15% | −18% to −25% | +22% to +34% |
| Holy Shock costs 50% less | −1% to +6% | −26% to −31% | +10% to +20% |
| Light's Vigil heals ×1.25 | −2% to +1% | −27% to −34% | +7% to +17% |
| Light's Vigil heals ×2 | +20% to +30% | −3% to −21% | +7% to +17% |
| Light's Vigil costs 50% less | +44% to +61% | +3% to +10% | +7% to +17% |
| Illumination returns mana for each critical heal of Light's Vigil (up to 5 for each cast) | −2% to +2% | −25% to −34% | +7% to +17% |
| The same, with Illumination at 75% (C20) | +53% to +78% | +13% to +20% | +13% to +23% |
| Light's Vigil coefficient 0% or 30% | −5% to +1% | −29% to −34% | +7% to +17% |

- A change to Holy Shock or Light's Vigil is not necessary: the raid healing is already at the level of the Shaman.
- Each Holy Shock change also increases the lead on one tank. With Holy Shock ×2, the lead is 15–25%: more than the W14 limit.
- With Illumination at 50%, the best play does not cast Light's Vigil. Thus, its two values with no test (coefficient, number of Illumination returns) change the raid result by 5% or less.
- The cost of Light's Vigil is sensitive: at 50% less, the Paladin is 44–61% above the Shaman.
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

- **Without C3, the hybrid Paladin has no good fast heal.** Flash of Light heals half of Lesser Healing Wave. A 2.5 sec Holy Light is easy to interrupt.
- **With C3, the Paladin heals about 2,230 in 3 sec** (Holy Light after Holy Strike, then Flash of Light). Two Lesser Healing Waves heal about 1,860. The Paladin cannot do this again before the next Holy Strike.
- **Mana is the main limit.** A Retribution Paladin with about 4,000 mana can cast 5–6 Holy Light. Then it has no mana for Seals and Judgement. A 7-point dip with Infusion of Light has no points for Reverence.
- **Players can stop it.** Kick, Pummel and Earth Shock interrupt the cast. Mortal Strike and Wound Poison decrease the heal by 50%. Spiritual Focus is in row 2. Concentration Aura gives only 35% pushback resistance.
- **It costs damage.** Each heal uses a global cooldown in which the Paladin does not attack.
- **Combinations.** Hammer of Justice or Repentance, then Holy Strike, then a 1.5 sec Holy Light gives a free heal of about 1,800. The beta already lets the Paladin cast Holy Light during Divine Shield.

## 8. Limits

The values in brackets are for a raid fight of 3 min at 715 healing power.

- **Prayer of Mending.** The model gives it 5 targets with 15% overhealing. It gives 43% of the Priest healing. With 3 targets, the Priest gives 786, not 948. The Priest is then about equal to the Druid.
- **Omen of Clarity.** With 2 free Wild Growth casts each minute, the Druid gives 855, not 769.
- **Mana Tide Totem.** With two Mana Tide Totems, the Shaman gives 736, not 703.
- **Swiftmend.** If it removes the heal over time that it uses, the Druid gives 756 in raids (not 769) and 587 on one tank (not 624).
- **Critical heals over time.** The values use critical ticks for all heals over time, as in Forever. With the Classic rule (no critical ticks), the proposed Paladin is −2% to +4% against the Shaman and −9% to +3% against the Druid in raids. It is first on one tank by 10–21%.
- **Spirit regeneration.** The Classic formulas give the Priest the most regeneration. Forever can use a different formula (see Open questions).
- **Overhealing.** The values are estimates. They change with the raid, the damage and the healer assignments.
- **Light's Vigil.** Only one Light's Vigil for each party can be active. The model gives the Paladin a full party of 5. With fewer players near the target, the heal is less.
- **Builds.** Analysis, Builds uses the first version of this model (with the Classic big heals of the other classes). Its values compare Paladin builds only. Thus, this comparison with the other healers does not change them.
