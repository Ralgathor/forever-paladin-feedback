# Healing

**Question.** How well does the Holy Paladin heal against the other healers of Forever: Priest, Druid and Shaman?

The design goal of Holy is a healer for long fights and the best healer on one target. It does not need to be the best raid healer. Three Holy talent proposals stay: Reverence 25/50% (C-H1), Light's Vigil (C-H7) and Oath of Light 30% (C-H8). The other values are for the live Holy Paladin.

All values are healing each sec after overhealing, at 715 healing power, from the healing model. A critical heal heals for 175% (Holy Power 5/5, main hypothesis since 3 November). All healers have the same gear. Part 10 gives each healer a set from the level 60 item pool.

**Review of 24 November 2026.** A check against the DoubleZug healer sheets (November 2026) and the game data of wowsims Forever corrected two model inputs. Spirit regeneration now uses the Forever formula (6.25 + Spirit/8 mana each sec, all classes), not the Classic formulas. Wild Growth now uses the game files. The Druid gains 5–8%, and the Paladin 1–3%. Against the Druid, the Paladin is 1–3 points lower.

The Druid, Shaman and Priest values use the development notes of 2 November 2026. Druid: Gift of the Earthmother is removed, Bloom (new) takes its place, Genesis gives 10% (was 5%), Wild Growth has a 3 sec base cast. Shaman: Riptide has no direct heal, a 12 sec cooldown (was 6 sec) and a 40% lower mana cost. Priest: Binding Heal is removed. The game files of client 1.60.1.70755 (3 November 2026) do not have these changes yet.

## Short answer

- **On one tank, the Druid is first.** The Paladin is 10–16% below the Druid. It is 10–14% above the Shaman and the Priest. This is not the design goal of Holy (W14).
- **After a large hit on the tank, the Druid is first with all cooldowns:** the Paladin is 8% below in the first 3 sec. With short cooldowns only, the Paladin is first: 11% above the Druid.
- **In raids, the Paladin is the weakest healer:** 40–43% below the Druid, 18–19% below the Shaman and 39–45% below the Priest. Light's Vigil (C-H7) gives the raid healing.
- **Why the Paladin is weak in raids.** Oath of Light helps only one ally. The Priest has Prayer of Mending. The Druid has Bloom and Genesis on each heal over time.
- **Why the Druid gains.** Bloom heals for 100% of Spirit each time a Rejuvenation or Regrowth ends, and Genesis now gives +10%. These gains are larger than the loss of Gift of the Earthmother.
- **The Paladin has the least mana.** Reverence keeps only 30% of the Spirit regeneration during casts. The other healers keep 50%. Reverence 50% (C-H1) gives the same 50%.
- **The results use the 175% hypothesis.** Holy Power can change them. At 225%, the Paladin is 0–7% below the Druid on one tank. A live test must give the real value (Open items).
- **Light's Vigil (C-H7) is the raid proposal (3 November).** A Holy Shock with the buff also heals the party for 60% of the heal, once each 6 sec. Raid: +22 to +30 points. With Reverence 50% (C-H1), the Paladin is 7–8% below the Druid in raids of 5 and 10 min. No change on one tank.
- **Reverence 50% (C-H1) is the Holy proposal for mana (2 November).** It gives +4 to +6 points in raids. On one tank, the Paladin is then 5–8% below the Druid. It has no link to critical heals. Lingering Light (C-H2) is withdrawn.
- **Oath of Light 30% (C-H8) is the one-tank proposal (3 November).** It gives 30% to Holy Light, Flash of Light and Holy Shock on the Oath target, in place of the flat values. With Reverence 50% and Light's Vigil, the Paladin is 0–4% above the Druid on one tank. No change in raids. At 225%, the value is 20%.
- **The same gear is not neutral (part 10).** In sets from the level 60 item pool, the Druid has 896 Spirit. The Druid uses Spirit for regeneration, Innervate and Bloom. The Paladin is limited by cast time, not by mana. Then the live Paladin is 58–62% below the Druid in raids and 27–33% below on one tank. With the three Holy proposals: 36–41% and 13–19% below.

## 1. Raid healing

All heals on all targets.

