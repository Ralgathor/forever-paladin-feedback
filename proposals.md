# Forever Paladin Talent Proposals

This document gives talent proposals for the WoW Forever Paladin. It has 18 changes and 7 moves. The proposals follow the rules that Forever uses for the other classes. Each proposal uses a talent from another class in the same beta build as a model.

## How to read this document

- **C (change).** C1 to C18 change what a talent does, add a talent or remove a talent. A change can also move the talent. The text then gives the new row.
- **M (move).** M1 to M7 move a talent to a different row or column. The talent text does not change.
- **C18a and C18b** are the two alternatives to C18.
- **Withdrawn ideas** have no ID. They are in the Withdrawn ideas section only.
- **Data.** Forever client build 1.60.1.70450, with the server hotfixes of 18 October 2026, from wowforevertalents.com. Player tests from 19 October 2026 and later. The text tells you when a value comes from an in-game tooltip.
- **Limits.** These are design proposals. Nobody has tested them in the game. The combat and mana values use Classic 1.12 rules when no test gives a different rule. Each estimate gives its assumptions.
- **Calculator.** You can try all proposals in the talent calculator. Use the Beta/Proposed button to compare.

## Summary

**Changes**

| ID | Talent | Tree and row | Beta | Proposed |
| --- | --- | --- | --- | --- |
| C1 | Reverence | Holy, row 3 → row 2 | 10/20/30% of mana regeneration while casting | 17/33/50% |
| C2 | Lingering Light (new) | Holy, row 5 | — | 2 ranks: a critical heal adds a heal over time of 15/30% of the heal |
| C3 | Infusion of Light | Holy, row 4 → row 2 | Holy Shock and Flash of Light critical hits make the next Holy Light faster | Holy Strike critical hits also do this |
| C4 | Healing Light | Holy, row 2 → row 6 | 3 ranks: 4/8/12% | 2 ranks: 6/12% |
| C5 | Improved Seals | Holy, row 2 → row 1 | 3 ranks: 5/10/15% | 5 ranks: 3/6/9/12/15% |
| C6 | Redoubt | Protection, row 1 | 10% chance when you are hit: +4–20% block | The same. Each Holy Shield cast also starts it |
| C7 | Iron Creed | Protection, row 6 | −2–10% damage taken for 6 sec after Holy Strike | −2–10% damage taken while Righteous Fury is active |
| C8 | Divine Strength replaces Toughness | Protection, row 1 | Toughness: +2–10% armor from items | Divine Strength: +2–10% Strength (from Holy row 1) |
| C9 | Improved Righteous Fury | Protection, row 3 | −2–6% damage taken with Righteous Fury | Removed |
| C10 | Righteous Defense (new) replaces Improved Seal of Fury | Protection, row 3, requires Guardian's Favor | Improved Seal of Fury: mana when the Seal of Fury shield absorbs a hit | Righteous Defense: Blessing of Protection also makes up to 3 enemies that attack the target attack you for 6 sec |
| C11 | Reckoning | Protection, row 5 | Extra attack after a block (40%) or a critical hit taken (100%). It hits with the next swing | Charge after a block, dodge or parry (once each 4 sec) or a critical hit taken. Holy Strike releases up to 2 charges |
| C12 | Fury's Reach (new) | Protection, row 4 | — | 2 ranks: Judgement range +5/10 yards while Seal of Fury is active |
| C13 | Shield Specialization | Protection, row 3 | Mana return once each 3 sec | Mana return once each 2 sec |
| C14 | Holy Shield | Protection, row 7 | 221 Holy damage for each block (rank 3) | 221 Holy damage plus 200% of your block value for each block |
| C15 | Conviction | Retribution, row 2 | +1–5% critical hit chance with melee attacks | +1–5% critical hit chance with attacks and spells |
| C16 | Sacred Arbiter | Retribution, row 4 → row 5 | +20% Holy Strike damage | Holy Strike always triggers your active Seal |
| C17 | Twist of Light | Retribution, row 7 | The Echo applies to the next melee attack only | The Echo applies to all melee attacks for 10 sec |
| C18 | Judgement of the Crusader | Baseline spell | Uses the one Judgement of the Paladin | Personal debuff. It does not count against the one-Judgement limit |

**Moves**

| ID | Talent | Tree | Beta | Proposed |
| --- | --- | --- | --- | --- |
| M1 | Consecrated Ground | Holy | Row 5 | Row 3 |
| M2 | Spiritual Focus | Holy | Row 2 | Row 4 |
| M3 | Unyielding Faith | Holy | Row 2, column 4 | Row 2, column 3 |
| M4 | Improved Hammer of Justice | Protection | Row 4, column 3 | Row 3, column 1 |
| M5 | Swift Judgement | Protection | Row 4, column 1, requires Improved Seal of Fury | Row 4, column 1, no requirement (same position) |
| M6 | Two-Handed Weapon Specialization | Retribution | Row 5 (20 points) | Row 4 (15 points) |
| M7 | Repentance | Retribution | Row 5 (20 points) | Row 4 (15 points) |

## Design rules

Forever uses five rules for its talent trees. All proposals follow these rules.

1. **No talents that improve a buff.** Buffs such as Blessing of Kings come from the trainer. Iron Creed (C7) is the one exception. The text of C7 gives the reason.
2. **Rows 1 and 2 are for all specs.** The first talents must give the other two specs a reason to put points in the tree.
3. **Shared stats are for melee and spells.** Precision gives hit for both. Thundering Strikes (Shaman) gives critical hit for both.
4. **Each tree has 1-point signature talents** in rows 3 and 4. Each tree ends with a 1-point talent at 30 points.
5. **The class identity stays.** Holy heals with the Light. Protection holds the enemy with a shield. Retribution judges with a two-handed weapon and Seals.

### What the other classes have

| Pattern | Other classes | Paladin beta |
| --- | --- | --- |
| Mana regeneration while casting (healers) | Meditation (Priest), Reflection (Druid), Mindfulness (Shaman): 50% | Reverence: 30% |
| Mana regeneration while casting (damage and hybrid specs) | 50% at about 20 points: Bestial Discipline, Resourcefulness (Hunter), Improved Stormstrike (Shaman), Spirit Tap (Priest) | None for Protection or Retribution |
| Healing bonus deep in the tree | Spiritual Healing (Priest, 25 points), Purification (Shaman, 25 points) | Healing Light (+12%) at 5 points |
| Shared critical hit | Thundering Strikes (Shaman, row 1): all spells and attacks | Conviction: melee only |
| Two-handed weapon talent | Warrior: 15 points | 20 points |
| Stun cooldown talent | Brutal Impact (Druid): 2 ranks, −15/−30 sec on Bash | Improved Hammer of Justice: 3 ranks, −5/−10/−15 sec |
| Area taunt | Challenging Shout (Warrior), Challenging Roar (Druid): 10 yards, 6 sec, 10 min | None |

## Holy

Most saved Holy builds stop at about 20 points. These proposals make the deep Holy talents better for healers. They also give Retribution and Protection a reason to put a few points in Holy.

### Holy layout

| Row (points necessary) | Talents | Points in the row |
| --- | --- | --- |
| 1 (0) | Improved Seals (C5), Divine Intellect | 10 |
| 2 (5) | Infusion of Light (C3), Reverence (C1), Unyielding Faith (M3) | 7 |
| 3 (10) | Voice of Truth, Purifying Power, Consecrated Ground (M1) | 5 |
| 4 (15) | Spiritual Focus (M2), Illumination, Divine Favor | 8 |
| 5 (20) | Divine Precision, Holy Shock, Lingering Light (C2) | 6 |
| 6 (25) | Healing Light (C4), Holy Power | 7 |
| 7 (30) | Light's Vigil | 1 |

- Holy has 44 points (beta: 46).
- You can use each talent when its row opens.
- Illumination still requires Reverence (straight arrow in column 2).
- Divine Strength leaves Holy. It goes to Protection row 1 (C8).

### C1. Reverence: 10/20/30% → 17/33/50%, row 3 → row 2

- **Proposed text.** "Allows 17/33/50% of your Mana regeneration to continue while casting."
- **Model.** Meditation (Priest), Reflection (Druid) and Mindfulness (Shaman) give 50% with 3 ranks.
- **Illumination is not sufficient.** Other healers have a mana return in addition to their 50% (Litany of Light, Water Shield, Mana Tide Totem). Forever also decreased Illumination to 50% of the base cost.
- **Row 2.** In row 2, Reverence is also the mana talent for Protection and Retribution. They get it with 8 Holy points (see Mana).
- **If it is too strong:** use 13/27/40%.

### C2. Lingering Light (new talent): row 5, column 3, 2 ranks

- **Proposed text.** "Your non-periodic critical heals cause the target to be healed for an additional 15/30% of the amount healed over 6 sec. Refreshing this effect carries over any remaining healing."
- **Identity.** A heal over time after a critical heal is a Paladin idea (Sheath of Light, a later expansion). It is not the same as Divine Aegis (Priest), because Divine Aegis is a shield. It is the only Holy heal over time.
- **Text model.** "Non-periodic critical heals" comes from Divine Aegis and Inspiration (Priest). "Refreshing this effect carries over any remaining healing" comes from Blessed Recovery (Priest). Blessed Recovery already works this way in Forever.
- **Why critical heals.** Healing Light already gives a flat healing bonus. The Holy tree has many critical hit talents (Illumination, Infusion of Light, Divine Favor, Holy Power). This talent gives them more value.
- **Value.** At 25% critical heal chance: 25% × 30% = about +7.5% healing. Some of it is overhealing on targets with full health.

**How the heal over time works.** It works as Ignite and Blessed Recovery do in Forever, not as Deep Wounds.

|  | Ignite (Mage) | Deep Wounds (Warrior) | Lingering Light |
| --- | --- | --- | --- |
| Amount | 8–40% of the critical hit damage | 20–60% of average weapon damage, the same for each critical hit | 15/30% of the critical heal |
| Duration | 4 sec, one tick each 2 sec | 12 sec | 6 sec, one tick each 2 sec |
| New critical hit while active | The remaining damage stays and the new damage is added | Only the duration starts again | The remaining healing stays. The new healing is added. The total spreads over a new 6 sec |
| Number | One for each Mage on each target | One for each target | One for each Paladin on each target |

