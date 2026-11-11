# Beta test results

## Development notes of 2 November 2026

Blizzard published the development notes on 3 November 2026 ([Blizzard forums](https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-november-2/2360696/9)). They give all changes since 15 October. Most Paladin changes are the beta trees of 30 October (next section). Client build 1.60.1.70755 (hotfix push 113578, 3 November 2026) has the two Retribution changes. The other changes in this table are not in its game files yet. A test on the live realms must confirm them.

| Change in the notes | Game files (1.60.1.70755) | Result |
| --- | --- | --- |
| Two-Handed Weapon Specialization: +2/4/6% Holy and Physical damage | In the game files since build 70755 | With the Vengeance change: Retribution +3.5% in wowsims master commit d97252f2a (default set: 906 → 938 DPS, full buffs, 2 min; item pool set on commit 8298ab833: 910; on commit ae9b8c23a: 939; on commit 9f254e8d8, with the Windfury Totem rule: 841; the same on commit 3633d376a). This is about 94% of the pure average (W15) |
| Vengeance: stacks up to 5 times | In the game files since build 70755 | See the row above. On master of 1 November, the two test flags gave +8.3% (981 DPS). The game data of build 70755 gives less |
| Warrior: Defensive Stance +80% threat (was +30%), Defiance 7/13/20% (was 5/10/15%) | +30%, 15% | The live Paladin tank has 70% of the Warrior threat with the same gear in the model (was 101%), and 71–82% from fresh level 60 to Naxxramas. In wowsims master commit 3633d376a (hotfixes of 10 and 11 November), with item pool tank sets and tank consumables, it has 71% (W28, Analysis, Threat) |
| Druid: Bear Form and Dire Bear Form +115% threat (was +50%) | +50% | The live Paladin tank has 77% of the Druid threat with the same gear in the model (was 110%). In wowsims master commit 3633d376a, it has 70% |
| Druid: Gift of the Earthmother removed, Bloom (new), Genesis 10%, Wild Growth 3 sec cast | Earthmother, 5%, no Bloom | Holy on one tank: 1–5% above the Druid in fights of 3 and 5 min, 3–5% below in fights of 10 min (was 3–12% above). Raid: 25–34% below the Druid (was 18–26%) (W14, Analysis, Healing) |
| Shaman: Riptide has no direct heal, 12 sec cooldown, −40% mana | Direct heal, 6 sec | Holy in raids: 7–10% below the Shaman (was 8–13%). On one tank: 25–32% above |
| Priest: Binding Heal removed (Holy Binding in its place) | Binding Heal | Raid Priest −1% |
| Most other classes: more damage. Retribution has only the two changes above | — | wowsims master commit 6ee3c30f35 (4 November 2026) has the Warrior, Rogue and Hunter changes: the pure average goes from 770 to 812, and Retribution from 118% to 112%. Master commit 8298ab833 (later on 4 November) adds the Warlock patch of 3 November: the pure average is 809, Retribution stays at 112%. Master commit df57e2571 (6 November) adds 2,447 items and halves the Natural flasks. With a new item search, the pure average is 817 and Retribution 111%. Master commit ae9b8c23a (8 November) adds 362 pool items for a Paladin. With a new item search, the pure average is 861 and Retribution 109%. Master commit 9f254e8d8 (9 November) changes the Windfury Totem rule and adds 262 items. With a new item search, the pure average is 869 and Retribution 97%. Master commit 3633d376a (11 November) adds 464 items, for example Ironfoe. With a new item search, the pure average is 898 and Retribution 94%. The Mage changes are not in wowsims yet (W15) |
| Warrior: Slam 15 sec cooldown, Improved Slam −2.5/5 sec | — | Answers the Slam open question |

## Beta trees of 30 October 2026