| Healer | 3 min | 5 min | 10 min | 3 min, 900 healing power | 5 min, 900 | 10 min, 900 |
| --- | --- | --- | --- | --- | --- | --- |
| Priest | 938 | 836 | 759 | 1,046 | 931 | 845 |
| Druid | 1,004 | 809 | 715 | 1,058 | 853 | 754 |
| Shaman | 701 | 592 | 512 | 793 | 670 | 579 |
| Paladin, beta of 18 October | 624 | 541 | 462 | 683 | 597 | 511 |
| **Paladin, live version** | **571** | **487** | **416** | **633** | **547** | **468** |

- **The Paladin is last in raids.**
- **It is 9–10% below the beta of 18 October.** Blessing of Light is gone, and a 175% critical heal does not give the loss back.
- **The Paladin casts mostly Flash of Light,** and Divine Favor with Holy Light each 2 min. In fights of 3 min, it also casts about 5 Light's Vigil. Its mana is empty before the end of fights of 3 and 5 min.
- **Oath of Light is not a raid tool.** With Oath of Light on all heals (not possible in the game), the Paladin is still 3–5% below the Shaman.

## 2. One tank

Only the heals on the tank. The tank has Oath of Light. "Maximum" is the raw healing each sec for 30 sec, with no mana limit and all cooldowns ready.

| Healer | 3 min | 5 min | 10 min | 3 min, 900 | 5 min, 900 | 10 min, 900 | Maximum | Maximum, 900 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Priest | 605 | 510 | 441 | 648 | 548 | 474 | 1,289 | 1,375 |
| Druid | 758 | 645 | 591 | 817 | 697 | 639 | 1,312 | 1,412 |
| Shaman | 605 | 508 | 436 | 654 | 549 | 472 | 1,224 | 1,322 |
| Paladin, beta of 18 October | 624 | 541 | 462 | 683 | 597 | 511 | 1,279 | 1,347 |
| **Paladin, live version** | **666** | **578** | **494** | **729** | **638** | **546** | **1,368** | **1,441** |

- **The Druid is first in all fight lengths** (Paladin −10% to −16% at 715, −9% to −15% at 900). The goal (W14) is the best single-target healer, with a lead of 20% or less.
- **The Paladin mana is the limit,** most in fights of 10 min. Reverence 50% (C-H1) decreases the gap to 5–8%. With Reverence 50% alone, the Druid stays first.
- **The Paladin maximum is the highest:** 2–4% above the Druid.
- **The cast plan is almost only Flash of Light,** with Divine Favor and Holy Light each 2 min.
- **Oath of Light 30% (C-H8)** with Reverence 50% gives 771 / 674 / 594 (Druid 758 / 645 / 591): 0–4% above the Druid. At 900 healing power, it is 4–8% above. The maximum is 1,493. See part 7.

## 3. Recovery after a large hit

The healing on the tank in the first 3 and 6 sec after a large hit, with no overhealing. "Long cooldowns" are Divine Favor, Nature's Swiftness and Inner Focus.

Before the hit, each healer heals the tank as usual. Thus, its heals over time are already on the tank at the hit: Renew, Rejuvenation, Regrowth, Riptide and Healing Stream Totem.

| Healer | 3 sec | 6 sec | 3 sec, no long cooldown | 6 sec, no long cooldown | 3 sec, 900 | 6 sec, 900 |
| --- | --- | --- | --- | --- | --- | --- |
| Priest | 3,932 | 7,416 | 3,569 | 7,052 | 4,193 | 7,905 |
| Druid | 6,424 | 10,198 | 3,904 | 7,678 | 6,981 | 11,031 |
| Shaman | 4,750 | 8,054 | 3,361 | 6,664 | 5,119 | 8,689 |
| Paladin, beta of 18 October | 5,024 | 8,232 | 3,947 | 7,155 | 5,337 | 8,745 |
| **Paladin, live version** | **5,940** | **9,339** | **4,346** | **7,744** | **6,297** | **9,891** |

- **With all cooldowns, the Druid is first:** the Paladin is 8% below the Druid after 3 sec and after 6 sec. Divine Favor and Holy Light with Oath of Light heal for about 4,900.
- **With short cooldowns only, the Paladin is first:** 11% above the Druid after 3 sec, 1% after 6 sec. Without Gift of the Earthmother, Rejuvenation and Swiftmend use the full 1.5 sec global cooldown. Bloom does not help in 6 sec.
- **The Paladin is 16% or more above the Shaman and the Priest** after 6 sec, with all cooldowns.
- **At 225%,** the Paladin is first with all cooldowns: 16% above the Druid after 3 sec, 10% after 6 sec.
- **Oath of Light 30% (C-H8), 175%:** 6,334 / 10,034 with all cooldowns (1–2% below the Druid) and 4,595 / 8,294 with short cooldowns only (18% and 8% above the Druid).
- Power Word: Shield is not in the table. It absorbs about 1,100 damage.