- **Amount.** It uses the full critical heal, with the overhealing.
- **No double bonus.** Healing bonuses apply one time, to the critical heal. They do not apply again to the heal over time. The heal over time cannot be a critical heal.
- **In play.** Many critical heals on the tank make a large heal over time. Divine Favor on Holy Light gives one large heal over time when you want it. Holy Shock critical heals (+15% from Holy Power) give many small amounts.

### C3. Infusion of Light: Holy Strike critical hits also count, row 4 → row 2

- **Proposed text.** "Your Holy Shock, Holy Strike and Flash of Light critical hits reduce the cast time of your next Holy Light cast within 15 sec by 0.5/1 sec."
- **Change.** Only Holy Strike is new. The values and the duration are the same as in the beta.
- **Why.** Holy Power gives +15% critical hit chance to Holy Shock and Holy Strike. But only Holy Shock triggers Infusion of Light in the beta.
- **In play.** A Holy Paladin who attacks between heals gets a reason to use Holy Strike. Retribution and Protection use Holy Strike in their rotation. They get faster Holy Light casts for emergencies.
- **Limit.** Holy Strike has a 10 sec cooldown. Thus, it gives a maximum of one more chance each 10 sec.
- **Row 2.** Retribution and Protection keep a healing reason to put points in Holy: faster heals, not larger heals.
- **Risk.** In row 2, a 7-point Holy dip gives Retribution or Protection a faster self-heal in PvP. The 10 sec cooldown keeps this small.

### C4. Healing Light: row 2 → row 6, 2 ranks

- **Proposed text.** "Increases the amount healed by your Holy Light, Flash of Light, and Holy Shock spells by 6/12%."
- **Change.** 2 ranks (6/12%), not 3 ranks (4/8/12%). The maximum stays 12%.
- **Why.** The +12% healing bonus is now at 25 points, as Spiritual Healing (Priest) and Purification (Shaman) are. A Holy Paladin with 28 points in Retribution has only 23 points for Holy. This Paladin cannot get Healing Light.
- **Deep Holy** keeps Healing Light, Holy Power, Lingering Light and Light's Vigil. Thus, a deep Holy build stays clearly better for healing.
- **Cost.** A Holy Paladin who levels gets the full +12% at level 36, not at level 17.

### C5. Improved Seals: row 2 → row 1, 5 ranks

- **Proposed text.** "Increases the damage done by your Seals and Judgements by 3/6/9/12/15%."
- **Change.** 5 ranks, not 3 ranks (5/10/15%). The maximum stays 15%. Improved Seals replaces Divine Strength in row 1. Divine Strength goes to Protection row 1 (C8).
- **Dip.** With 5 Holy points, Retribution and Protection get +15% Seal and Judgement damage. Seals are the Paladin's own damage. Thus, this dip is more specific to the Paladin than Strength.

### M1. Consecrated Ground: row 5 → row 3

- Row 3 opens at level 20. Paladins learn Consecration at level 20.
- Protection gets it with 12 Holy points (beta: 22) for more area threat.

### M2. Spiritual Focus: row 2 → row 4

- It makes space in row 2.
- Only healers need resistance to spell pushback.

### M3. Unyielding Faith: row 2, column 4 → column 3

- It fills the space that Improved Seals leaves when it goes to row 1 (C5).
- Thus, row 2 has no empty space between talents.

## Protection

The Protection proposals give:

- A fix for crushing blows (C6). This is the largest difference between the Paladin and the Warrior.
- A simpler tree (C7, C8, C9, C10, M4, M5).
- A Reckoning that works at level 60 (C11).
- A ranged pull (C12).
- More stable mana for tanks (C13).
- Threat that increases with gear (C14).

### Protection layout

| Row (points necessary) | Talents | Points in the row |
| --- | --- | --- |
| 1 (0) | Divine Strength (C8), Redoubt (C6) | 10 |
| 2 (5) | Precision, Guardian's Favor, Anticipation | 10 |
| 3 (10) | Improved Hammer of Justice (M4), Righteous Defense (C10), Shield Specialization (C13), Sacred Duty | 9 |
| 4 (15) | Swift Judgement (M5), Fury's Reach (C12), One-Handed Weapon Specialization | 6 |
| 5 (20) | Templar's Bulwark, Reckoning (C11) | 6 |
| 6 (25) | Iron Creed (C7) | 5 |
| 7 (30) | Holy Shield (C14) | 1 |

Arrows: Guardian's Favor → Righteous Defense (column 2, down). Swift Judgement → Fury's Reach (row 4, column 1 to column 2). Redoubt → Shield Specialization (column 3, down).

- Protection has 47 points (beta: 48).
- Rows 1–4 have 35 points. Row 5 opens at 20 points.

### C6. Redoubt: Holy Shield also starts it

- **Proposed text.** "Damaging melee attacks against you have a 10% chance to increase your chance to block by 4/8/12/16/20%. Lasts 10 sec or 5 blocks. Casting Holy Shield also triggers this effect."
- **Change.** Only the Holy Shield trigger is new. If Redoubt is active, a new trigger sets it again to 10 sec and 5 blocks.
- **Why.** It removes most crushing blows (see Analysis, Crushing blows).
- **Blizzard's direction.** The patch of 1 October moved block from Redoubt (6–30% → 4–20%) to Holy Shield (20% → 30%). C6 keeps these values. Redoubt is only active for a longer time.
- **Other specs.** Holy and Retribution do not have Holy Shield. Thus, their Redoubt does not change.
- **Side effects.** Block from talents increases from about 40% (30% Holy Shield + about 10% Redoubt) to 50%. Reckoning, Shield Specialization and Holy Shield get a little more value.

### C7. Iron Creed: damage reduction while Righteous Fury is active

- **Proposed text.** "Increases the threat generated by your Holy Strike ability by 5/10/15/20/25%. While Righteous Fury is active, reduces your damage taken by 2/4/6/8/10%."
- **Problem.** In the beta, the reduction lasts 6 sec after a Holy Strike. Holy Strike has a 10 sec cooldown. At 5/5, the average is 6 sec ÷ 10 sec × 10% = 6%.
- **Change.** The reduction is active while Righteous Fury is active. It has no timer and no Holy Strike condition. Thus, Holy Strike has only one more mechanic (Reckoning, C11).
- **Threat bonus.** The +25% Holy Strike threat stays. It gives about 11 threat per second (TPS) at 5/5 and 200 spell power (see Analysis, Threat).
- **Total.** −10% damage taken. This is the same as Defensive Stance (Warrior). Improved Righteous Fury added to this (about 15% total). C9 removes it.
- **Rule exception.** Iron Creed works as an improved Righteous Fury. But it needs 25 Protection points. Monitor it in PvP, because all specs can use Righteous Fury.

### C8. Divine Strength replaces Toughness

- **Proposed text.** "Increases your Strength by 2/4/6/8/10%." This is the beta text. Only the tree changes (Holy row 1 → Protection row 1).
- **Why remove Toughness.** Forever removed flat armor talents for tanks. Toughness (Warrior) was removed. Toughness (Shaman) now gives Stamina. Thick Hide (Druid) increases with Defense. Toughness (Paladin) was the last flat armor talent.
- **Why Divine Strength.** Strength is the stat of the Protection Paladin. It gives Attack Power for threat and block value (20 Strength = 1 block value). Holy does not need it now (C5).
- **Row 1 for all specs.** Holy and Retribution go through Protection row 1 to get Precision. Divine Strength is useful for all three specs.
- **Parity.** The class has one % Strength talent, as the Druid has Heart of the Wild. There is no other Stamina talent: only +4% from Sacred Duty.

### C9. Improved Righteous Fury: removed

- With Iron Creed always active (C7), the two talents gave about 15% damage reduction.
- Iron Creed alone gives 10%, the same as the Warrior.

### C10. Righteous Defense (new talent) replaces Improved Seal of Fury: row 3, column 2

- **Proposed text.** "Your Blessing of Protection also forces up to 3 enemies that are attacking the target to attack you for 6 sec." Passive, 1 point.
- **Requirement.** Guardian's Favor 2/2 (straight arrow from row 2). Guardian's Favor decreases the cooldown of Blessing of Protection. Righteous Defense adds the taunt. The two talents make one Blessing of Protection path.
- **Why remove Improved Seal of Fury.** It was a second "mana when you are hit" talent. Its mana return does not change with the rank of the Seal. Reverence in row 2 (C1) is the mana talent now (see Analysis, Mana).
- **Problem.** Blessing of Protection stops physical attacks on an ally. But the enemies then attack the next player on their threat list. This is often a healer.
- **Change.** With Righteous Defense, up to 3 of these enemies attack the Paladin. The Paladin saves the ally and keeps the enemies.
- **No new button.** Blessing of Protection is a baseline spell. Guardian's Favor (row 2) decreases its cooldown by 2 min.
- **Use.** Cast Blessing of Protection on a healer or a player in cloth armor. Blessing of Protection does not stop spells. Thus, a healer can continue to heal.
- **Model.** Righteous Defense (Paladin, a later expansion) forces up to 3 enemies that attack an ally to attack the Paladin. Guardian's Favor is the Forever precedent for a talent that changes Blessing of Protection.
- **Not an area taunt.** The Paladin protects allies with Blessing of Protection. An area taunt with a 10 min cooldown gives little (see Withdrawn ideas).
- **Signature talents.** Each tree keeps a 1-point signature talent in rows 3 and 4:
  - Holy: Voice of Truth and Divine Favor.
  - Retribution: Seal of Command and Repentance (M7).
  - Protection: Swift Judgement and Righteous Defense.
- **Other specs.** Holy and Retribution can get it with 15 points. In PvP, a taunt has no effect on players.
- **No change.** Righteous Fury, Seal of Fury and its absorb shield stay baseline spells.

### C11. Reckoning: charges from block, dodge and parry, released by Holy Strike

- **Proposed text.** "Gives you a 20/40/60/80/100% chance to gain an extra attack after Blocking, Dodging, Parrying or being the victim of a non-periodic critical strike. Cannot occur from Blocks, Dodges or Parries more than once every 4 sec. Stores up to 4 extra attacks. Your Holy Strike releases up to 2 stored extra attacks."
- **Beta text.** "Gives you a 8/16/24/32/40% chance after Blocking and a 20/40/60/80/100% chance after receiving a non-periodic critical strike to gain an extra attack. Stores up to 4 extra attacks. Cannot occur from Blocks more than once every 1.5 sec."
- **Text model.** The extra-attack effects of Classic: Reckoning, Sword Specialization and Hand of Justice.