Hotfix push 113554 (client build 1.60.1.70707) changes the three Paladin trees. Blizzard published the tree changes in the development notes of 3 November 2026 (Sources). The values come from the game files in wowsims Forever (branch `paladin/hotfix-113554-port`, 30 October 2026). Build 70755 (hotfix push 113578, 3 November 2026) keeps these trees. For the Paladin, it changes only Two-Handed Weapon Specialization, Vengeance and Holy Shield rank 4 (wowsims master, commit `d97252f2a`). The talent calculator shows these trees in Live mode.

The proposals now change these trees. The beta adopts six earlier proposals (see Overview). The tables after the model results give player tests of the beta of 18 October.

| Tree | Changes |
| --- | --- |
| Holy | New: Oath of Light (row 4) and Boundless Light (row 5). Removed: Voice of Truth. Holy Power now increases the critical heal bonus of Holy spells by 10–50%. Light's Vigil now heals only. Reverence (2 ranks, 15/30%) goes to row 2. Divine Precision (2 ranks, 4/8%) goes to row 4 with no requirement. Holy Conduit comes from Retribution. Divine Intellect goes to Protection. Unyielding Faith goes to Retribution |
| Protection | New: Stoicism (row 5) and Shieldsworn (row 7). Removed: Improved Seal of Fury and One-Handed Weapon Specialization. Holy Shield goes to row 5. Redoubt gives 6–30% block. Iron Creed has 3 ranks. Shield Specialization has 2 ranks. Swift Judgement is now a second Judgement with a 1 min cooldown. Toughness goes to row 3 |
| Retribution | New: Turn Evil (row 5) and Unsealed Wrath (row 7). Removed: Twist of Light and Instrument of Law. Conviction (3 ranks, 2/4/6%) now applies to all spells and attacks. Two-Handed Weapon Specialization goes to row 4. It increases all Physical damage and decreases threat. Champion of the Light has 5 ranks and decreases the cast time of Hammer of Wrath. Vindication does not increase your Attack Power now |
| Spells | Blessing of Light, Greater Blessing of Light, Salvation and Greater Blessing of Salvation are removed. Righteous Fury also increases all threat by 33%. The Judgement of Fury taunt lasts 3 sec (was 4 sec). Holy Shield rank 1 does 75 damage (was 110). Rank 4 (221 damage, 4 charges) is a level 60 spell since build 70755. Its mana cost is not in the data yet. Light's Vigil has a 40 yd range (was 20 yd) |

### Model results on the beta of 30 October

The models of the Analysis tabs ran again on the new trees, with no proposal. Healing build 38/5/8 and tank build 0/38/13. The scripts are in models/beta-30-oct in the repository.

| Role | Beta of 18 October | Beta of 30 October |
| --- | --- | --- |
| Holy, raid (715 and 900 healing power, 3–10 min) | 19–28% below the Druid | 18–26% below the Druid, 8–13% below the Shaman |
| Holy, one tank | 7–13% below the Druid | 3–12% above the Druid, with Oath of Light on the tank |
| Holy, after a large hit (3 and 6 sec, all cooldowns) | 18–20% below the Druid | 9–18% above the Druid |
| Protection threat, same gear for all tanks | 63% of the Warrior | 101% of the Warrior |
| Protection threat, fresh level 60 to Naxxramas | 65–74% of the Warrior | 102–118% of the Warrior (120–142% with Consecration) |
| Protection mana while it tanks, Blessing of Wisdom | +24 to +39 per sec | +15 to +37 per sec |
| Retribution damage (wowsims test runs) | 824 DPS | 848 DPS (+3%). After the wowsims update of 1 November: 906 DPS. With build 70755 (wowsims master commit d97252f2a): 938 DPS (default set). With the item pool set (commit 8298ab833): 910 DPS. With the item pool set of 8 November (commit ae9b8c23a): 939 DPS. With the Windfury Totem rule of commit 9f254e8d8 (9 November): 841 DPS, the same on commit 3633d376a (11 November). This is about 94% of the pure average at fresh level 60 and 90% in Naxxramas (wowsims of 11 November and model) |