## 4. Mana

The mana for a full fight: mana pool, MP5, Spirit regeneration during casts, potions, Mana Tide Totem and class tools.

| Healer | Mana pool | Spirit regeneration during casts (each sec) | 3 min | 5 min | 10 min |
| --- | --- | --- | --- | --- | --- |
| Priest | 7,486 | 24.1 | 20,800 | 28,304 | 47,321 |
| Druid (Innervate on itself) | 7,534 | 27.2 | 26,316 | 34,194 | 59,054 |
| Shaman | 7,810 | 24.1 | 21,124 | 28,628 | 47,645 |
| Paladin | 7,802 | 14.5 | 19,380 | 25,724 | 41,847 |

- **The Paladin has the least mana:** 7% less than the Priest and 26% less than the Druid in fights of 3 min.
- **Spirit regeneration** uses the Forever formula: 6.25 + Spirit/8 mana each sec, the same for all classes (wowsims Forever). All healers have 336 Spirit, the Druid 386 (Living Spirit).
- **The cause is Reverence.** It keeps 30% of the Spirit regeneration during casts. Meditation, Reflection and Mindfulness keep 50%. Reverence 50% (C-H1) fixes this.
- In raids, a Druid often gives Innervate to a Priest. The table gives it to the Druid.

## 5. Healing for each mana point

Two values for each spell: raw healing for each mana point · healing for each mana point after overhealing.

| Healer | Cooldown heals | Other heals |
| --- | --- | --- |
| Priest | Prayer of Mending: 18.5 · 15.7 | Renew 7.2 · 5.4. Greater Heal 6.5 · 4.9. Prayer of Healing 5.2 · 3.4. Flash Heal 4.1 · 3.1 |
| Druid | Tranquility: 11.9 · 7.2. Swiftmend: 9.2 · 7.4. Wild Growth: 6.3 · 3.2 | Regrowth with Bloom 8.6 · 6.5. Rejuvenation with Bloom 8.3 · 6.2. Healing Touch 4.7 · 3.8 |
| Shaman | Healing Stream Totem: 160 · 80. Riptide: 7.0 · 5.3 | Chain Heal 7.5 · 5.6. Healing Wave 6.0 · 4.8. Lesser Healing Wave 4.1 · 3.5 |
| Paladin, raid (no Oath) | Divine Favor and Holy Light: 10.5 · 8.4. Light's Vigil and Holy Shock: 5.5 · 4.2. Holy Shock: 4.8 · 4.1 | Flash of Light 6.6 · 5.6. Holy Light 4.7 · 3.8 |
| Paladin, tank with Oath | Divine Favor and Holy Light: 12.5 · 10.0. Light's Vigil and Holy Shock: 5.4 · 4.1. Holy Shock: 4.4 · 3.8 | Flash of Light 7.8 · 6.6. Holy Light 5.7 · 4.5 |
| Paladin, tank with Oath of Light 30% (C-H8) | Divine Favor and Holy Light: 13.6 · 10.9 | Flash of Light 8.5 · 7.3. Holy Light 6.2 · 4.9 |

- **On the tank, Flash of Light** heals 7.8 for each mana point. The Druid heals over time give 8.3–8.6 with Bloom. With Oath of Light 30% (C-H8), Flash of Light gives 8.5.
- **In raids, Flash of Light (6.6) is about equal** to Greater Heal and Healing Wave. Chain Heal (7.5) and the Druid heals over time (8.3–8.6 with Bloom) cost less for each heal. The Priest also has a strong cooldown heal: in fights of 3 min, Prayer of Mending gives 43% of the Priest healing. Swiftmend gives 12% of the Druid healing.
- **Riptide is now weaker.** It has no direct heal. In raids, the Shaman cast plan uses Chain Heal and no Riptide.
- **Divine Favor and Holy Light** is the most efficient Paladin heal, but only once each 2 min.

## 6. Holy Power: 175%, 200% or 225%

The Holy Power text says: "increases the critical heal bonus of Holy spells by 50%". A normal critical heal heals for 150%. The text has three possible meanings:

- **175% (main hypothesis since 3 November):** +50% of the bonus, the rule of Ruin and Elemental Fury. This is the general view of the players.
- **200% (main hypothesis from 1 to 2 November):** +50 points on 150%.
- **225% (main hypothesis on 2 November):** ×1.5 on the full critical heal. This is the wowsims value.

**Why the three cases.** The game files give Holy Power the aura A_MOD_CRITICAL_HEALING_AMOUNT (+10/20/30/40/50%). No other spell in the Forever files has this aura. All other talents that change the critical size use the critical damage bonus modifier. Examples: Ruin, Elemental Fury, Ice Shards, Arcane Mind, Shadowform, Impale, Lethality, Mortal Shots and Vengeance. They give +100% of the bonus: a 200% critical hit.

- **For 175%.** The tooltip says "critical strike healing bonus". With the Ruin rule and +50%, this gives 175%. The players agree on this value (3 November).
- **For 225%.** The designers did not use the usual modifier. In later game versions, the server multiplies the full critical heal by this aura. wowsims does the same.
- **Against 200%.** It needs the Ruin modifier and +100%. The data has neither.

| Case | Raid against the Druid, 3 / 5 / 10 min | One tank against the Druid, 3 / 5 / 10 min |
| --- | --- | --- |
| **175% (main)** | **−43% / −40% / −42%** | **−12% / −10% / −16%** |
| 200% | −40% / −36% / −39% | −7% / −5% / −12% |
| 225% | −36% / −33% / −35% | −2% / −0% / −7% |

- **At 175% and at 200%,** the Druid is first on one tank in all fight lengths. The design goal is not reached (W14).
- **At 225%,** the Paladin is equal to the Druid on one tank in fights of 3 and 5 min. The Druid stays first in fights of 10 min.
- **The test (Open items):** take Holy Power 5/5, cast Divine Favor, then Holy Light on a target with no Oath of Light. Compare the heal with the tooltip average: 2 times is 200%, 2.25 times is 225%, 1.75 times is 175%.

## 7. Options examined

Reverence 50% (C-H1), Light's Vigil (C-H7) and Oath of Light 30% (C-H8) are proposals. The other options are withdrawn (see Withdrawn ideas). The values use 175%.

| Option | Raid against the Druid, 3 / 5 / 10 min | One tank against the Druid, 3 / 5 / 10 min |
| --- | --- | --- |
| Live version | −43% / −40% / −42% | −12% / −10% / −16% |
| **Reverence 50% (C-H1, proposal)** | **−39% / −35% / −36%** | **−7% / −5% / −8%** |
| **Light's Vigil (C-H7, proposal)** | **−21% / −13% / −12%** | **−12% / −10% / −16%** |
| **Reverence 50% and Light's Vigil (C-H1 and C-H7)** | **−18% / −8% / −7%** | **−7% / −5% / −8%** |
| **Oath of Light 30% (C-H8, proposal)** | **−43% / −40% / −42%** | **−4% / −2% / −9%** |
| **All three Holy proposals (C-H1, C-H7 and C-H8)** | **−18% / −8% / −7%** | **+2% / +4% / +0%** |
| Oath of Light 20% / 25% / 35%, with C-H1 and C-H7 | −18% / −8% / −7% | −6% / −4% / −7%, −2% / +0% / −3%, +6% / +8% / +4% |
| Lingering Light 2/2 (C-H2) | −40% / −36% / −39% | −7% / −6% / −12% |
| Reverence 50% and Lingering Light 2/2 | −36% / −32% / −33% | −2% / +1% / −3% |
| Boundless Light also +15% critical chance for Flash of Light | −37% / −32% / −32% | −12% / −10% / −16% |
| Flash of Light +30% critical chance | −31% / −24% / −22% | −12% / −10% / −16% |