**Problems in the beta**

- **The critical hit trigger does not work at level 60.** At 440 Defense, a raid boss cannot make critical hits (see Analysis, Crushing blows). Thus, half of the talent works only while you level or in PvP.
- **The storage does not work when you tank.** A tank attacks all the time. Thus, a stored attack hits with the next swing. The storage is useful only when you stop your attacks (the Classic "Reckoning bomb").
- **Low value on a boss:** about one extra attack each 10 sec.

**Changes**

- **New triggers: block, dodge and parry.** They work at the critical hit cap, as Master of Defense (Warrior) does with dodge and parry. At the stat targets, about 86% of the boss swings are blocked, dodged or parried.
- **The ranks increase the chance (20–100%).** The 4 sec limit does not change with the ranks, as with other proc talents.
- **Holy Strike releases the charges, 2 at a time.** One Holy Strike gives a maximum of 3 hits. The charges stay between Holy Strikes. You can keep them for a target change, a taunt or a dangerous enemy.
- **The critical hit trigger stays, without the 4 sec limit.** Thus, the Classic Reckoning bomb still works while you level and in PvP. 4 critical hits taken give 4 charges. Two Holy Strikes release them.
- **A link between the shield and the attacks,** as Shield Slam (Warrior) has. Players on Wowhead say that the Paladin does not have this link.

**Value for a tank at 5/5**

Simulation: the boss swings each 2 sec. 60% block with C6, 10.7% dodge, 15% parry. No critical hits. Holy Strike each 10 sec. Each extra attack does about 200 damage and about 273 threat. The beta values use 50% block.

| Case | Charges each 10 sec | Extra attacks each 10 sec | Extra damage per sec | Extra TPS |
| --- | --- | --- | --- | --- |
| Beta, 1 boss | 1.0 | 1.0 | +20 | +27 |
| Beta, 3 enemies | 2.2 | 2.2 | +45 | +61 |
| **Proposed, 1 boss** | **2.3** | **2.0** | **+40** | **+55** |
| **Proposed, 3 enemies** | **2.4** | **2.0** | **+40** | **+55** |

- **On a boss,** the proposal gives two times the value of the beta: +27 TPS more.
- **The charges come a little faster than Holy Strike uses them** (2.3 and 2.0 each 10 sec). The Paladin usually has 2–4 charges. About 13% of the procs are lost at the maximum of 4.
- **On groups of enemies,** the 4 sec limit keeps the same value as on a boss. The beta is a little stronger on groups (+45 and +40 damage per sec), because its block trigger has a 1.5 sec limit.
- **PvP burst.** See Analysis, PvP burst check.

### C12. Fury's Reach (new talent): a ranged pull for Protection

- **Proposed text.** "Increases the range of your Judgement by 5/10 yards while Seal of Fury is active."
- **Position.** Row 4, column 2, 2 ranks. It requires Swift Judgement (arrow from column 1 in the same row). One-Handed Weapon Specialization moves from column 2 to column 3. Its text does not change.
- **Why.** Protection has no ranged pull and no ranged taunt. The Seal of Fury Judgement does 153–167 Holy damage and taunts for 4 sec. But its range is only 10 yards. At 2/2, the range is 20 yards: two times the base range.
- **Model.** Vanguard (Warrior): Charge in Defensive Stance, row 4, 1 point. Feral Charge (Druid, row 3) and a ranged pull in Feral.
- **Why 2 ranks.** Row 4 already has a 1-point talent (Swift Judgement). Thus, this talent has ranks, as the other talents in the row.
- **Why only with Seal of Fury.** Judgement of Command does 388–422 damage to a stunned target. Without the Seal of Fury condition, a 20 yard range gives more burst to hybrids in PvP. With the condition, Holy and Retribution get almost nothing from the dip.
- **Threat and mana.** No change while you tank. Judgement still costs 91 mana and has a 10 sec cooldown. Only the first pull changes. The full path costs 3 points (Swift Judgement and 2 ranks).

### C13. Shield Specialization: mana return once each 2 sec

- **Proposed text (rank 3).** "Increases the amount of damage absorbed by your shield by 30%, and gives your blocks a 100% chance to restore 4% of your maximum Mana. May only occur once every 2 sec."
- **Change.** Only the limit changes: once each 2 sec, not once each 3 sec. The ranks, the chance and the 4% return do not change.
- **Why.** C10 removes Improved Seal of Fury (about 23 mana per sec while you tank). Reverence (C1) and the extra blocks from C6 give back about 13. Holy Shield rank 3 costs 24 mana per sec. Without C13, a fresh level 60 tank (2,897 mana) loses about 9 mana per sec without Consecration.
- **Value.** A boss that swings each 2 sec can trigger it with each block: 4% of maximum mana × 60% block ÷ 2 sec. This is 35 mana per sec at fresh level 60 and 59 in Naxxramas (beta: 19 and 33). Tanking without Consecration gives +4 to +30 mana per sec (see Analysis, Mana).
- **Model.** Warriors and Druids get rage when they are hit. Water Shield (Shaman) gives mana when the Shaman is hit. Shield Specialization is already the Paladin version. Thus, no new talent is necessary.
- **Synergy.** More block gives more mana. Thus, the crushing blow fix (C6) and the mana fix help each other.
- **Limits.** Against groups of enemies, it gives a maximum of 2% of maximum mana each sec: 58 at fresh level 60, 98 in Naxxramas (beta: 39 and 65). It gives nothing to a Paladin who is not hit. Reverence (C1) is for that case.

### C14. Holy Shield: damage increases with block value

- **Proposed text (rank 3).** "Increases chance to block by 30% for 10 sec, and deals 221 Holy damage plus 200% of your block value for each attack blocked while active. Damage caused by Holy Shield causes 20% additional threat. Each block expends a charge. 4 charges."
- **Change.** Each block adds 200% of your block value to the Holy Shield damage. The block chance, the charges, the cooldown and the threat bonus do not change.
- **Problem.** Warrior and Druid threat increases with gear and with boss damage, because their rage comes from the hits they take. Paladin threat increases only with spell power: about +32 TPS for each +100 spell power. Without C14, the Paladin falls from 107% of the Druid threat at fresh level 60 to 80% in Naxxramas (see Analysis, Threat).
- **Why block value.** It is a gear stat on the character sheet. It is easy to read and easy to collect. It increases about 5 times from fresh level 60 to Naxxramas, much faster than spell power. It connects the tank stats of the Paladin: the shield, Strength (C8) and Shield Specialization (+30% block value). Shield Slam (Warrior) already adds block value to its damage.
- **Result.** The Paladin stays between the Druid and the Warrior at all gear tiers: 116% of the Druid threat at fresh level 60, 102% in Naxxramas. With flatter gear progression, it is 94–110% in Naxxramas (see Threat, part 3).
- **Why 200%.** At 100%, the Paladin has only 91% of the Druid threat in Naxxramas. At 300%, the Paladin has more threat than the Warrior from pre-raid gear.
- **No new button.** You already use Holy Shield on cooldown. C6 keeps about 3 blocks each 10 sec.
- **PvP.** At about 125 block value, each block does about 250 more Holy damage. The maximum is 4 blocks each 10 sec, against melee attacks only. Only Protection has Holy Shield.

### M4. Improved Hammer of Justice: row 4, column 3 → row 3, column 1

- **Text.** "Decreases the cooldown of your Hammer of Justice spell by 5/10/15 sec." 3 ranks, the same as the beta.
- **Model.** Brutal Impact (Druid) on Bash. Bash also has a 60 sec base cooldown.
- **Why.** It is one of the Paladin talents that players take least. Improved Seal of Fury leaves row 3 (C10) and makes space.
- **PvP.** Holy or Retribution get the full −15 sec (a 45 sec Hammer of Justice) with 13 Protection points (beta: 18). Brutal Impact is in Feral row 2 (−30 sec on Bash). Thus, this stays in line with the Druid.

### M5. Swift Judgement: row 4, column 1, no requirement

- In the beta, Swift Judgement requires Improved Seal of Fury. C10 removes Improved Seal of Fury. Thus, Swift Judgement has no requirement.
- It stays in row 4, column 1, the same position as in the beta. Only the requirement changes.
- It is the 1-point signature talent of row 4.
- Fury's Reach (C12) is next to it in column 2. Fury's Reach requires Swift Judgement.

## Retribution

These proposals connect the melee attacks of Retribution to its Holy spells. They also decrease the work of Seal swaps.

### Retribution layout

| Row (points necessary) | Talents | Points in the row |
| --- | --- | --- |
| 1 (0) | Deflection, Benediction | 10 |
| 2 (5) | Improved Judgement, Holy Conduit, Conviction (C15) | 9 |
| 3 (10) | Vindication, Sanctified Judgement, Seal of Command, Pursuit of Justice | 9 |
| 4 (15) | Eye for an Eye, Repentance (M7), Two-Handed Weapon Specialization (M6) | 6 |
| 5 (20) | Vengeance, Sacred Arbiter (C16) | 4 |
| 6 (25) | Champion of the Light, Instrument of Law | 5 |
| 7 (30) | Twist of Light (C17) | 1 |

Retribution has 44 points (beta: 44).

### C15. Conviction: attacks and spells

- **Proposed text.** "Improves your chance to get a critical strike with attacks and spells by 1/2/3/4/5%."
- **Model.** Thundering Strikes (Shaman) has the same change.
- **Real change.** In the beta, Conviction already applies to damage Seals and Hammer of Wrath. The change adds only Holy Shock, Exorcism, Consecration and heals.
- **Cost for healers.** A Holy Paladin needs 10 Retribution points: 5 in row 1, then 5 in Conviction.

### C16. Sacred Arbiter: Holy Strike always triggers your Seal, row 4 → row 5