- **Holy Power.** The Holy values use a 175% critical heal (main hypothesis, decision of 3 November, the general view of the players). Before the notes of 2 November, the Paladin was 1–7% below the Druid on one tank at 175%, and 3–10% above at 225%. With the Druid changes of the notes of 2 November: 8–15% below at 175%, 5% below to 5% above at 225%.
- **Mana.** In raids, mana is still the limit of the Paladin. The best cast plan is almost only Flash of Light.
- **Righteous Fury.** The +33% and Shieldsworn give most of the threat increase.

## Holy talents

| Talent | Result in the beta | Effect on the proposals |
| --- | --- | --- |
| Divine Strength, Divine Intellect | % of base, gear and flat buff stats. Multiplies with Kings | None |
| Healing Light | Increases the full heal, not only the base | None |
| Spiritual Focus | Adds to other pushback resistance (Concentration Aura 35% + 70% = immune) | None |
| Improved Seals | Increases the full damage, not only the base. No effect on Seal of the Crusader | None |
| Unyielding Faith | Diminishing returns not tested | None. The beta of 30 October moves it to Retribution row 3 |
| Reverence | Keeps a % of Spirit regeneration during casts. The 5-second rule starts again when a cast ends | None |
| Purifying Power | Multiplies with Benediction (×0.80 × 0.90) | None |
| Illumination | Returns 50% of the base cost. Cost decreases do not decrease the return | None |
| Divine Favor | Not on the global cooldown | None |
| Divine Precision | The spell hit cap is 18%, with no fixed 1% miss. 3/3 gives the full cap | None |
| Holy Shock | Damage uses spell damage. Healing uses healing power. Both at 42.9% | None |
| Consecrated Ground | Increases all your Holy damage on those targets, also Retribution Aura and Consecration | None |
| Light's Vigil | 3 ranks: 730, 1,000 and 1,340 mana. Rank 3 heals each party member for 684–724 | None |

## Protection talents

| Talent | Result in the beta | Effect on the proposals |
| --- | --- | --- |
| Toughness | Only armor from items. Nothing from Devotion Aura, scrolls, elixirs, potions or Mark of the Wild | None |
| Redoubt | A blocked hit can start it without the use of a charge | Redoubt (C-P1) keeps the proc |
| Precision | Melee, ranged and spell hit. Each ability uses the correct hit type | Confirms it as the shared hit talent |
| Anticipation | A raid boss stops critical hits at 440 Defense. Anticipation gives 20 | The stat targets use this cap |
| Improved Seal of Fury | The mana return does not change with the rank of the Seal. The mana gives no threat | Removed by Shoulder the Burden (C-P5) |
| Improved Righteous Fury | Applies after armor. Multiplies with Iron Creed (×0.94 × 0.91, about −15% in total) | None. See W7 |
| Shield Specialization | Multiplies Shield Block Value. Mana return is 4%. The mana gives no threat | Stays the main mana source. Shieldsworn adds a return on each Holy Strike |
| Sacred Duty | % of total Stamina, multiplies with Kings. Decreases the cooldowns of Forbearance spells | None |
| Swift Judgement | Not on the global cooldown | None |
| One-Handed Weapon Specialization | Melee attacks, Seals, Judgements, Holy Strike and the Twist of Light Echo | None |
| Templar's Bulwark | An absorb, not a heal. Mortal Strike effects do not decrease it | None |
| Reckoning | Stored attacks hit with the next melee hit. Each can trigger Seals and Judgements | See W6 |
| Iron Creed | Holy Strike threat ×1.90 (Righteous Fury) × 1.25 | See W7 |
| Holy Shield | Threat ×1.90 (Righteous Fury) × 1.20. More tests are necessary | None |

## Retribution talents