- **C-H1 and C-H2 together** gave 20–25% above the Druid on one tank before the notes of 2 November, past the 20% limit. This was the reason to withdraw them on 31 October. With the notes of 2 November and the review of 24 November, they give 9–14% at 225%, and 3% below to 1% above at 175%.
- **Reverence 50% alone** gives −7% / −5% / −8% on one tank. At 225%, it gives +3% / +6% / +2%, below the limit (+4% / +8% / +4% at 900 healing power).
- **Lingering Light alone** gives about the same raid gain, but its value grows with the critical heal size. At 225% and at 175%, it gives +6–7 and +4–5 points on one tank. Reverence gives +5–9 and +5–8 points. Reverence has no link to critical heals, thus it is the proposal (decision of 2 November).
- **Boundless Light for Flash of Light** changes only the raid values, because the tank has Oath of Light.
- **Infusion of Light on all hits (C-H3)** adds nothing in the model, because the Paladin casts almost only Flash of Light.
- **Light's Vigil (C-H7)** gives +22 to +30 points in raids and no change on one tank. With Reverence 50%, the Paladin is 7–8% below the Druid in raids of 5 and 10 min, and 18% below in fights of 3 min. The party heal has 50% overhealing, as Wild Growth. With 3 stacks, the group burst is about 15,800 in 6 sec and 20,700 in 10 sec. Divine Favor on the first Holy Shock adds about 6%.
- **Oath of Light 30% (C-H8)** is the smallest value of the model that puts the Paladin at or above the Druid on one tank in all fight lengths at 175%. At 900 healing power, it gives +4% / +8% / +5%. At 225%, it gives +12% to +16% (900: +16% to +20%), at the 20% limit. Thus at 225%, the value is 20%: +3% to +7% (900: +7% to +11%). Oath of Light helps only one ally, thus the raid values do not change. Model: `models/beta-30-oct/oath_light_ch8.py`.
- **The party heal of 60% depends on 175%.** At 225%, a 60% party heal with Reverence 50% puts the Paladin 7–8% above the Druid in raids of 5 and 10 min. Then 35% gives 9% below the Druid. Model: `models/beta-30-oct/light_vigil_ch7.py`.

**Light's Vigil: options examined (3 November)**

The values are raid healing against the Shaman, 3 / 5 / 10 min, without Reverence 50%. The first five rows use 175% (live: −19% / −18% / −19%). The other rows use 225% (live: −8% / −7% / −9%): they were examined before the decision of 3 November. The C-H7 rows use 50% overhealing on the party heal, as Wild Growth.

| Option | Raid against the Shaman | Why not the proposal |
| --- | --- | --- |
| **Buff on Holy Shock, 6 sec, 3 stacks, party heal 60% (C-H7)** | **+13% / +19% / +23%** | Proposal |
| The same, party heal 35% / 50% | −2% / +1% / +3% and +7% / +12% / +15% | Smaller raid value. Decision of 3 November: 60% at 175% |
| The same, party heal 70% | +19% / +26% / +31% | With Reverence 50%, the Paladin is equal to the Druid in fights of 5 and 10 min (−3% / −1%) |
| The same, 8 sec cooldown, party heal 70% | +10% / +15% / +19% | Fewer and larger heals. Smaller value in fights of 3 min |
| Live spell, instant, 20 sec cooldown | +11% / +18% / +21% | Still two casts for one party heal |
| Light's Vigil releases your Seal on the party of an ally (Seal of Light: party heal) | +13% / +20% / +23% (15 sec cooldown) | Three Seals have no model. It consumes the Seal |
| Heal over time on the party, Holy Shock ends it for a burst | +22% / +20% / +18% (75% cost, 1.5 × the live heal) | Small changes in cost give large changes in value. Close to Swiftmend (Druid) |
| Stacks from heals on the Oath target, Holy Shock uses them (3 stacks) | +15% / +20% / +18% | The value depends on how much the Paladin heals one target (+5% to +29%) |
| Charges from critical heals, Judgement and Holy Strike (3 charges) | +20% / +22% / +21% (melee), +13% / +16% / +14% (ranged) | Critical heals give a random number of charges. Ranged Paladins receive 5–7% less |
| Charges as above, Holy Shock critical heals also give a charge | +23% / +22% / +22% (party heal 20%) | A loop: about 6 Holy Shocks from 3 charges. Holy Shock replaces Flash of Light |
| Live spell + your Holy damage heals the party of the target | about +10% | The value depends on spell damage from items. Close to a later-expansion healer |

## 8. Inputs of the model

**Gear and buffs**

- 715 healing power, 315 Intellect, 249 Spirit, 40 MP5, 4% spell critical chance. Parts 1 and 2 also give 900 healing power.
- Raid buffs give stats, mana and +3% spell critical chance. Each healer has 117 MP5.
- One major mana potion each 2 min (1,800 mana) and one Mana Tide Totem each 5 min (1,160 mana).
- Mana pool: Classic base mana plus 15 mana for each Intellect point. Spirit regeneration: 6.25 + Spirit/8 mana each sec for all classes (Forever, wowsims `sim/core/mana.go`). Before 24 November, the model used the Classic 1.12 formula of each class.