- **Proposed text.** "Causes your Holy Strike ability to always trigger the effect of your active Seal and to refresh all Judgement effects on the target, including those of other Paladins. Does not trigger the stun of Seal of Justice."
- **Row.** Sacred Arbiter goes from 15 to 20 points. Repentance goes from 20 to 15 points (M7).
- **What it replaces.** The beta gives +20% Holy Strike damage: about 5 damage per sec with a usual two-handed weapon. In the beta, Holy Strike does not trigger Seals. A Seal of Command effect on each Holy Strike gives about 22 damage per sec (70% of a 300 swing, +6% from Two-Handed Weapon Specialization, each 10 sec).
- **Model.** The core talent of Retribution, as Stormstrike is for Enhancement (Shaman).
- **Safety.** It triggers the Seal, not a second Judgement. The stun exception prevents a stun each 10 sec in PvP.
- **Tradeoffs.** Protection builds that take Sacred Arbiter for its Judgement refresh now need 20 Retribution points.

### C17. Twist of Light: the Echo lasts 10 sec

- **Problem.** Each Echo lasts for one melee attack. For full value, you must change Seals before almost each swing. With a 3.5 sec two-handed weapon, the global cooldown is active about 80% of the time. Players on the beta forums give a developer statement: rotations must stay at about four buttons.
- **Proposed text.** "Reduces the Mana cost of your Seal spells by 20%. When you replace your Seal of Command, Seal of Righteousness, Seal of Fury, or Seal of Justice with a different Seal, you gain an Echo of that Seal for 10 sec. While the Echo lasts, your melee attacks also apply the replaced Seal's effects."
- **Same action, slower rhythm.** You still change Seals, but one time each 10 sec, together with Holy Strike and Judgement.

| Each 10 sec, 3.5 sec weapon | Beta | With C17 |
| --- | --- | --- |
| Seal casts | About 3 | 1 |
| Holy Strike | 1 | 1 |
| Judgement (8 sec cooldown with Improved Judgement 2/2) | 1.25 | 1.25 |
| Time in global cooldown (1.5 sec each, Judgement included) | About 79% | About 49% |
| Mana used, one target | About 41.6 per sec | About 11.4 per sec |

- **Mana.** With one Seal change each 10 sec, the Sanctified Judgement refund pays for most of the cost. Thus, C17 is also the main mana fix for Retribution (see Analysis, Mana).

### M6. Two-Handed Weapon Specialization: row 5 → row 4 (20 → 15 points)

- **Model.** The Warrior version opens at 15 points.
- **Values.** 2/4/6%, the same as the beta.
- **Space.** Row 4 has space after C16.

### M7. Repentance: row 5 → row 4 (20 → 15 points)

- It takes the row 4 place of Sacred Arbiter (C16).
- Holy and Protection can get it more easily in PvP (see Watch list, W9).

## Judgements in raids

### The problem

- **The rule.** Each Paladin can have only one Judgement active on a target.
- **The conflict.** Since the patch of 15 October, Salvation does not use a Blessing slot. Thus, two Paladins can give all Blessings to a raid. But raids prefer Judgement of Light and Judgement of Wisdom, because they help all players. Judgement of the Crusader helps mostly the Holy damage of the Paladins. Raids remove it. Thus, Retribution loses damage and Protection loses threat.
- **Judgement of Fury does not remove Judgement of the Crusader.** The problem is the one-Judgement limit, not the taunt.
- **Sacred Arbiter does not fix it.** Holy Strike refreshes all Judgements on the target, also those of other Paladins. But each Paladin still has only one Judgement.

### C18. Personal Judgement of the Crusader (recommended)

- **Change.** Judgement of the Crusader does not count against the one-Judgement limit. But it increases only the Holy damage of the Paladin who applies it.
- **Precedent.** Salvation does not use a Blessing slot now. Improved Seal of the Crusader is now baseline.
- **Tradeoff.** Other players who do Holy damage do not get the bonus.
- **For Protection.** A raid can need the one Judgement of the tank for Light or Wisdom. In the beta, the tank then loses Judgement of the Crusader. With C18, the tank keeps it and can also apply Light or Wisdom. Judgement of the Crusader gives a Protection Paladin about +50 TPS (see Analysis, Threat).

### Alternatives to C18

| ID | Option | How it works | Precedent | Tradeoff |
| --- | --- | --- | --- | --- |
| C18a | Merge Light and Wisdom (use this if C18 is rejected) | A Judgement of Seal of Light or Seal of Wisdom applies one Judgement of Grace. Attacks can heal the attacker for 61 and restore 59 mana | Weaponmaster merged four weapon talents | One Paladin must still choose |
| C18b | Judgement Echo (optional, with C18) | When your next Judgement replaces your Judgement of Light, Wisdom or Justice, the replaced Judgement stays on the target as an Echo for 40 sec | The Seal Echo of Twist of Light | It needs a Retribution Paladin with 30 points |

| Raid with two Paladins | Beta | C18 | C18a | C18b alone |
| --- | --- | --- | --- | --- |
| Holy + Holy | Light + Wisdom | Light + Wisdom | Grace | Light + Wisdom |
| Holy + Retribution | Two of three | All three | Grace + Crusader | All three |
| Holy + Protection | Two of three | All three | Grace + Crusader | Two of three |
| Protection + Retribution | Two of three | All three | Grace + Crusader | All three |

## Analysis

This part gives the calculations that support the proposals.

### Crushing blows

#### The problem

- A raid boss is 3 levels above the player.
- With Classic rules, the boss has a 15% chance to hit with a crushing blow (150% damage).
- Crushing blows stop only when miss + dodge + parry + block = 100% against the boss (about 102.4% on the character sheet).
- A tank can remove crushing blows from the attack table (Warrior). Or the tank can survive them with armor and health (Druid).

| Tank | How the tank handles crushing blows | Result |
| --- | --- | --- |
| Warrior | Shield Block: +75% block, 2 blocks, 7 sec, 5 sec cooldown. Shield Specialization: +5% block | Removes crushing blows with average gear. But some crushing blows come after the 2 blocks |
| Druid | No shield. Thick Hide armor increases with Defense. Bear Form gives up to +20% Stamina | Crushing blows always occur. The Druid has the armor and health to survive them |
| Paladin (beta) | Holy Shield: +30% block, 4 charges, 10 sec, 10 sec cooldown. Redoubt is a 10% proc | Needs about 72% avoidance from gear. Crushing blows occur, as for the Druid, but without the Druid armor and health |

C6 uses the Warrior method: it removes crushing blows with block. The Protection tree already gives block.

#### How C6 fixes the problem

- **Redoubt in the beta** gives +4–20% block for 10 sec or 5 blocks. Only 10% of melee hits start it. Thus, it is active about half of the time.
- **With C6,** each Holy Shield cast (each 10 sec) starts Redoubt again. Thus, the two buffs are always active together.
- **The charges are sufficient.** A boss that swings each 2 sec swings 5 times in 10 sec. About 3 of these swings are blocked. Redoubt has 5 blocks and Holy Shield has 4 charges.
- **First hit.** Cast Holy Shield before the pull. Then it covers the first swing of the boss.
- **Holy Shield stays at +30%.** With the Redoubt trigger, +30% already gives the same result as the Warrior.

#### Stat targets

Against a level 63 boss (attack skill 315), with Classic rules.

- **No critical hits: 440 Defense.** The boss has 5.6% critical hit chance against a level 60 player. Each Defense point removes 0.04%. Anticipation gives 20 Defense. Thus, gear and enchants must give +120 Defense.
- **No crushing blows: miss + dodge + parry + block = 100%.** At 440 Defense, each of these increases by 5%.

With Deflection 5/5, Holy Shield and Redoubt active:

| Roll | Sources | Against the boss |
| --- | --- | --- |
| Miss | 5% base + 5% Defense | 10% |
| Dodge | About 0.7% base + 5% Defense + Agility ÷ 20 | 5.7% + Agility ÷ 20 |
| Parry | 5% base + 5% Deflection + 5% Defense | 15% |
| Block | 5% base + 5% Defense + 30% Holy Shield + 20% Redoubt | 60% |
| Total |  | 90.7% + Agility ÷ 20 |

- **Difference after the critical hit cap: 9.3%.** This is about 186 Agility or 58 Defense above 440. Until the tank closes this difference, the missing % is the crushing blow chance. With about 100 Agility, about 4.3% of the swings can be crushing blows. This is close to a Warrior between Shield Blocks.
- **Holy Shield is the full mechanism.** Without it, crushing blows occur at the full rate.
- **Gaps.** A late Holy Shield gives a short gap. Fast bosses or bosses with two weapons can use all charges early.

#### Comparison with the Warrior

Both tanks have 440 Defense and about 100 Agility. The boss swings each 2 sec. Shield Block tooltip on Wowhead: "Increases chance to block by 75% for 7 sec, but will only block 2 attacks", 10 Rage, 5 sec cooldown.

|  | Swings covered | Crushing blow chance on other swings | Swings that can be crushing blows |
| --- | --- | --- | --- |
| Warrior | About 80% (2 of 2.5 swings each 5 sec) | 15% | About 3% |
| Paladin with C6 | About 100% | About 4.3% | About 4.3% |

The two tanks are equal. Gear closes the Paladin gap. The Warrior gaps change with the swing speed of the boss.

### Threat

This section compares the threat of the three tanks: Warrior, Druid and Paladin. The unit is threat per second (TPS) on one boss. The tanks are level 60. The boss is level 63.

The values come from a model. The model uses beta tests and developer notes. It is not a combat log. The inputs are in part 6. The spell data from beta tests is in Beta test results. The values that are not known are in Open questions.

#### Summary

- With all proposals, the Paladin has about the same threat as the Druid and the Warrior.
- Without the proposals, the Paladin has less threat than the other two tanks at all gear levels.
- C14 (Holy Shield damage increases with block value) is necessary. Without C14, the Paladin falls behind in raids.
- Judgement of the Crusader gives the Paladin tank about +50 TPS. Judgement of Fury does not remove it. C18 lets the tank keep it when the raid also needs the Judgement of the tank for Light or Wisdom.
- If the gear progression is flatter, C14 at 200% is still correct.

#### 1. Result with the same gear

Conditions:

- All tanks have pre-raid gear.
- The Paladin has 200 spell power and 60 block value.
- The boss has 5 Sunder Armor and Faerie Fire.

| Boss hit before armor | Warrior | Druid | Paladin, beta | Paladin, all proposals | Paladin, all proposals + Consecration |
| --- | --- | --- | --- | --- | --- |
| 3,000 | 525 | 520 | 400 | 540 | 625 |
| 4,500 | 600 | 585 | 400 | 540 | 625 |
| 6,000 | 660 | 650 | 400 | 540 | 625 |