| Talent | Result in the beta | Effect on the proposals |
| --- | --- | --- |
| Benediction | Its cost decrease multiplies with Purifying Power, Holy Conduit and Twist of Light | None |
| Holy Conduit | With Benediction, Consecration costs ×0.60 × 0.90 | None |
| Conviction | Also applies to damage Seals and Hammer of Wrath | Conviction (C-R1) adds only Holy Shock, Exorcism, Consecration and heals |
| Vindication | About 5 procs each minute. Ranks: −67/136/204 Attack Power on the target and +1/2/3% on you | None. The beta of 30 October removes the Attack Power buff |
| Sanctified Judgement | Returns 60% of the base cost of the Seal, before talent cost decreases: 126 mana for Seal of Command with Benediction and Twist of Light | The mana models use 126 |
| Pursuit of Justice | 15% at 2/2. Better than the 8% boot enchant | On the watch list (W1) |
| Eye for an Eye | Uses the damage taken after armor and resistance | None |
| Sacred Arbiter | +20% Holy Strike damage. Refreshes Light, Wisdom, Justice and Crusader | None |
| Two-Handed Weapon Specialization | Melee attacks, Seals, Judgements, Holy Strike and the Twist of Light Echo | None. The beta of 30 October moves it to row 4 (adopted) |
| Vengeance | Multiplies with other % damage. Critical hits from procs add stacks | None |
| Repentance | Diminishing returns category not tested | None |
| Instrument of Law | Rank 2 makes Hammer of Wrath instant. The threat decrease multiplies with Salvation | None |
| Twist of Light | More tests are necessary. With Benediction, Seals cost ×0.72 | None |

## Spells

| Spell | Result in the beta | Source |
| --- | --- | --- |
| Holy Strike | Uses normalized weapon damage. The Holy part uses 0.429 × weapon %: 21.45% of spell power at rank 8. Does not trigger Seal of Fury, Righteousness or Command. Triggers Seal of Light, Justice and Wisdom | Player tests |
| Seal of Fury | 35 Holy damage + 10% of spell power for each hit (rank 7). Improved Seals multiplies the full hit: 40.25 + 11.5% of spell power. No Attack Power. Critical hit: ×2 damage, with a separate roll. Cannot miss | Player tests; game files (flat 35, spell 20418) |
| Seal of Righteousness | 10% of spell power with a one-handed weapon, 12% with a two-handed weapon. Weapon speed has no effect | Player tests; patch note, 16 October |
| Seal of Command | 29% × 70% weapon damage = 20.3% of spell power. 7 procs each minute. Uses the melee hit table | Player tests |
| Judgement of Fury, Righteousness and Command | 42.9% of spell power. Melee hit table. Critical hit: ×2 damage. Judgement of Command: ×2 damage against a stunned target | Player tests; patch note, 16 October |
| Judgement of Fury | The damage hits before the taunt. The taunt copies the top threat. The threat from the damage is not added. The taunt does not remove Judgement of the Crusader | Player tests |
| Judgement of the Crusader | The bonus uses the coefficient of each spell, as spell power does. Seal of Command receives the full 29% | Player tests |
| Consecration | 0.042 of spell power for each tick (33.6% for each target). First 4 enemies only. Ticks can be critical hits (×1.5) | Patch note, 16 October; player tests |
| Retribution Aura | 6% of spell power | Patch note, 8 October |
| Holy Shield | The spell power coefficient is not known. Classic: 5% for each block | Classic data |
| Mana return | Mana from Shield Specialization, Improved Seal of Fury and Sanctified Judgement gives no threat | Patch notes, 8 and 16 October |
| Rage | Rage from damage taken was repaired on 8 October. It uses 20–40% armor, related to level. Critical hits give ×2 rage. Bear Form: ×1.5 threat | Patch note, 8 October |
| Lay on Hands | Heals for your maximum health. Drains all your current mana. The drain does not stop mana regeneration. 20 min cooldown (Classic: 1 hour). Ranks 2 and 3 restore 250 and 550 mana to the target | Forever spellbook (client data); player tests |