**Paladin build (38/5/8)**

- Holy: Healing Light 3/3 (+12%), Reverence 2/2, Illumination 5/5, Divine Favor, Holy Shock, Holy Power 5/5, Boundless Light 2/2, Light's Vigil, Purifying Power 1.
- Divine Intellect 5/5, Benediction 5/5, Conviction 3/3 (+6% critical chance). Base spell critical chance 3.5% (game files).
- Oath of Light on one ally: Holy Light +400, Flash of Light +115, Holy Shock +229. Oath of Light (C-H8): +30% to the three heals, on the full heal.
- Boundless Light 2/2: Holy Shock +30% critical chance on an ally with no Oath of Light.
- Light's Vigil rank 3: 1,340 mana. The next Holy Shock heals each party member for 684–724 (704 + 14.3% of healing power, game files at level 60).

**Other healers**

- Druid: Gift of Nature, Improved Rejuvenation, Genesis 5/5 (+10%), Improved Regrowth, Bloom (100% of 386 Spirit when a Rejuvenation or Regrowth ends), Nature's Splendor, Naturalist 5/5 (Wild Growth 2.5 sec). Wild Growth rank 3: 97 each sec for 7 sec on 5 targets, 6.6% of healing power each tick (game files). No Gift of the Earthmother: Rejuvenation and Swiftmend use the 1.5 sec global cooldown.
- Priest: Prayer of Mending, no Penance. Binding Heal is removed. Holy Binding heals only the Priest: the model does not count it.
- Shaman: Purification, Healing Way, Tidal Mastery. Riptide: no direct heal, 12 sec cooldown, 205 mana.

**Rules**

- **Cast plan.** A linear program finds the best mix of casts for the mana and the fight length.
- **Critical ticks.** In Forever, each tick of a heal over time can be a critical heal. The model gives each tick the critical chance of the class.
- **Raid and one tank.** "Raid" counts all heals. "One tank" counts only the heals on the tank.
- **Overhealing.** Flash of Light 15%, Holy Light 20%, Holy Shock 15%, Light's Vigil 25%, Light's Vigil (C-H7) party heal 50%, Prayer of Mending 15%, Renew, Greater Heal and Binding Heal 25%, Regrowth and Rejuvenation 25%, Swiftmend 20%, Tranquility 40%, Wild Growth 50%, Riptide and Chain Heal 25%, Healing Wave 20%, Healing Stream Totem 50%.
- **Not in the model.** Power Word: Shield, Divine Aegis, Inspiration, Ancestral Healing, Lay on Hands and Nature's Swiftness.

## 9. Method and limits

- **Source.** The model uses the method of the DoubleZug sheets for the Forever healers. Three reviews corrected it (22 October 2026). A check against the game files in wowsims Forever (23 October 2026) corrected the Paladin critical chance, Regrowth and Chain Heal. A check against the DoubleZug sheets of November 2026 and the wowsims game data (24 November 2026) corrected the Spirit regeneration and Wild Growth. The spell values of the model are the level 60 values of the game files. The DoubleZug sheets use the level 65 tooltip values (for example Holy Light 1,609, not 1,580): this adds 2–3% to the heals.
- **Scripts.** `models/healing/healing_model.py` (Priest, Druid, Shaman, solver; `NOTES_NOV2` gives the notes of 2 November), `models/beta-30-oct/healing_b2.py` (Paladin), `recovery_b2.py` (part 3), `holy_proposals_b2.py` (part 7), `healing_sens_b2.py` (parts 5, 6 and 9), `light_vigil_ch7.py` and `oath_light_ch8.py` (part 7), `pool_gear_b2.py` and `class_gear_b2.py` (part 10).
- **Holy Power** is the largest open question (part 6). The model uses 175%.
- **Prayer of Mending.** The model gives it 5 targets. With 3 targets, the raid Priest gives 777, not 938.
- **Omen of Clarity.** With 2 free Wild Growth casts each min, the raid Druid gives 1,106, not 1,004.
- **Mana Tide Totem.** With two totems, the raid Shaman gives 733, not 701.
- **Swiftmend.** A player test shows that it does not remove the heal over time. If it does, the Druid gives 993 in raids and 689 on one tank.
- **Nature's Splendor** needs 11 Balance points. Without it, the Druid gives 887 in raids and 710 on one tank.
- **Bloom.** The model gives Bloom to each Rejuvenation and Regrowth that ends at its full duration, with the critical chance of the Druid. The value of Bloom depends on the Spirit of the Druid (386 in the model, 896 in part 10).
- **Chain Heal** keeps the Riptide bonus of the DoubleZug sheet: 90% of the heals land on a Riptide target. The model keeps it also when the raid plan casts no Riptide. This gives the Shaman a little too much.
- **Classic tick rule.** With no critical ticks, the Paladin is 17–18% below the Shaman and 38–41% below the Druid in raids. On one tank, it is 8–14% below the Druid.
- **Overhealing** values are estimates. They change with the raid and the healer tasks.
- **Oath of Light.** The model puts all tank heals on the Oath target. With two tanks, only one has the Oath.
- **Oath of Light 30% (C-H8) and Healing Light.** The model multiplies the two: ×1.12 × 1.30 on the Oath target. If the game adds them (+42%), 30% has the value of 26.8%. The Paladin is then −1% / +2% / −2% against the Druid on one tank at 175% (900 healing power: +2% / +5% / +2%).
- **Light's Vigil.** The model gives the Paladin a full party of 5.
- **No wowsims check.** wowsims Forever has no Holy heal rotation and no Druid or Shaman heals. The earlier check (beta of 18 October) found the Paladin model within −4.3% to +5.3% of wowsims.