All values are approximate.

- Warrior and Druid get rage when the boss hits them. Thus, their threat increases when the boss hits harder. Paladin threat does not change with boss damage.
- If Shield Slam has a ×2.25 threat multiplier (not tested), add 135 TPS to the Warrior.
- Both Paladin columns include Judgement of the Crusader. Judgement of Fury does not remove it. In the beta, a raid can need the tank's only Judgement for Light or Wisdom. Then the beta Paladin has no Crusader and about 355 TPS. With C18, the tank keeps Crusader in all cases.
- Without C14, the proposed Paladin has about 455 TPS (545 TPS with Consecration).
- If the boss has no armor debuffs (4,500 hits): Warrior 470 TPS, Druid 425 TPS, Paladin 515 TPS. Most Paladin threat is Holy damage. Armor does not decrease Holy damage.
- Retribution Aura gives the Paladin about +25 TPS. But the Paladin then does not have Devotion Aura (735 armor).

**Threat sources of the proposed Paladin (200 spell power, 60 block value)**

| Source | TPS |
| --- | --- |
| Holy Shield blocks: 180 from the base damage, 80 from block value (C14) | 260 |
| Judgement of Fury: one each 10 sec, plus one Swift Judgement each minute | 70 |
| Holy Strike with Iron Creed | 57 |
| Reckoning extra attacks (C11) | 53 |
| Seal of Fury | 49 |
| Auto attacks | 49 |
| **Total** | **540** |

The proposals give the Paladin about +140 TPS more than the beta:

- C14 (block value on Holy Shield): about +80 TPS.
- C6 (more Holy Shield blocks) and C11 (Reckoning): about +60 TPS.
- C18 (Judgement of the Crusader for each Paladin): +50 TPS more when the raid needs the tank's Judgement for Light or Wisdom.

**Spell power**

Each +100 spell power gives about +32 TPS.

| Spell power | 100 | 150 | 200 | 250 | 300 | 350 |
| --- | --- | --- | --- | --- | --- | --- |
| Paladin, all proposals (60 block value) | 505 | 525 | 540 | 555 | 570 | 585 |

Judgement of the Crusader adds 161 spell power against the boss. This is more than the difference between 150 and 300 spell power.

Spell power at level 60 is not known. At level 30, players have 100–120 spell power. The estimates for level 60 are:

- Pre-raid tank gear: about 150.
- Pre-raid gear with some threat items: 200–250.
- First raid gear: 300–350.

#### 2. Result with gear progression

In raids, the gear and the boss damage increase together. This table shows the five gear tiers of the model.

- The fresh level 60 tier uses a real gear profile (crafted items and dungeon items, without talents).
- The other tiers are estimates. Each tier has about 15–20% more stats, as in Classic.
- The Warrior and the Druid have the same Attack Power and weapon as the Paladin.

| Tier | Spell power | Attack Power | Weapon damage per sec | Block value (with Shield Specialization) | Maximum mana | Boss hit before armor |
| --- | --- | --- | --- | --- | --- | --- |
| Fresh level 60 (real profile) | 208 | 428 | 27.5 (2.2 sec) | 26 | 2,897 | 3,000 |
| Pre-raid best in slot | 260 | 520 | 42 | 60 | 3,400 | 3,500 |
| Molten Core | 310 | 600 | 52 | 80 | 3,900 | 4,500 |
| Blackwing Lair | 380 | 700 | 60 | 100 | 4,400 | 6,000 |
| Naxxramas | 440 | 800 | 66 | 125 | 4,900 | 8,000 |

TPS on one boss. The percentage is the Paladin TPS divided by the Druid TPS.

| Tier | Warrior | Druid | Paladin, beta | Paladin, proposals without C14 | **Paladin, all proposals** | All proposals + Consecration |
| --- | --- | --- | --- | --- | --- | --- |
| Fresh level 60 | 490 | 405 | 380 (94%) | 430 (107%) | **470 (116%)** | 555 |
| Pre-raid best in slot | 545 | 455 | 415 (91%) | 470 (104%) | **555 (122%)** | 645 |
| Molten Core | 640 | 530 | 450 (86%) | 515 (97%) | **625 (118%)** | 720 |
| Blackwing Lair | 755 | 635 | 495 (78%) | 565 (89%) | **700 (111%)** | 800 |
| Naxxramas | 815 | 760 | 535 (70%) | 605 (80%) | **775 (102%)** | 880 |

- All Paladin columns include Judgement of the Crusader. Without it (a raid that needs the beta tank's Judgement for Light or Wisdom), subtract about 50 TPS from the beta column.
- With all proposals, the Paladin is between the Druid and the Warrior at all tiers.
- Without C14, the Paladin falls behind from Molten Core. The Warrior and the Druid get more Attack Power and more rage. The Paladin gets only spell power.
- The beta Paladin is behind at all tiers: 94% of the Druid at fresh level 60, and 70% in Naxxramas.
- Shield Specialization gives 4% of maximum mana. Thus, more mana gives more mana return. Tanking without Consecration gives about +4 mana per sec at fresh level 60 and about +30 mana per sec in Naxxramas (see Analysis, Mana).

#### 3. Result with flatter gear

Blizzard said that it wants flatter gear progression. This is an intention, not a promise. This part shows the result if the gear increases more slowly.

Model:

- Fresh level 60 and pre-raid are the same as in part 2.
- From Molten Core, the gear increases at half the rate of part 2. Block value is 70, 80 and 92 (not 80, 100 and 125).
- Two cases for boss damage: boss hits as in part 2, or boss hits that also increase at half the rate (4,000, 4,750 and 5,750 before armor).

Paladin with all proposals. The first value is the percentage of the Druid TPS. The value in brackets is the percentage of the Warrior TPS.

| Tier | Gear as in part 2 | Flatter gear, boss hits as in part 2 | Flatter gear, flatter boss hits |
| --- | --- | --- | --- |
| Fresh level 60 | 116% (96%) | 116% (96%) | 116% (96%) |
| Pre-raid best in slot | 122% (101%) | 122% (101%) | 122% (101%) |
| Molten Core | 118% (97%) | 114% (95%) | 120% (99%) |
| Blackwing Lair | 111% (93%) | 104% (88%) | 115% (95%) |
| Naxxramas | 102% (95%) | 94% (89%) | 110% (91%) |
| Naxxramas, without C14 | 80% | 76% | 89% |

- C14 at 200% is correct for all three cases. At 150%, the Paladin falls to 89% of the Druid if boss hits continue to increase. At 300%, the Paladin has more threat than the Warrior if all values are flat.
- Without C14, the Paladin falls behind in all cases. Thus, C14 is more important with flatter gear.
- The weakest case is flatter gear with boss hits that continue to increase. The Warrior and the Druid still get more rage from bigger hits. Monitor the block value of each gear tier.
- Mana: if maximum mana increases more slowly (3,650, 3,900 and 4,150), tanking without Consecration gives +14, +17 and +20 mana per sec. C13 is more important.
- Defense: if gear gives Defense more slowly, tanks get to 440 Defense later. The boss can then make critical hits for a longer time. C6 and the Reckoning critical-hit trigger stay useful for a longer time.
- C18: the +161 bonus from Judgement of the Crusader is more important when gear gives less spell power.
- The PvP burst check (C11) uses fresh and pre-raid stats. It stays correct for a longer time.

#### 4. Why the Paladin is different

- **No stance or form multiplier.** Righteous Fury (×1.9) is for Holy damage only. Paladin auto attacks and Reckoning attacks get ×1.0. Defensive Stance gives ×1.495 to all Warrior damage. Bear Form gives ×1.5 to all Druid damage.
- **No strong attack with a short cooldown.**

| Attack | Total threat multiplier | Cooldown |
| --- | --- | --- |
| Primal Bite (Druid, new in Forever) | ×4.5 (×3, Bear Form ×1.5) | 6 sec |
| Revenge (Warrior) | ×3.4 (×2.25, Defensive Stance and Defiance ×1.495) | 5 sec |
| Maul (Druid) | ×2.6 (×1.75, Bear Form ×1.5) | Each swing |
| Holy Strike with Iron Creed 5/5 (Paladin) | ×2.4 (Righteous Fury ×1.9, Iron Creed ×1.25) | 10 sec |
| Paladin auto attacks and Reckoning attacks | ×1.0 | — |

- **Paladin advantages.** Boss armor and rage do not change Paladin threat. Consecration and Holy Shield hit all attackers. Thus, the Paladin is strongest against groups of enemies.

#### 5. Next steps if threat is too low

Use these steps only if tests show that Protection threat is too low with C14. They are not proposals now.

| Step | Effect |
| --- | --- |
| Iron Creed: Holy Strike threat +20/40/60/80/100% (not +5/10/15/20/25%) | +30 to +50 TPS at each tier. Threat only, no PvP effect |
| A shield attack in Protection row 4: 6 sec cooldown, weapon damage + 100 Holy damage, ×2 threat | +170 to +200 TPS. Adds a button. The new Druid attack Primal Bite is the precedent |

Other options were examined and rejected. See Withdrawn ideas.

#### 6. Inputs

**All tanks**

- Level 60, 500 Attack Power, 3% hit.
- One-handed weapon: 45 damage per sec, 2.7 sec speed. Druid: 260 damage for each swing, 2.5 sec.
- Critical hit chance: 6%. Druid: 12% (Sharpened Claws).

**Attacks against a level 63 boss (from the front)**

- 6% miss, 6.5% dodge, 14% parry.
- 40% of auto attacks are glancing blows (−35% damage).

**Boss**

- 3,731 armor. 976 armor after 5 Sunder Armor (450 each) and Faerie Fire.
- One swing each 2 sec. 64% of the swings hit the tank.

**Rage (normalized in Forever)**

- Auto attack: 3.46 rage × weapon speed. ×1.3 for two-handed weapons and Bear Form. ×2 for a critical hit. No rage for a miss, dodge or parry.
- Damage taken: 2.5 × 0.6 × boss hit before armor ÷ 243.6 (level 63). ×1.5 for a crushing blow.
- Heroic Strike and Maul hits give no rage (assumed, as in Classic).
- Each rage point gives 5 threat.

**Warrior**

- Defensive Stance: ×1.3 threat, −10% damage. Defiance 3/3: ×1.15 threat.
- One-Handed Weapon Specialization: +10% damage. Improved Revenge 3/3.
- Revenge: threat = damage × 2.25. Damage includes 28% of Attack Power.
- Shield Slam: 640–670 damage + 50 block value. Threat = damage.
- Heroic Strike rank 9: threat = damage + about 145.
- 5 rage for each block, dodge and parry.
- Extra rage goes to Sunder Armor (about 225 threat before Defensive Stance).

**Druid**

- Bear Form ×1.5, Maul ×1.75, Primal Bite ×3, Swipe ×1.75.
- Ferocity 5/5, Savage Fury 2/2, Feral Instinct 3/3.
- Lacerate and Faerie Fire are not in the model.

**Paladin**

- Righteous Fury: ×1.9 threat for Holy damage only.
- One-Handed Weapon Specialization: +10% damage (not for Consecration or Retribution Aura).
- Improved Seals: +15% (8-point dip into Holy).
- Spell power coefficients: Seal of Fury 10% for each hit, Judgement of Fury 42.9%, Holy Strike 21.45%, Holy Shield 10.7% for each block (assumed: 42.9% divided by 4 charges), Consecration 33.6% (15% of ticks miss).
- Holy Shield: 3 blocks each 10 sec (beta: 2.5).
- Reckoning: 2.0 extra attacks each 10 sec (beta: 1.0).

### PvP burst check

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
- In the beta, Holy Strike does not trigger Seals. Extra attacks are the same as auto attacks, with Seal of Command procs.

| Part of the burst | Proposed | Beta, no stored attacks | Beta, 4 stored attacks |
| --- | --- | --- | --- |
| Holy Strike | 600 (always triggers Seal of Command, C16) | 390 (+20% damage, no Seal effect) | 390 |
| Extra attacks (about 390 each) | 2: 780 | 0 | 4: 1,570 |
| Auto attacks (about 1.7) | 670 | 670 | 670 |
| Two Judgements on a stunned target (about 535 each) | 1,070 | 1,070 | 1,070 |
| **Total** | **3,130** | **2,130** | **3,700** |

All values are approximate.

- **Result.** The proposal is about 47% above the usual beta burst. It is about 15% below the best beta burst (the Classic bomb with 4 stored attacks).
- **Uncertainty.** About ±25%: 2,350–3,900.
- **Swift Judgement** gives about 17% of the burst. When Swift Judgement is on cooldown (60 sec, and 50 sec for Hammer of Justice), the proposed total is about 2,590. It is on the watch list (W6).

### Mana

This section compares the mana of the Paladin in the beta and with the proposals. The unit is mana per second (MPS). A positive value means that the mana increases. A negative value means that the mana decreases.

#### Summary

- A Protection Paladin at fresh level 60 has almost no extra mana when tanking: +3.9 MPS with the proposals, +1.5 MPS in the beta.
- The tank gets more mana with better gear. In Naxxramas, the tank gets +29.8 MPS with the proposals.
- C13 (Shield Specialization once each 2 sec) is necessary. Without C13, a fresh level 60 tank loses about 9 MPS.
- Consecration uses much mana. Use it against groups of enemies, not all the time.
- C17 (Twist of Light) fixes the mana of Retribution.

#### 1. Problems in the beta

- **Spirit regeneration stops when you cast.** It gives 15 + Spirit ÷ 5 mana each 2 sec. It stops for 5 sec after each cast. In combat, it is almost zero.
- **Protection and Retribution have no talent for regeneration while casting.** Other classes give 50% to their damage and hybrid specs at about 20 points (see What the other classes have).
- **Protection gets mana only when it is hit.** Shield Specialization and Improved Seal of Fury give this mana. A Protection Paladin who does not tank gets no mana.
- **Retribution loses mana because of Seal swaps.** The cause is not the regeneration.

#### 2. Fixes

| Fix | Effect |
| --- | --- |
| Reverence in row 2 at 50% (C1) | Protection and Retribution get regeneration while casting with 8 Holy points. This gives about 10 MPS. Enhancement Shaman gets Mindfulness in the same way |
| Shield Specialization once each 2 sec (C13) | It stays the main mana source of the tank. Water Shield (Shaman) is the Forever precedent |
| Improved Seal of Fury removed (C10) | One talent for "mana when you are hit" is sufficient |
| Echo of 10 sec (C17) | Retribution changes Seals one time each 10 sec, not before each swing |

#### 3. Inputs

**Gear**

- Maximum mana and mp5 come from the gear tiers (see Threat, part 2).
- Fresh level 60 uses the real gear profile: 2,897 mana, 3 mp5.
- Tank gear does not give much Spirit. All tiers use 130 Spirit.

**Combat**

- The boss swings each 2.0 sec.
- One-handed weapon: 2.7 sec.
- Block: 50% in the beta, 60% with C6.

**Spell costs at level 60 (Forever spellbook)**

| Spell | Cost |
| --- | --- |
| Holy Shield rank 3 | 240 mana, each 10 sec |
| Holy Strike | 20 mana, each 10 sec |
| Judgement | 91 mana (6% of base mana 1,512), each 10 sec |
| Seal of Fury rank 7 | 200 mana, each 30 sec |
| Seal of Command | 210 mana |
| Consecration rank 5 | 565 mana, each 8 sec |

- Base mana 1,512 is the Classic value. It is not confirmed for Forever.
- The Retribution dip gives Benediction (all costs ×0.90) and Holy Conduit (Consecration ×0.60).
- Raid buffs are not in the model. Blessing of Wisdom gives 8 MPS. Judgement of Wisdom on the boss gives more.

#### 4. Protection results

**Mana income while tanking**

| Source | Beta | Proposed | Calculation |
| --- | --- | --- | --- |
| Shield Specialization | Maximum mana × 4% ÷ 6 sec | Maximum mana × 4% × 60% ÷ 2 sec | Beta: the 3 sec limit skips the next swing. 50% block. Proposed: each block counts (C13). 60% block (C6) |
| Improved Seal of Fury | 23.3 | 0 (C10) | 87 mana for each shield that a boss hit uses |
| Reverence 50% (C1) | 0 | 10.3 | Half of 41 mana each 2 sec, at 130 Spirit |
| mp5 from gear | 0.6–2.4 | 0.6–2.4 | 3–12 mp5 |

**Mana used**

| Case | MPS |
| --- | --- |
| Tanking, no Consecration | 41.7 |
| Tanking, Consecration on cooldown | 112.4 |
| Tanking, no Consecration, Retribution dip | 37.6 |
| Tanking, Consecration on cooldown, Retribution dip | 75.7 |

The costs do not change with gear.

**Income and result for each gear tier (tanking, no Consecration)**

| Tier (maximum mana) | Income, beta | Income, proposed | Result, beta | Result, proposed | Result, proposed, flatter gear |
| --- | --- | --- | --- | --- | --- |
| Fresh level 60 (2,897) | 43.2 | 45.6 | +1.5 | +3.9 | +3.9 |
| Pre-raid best in slot (3,400) | 47.0 | 52.0 | +5.3 | +10.3 | +10.3 |
| Molten Core (3,900) | 50.9 | 58.6 | +9.2 | +16.9 | +13.7 |
| Blackwing Lair (4,400) | 54.6 | 65.0 | +12.9 | +23.3 | +16.9 |
| Naxxramas (4,900) | 58.4 | 71.5 | +16.7 | +29.8 | +20.1 |

"Flatter gear" uses the model of Threat, part 3.

**Other cases: MPS and time until the mana is zero**

| Case | Fresh level 60, beta | Fresh level 60, proposed | Naxxramas, beta | Naxxramas, proposed |
| --- | --- | --- | --- | --- |
| Tanking, Consecration on cooldown | −69.2: 42 sec | −66.8: 43 sec | −54.0: 1 min 30 sec | −41.0: 1 min 59 sec |
| Tanking, Consecration on cooldown, Retribution dip | −32.5: 1 min 29 sec | −30.1: 1 min 36 sec | −17.3: 4 min 42 sec | −4.2: 19 min |
| Not hit, no Consecration | −41.1: 1 min 10 sec | −30.9: 1 min 33 sec | −39.3: 2 min 4 sec | −29.1: 2 min 48 sec |
| Not hit, Consecration on cooldown | −111.8: 26 sec | −101.5: 29 sec | −110.0: 45 sec | −99.7: 49 sec |

#### 5. Retribution results

One target. Sanctified Judgement returns 126 mana (60% of the base cost of the Seal) for each Judgement. Tests show this.

| Case | Mana used | Time until zero, no regeneration (2,897 → 4,900 mana) | Time until zero, with Reverence 50% (9.75 MPS) |
| --- | --- | --- | --- |
| Beta: about 3 Seals each 10 sec | 41.6 MPS | 1 min 10 sec → 1 min 58 sec | 1 min 31 sec → 2 min 34 sec |
| C17: one Seal each 10 sec | 11.4 MPS | 4 min 14 sec → 7 min 10 sec | 29 min → 49 min |

#### 6. What the results mean

- **The tank gets more mana with gear.** Shield Specialization returns 4% of maximum mana for each block. More mana gives a larger return.
- **At fresh level 60, the tank has almost no extra mana.** It gets +3.9 MPS with the proposals. Without C13, it loses about 9 MPS.
- **In raids, the tank does not lose mana without Consecration.** It gets +10 to +30 MPS (beta: +5 to +17).
- **Consecration on cooldown uses all mana quickly:** in 43 sec at fresh level 60, in about 2 min in Naxxramas. With the Retribution dip, it lasts 1 min 36 sec to 19 min.
- **Reverence helps when the Paladin is not hit.** It gives 20–45 sec more without Consecration.
- **Flatter gear gives less mana.** In late raids, the tank gets +14 to +20 MPS. C13 is then more important.
- **Intellect is a tank stat for the Paladin.** It gives more mana. It also increases the Shield Specialization return.
- **Retribution with C17 almost does not lose mana** when it has Reverence.

### Tree balance

Two checks:

1. Rows 1 and 2 must give something to the other specs.
2. Talents must be equal to the talents of other classes.

| Tree | Talents in rows 1–2 for other specs | Specs that use them | Cost |
| --- | --- | --- | --- |
| Holy | Improved Seals (+15% Seal damage), Divine Intellect, Infusion of Light, Reverence, Unyielding Faith | Retribution and Protection (Seal damage, mana regeneration, faster Holy Light). Casters (Intellect) | 5–8 points |
| Retribution | Deflection, Benediction, Improved Judgement, Holy Conduit, Conviction | Protection (parry, critical hit, mana costs). Holy (Benediction, Holy Conduit) | 5–10 points |
| Protection | Divine Strength, Precision (+3% hit), Guardian's Favor | All specs (Strength, hit). Holy (Guardian's Favor in PvP) | 5–8 points |