## 10. Gear from the item pool

Parts 1 to 9 give all healers the same gear. That gear has little Spirit (336). The Druid uses Spirit three times: regeneration, Innervate and Bloom. In raids, the Druid is limited by mana. The Paladin is limited by cast time: it casts all the fight. Thus more Spirit helps the Druid, and it does not help the Paladin.

This part gives each healer a set from the level 60 item pool, with the same rules for all. Model: `models/beta-30-oct/pool_gear_b2.py`.

- **Item pool.** The rules of the matched sets: launch items of item level 63 or less. No raid or world boss drop, no PvP item, no Revered or Exalted reputation reward. Armor and weapons by class. Enchants with the same rules. Dungeon set bonuses: 3 pieces +18 healing, 6 pieces +8 MP5.
- **Set choice.** A search slot by slot on the model value: the mean of raid and one tank healing in a fight of 5 min. The Paladin set uses the live talents.
- **Totals.** Base stats, talents and buffs from the game files (wowsims Forever), with the buffs and consumables of the DoubleZug profiles for all classes. Blessing of Kings ×1.10, the class Intellect talent ×1.10, Dark Inspiration ×1.15 Spirit. Druid: Living Spirit ×1.15 Spirit, Mystic Mushroom ×1.05 Spirit (idol). Insight: ×1.20 Spirit (weapon enchant, mean). Brilliant Mana Oil gives 30 healing and 15 MP5 (game files).

| Class | Healing power | Intellect | Spirit | Critical chance | MP5 |
| --- | --- | --- | --- | --- | --- |
| Paladin | 762 | 375 | 356 | 20.8% (with Conviction) | 108 |
| Druid | 484 | 346 | 896 | 14.6% | 86 |
| Priest | 599 (769 with Spiritual Guidance) | 372 | 682 | 16.0% | 82 |
| Shaman | 759 | 385 | 430 | 21.8% | 99 |