**Parity with other classes**

- Divine Intellect = Ancestral Knowledge (Shaman, +10%).
- Deflection = Deflection (Warrior).
- Conviction = Cruelty (Warrior, +5%).
- Benediction = Convection (Shaman, −10%).
- Anticipation = Anticipation (Warrior, +20 Defense).
- Divine Strength = Heart of the Wild (Druid).

**Points in each tree.** Beta: Holy 46, Protection 48, Retribution 44. Proposed: Holy 44, Protection 47, Retribution 44.

## Beta test results

### Holy talents

| Talent | Result in the beta | Effect on the proposals |
| --- | --- | --- |
| Divine Strength, Divine Intellect | % of base, gear and flat buff stats. Multiplies with Kings | Divine Strength goes to Protection (C8) |
| Healing Light | Increases the full heal, not only the base | Supports C2: a second flat healing talent would overlap |
| Spiritual Focus | Adds to other pushback resistance (Concentration Aura 35% + 70% = immune) | None |
| Improved Seals | Increases the full damage, not only the base. No effect on Seal of the Crusader | None |
| Unyielding Faith | Diminishing returns not tested | None |
| Reverence | Keeps a % of Spirit regeneration while casting. The 5-second rule starts again when a cast ends | Supports C1 |
| Purifying Power | Multiplies with Benediction (×0.80 × 0.90) | None |
| Illumination | Returns 50% of the base cost. Cost decreases do not decrease the return | None |
| Divine Favor | Not on the global cooldown | None |
| Divine Precision | The spell hit cap is 18%, with no fixed 1% miss. 3/3 gives the full cap | None |
| Holy Shock | Damage uses spell damage. Healing uses healing power. Both at 42.9% | None |
| Consecrated Ground | Increases all your Holy damage on those targets, also Retribution Aura and Consecration | None |
| Light's Vigil | 3 ranks: 730, 1,000 and 1,340 mana. Rank 3 heals each party member for 684–724 | None (see Withdrawn ideas) |

### Protection talents

| Talent | Result in the beta | Effect on the proposals |
| --- | --- | --- |
| Toughness | Only armor from items. Nothing from Devotion Aura, scrolls, elixirs, potions or Mark of the Wild | Supports C8 |
| Redoubt | A blocked hit can start it without the use of a charge | C6 keeps the proc |
| Precision | Melee, ranged and spell hit. Each ability uses the correct hit type | Confirms it as the shared hit talent |
| Anticipation | A raid boss stops critical hits at 440 Defense. Anticipation gives 20 | The stat targets use this cap |
| Improved Seal of Fury | The mana return does not change with the rank of the Seal. The mana gives no threat | Removed by C10 |
| Improved Righteous Fury | Applies after armor. Multiplies with Iron Creed (×0.94 × 0.90) | Removed by C9 |
| Shield Specialization | Multiplies Shield Block Value. Mana return is 4%. The mana gives no threat | Stays the main mana source. C13 changes the limit to 2 sec |
| Sacred Duty | % of total Stamina, multiplies with Kings. Decreases the cooldowns of Forbearance spells | None |
| Swift Judgement | Not on the global cooldown | None |
| One-Handed Weapon Specialization | Melee attacks, Seals, Judgements, Holy Strike and the Twist of Light Echo | None |
| Templar's Bulwark | An absorb, not a heal. Mortal Strike effects do not decrease it | None |
| Reckoning | Stored attacks hit with the next melee hit. Each can trigger Seals and Judgements | C11: Holy Strike releases the charges |
| Iron Creed | Holy Strike threat ×1.90 (Righteous Fury) × 1.25 | C7 keeps these multipliers |
| Holy Shield | Threat ×1.90 (Righteous Fury) × 1.20. More tests are necessary | None |

### Retribution talents

| Talent | Result in the beta | Effect on the proposals |
| --- | --- | --- |
| Benediction | Its cost decrease multiplies with Purifying Power, Holy Conduit and Twist of Light | None |
| Holy Conduit | With Benediction, Consecration costs ×0.60 × 0.90 | None |
| Conviction | Also applies to damage Seals and Hammer of Wrath | C15 adds only Holy Shock, Exorcism, Consecration and heals |
| Vindication | About 5 procs each minute. Ranks: −67/136/204 Attack Power on the target and +1/2/3% on you | None |
| Sanctified Judgement | Returns more than 60% of the base cost of the Seal with Benediction | Possibly a bug (see Problems to report to Blizzard) |
| Pursuit of Justice | 15% at 2/2. Better than the 8% boot enchant | On the watch list (W1) |
| Eye for an Eye | Uses the damage taken after armor and resistance | None |
| Sacred Arbiter | +20% Holy Strike damage. Refreshes Light, Wisdom, Justice and Crusader | C16 replaces the +20% with the Seal trigger |
| Two-Handed Weapon Specialization | Melee attacks, Seals, Judgements, Holy Strike and the Twist of Light Echo | Supports M6 |
| Vengeance | Multiplies with other % damage. Critical hits from procs add stacks | None |
| Repentance | Diminishing returns category not tested | None |
| Instrument of Law | Rank 2 makes Hammer of Wrath instant. The threat decrease multiplies with Salvation | None |
| Twist of Light | More tests are necessary. With Benediction, Seals cost ×0.72 | None |

### Spells

| Spell | Result in the beta | Source |
| --- | --- | --- |
| Holy Strike | Uses normalized weapon damage. The Holy part uses 0.429 × weapon %: 21.45% of spell power at rank 8. Does not trigger Seal of Fury, Righteousness or Command. Triggers Seal of Light, Justice and Wisdom | Player tests |
| Seal of Fury | 10% of spell power for each hit (11.5% with Improved Seals). No Attack Power. Critical hit: ×2 damage, with a separate roll. Cannot miss | Player tests |
| Seal of Righteousness | 10% of spell power with a one-handed weapon, 12% with a two-handed weapon. Weapon speed has no effect | Player tests; patch note, 16 October |
| Seal of Command | 29% × 70% weapon damage = 20.3% of spell power. 7 procs each minute. Uses the melee hit table | Player tests |
| Judgement of Fury, Righteousness and Command | 42.9% of spell power. Melee hit table. Critical hit: ×2 damage. Judgement of Command: ×2 damage against a stunned target | Player tests; patch note, 16 October |
| Judgement of Fury | The damage hits before the taunt. The taunt copies the top threat. The threat from the damage is not added. The taunt does not remove Judgement of the Crusader | Player tests |
| Judgement of the Crusader | The bonus uses the coefficient of each spell, as spell power does. Seal of Command gets the full 29% | Player tests |
| Consecration | 0.042 of spell power for each tick (33.6% for each target). First 4 enemies only | Patch note, 16 October |
| Retribution Aura | 6% of spell power | Patch note, 8 October |
| Holy Shield | Spell power scaling is not known. Classic: 5% for each block | Classic data |
| Mana return | Mana from Shield Specialization, Improved Seal of Fury and Sanctified Judgement gives no threat | Patch notes, 8 and 16 October |
| Rage | Rage from damage taken was repaired on 8 October. It uses 20–40% armor, related to level. Critical hits give ×2 rage. Bear Form: ×1.5 threat | Patch note, 8 October |

## Problems to report to Blizzard

- **Judgement of Fury: the damage hits before the taunt.** The taunt must apply first. Then the Paladin gets a small threat lead, not only equal threat.
- **Holy Strike triggers only some Seals.** It triggers Seal of Light, Justice and Wisdom. It does not trigger Seal of Fury, Righteousness or Command. C16 makes this consistent for Retribution.
- **Sanctified Judgement with Benediction** returns more than 60% of the base cost of the Seal. This is possibly a bug.

## Watch list

These are risks to check in tests. None of them needs a change now.

| # | Risk | Action if it occurs |
| --- | --- | --- |
| W1 | Pursuit of Justice (+15% speed at 10 Retribution points) is better than the boot enchant | Decrease it to 10% if all Paladins take it |
| W2 | Sacred Duty gives Divine Shield −60 sec at 10 Protection points. This is a PvP dip | Decrease it to −30 sec if all players take it |
| W3 | Retribution gets Strength and 3% hit with one 8-point Protection dip | Monitor |
| W4 | A 7-point Retribution dip decreases the mana that Protection uses with Consecration from about 112 to 76 per sec | Monitor: all Protection players can take this dip |
| W5 | Holy is the main dip for the two other trees (Seal damage, Infusion of Light, Reverence, Consecrated Ground) | Monitor: Retribution and Protection still give parry, critical hit, mana costs, Strength and hit |
| W6 | Reckoning (C11): a 0/26/25 two-handed build bursts for about 3,130 in one Hammer of Justice stun | Monitor: this is below the best beta case (about 3,700). Swift Judgement gives about 17% of it |
| W7 | Iron Creed (C7) gives −10% damage taken to all specs with Righteous Fury and 25 Protection points | Monitor in PvP. This is the one exception to the rule on talents that improve a buff |
| W8 | Fury's Reach (C12): a 15-point Protection dip with Swift Judgement gives a 20 yard Judgement | Monitor: the range works only with Seal of Fury |
| W9 | Repentance at 15 Retribution points (M7) and Templar's Bulwark (an absorb of 100% of health, three times Last Stand) are strong PvP dips | Monitor |
| W10 | Shield Specialization (C13) can make Consecration too cheap against groups that hit fast (up to 58–98 mana per sec, related to maximum mana) | Go back to 3 sec, or decrease the return from 4% to 3% |
| W11 | Protection threat in late raids depends on C14 and on the block value of Forever gear (see Threat, part 2) | Change the 200% of C14. Then Iron Creed +100% Holy Strike threat. A shield attack only as the last step |

## Open questions

- [ ] Forever changed the spell hit cap. Did the crushing blow rules also change? A test against a raid boss can confirm the stat targets.
- [ ] Do the effects that keep regeneration while casting add together (maximum 100%) in Forever, as in Classic?
- [ ] Does C15 (Conviction for spells) make a Holy dip into Retribution too strong for healers?
- [ ] Must Retribution have a group buff, as Leader of the Pack (Druid)? Or is the Attack Power debuff of Vindication sufficient?
- [ ] Is a 20 yard pull worth 3 Protection points (C12)?
- [ ] Does Judgement use the global cooldown in Forever? The C17 table assumes that it does.
- [ ] Does the Holy Shield damage increase with spell power? By how much for each block?
- [ ] Does Shield Slam have a threat multiplier, as Revenge (×2.25) has? (Warrior testers)
- [ ] Do Heroic Strike and Maul hits give rage? (Warrior and Druid testers)
- [ ] Champion of the Light: the patch note of 16 October gives 10/20/30% of Intellect. The client data of 18 October gives 20/40/60%. Which value is live?
- [ ] How much block value do Forever shields and tank gear give at each tier? The 200% of C14 uses Classic values.

**Answered**

- [x] Does Judgement of Fury remove your own Judgement of the Crusader? No (player test).
- [x] Vindication ranks: −67/136/204 Attack Power on the target and +1/2/3% on you.
- [x] Shield Specialization mana return: 4%.
- [x] Spell hit cap: 18%, with no fixed 1% miss.
- [x] Champion of the Light needs 28 Retribution points for 3/3 (row 6).
- [x] Level 60 costs (Forever spellbook): Seal of Fury rank 7: 200 mana. Seal of Command: 210. Consecration: 565. Holy Shield rank 3: 240.
- [x] Light's Vigil has 3 ranks: 730, 1,000 and 1,340 mana.

## Withdrawn ideas

We examined these ideas and rejected them. They are not proposals.

| Idea | Why it was rejected |
| --- | --- |
| Light's Vigil from 730 to about 500 mana | The estimate used rank 1. At level 60, rank 3 plus Holy Shock rank 4 costs 1,665 mana and heals about 3,840 on 5 players: 2.3 healing for each mana point. Holy Light rank 9 gives 2.4 on one target. At rank 1 (level 40), it is already better than Holy Light rank 6 (2.0 and 1.8) |
| One-Handed Weapon Specialization increases all damage while you have a shield | The beta talent already increases all damage, but not Consecration and Retribution Aura |
| Unyielding Faith decreases spell threat | Not necessary: Salvation does not use a Blessing slot now. A threat decrease must not affect Protection |
| Holy Shield +35% or +40% block | With the Redoubt trigger, +30% already gives the same result as the Warrior. +35% is better than the Warrior. +40% also removes critical hits below 440 Defense |
| Holy Strike critical hits reset Hammer of Wrath | Hammer of Wrath has a 6 sec cooldown, shorter than the 10 sec of Holy Strike. It works only below 20% health: about +1 damage per sec |
| Champion of the Light adds healing | At 60% of Intellect, it gives the same healing as deep Holy. Holy Paladins would go into Retribution. Possible at 10/20/30%, because C4 puts Healing Light too deep for a Retribution hybrid |
| Sacred Ward (critical heals add a shield) | The same talent as Divine Aegis (Priest). Lingering Light (C2) replaces it |
| Other ideas for the new Holy talent (heal splash, aura bonus, Cleanse, Lay on Hands) | Too modern, or utility and not healing |
| Steadfast Faith (stun duration) in Protection row 1 | Two talents against crowd control. Other classes have one |
| Toughness that also gives Stamina | Divine Strength from Holy (C8) replaces it |
| Hallowed Ground or Shield Specialization in Protection row 1 | Talents only for tanks. Holy and Retribution would lose 5 points before Precision |
| A mana talent in each tree (Iron Creed, Righteous Fury, Seal of Fury) | Reverence in row 2 does the same with one talent. Holy could use the Righteous Fury and Seal of Fury versions |
| Survive crushing blows with more armor, health and a stronger Seal of Fury absorb | Healers would still get the damage spikes. C6 removes the crushing blows |
| Holy Shield or Seal of Fury changes crushing blows into normal hits | It goes around the attack table |
| Redoubt charges that each add a % of block | Block buffs with charges give one fixed bonus |
| Redoubt on each hit with a 6 sec cooldown | The Holy Shield trigger gives the same uptime with no new rule |
| Bring back Improved Blessing of Wisdom or Improved Lay on Hands | Forever removes talents that improve a buff |
| Move Precision into Retribution | The Protection dip for hit is intentional |
| Exchange Light's Vigil and Holy Power | Each tree ends with a 1-point talent |
| Divine Precision below 18% | Holy Precision (Priest) is the same, and the spell hit cap is 18% |
| Two-Handed Weapon Specialization at 10% | 6% is already more than the 3% of the Warrior |
| Fix the flat ranks of Vindication | Forever already changed it |
| Reckoning works only with a shield | It would stop the Classic two-handed Reckoning bomb |
| Holy Strike releases all 4 Reckoning charges | The 0/26/25 burst would be about 3,910, not 3,130 (+25%) |
| Reckoning at 40% chance, once each 1.5 sec | Not sufficient charges on a boss (about 1.6 extra attacks each 10 sec) |
| Reckoning at 100% chance, once each 1.5 sec | The charges stay at the maximum of 4. More than half of the procs are lost. You cannot choose when to keep charges |
| Exchange Reckoning (row 5) and Iron Creed (row 6) | Reckoning then costs 25 points, but this does not stop a 0/30/21 hybrid. The 2-charge limit does the job without a move |
| Iron Creed without the Holy Strike threat bonus | Simpler text, but about 10 TPS less |
| Aura Mastery or another talent that improves an aura | A talent that improves a buff, with low value (about −4% damage taken at 3 points). Fury's Reach (C12) gives the utility |
| Sacred Arbiter with +30% Holy Strike damage | About +8 damage per sec: too small for a 20-point talent |
| Two Seals active at the same time (not C17) | Fewer global cooldowns, but no Seal swaps. The talent is about Seal swaps |
| Two Judgements for each Paladin | More global cooldowns. This is against C17 |
| Judgement of the Crusader goes into Retribution (Holy Strike applies it) | A raid without a Retribution Paladin loses the debuff |
| Holy Shield does 3% of the damage of each blocked attack (not C14) | The same result as C14, but it uses damage taken, not a stat. It is difficult to read and to collect |
| Righteous Fury threat ×2.2 or ×2.5 (not ×1.9) | Flat: too strong early or too weak late. It also increases Consecration on all targets. It changes a baseline spell that Blizzard changed on 16 October |
| Holy Shield threat bonus +50% or +100% (not +20%) | Flat: +100% is better than the Warrior at fresh level 60. +50% is too weak in late raids |
| Iron Creed: +25% threat on all Holy damage | Flat. It works as an improved Righteous Fury. It does not increase with content |
| Righteous Fury also increases physical damage threat (×1.5) with a shield | Too weak in late raids (88% of the Druid). It changes Righteous Fury for all specs |
| Righteous Defense as an area taunt (10 yards, 6 sec, 10 min cooldown, as Challenging Shout) | The Paladin protects allies with Blessing of Protection. An area taunt with a 10 min cooldown gives little. C10 links a taunt to Blessing of Protection |
| A shield interrupt in Protection row 4 | Paladins have no interrupt by design |

## Sources

- [WoW Forever Talents – Paladin](https://wowforevertalents.com/paladin/)
- [WoW Forever Talents – Paladin spellbook](https://wowforevertalents.com/abilities/paladin/)
- [WoW Forever Talents – Warrior](https://wowforevertalents.com/warrior/)
- [WoW Forever Talents – Warrior spellbook](https://wowforevertalents.com/abilities/warrior/)
- [WoW Forever Talents – Druid](https://wowforevertalents.com/druid/)
- [WoW Forever Talents – Druid spellbook](https://wowforevertalents.com/abilities/druid/)
- [WoW Forever Talents – Priest](https://wowforevertalents.com/priest/)
- [WoW Forever Talents – Shaman](https://wowforevertalents.com/shaman/)
- [WoW Forever Talents – Hunter](https://wowforevertalents.com/hunter/)
- [WoW Forever Talents – Mage](https://wowforevertalents.com/mage/)
- [WoW Forever Talents – Changes from Classic](https://wowforevertalents.com/talent-changes/)
- [ForeverChanges – Paladin talents](https://foreverchanges.pro/talents/paladin)
- [Wowhead – Shield Block tooltip (Forever)](https://nether.wowhead.com/forever/tooltip/spell/2565)
- [Wowhead – Hammer of Wrath tooltip (Forever)](https://nether.wowhead.com/forever/tooltip/spell/24239)
- [RankedBoost – WoW Forever block and patch notes](https://rankedboost.com/world-of-warcraft/forever/stats/block/)
- [Blizzard – WoW Forever Paladin deep dive](https://news.blizzard.com/en-us/article/24302099/world-of-warcraft-forever-class-deep-dives-paladin)
- [Blizzard EU forums – WoW Forever Beta Development Notes, updated 15 October](https://eu.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-15-october/631316)
- [Blizzard forums – WoW Forever Beta Development Notes](https://us.forums.blizzard.com/en/wow/t/wow-classic-forever-beta-patch-notes/2360696)
- [Blizzard forums – No extra Rage on crit has been reverted](https://us.forums.blizzard.com/en/wow/t/warriors-rejoice-no-extra-rage-on-crit-has-been-reverted/2367562)
- [Icy Veins – WoW Forever reworked Warrior rage](https://www.icy-veins.com/wow-forever/news/wow-forever-just-reworked-warrior-rage-and-players-cant-stop-talking-about-it/)
- [Kami-labs – Consecration in WoW Forever](https://kami-labs.fr/en/wow-forever/consecration-wow-forever-quatre-cibles/)
- [Warcraft Tavern – Mage and Shaman deep dive](https://www.warcrafttavern.com/forever/news/scrolls-totems-mage-shaman-deep-dive-for-wow-forever/)
- [Outputlag – Seal of Fury tooltip](https://outputlag.com/news/world-of-warcraft-forevers-paladins-tank-with-seal-of-fury-and-a-10-yard-judgement-taunt/)
- [Notebookcheck – Blizzard on class simplicity](https://notebookcheck.net/WoW-Forever-won-t-modernize-Classic-classes-but-Blizzard-admits-some-were-too-simple.1424285.0.html)