| Slot | Paladin | Druid | Priest | Shaman |
| --- | --- | --- | --- | --- |
| Head | Living Crown | Living Crown | Virtuous Crown | Living Crown |
| Neck | Jeweled Amulet of Cainwyn | Jeweled Amulet of Cainwyn | Jeweled Amulet of Cainwyn | Jeweled Amulet of Cainwyn |
| Shoulder | Justice Epaulets | Grovekeeper Pauldrons | Pauldrons of Conviction | Spiritcaller Epaulets |
| Back | Hide of the Wild | Amplifying Cloak | Hide of the Wild | Hide of the Wild |
| Chest | Breastplate of Salvation | Embrace of the Wind Serpent | Truefaith Vestments | Embrace of the Wind Serpent |
| Wrist | Loomguard Armbraces | Bleak Howler Armguards | Wyrmthalak's Shackles | Loomguard Armbraces |
| Hands | Hands of the Exalted Herald | Feralheart Gauntlets | Virtuous Mitts | Hands of the Exalted Herald |
| Waist | Sash of Mercy | Caretaker's Cord | Penitent's Cinch | Sash of Mercy |
| Legs | Martyr's Legplates | Devout Skirt | Leggings of Conviction | Legplates of the Chromatic Defier |
| Feet | Justice Treads | Feralheart Sandals | Virtuous Sandals | Greaves of The Five Thunders |
| Finger | Fordring's Seal | Ring of Nature's Cycles | Ring of Nature's Cycles | Fordring's Seal |
| Finger | Rosewine Circle | The Postmaster's Seal | Fordring's Seal | Rosewine Circle |
| Trinket | Burst of Knowledge | Ankh of Life | Ankh of Life | Burst of Knowledge |
| Trinket | Mindtap Talisman | Lucky Shovelnose Tuft | Lucky Shovelnose Tuft | Uther's Strength |
| Weapon (two-hand) | Hammer of the Grand Crusader | Hammer of the Grand Crusader | Glowing Brightwood Staff | Glowing Brightwood Staff |
| Relic | none | Mystic Mushroom | Bonecreeper Stylus (wand) | none |
| Weapon enchant | +healing | Insight | Insight | +healing |

| Healer, item pool sets, 175% | Raid, 3 / 5 / 10 min | One tank, 3 / 5 / 10 min |
| --- | --- | --- |
| Druid | 1,378 / 1,133 / 1,055 | 878 / 757 / 719 |
| Priest | 978 / 893 / 829 | 654 / 574 / 516 |
| Shaman | 714 / 614 / 540 | 606 / 518 / 453 |
| **Paladin, live version** | **545 / 470 / 405** | **639 / 556 / 479** |
| Paladin, Light's Vigil (C-H7) | 778 / 689 / 621 | 639 / 556 / 479 |
| Paladin, C-H7 and Reverence 50% (C-H1) | 810 / 730 / 659 | 678 / 599 / 528 |
| Paladin, C-H7, C-H1 and Oath of Light 30% (C-H8) | 810 / 730 / 659 | 745 / 659 / 581 |

| Paladin against the Druid, item pool sets | Raid, 3 / 5 / 10 min | One tank, 3 / 5 / 10 min |
| --- | --- | --- |
| **Live version, 175%** | **−60% / −58% / −62%** | **−27% / −27% / −33%** |
| C-H7, 175% | −44% / −39% / −41% | −27% / −27% / −33% |
| C-H7 and C-H1, 175% | −41% / −36% / −38% | −23% / −21% / −27% |
| C-H7, C-H1 and C-H8, 175% | −41% / −36% / −38% | −15% / −13% / −19% |
| Live version, 225% | −56% / −54% / −58% | −20% / −19% / −27% |
| C-H7 and C-H1, 225% | −33% / −26% / −28% | −15% / −13% / −19% |

- **With gear from the item pool, the Druid is far ahead.** The live Paladin is 58–62% below in raids and 27–33% below on one tank. With the three Holy proposals: 36–41% below in raids and 13–19% below on one tank.
- **Insight.** The weapon enchant Insight (vendor) gives Spirit +100% for 10 sec. A spell cast has a 35% chance to start it, with a 45 sec cooldown. The model uses the mean uptime of 20%: Spirit ×1.20. The Druid and the Priest take it in place of the +healing weapon enchant (−100 healing power). The Paladin and the Shaman keep the +healing enchant.
- **The gap is 2–5 points smaller than with the DoubleZug profiles** (`class_gear_b2.py`: 61–64% below in raids, 31–38% on one tank). The Druid has almost the same Spirit (896, DoubleZug: 878). The Paladin set has more healing power (762, DoubleZug: 623).
- **The Paladin passes the Shaman** with Light's Vigil (C-H7) in raids: +9% to +15%. On one tank, the live Paladin is 2–7% below the Priest and 5–7% above the Shaman.
- **The Druid is limited by mana.** In raids of 5 min, it casts only Regrowth and does not cast for 108 sec. The Paladin does not cast for 11 sec. More healing power or more critical chance helps the Paladin. More Spirit helps the Druid.
- **Limits.** Other procs, use effects and relic effects on spells (librams, totems) are not counted. Some items are world drops (Jeweled Amulet of Cainwyn, Glowing Brightwood Staff, Sash of Mercy, Ankh of Life). The database has no source for Ring of Nature's Cycles. The Insight uptime is lower with fewer casts. A set for raids only can be different.
