# Forever Paladin Talent Proposals

This document proposes 18 talent changes and 1 Judgement change for the WoW Forever Paladin. Three of the talent changes are new talents. The goal is to follow the rules Forever already uses for the other classes, without changing what each tree is about. Each proposal points to a talent that another class already has in the same beta build.

## How to read this document

- **IDs.** Each change has one ID, C1 to C19, numbered in the order of this document. C19a and C19b are the two alternatives to C19. Only active proposals have an ID. Ideas that were dropped are listed at the end, under Withdrawn ideas, and are not used anywhere else.
- **Each proposal** gives the change, the proposed tooltip, the reason and the talent it follows.
- **Data.** Forever client build 1.60.1.70450 with the server hotfixes of 18 October 2026, read from wowforevertalents.com. Tested behavior comes from player tests shared on 19 October 2026. Where an in-game tooltip was used instead, the text says so.
- **Limits.** These are design ideas, not tested in play. Combat and mana numbers use Classic 1.12 rules unless a test says otherwise. Every estimate lists its assumptions.
- **Calculator.** All proposals can be tried in the talent calculator, with a Beta/Proposed toggle.

## Summary

| ID | Talent | Tree and row | Beta | Proposed |
| --- | --- | --- | --- | --- |
| C1 | Reverence | Holy, row 2 | 10/20/30% of mana regen while casting | 17/33/50% |
| C2 | Lingering Light (new) | Holy, row 5 | — | 2 ranks: critical heals add a heal over time worth 15/30% of the heal |
| C3 | Infusion of Light | Holy, row 2 | Holy Shock and Flash of Light crits speed up the next Holy Light | Holy Strike crits also count |
| C4 | Holy layout | Holy, rows 2–6 | Healing Light in row 2 | Healing Light moves to row 6 with 2 ranks (6/12%); five other talents move up or across |
| C5 | Improved Seals | Holy, row 1 | Row 2, 3 ranks, 5/10/15% | Row 1, 5 ranks, 3/6/9/12/15%; replaces Divine Strength |
| C6 | Improved Hammer of Justice | Protection, row 3 | Row 4 | Row 3; same values (3 ranks, −5/10/15 sec) |
| C7 | Redoubt | Protection, row 1 | 10% chance on being hit: +4–20% block | Same, and every Holy Shield cast also triggers it |
| C8 | Iron Creed | Protection, row 6 | −2–10% damage taken for 6 sec after Holy Strike | −2–10% damage taken while Righteous Fury is active; same threat bonus |
| C9 | Divine Strength | Protection, row 1 | Toughness: +2–10% armor from items | Divine Strength (+2–10% Strength), moved from Holy |
| C10 | Righteous Defense (new) | Protection, rows 3–4 | Improved Seal of Fury and Improved Righteous Fury in row 3 | Both removed; Swift Judgement moves to row 3; new area taunt in row 4 |
| C11 | Reckoning | Protection, row 5 | Extra attack from block (40%) or being crit (100%); fires on the next swing | Charge from block, dodge, parry (once every 4 sec) or being crit; Holy Strike releases up to 2 |
| C12 | Fury's Reach (new) | Protection, row 4 | — | 2 ranks: Judgement range +5/10 yards while Seal of Fury is active |
| C13 | Shield Specialization | Protection, row 3 | Mana return at most once every 3 sec | At most once every 2 sec; nothing else changes |
| C14 | Holy Shield | Protection, row 7 | 221 Holy damage per block (rank 3) | 221 Holy damage plus 200% of your block value per block |
| C15 | Conviction | Retribution, row 2 | Melee crit +1–5% | Attack and spell crit +1–5% |
| C16 | Two-Handed Weapon Specialization | Retribution, row 4 | Opens at 20 points | Opens at 15 points |
| C17 | Sacred Arbiter and Repentance | Retribution, rows 4–5 | Sacred Arbiter at 15 points (+20% Holy Strike damage), Repentance at 20 | Rows swapped; Holy Strike always triggers your active Seal |
| C18 | Twist of Light | Retribution, row 7 | The Echo applies to the next melee attack only | The Echo applies to every melee attack for 10 sec |
| C19 | Judgement of the Crusader | Baseline | Uses the Paladin's one Judgement slot | Personal debuff outside the one-Judgement limit |

C19 has two alternatives in the Judgements section: C19a (fallback) and C19b (optional add-on).

## Design rules

Forever builds its talent trees with five rules. Every proposal follows them.

1. **No improved-buff talents.** Buffs such as Blessing of Kings come from the trainer, not from talents. Iron Creed (C8) is the one stated exception.
2. **Rows 1–2 tempt the other specs.** Early talents should make the other two specs want to put a few points into the tree.
3. **Shared stats cover melee and spells.** Precision gives hit for both, like Thundering Strikes gives crit for both to Shaman.
4. **Each tree has 1-point signature talents** in rows 3 and 4, and ends on a 1-point capstone at 30 points.
5. **The class fantasy stays.** Holy heals with the Light. Protection holds the line with a shield. Retribution judges with a two-handed weapon and Seals.

### What the other classes do

| Pattern | Other classes | Paladin beta |
| --- | --- | --- |
| Mana regen while casting (healers) | Meditation (Priest), Reflection (Druid), Mindfulness (Shaman): 50% | Reverence: 30% |
| Mana regen while casting (damage and hybrid specs) | 50% at about 20 points: Bestial Discipline, Resourcefulness (Hunter), Improved Stormstrike (Shaman), Spirit Tap (Priest) | None for Protection or Retribution |
| Deep healing bonus | Spiritual Healing (Priest, 25 points), Purification (Shaman, 25 points) | Healing Light (+12%) at 5 points |
| Shared crit | Thundering Strikes (Shaman, row 1): all spells and attacks | Conviction: melee only |
| Two-handed weapon talent | Warrior: 15 points | 20 points |
| Stun cooldown talent | Brutal Impact (Druid): 2 ranks, −15/−30 sec on Bash | Improved Hammer of Justice: 3 ranks, −5/−10/−15 sec |
| Area taunt | Challenging Shout (Warrior), Challenging Roar (Druid): 10 yards, 6 sec, 10 min | None |

## Holy

Most saved Holy builds stop around 20 points. These changes make the deep Holy talents worth taking for a healer, and give Retribution and Protection clear reasons to put a few points into Holy.

### Holy layout after C2, C4 and C5

| Row (points needed) | Talents | Points in the row |
| --- | --- | --- |
| 1 (0) | Improved Seals (C5), Divine Intellect | 10 |
| 2 (5) | Infusion of Light, Reverence, Unyielding Faith | 7 |
| 3 (10) | Voice of Truth, Purifying Power, Consecrated Ground | 5 |
| 4 (15) | Spiritual Focus, Illumination, Divine Favor | 8 |
| 5 (20) | Divine Precision, Holy Shock, Lingering Light (C2) | 6 |
| 6 (25) | Healing Light, Holy Power | 7 |
| 7 (30) | Light's Vigil | 1 |

Holy goes from 46 to 44 points. Every talent can be used when its row opens. Illumination still requires Reverence (straight arrow down column 2).

### C1. Reverence: 10/20/30% → 17/33/50%

- **Proposed text.** "Allows 17/33/50% of your Mana regeneration to continue while casting."
- **Model.** Meditation (Priest), Reflection (Druid) and Mindfulness (Shaman) all give 50% in 3 ranks.
- **Why Illumination is not enough.** Other healers also have a mana return on top of their 50% (Litany of Light, Water Shield, Mana Tide Totem). Forever also halved Illumination: it returns 50% of the base cost.
- **With C4.** Reverence moves to row 2, so it is also the regen talent for Protection and Retribution (see Mana).
- **If it proves too strong:** 13/27/40%.

### C2. New talent: Lingering Light (row 5, column 3, 2 ranks)

- **Proposed text.** "Your non-periodic critical heals cause the target to be healed for an additional 15/30% of the amount healed over 6 sec. Refreshing this effect carries over any remaining healing."
- **Identity.** A heal over time from crits is a Paladin idea (Sheath of Light in a later expansion). It is not Priest's Divine Aegis, which is a shield, and it is Holy's only heal over time.
- **Wording.** "Non-periodic critical heals" comes from Priest's Divine Aegis and Inspiration. "Refreshing this effect carries over any remaining healing" comes from Priest's Blessed Recovery, which already rolls its healing in Forever.
- **Why crit.** Healing Light already gives a flat healing bonus. The Holy tree invests in crit (Illumination, Infusion of Light, Divine Favor, Holy Power), and this talent pays it off.
- **Value.** At 25% crit: 25% × 30% = about +7.5% healing. Part of it overheals on full targets.

**How it rolls.** It follows Forever's Ignite and Blessed Recovery, not Deep Wounds.

|  | Ignite (Mage) | Deep Wounds (Warrior) | Lingering Light |
| --- | --- | --- | --- |
| Amount | 8–40% of the crit's damage | 20–60% of average weapon damage, the same for every crit | 15/30% of the crit heal |
| Duration | 4 sec, a tick every 2 sec | 12 sec | 6 sec, a tick every 2 sec |
| New crit while active | Remaining damage is kept and added | Refreshes the duration only | Remaining healing is added, then spread over a new 6 sec |
| Per caster | One per Mage per target | One per target | One per Paladin per target |

- **Amount.** Taken from the full crit heal, overhealing included.
- **No double bonus.** Healing bonuses apply once, to the crit. The heal over time is not increased again and cannot crit.
- **In play.** Repeated crits on the tank build a bigger heal over time. Divine Favor on Holy Light gives a planned large one. Holy Shock crits (+15% crit from Holy Power) add frequent small amounts.

### C3. Infusion of Light: Holy Strike crits also count

- **Proposed text.** "Your Holy Shock, Holy Strike and Flash of Light critical hits reduce the cast time of your next Holy Light cast within 15 sec by 0.5/1 sec."
- **What changes.** Only Holy Strike is added. Values and duration stay as in the beta.
- **Why.** Holy Power gives +15% crit to both Holy Shock and Holy Strike, but only Holy Shock feeds Infusion of Light today.
- **In play.** A Holy Paladin who melees between heals gets a reason to use Holy Strike. Retribution and Protection, who use Holy Strike in their rotation, get faster emergency Holy Lights.
- **Limit.** Holy Strike has a 10 sec cooldown, so it adds at most one chance every 10 sec.
- **Risk.** With C4 it is in row 2, so a 7-point Holy dip gives Retribution or Protection a faster self-heal in PvP. The 10 sec cooldown keeps it small.

### C4. Holy layout: Healing Light moves to row 6

| Talent | Beta | Proposed | Why |
| --- | --- | --- | --- |
| Healing Light | Row 2, 3 ranks (4/8/12%) | Row 6, 2 ranks (6/12%) | Puts the +12% healing bonus at 25 points, like Spiritual Healing and Purification. A Holy Paladin with 28 points in Retribution has only 23 for Holy and can't reach it |
| Infusion of Light | Row 4 | Row 2 | Retribution and Protection keep a healing reason to dip into Holy: faster heals, not bigger ones |
| Reverence | Row 3 | Row 2 | Gives Protection and Retribution regen while casting for 8 Holy points, like Enhancement Shaman reaches Mindfulness with 8 Restoration points |
| Consecrated Ground | Row 5 | Row 3 | Row 3 opens at level 20, when Consecration is learned. Protection reaches it with 12 Holy points instead of 22, for area threat |
| Spiritual Focus | Row 2 | Row 4 | Makes room in row 2. Spell pushback only matters to healers |
| Lingering Light (C2) | — | Row 5 | Next to Holy Shock, whose crits trigger it |
| Unyielding Faith | Row 2, column 4 | Row 2, column 3 | Fills the slot left when Improved Seals moves to row 1 (C5), so row 2 has no empty slot between talents |

- **Deep Holy** keeps Healing Light, Holy Power, Lingering Light and Light's Vigil, so going deep stays clearly better for healing.
- **Cost.** A leveling Holy Paladin gets the full +12% healing at level 36 instead of level 17.

### C5. Row 1: Improved Seals replaces Divine Strength

- **Proposed text.** "Increases the damage done by your Seals and Judgements by 3/6/9/12/15%."
- **What changes.** Improved Seals moves from row 2 (3 ranks, 5/10/15%) to row 1 with 5 ranks. Max rank stays 15%. Divine Strength leaves Holy and moves to Protection row 1 (C9).
- **Dip.** 5 Holy points now give +15% Seal and Judgement damage to Retribution and Protection. Seals are the class's own damage, so this dip is more Paladin-specific than Strength.

### Holy: beta test results

| Talent | Observed in the beta | Effect on the proposals |
| --- | --- | --- |
| Divine Strength, Divine Intellect | % of base, gear and flat-buff stats; multiplies with Kings | Divine Strength moves to Protection (C9) |
| Healing Light | Boosts the whole heal, not just its base | Supports C2: a second flat healing talent would overlap |
| Spiritual Focus | Adds to other pushback resistance (Concentration Aura 35% + 70% = immune) | None |
| Improved Seals | Boosts the whole damage, not just its base; doesn't affect Seal of the Crusader | None |
| Unyielding Faith | Diminishing returns not tested | None |
| Reverence | Keeps a % of Spirit regen while casting; the 5-second rule restarts when a cast ends | Supports C1 |
| Purifying Power | Multiplies with Benediction (×0.80 × 0.90) | None |
| Illumination | Returns 50% of the base cost, so cost discounts don't reduce the return | None |
| Divine Favor | Off the global cooldown | None |
| Divine Precision | The spell hit cap is 18% with no unavoidable 1% miss; 3/3 covers it alone | None |
| Holy Shock | Damage scales with spell damage, healing with healing power; both at 42.9% | None |
| Consecrated Ground | Boosts all your Holy damage on those targets, including Retribution Aura and Consecration | None |
| Light's Vigil | 3 ranks: 730, 1,000 and 1,340 mana; rank 3 heals each party member for 684–724 | None (see Withdrawn ideas) |

## Protection

Protection gets a fix for crushing blows (C7), its biggest gap with Warrior, a cleaner tree (C6, C8, C9, C10), a Reckoning that works at endgame (C11), a ranged pull (C12), steadier tanking mana (C13) and threat that grows with gear (C14).

### Protection layout after C6, C9, C10 and C12

| Row (points needed) | Talents | Points in the row |
| --- | --- | --- |
| 1 (0) | Divine Strength (C9), Redoubt | 10 |
| 2 (5) | Precision, Guardian's Favor, Anticipation | 10 |
| 3 (10) | Swift Judgement, Improved Hammer of Justice (C6), Shield Specialization, Sacred Duty | 9 |
| 4 (15) | Fury's Reach (C12), One-Handed Weapon Specialization, Righteous Defense (C10) | 6 |
| 5 (20) | Templar's Bulwark, Reckoning | 6 |
| 6 (25) | Iron Creed | 5 |
| 7 (30) | Holy Shield | 1 |

Protection goes from 48 to 47 points. Rows 1–4 hold 35 points, more than the 20 needed to open row 5.

### C6. Improved Hammer of Justice: moves to row 3

- **Proposed text.** "Decreases the cooldown of your Hammer of Justice spell by 5/10/15 sec." Same 3 ranks and values as the beta. Only the row changes.
- **Model.** Druid's Brutal Impact on Bash, which also has a 60 sec base cooldown.
- **Why.** It is one of the least-taken Paladin talents, and C10 frees space in row 3.
- **PvP.** Holy or Retribution now reach the full −15 sec (a 45 sec Hammer of Justice) with 13 Protection points instead of 18. Druid has Brutal Impact in Feral row 2 (−30 sec on Bash), so this stays in line.

### C7. Redoubt: Holy Shield also triggers it

- **Proposed text.** "Damaging melee attacks against you have a 10% chance to increase your chance to block by 4/8/12/16/20%. Lasts 10 sec or 5 blocks. Casting Holy Shield also triggers this effect."
- **What changes.** Only the Holy Shield trigger is new. Triggering Redoubt while it is active resets it to 10 sec and 5 blocks.
- **Why.** It removes most crushing blows. See Crushing blows below.
- **Blizzard's direction.** The October 1 patch moved block from Redoubt (6–30% → 4–20%) to Holy Shield (20% → 30%). C7 keeps those values. Redoubt only gains uptime.
- **Other specs.** Holy and Retribution don't have Holy Shield, so their Redoubt doesn't change.
- **Side effects.** Block from talents goes from about 40% on average (30% Holy Shield + about 10% Redoubt) to 50%. This gives slightly more Reckoning charges, Shield Specialization mana and Holy Shield damage.

### C8. Iron Creed: damage reduction while Righteous Fury is active

- **Proposed text.** "Increases the threat generated by your Holy Strike ability by 5/10/15/20/25%. While Righteous Fury is active, reduces your damage taken by 2/4/6/8/10%."
- **Problem.** In the beta the reduction lasts 6 sec after a Holy Strike, which has a 10 sec cooldown. At 5/5 it averages 6 sec ÷ 10 sec × 10% = 6%.
- **Change.** The reduction works whenever Righteous Fury is active. It has no timer and no Holy Strike condition, so Holy Strike keeps only one extra mechanic (Reckoning, C11).
- **Threat bonus kept.** +25% Holy Strike threat is worth about 11 threat per second at 5/5 and 200 spell power (see Threat).
- **Total.** −10% damage taken, the same as Warrior's Defensive Stance. Improved Righteous Fury, which stacked to about 15% in total, is removed by C10.
- **Rule exception.** It works like an improved Righteous Fury, but it needs 25 Protection points. Watch it in PvP, because any spec can use Righteous Fury.

### C9. Toughness → Divine Strength (from Holy)

- **Proposed text.** "Increases your Strength by 2/4/6/8/10%." Same as the beta. Only its tree changes.
- **Why remove Toughness.** Forever moved away from flat armor talents for tanks: Warrior's Toughness was removed, Shaman's now gives Stamina, and Druid's Thick Hide grows with Defense. Paladin's Toughness was the last flat armor talent.
- **Why Divine Strength.** Strength is the Protection Paladin's stat: Attack Power for threat, and block value (20 Strength = 1). Holy no longer needs it (C5).
- **Row 1 for every spec.** Holy and Retribution pass through Protection row 1 to reach Precision, and Divine Strength is useful to all three specs.
- **Parity.** One % Strength talent for the class, like Druid's Heart of the Wild. No extra Stamina talent: only Sacred Duty's +4%.

### C10. Rows 3–4: remove two talents, add Righteous Defense

- **Improved Righteous Fury: removed.** With Iron Creed always active (C8), the two stacked to about 15% damage reduction. Iron Creed alone gives Warrior's 10%.
- **Improved Seal of Fury: removed.** It was a second "mana from being hit" talent, and its return ignores the Seal's rank. Reverence in row 2 (C4) is the mana talent instead (see Mana).
- **Swift Judgement moves to row 3** and no longer needs Improved Seal of Fury.
- **New: Righteous Defense (row 4, column 3, 1 point).** "Forces all enemies within 10 yards to attack you for 6 sec." Instant, 10 min cooldown.
  - It matches Warrior's Challenging Shout and Druid's Challenging Roar: same range, duration and cooldown.
  - Judgement of Fury stays the single-target taunt.
  - Every tree keeps a 1-point signature talent in rows 3 and 4: Holy has Voice of Truth and Divine Favor, Retribution has Seal of Command and Repentance (after C17), Protection has Swift Judgement and Righteous Defense.
  - Holy and Retribution can reach it with 15 points but have no use for an area taunt.
- **Unchanged.** Righteous Fury, Seal of Fury and its absorb shield stay baseline.

### C11. Reckoning: charges from avoidance, released by Holy Strike

- **Proposed text.** "Gives you a 20/40/60/80/100% chance to gain an extra attack after Blocking, Dodging, Parrying or being the victim of a non-periodic critical strike. Cannot occur from Blocks, Dodges or Parries more than once every 4 sec. Stores up to 4 extra attacks. Your Holy Strike releases up to 2 stored extra attacks."
- **Beta text.** "Gives you a 8/16/24/32/40% chance after Blocking and a 20/40/60/80/100% chance after receiving a non-periodic critical strike to gain an extra attack. Stores up to 4 extra attacks. Cannot occur from Blocks more than once every 1.5 sec."
- **Wording.** Follows Classic's extra-attack effects: Reckoning, Sword Specialization and Hand of Justice.

**Problems in the beta**

- **The crit trigger does nothing at endgame.** At 440 Defense a raid boss can't crit (see Stat targets), so half the talent only works while leveling or in PvP.
- **Storage does nothing while tanking.** A tank attacks all the time, so a stored attack fires on the next swing. Storage only matters when you stop attacking (the Classic "Reckoning bomb").
- **Low value on a boss:** about one extra attack every 10 sec.

**What changes**

- **New triggers: block, dodge and parry.** They work at the crit cap, like Warrior's Master of Defense (Rage on dodge or parry). At the stat targets, about 86% of boss swings are blocked, dodged or parried.
- **Ranks raise the chance (20–100%).** The 4 sec limit is fixed, like other proc talents.
- **Holy Strike releases the charges, 2 at a time.** One Holy Strike is at most 3 hits. Charges wait between Holy Strikes, so the Paladin can hold them for a target switch, a taunt or a dangerous add.
- **The crit trigger stays, without the 4 sec limit,** so the Classic Reckoning bomb still works while leveling and in PvP: 4 crits taken give 4 charges, released over two Holy Strikes.
- **A shield-to-attack link,** like Warrior's Shield Slam, which community discussion on Wowhead says Paladins lack.

**Value for a tank at 5/5**

Simulation: boss swings every 2 sec; 60% block with C7, 10.7% dodge, 15% parry; no crits; Holy Strike every 10 sec. Each extra attack deals about 200 damage and causes about 273 threat (200 physical + Seal of Fury's 35 Holy damage, +10% from One-Handed Weapon Specialization, ×1.9 from Righteous Fury). The beta rows use the beta's 50% block.

| Case | Charges gained per 10 sec | Extra attacks per 10 sec | Extra damage per sec | Extra threat per sec |
| --- | --- | --- | --- | --- |
| Beta, 1 boss | 1.0 | 1.0 | +20 | +27 |
| Beta, 3 attackers | 2.2 | 2.2 | +45 | +61 |
| **Proposed, 1 boss** | **2.3** | **2.0** | **+40** | **+55** |
| **Proposed, 3 attackers** | **2.4** | **2.0** | **+40** | **+55** |

- **On a boss** the proposal doubles Reckoning's value: +27 threat per second over the beta.
- **Charges fill a little faster than Holy Strike spends them** (2.3 against 2.0 per 10 sec). The Paladin usually has 2–4 charges ready, and about 13% of procs are lost at the cap of 4.
- **On packs** the 4 sec limit keeps the value the same as on a boss. The beta is slightly stronger on packs (+45 against +40 damage per second), because its block trigger has a 1.5 sec limit.

**PvP burst check: build 0/26/25 with a two-handed weapon**

This is the build p-5532000210215-50005031211331 in the calculator: Protection 26 (Reckoning 5/5, Swift Judgement, Improved Hammer of Justice 2/3) and Retribution 25 (Seal of Command, Sacred Arbiter, Two-Handed Weapon Specialization 3/3, Vengeance 3/3, Conviction 5/5). The numbers are estimates, not a simulation.

**Assumptions**

- One 6 sec Hammer of Justice stun. Hammer of Justice has a 50 sec cooldown in this build (60 sec, −10 sec at 2/3).
- Two-handed weapon: 3.5 sec speed, 300 damage per swing including Attack Power. About 1.7 auto attacks fit in the stun.
- Two-Handed Weapon Specialization (+6%) applies to melee, Seals, Judgements and Holy Strike. 25% crit chance, crits deal double damage. Armor removes 30% of physical damage. Vengeance is left out.
- Seal of Command procs 7 times per minute: a 41% chance per swing, each proc 70% of weapon damage as Holy damage.
- Holy Strike rank 8: 50% of weapon damage plus 81–105, all as Holy damage.
- Judgement of Command on a stunned target: 388–422 (in-game tooltip with gear; the base value is 339–373). Swift Judgement allows a second Judgement in the same stun.
- Holy Strike does not trigger Seals in the beta. Extra attacks count as auto attacks, Seal of Command procs included.

| Part of the burst | Proposed | Beta, nothing stored | Beta, 4 charges stored |
| --- | --- | --- | --- |
| Holy Strike | about 600 (always triggers Seal of Command, C17) | about 390 (+20% damage, no Seal effect) | about 390 |
| Extra attacks (about 390 each) | 2: about 780 | 0 | 4: about 1,570 |
| Auto attacks (about 1.7) | about 670 | about 670 | about 670 |
| Two stunned Judgements (about 535 each) | about 1,070 | about 1,070 | about 1,070 |
| **Total** | **about 3,130** | **about 2,130** | **about 3,700** |

- **Result.** The proposal is about 47% above the beta's usual burst and about 15% below the beta's best case (the Classic bomb with 4 stored attacks).
- **Uncertainty.** About ±25%, so 2,350–3,900.
- **Swift Judgement** is about 17% of the burst. When it is on cooldown (60 sec, against 50 sec for Hammer of Justice), the proposed total is about 2,590. It stays on the watch list.

### C12. Fury's Reach: a ranged pull for Protection (new)

- **Proposed text.** "Increases the range of your Judgement by 5/10 yards while Seal of Fury is active."
- **Place.** Row 4, column 1, 2 ranks. Requires Swift Judgement (straight arrow from row 3). Righteous Defense sits in column 3.
- **Why.** Protection has no ranged pull or taunt. Seal of Fury's Judgement already deals 153–167 Holy damage and taunts for 4 sec, but only from 10 yards. At 2/2 it reaches 20 yards, double the base range.
- **Model.** Warrior has Vanguard (Charge in Defensive Stance, row 4, 1 point). Druid has Feral Charge (row 3) and a ranged pull in Feral.
- **Why 2 ranks.** Row 4 already has a 1-point talent (Righteous Defense), so this one has ranks like the rest of the row.
- **Why only with Seal of Fury.** Judgement of Command deals 388–422 to a stunned target. Without the condition, a 20 yard range would add burst for hybrids in PvP. With it, Holy and Retribution gain almost nothing from the dip.
- **Threat and mana.** No change while tanking: Judgement still costs 91 mana and has a 10 sec cooldown. Only the opening pull changes. The full path costs 3 points (Swift Judgement plus 2 ranks).

### C13. Shield Specialization: mana return once every 2 sec

- **Proposed text (rank 3).** "Increases the amount of damage absorbed by your shield by 30%, and gives your blocks a 100% chance to restore 4% of your maximum Mana. May only occur once every 2 sec."
- **What changes.** Only the limit, from once every 3 sec to once every 2 sec. The ranks, the chance and the 4% return stay as in the beta.
- **Why.** C10 removes Improved Seal of Fury, worth about 23 mana per sec while tanking. Reverence (C1) and the extra blocks from C7 give back about 13, and Holy Shield rank 3 costs 24 mana per sec. Without C13, tanking without Consecration is about break-even (−1.4 mana per sec).
- **Value.** A boss swinging every 2 sec can now trigger it on every blocked swing: 160 mana × 60% block ÷ 2 sec = 48 mana per sec, up from 30. Tanking without Consecration goes to +16.6 mana per sec (see Mana).
- **Model.** Warriors and Druids gain Rage from being hit, and Shaman's Water Shield is Forever's precedent for mana from being hit. Shield Specialization is already the Paladin's version, so no new talent is needed.
- **Synergy.** More block means more mana, so the crush fix (C7) and the mana fix support each other.
- **Limits.** Against packs it returns at most 80 mana per sec (beta: 53). It gives nothing to a Paladin who is not being hit; Reverence (C1) covers that case.

### C14. Holy Shield: damage grows with block value

- **Proposed text (rank 3).** "Increases chance to block by 30% for 10 sec, and deals 221 Holy damage plus 200% of your block value for each attack blocked while active. Damage caused by Holy Shield causes 20% additional threat. Each block expends a charge. 4 charges."
- **What changes.** Each block adds 200% of your block value to Holy Shield's damage. Block chance, charges, cooldown and the threat bonus stay as in the beta.
- **Problem.** Warrior and Druid threat grows with gear and with boss damage, because their rage comes from the hits they take. Paladin threat only grows with spell power: about +32 threat per second per +100 spell power. In the gear model, the Paladin without C14 falls from 107% of the Druid's threat at fresh level 60 to 80% in Naxxramas (see Threat).
- **Why block value.** It is a gear stat on the character sheet, easy to read and to gear for. It grows about 5 times from fresh level 60 to Naxxramas, much faster than spell power. It ties the Paladin's tank stats together: the shield, Strength (Divine Strength, C9) and Shield Specialization (+30% block value). Warrior's Shield Slam already adds block value to its damage.
- **Result.** The Paladin stays between the Druid and the Warrior at every gear tier: 116% of the Druid's threat at fresh level 60, 102% in Naxxramas. With flatter gear progression it ends at 94–110% in Naxxramas (see Threat, Flatter gear progression).
- **Why 200%.** At 100% the Paladin is still at 91% of the Druid in Naxxramas. At 300% it passes the Warrior from pre-raid gear on.
- **No new button.** Holy Shield is already used on cooldown, and C7 keeps it blocking about 3 attacks per 10 sec.
- **PvP.** At about 125 block value, each block deals about 250 more Holy damage, at most 4 blocks per 10 sec, and only against melee attacks. Only Protection has Holy Shield.

### Crushing blows

#### The problem

A raid boss is 3 levels above the player. With Classic rules, it has a 15% chance to land a crushing blow for 150% damage. Crushes only disappear when miss + dodge + parry + block reach 100% against the boss (about 102.4% on the character sheet). A tank can either push crushes off the attack table (Warrior) or survive them with armor and health (Druid).

| Tank | How crushes are handled | Result |
| --- | --- | --- |
| Warrior | Shield Block: +75% block, 2 blocks, 7 sec, 5 sec cooldown; Shield Specialization +5% block | Pushes crushes off the table with modest gear, but leaks after the 2 blocks |
| Druid | No shield; Thick Hide armor grows with Defense; Bear Form adds up to +20% Stamina | Always crushable, but has the armor and health to take it |
| Paladin (beta) | Holy Shield: +30% block, 4 charges, 10 sec, 10 sec cooldown; Redoubt is a 10% proc | Needs about 72% avoidance from gear: crushable like a Druid, without the Druid's armor and health |

C7 takes Warrior's path: push crushes off the table with block, the stat the tree already builds on.

#### How C7 fixes it

- **Redoubt in the beta** is a block buff with charges: +4–20% block for 10 sec or 5 blocks. Only 10% of melee hits start it, so it is up about half the time.
- **With C7,** each Holy Shield cast (every 10 sec) restarts Redoubt, so both buffs are always up together.
- **The charges are enough.** A boss swinging every 2 sec swings 5 times in 10 sec, and about 3 of those are blocked. That is fewer than Redoubt's 5 blocks and Holy Shield's 4 charges.
- **First hit.** Casting Holy Shield before the pull covers the boss's first swing.
- **Holy Shield stays at +30%.** With the Redoubt trigger, +30% already matches Warrior.

#### Stat targets

Against a level 63 boss (attack skill 315), with Classic rules.

- **Crit immunity: 440 Defense.** The boss has 5.6% crit against a level 60, and each Defense point removes 0.04%. Anticipation gives 20, so gear and enchants must give +120.
- **Crush immunity: miss + dodge + parry + block = 100%.** At 440 Defense each roll gets +5% from Defense.

With 5/5 Deflection, Holy Shield and Redoubt up:

| Roll | Sources | Against the boss |
| --- | --- | --- |
| Miss | 5% base + 5% Defense | 10% |
| Dodge | About 0.7% base + 5% Defense + Agility ÷ 20 | 5.7% + Agility ÷ 20 |
| Parry | 5% base + 5% Deflection + 5% Defense | 15% |
| Block | 5% base + 5% Defense + 30% Holy Shield + 20% Redoubt | 60% |
| Total |  | 90.7% + Agility ÷ 20 |

- **Gap after the crit cap: 9.3%.** That is about 186 Agility or 58 Defense above 440. Until it closes, the missing % is the crush chance. With about 100 Agility, about 4.3% of swings can crush, close to a Warrior between Shield Blocks.
- **Holy Shield is the whole mechanism.** Without it, the Paladin is fully crushable.
- **Gaps.** A late Holy Shield leaves a short gap, and fast or dual-wielding bosses can use up the charges early.

#### Compared with Warrior

Both tanks at 440 Defense with about 100 Agility, against a boss swinging every 2 sec. Shield Block tooltip on Wowhead: "Increases chance to block by 75% for 7 sec, but will only block 2 attacks", 10 Rage, 5 sec cooldown.

|  | Swings covered | Crush chance on the other swings | Swings that can crush |
| --- | --- | --- | --- |
| Warrior | About 80% (2 of 2.5 swings per 5 sec) | 15% | About 3% |
| Paladin with C7 | About 100% | About 4.3% | About 4.3% |

The two tanks are level. The Paladin's gap closes with gear; the Warrior's gaps depend on boss swing speed.

### Threat

This section compares single-target threat per second for the three tanks at level 60 against a level 63 boss. It is a model built from beta tests and developer notes, not a combat log. The inputs are listed at the end, and the unknowns are in Open questions.

#### Results

One boss. Boss armor reduced by 5 Sunder Armor and Faerie Fire. Paladin with 200 spell power (pre-raid estimate).

| Boss hit before armor | Warrior | Druid | Paladin, beta | Paladin, all proposals | Paladin, all proposals + Consecration |
| --- | --- | --- | --- | --- | --- |
| 3,000 | about 525 | about 520 | about 355 | about 540 | about 625 |
| 4,500 | about 600 | about 585 | about 355 | about 540 | about 625 |
| 6,000 | about 660 | about 650 | about 355 | about 540 | about 625 |

- **Warrior** gains about +135 if Shield Slam has a ×2.25 threat multiplier like Revenge (not tested).
- **Paladin, beta** has no Judgement of the Crusader, because Judgement of Fury may remove it (see below). With Crusader it is about 400.
- **Paladin, all proposals** includes Judgement of the Crusader (C19) and C14 with about 60 block value (pre-raid estimate). Without C14 it is about 455, or about 545 with Consecration.
- **Without armor debuffs on the boss** (4,500 hits): Warrior about 470, Druid about 425, Paladin with all proposals about 515. Most Paladin threat is Holy damage, which ignores armor.
- **Retribution Aura** instead of Devotion Aura adds about +25 for the Paladin, at the cost of 735 armor.

**Proposed Paladin, where the threat comes from (200 spell power)**

| Source | Threat per sec |
| --- | --- |
| Holy Shield blocks (about 180 base, about 80 from block value with C14) | about 260 |
| Judgement of Fury (every 10 sec, plus Swift Judgement once per minute) | about 70 |
| Holy Strike with Iron Creed | about 57 |
| Reckoning extra attacks (C11) | about 53 |
| Seal of Fury | about 49 |
| Auto attacks | about 49 |
| **Total** | **about 540** |

**Spell power.** Each +100 spell power adds about +32 threat per second. Judgement of the Crusader counts like +161 spell power against its target, so it is worth about +50, more than going from 150 to 300 spell power.

| Spell power | 100 | 150 | 200 | 250 | 300 | 350 |
| --- | --- | --- | --- | --- | --- | --- |
| Paladin, all proposals (60 block value) | about 505 | about 525 | about 540 | about 555 | about 570 | about 585 |

Expected spell power at level 60, based on about 100–120 at level 30: about 150 in balanced pre-raid tank gear, 200–250 with some threat gear, 300–350 in early raid gear. No Forever level 60 item data is public yet.

#### What the results mean

- **With the same gear, the three tanks are close on moderate bosses.** All proposals raise the Paladin by about +185 threat per second over the beta: block value on Holy Shield (C14, about +80), Judgement of the Crusader (C19, about +50), more Holy Shield blocks (C7) and Reckoning (C11).
- **With the same gear, harder-hitting bosses still favor Warriors and Druids.** They get rage from the damage they take, so their threat grows with boss damage. Paladin threat does not. In real progression, gear and boss damage rise together, and C14 makes Paladin threat grow with gear (see Gear tiers).
- **The Paladin has no stance or form multiplier.** Righteous Fury (×1.9) only applies to Holy damage. Auto attacks and Reckoning attacks get ×1.0, while Defensive Stance gives ×1.495 and Bear Form ×1.5 on everything.
- **The Paladin has no strong, frequent attack.**

| Attack | Total threat multiplier | Cooldown |
| --- | --- | --- |
| Primal Bite (Druid, new in Forever) | ×4.5 (×3, Bear Form ×1.5) | 6 sec |
| Revenge (Warrior) | ×3.4 (×2.25, Defensive Stance and Defiance ×1.495) | 5 sec |
| Maul (Druid) | ×2.6 (×1.75, Bear Form ×1.5) | Every swing |
| Holy Strike with Iron Creed 5/5 (Paladin) | ×2.4 (Righteous Fury ×1.9, Iron Creed ×1.25) | 10 sec |
| Paladin auto attacks and Reckoning attacks | ×1.0 | — |

- **Paladin strengths.** Its threat does not depend on boss armor or rage. Consecration and Holy Shield work on every attacker, so the Paladin is strongest on packs.

#### Gear tiers

The fresh level 60 row uses a real gear profile: crafted and dungeon items, before talents. The later tiers are extrapolated: about 15–20% more stats per tier, following Classic item levels. Warrior and Druid get the same Attack Power and weapon as the Paladin.

| Tier | Spell power | Attack Power | Weapon damage per sec | Block value (with Shield Specialization) | Max mana | Boss hit before armor |
| --- | --- | --- | --- | --- | --- | --- |
| Fresh level 60 (real profile) | 208 | 428 | 27.5 (2.2 sec) | 26 | 2,897 | 3,000 |
| Pre-raid best in slot | 260 | 520 | 42 | 60 | 3,400 | 3,500 |
| Molten Core | 310 | 600 | 52 | 80 | 3,900 | 4,500 |
| Blackwing Lair | 380 | 700 | 60 | 100 | 4,400 | 6,000 |
| Naxxramas | 440 | 800 | 66 | 125 | 4,900 | 8,000 |

Threat per second, one boss, boss armor debuffed. The percentage is the share of the Druid's threat.

| Tier | Warrior | Druid | Paladin, beta | Paladin, proposals without C14 | **Paladin, all proposals** | All proposals + Consecration |
| --- | --- | --- | --- | --- | --- | --- |
| Fresh level 60 | about 490 | about 405 | about 335 (83%) | about 430 (107%) | **about 470 (116%)** | about 555 |
| Pre-raid best in slot | about 545 | about 455 | about 370 (81%) | about 470 (104%) | **about 555 (122%)** | about 645 |
| Molten Core | about 640 | about 530 | about 405 (76%) | about 515 (97%) | **about 625 (118%)** | about 720 |
| Blackwing Lair | about 755 | about 635 | about 450 (71%) | about 565 (89%) | **about 700 (111%)** | about 800 |
| Naxxramas | about 815 | about 760 | about 485 (64%) | about 605 (80%) | **about 775 (102%)** | about 880 |

- **Without C14** the Paladin falls behind from Molten Core on. Warriors and Druids gain Attack Power and more rage from harder boss hits; the Paladin only gains spell power.
- **With C14** the Paladin stays between the Druid and the Warrior at every tier.
- **The beta Paladin** is behind at every tier, from 83% of the Druid at fresh level 60 to 64% in Naxxramas.
- **Mana improves with gear,** because Shield Specialization returns 4% of max mana. Tanking without Consecration goes from about +3 mana per sec at fresh level 60 (2,897 mana) to about +27 in Naxxramas.

#### Flatter gear progression

Blizzard has said it wants flatter, more horizontal gear progression. This is an intention, not a promise. In a model where gear grows half as fast after pre-raid, C14 still keeps the Paladin at 94–120% of the Druid's threat. The weakest case is flat gear with bosses that keep hitting harder, because Warrior and Druid rage still grows with boss damage. Block value per tier is the value to watch.

Model: fresh level 60 and pre-raid as above. From Molten Core on, spell power, Attack Power, weapon damage, crit and block value gain half of the growth in the Gear tiers table (block value 70, 80 and 92 instead of 80, 100 and 125).

| Tier | Gear as in Gear tiers | Flat gear, boss hits as in Gear tiers | Flat gear, boss hits also flatter |
| --- | --- | --- | --- |
| Fresh level 60 | 116% (96%) | 116% (96%) | 116% (96%) |
| Pre-raid best in slot | 122% (101%) | 122% (101%) | 122% (101%) |
| Molten Core | 118% (97%) | 114% (95%) | 120% (99%) |
| Blackwing Lair | 111% (93%) | 104% (88%) | 115% (95%) |
| Naxxramas | 102% (95%) | 94% (89%) | 110% (91%) |
| Without C14, Naxxramas | 80% | 76% | 89% |

Paladin with all proposals, as a share of the Druid's threat, with the share of the Warrior's in brackets. "Boss hits also flatter": boss hits grow half as fast after pre-raid (4,000, 4,750 and 5,750 before armor instead of 4,500, 6,000 and 8,000).

- **C14 at 200% fits all three cases.** At 150% the Paladin would fall to 89% of the Druid in Naxxramas when boss hits keep growing. At 300% it would pass the Warrior when everything is flat.
- **Without C14 the Paladin falls behind in every case,** so flatter gear makes C14 more important.
- **Mana.** Shield Specialization returns 4% of max mana. With max mana growing half as fast (about 3,650, 3,900 and 4,150), tanking without Consecration gives about +12, +15 and +18 mana per sec instead of +15, +21 and +27. C13 matters more.
- **Defense.** If gear gives Defense more slowly, tanks reach 440 Defense later and bosses keep a small crit chance for longer. C7 (Holy Shield triggers Redoubt) and Reckoning's crit trigger stay useful longer.
- **Judgement of the Crusader (C19).** Its +161 bonus is worth relatively more when spell power on gear grows slowly.
- **PvP burst check (C11).** It uses fresh and pre-raid level stats, so it stays valid longer with flatter gear.

#### Options if Protection threat is too low

If testing shows Protection threat is still short with C14, these are the next steps. They are not proposals yet.

| Option | Effect |
| --- | --- |
| Iron Creed: Holy Strike threat +20/40/60/80/100% instead of +5/10/15/20/25% | About +30 to +50 threat per second at every tier. Threat only, so no PvP effect |
| A shield attack in Protection row 4 (6 sec cooldown, weapon damage + 100 Holy damage, ×2 threat) | About +170 to +200 threat per second. Adds a button; the Druid's new Primal Bite is the precedent |

Other options were checked and dropped (see Withdrawn ideas).

#### Inputs

- **All tanks.** Level 60, 500 Attack Power, 3% hit, one-handed weapon of 45 damage per sec at 2.7 sec (Druid: 260 per swing every 2.5 sec). Crit 6% (Druid 12% with Sharpened Claws).
- **Attacking a level 63 boss from the front.** 6% miss, 6.5% dodge, 14% parry, 40% glancing white hits at −35% damage.
- **Boss.** 3,731 armor; 976 after 5 Sunder Armor (450 each) and Faerie Fire. A swing every 2 sec. 64% of its swings land on the tank.
- **Rage (normalized in Forever).** Auto attacks: 3.46 rage × weapon speed (×1.3 for two-handers and Bears), double on a crit, none on a miss, dodge or parry. Damage taken: 2.5 × 0.6 × unmitigated hit ÷ 243.6 at level 63, ×1.5 for crushing blows. Heroic Strike and Maul hits give no rage (assumed, as in Classic). 5 threat per rage gained.
- **Warrior.** Defensive Stance ×1.3 threat and −10% damage, Defiance 3/3 ×1.15, One-Handed Weapon Specialization +10%, Improved Revenge 3/3. Revenge: damage × 2.25, with 28% of Attack Power. Shield Slam: 640–670 + 50 block value, threat = damage. Heroic Strike rank 9: damage + about 145. 5 rage on each block, dodge and parry. Spare rage goes to Sunder Armor (about 225 threat before stance).
- **Druid.** Bear Form ×1.5, Maul ×1.75, Primal Bite ×3, Swipe ×1.75. Ferocity 5/5, Savage Fury 2/2, Feral Instinct 3/3. Lacerate and Faerie Fire are not included.
- **Paladin.**
  - Threat and damage modifiers: Righteous Fury ×1.9 on Holy damage only; One-Handed Weapon Specialization +10% (not on Consecration or Retribution Aura); Improved Seals +15% from the 8-point Holy dip.
  - Spell power coefficients: Seal of Fury 10% per hit, Judgement of Fury 42.9%, Holy Strike 21.45%, Holy Shield 10.7% per block (assumed: 42.9% split over 4 charges), Consecration 33.6% (15% of ticks miss).
  - Rates: 3 Holy Shield blocks per 10 sec (2.5 in the beta), 2.0 Reckoning attacks per 10 sec (1.0 in the beta).

#### Spell data from beta tests

| Spell | Behavior in the beta | Source |
| --- | --- | --- |
| Holy Strike | Normalized weapon damage. The flat Holy part scales at 0.429 × the weapon %: 21.45% of spell power at rank 8. Does not trigger Seal of Fury, Righteousness or Command; does trigger Seal of Light, Justice and Wisdom | Player tests |
| Seal of Fury | 10% of spell power per hit (11.5% with Improved Seals). No Attack Power scaling. Melee crit for double damage, rolled on its own. Cannot miss | Player tests |
| Seal of Righteousness | 10% of spell power with a one-hander, 12% with a two-hander, whatever the speed | Player tests; patch note of 16 October |
| Seal of Command | 29% × 70% weapon damage = 20.3% of spell power. 7 procs per minute. Uses the melee hit table | Player tests |
| Judgements of Fury, Righteousness and Command | 42.9% of spell power (instant-cast value). Melee hit table, double damage on a crit. Judgement of Command deals double damage to stunned targets | Player tests; patch note of 16 October |
| Judgement of Fury | The damage lands before the taunt, so the taunt copies the top threat but the Judgement's own threat is not added on top | Player tests |
| Judgement of the Crusader | Its bonus uses each spell's coefficient, like spell power. Seal of Command gets the full 29% from it | Player tests |
| Consecration | 0.042 of spell power per tick (33.6% per target), first 4 enemies only | Patch note of 16 October |
| Retribution Aura | 6% of spell power | Patch note of 8 October |
| Holy Shield | Spell power scaling not known. Classic used 5% per block | Classic data |
| Mana gains | Shield Specialization, Improved Seal of Fury and Sanctified Judgement mana returns cause no threat | Patch notes of 8 and 16 October |
| Rage | Damage-taken rage fixed on 8 October and balanced around 20–40% armor depending on level. Crits give double rage. Bear Form threat ×1.5 | Patch note of 8 October |

#### Findings to report to Blizzard

- **Judgement of Fury applies its damage before its taunt.** The taunt should come first, so the Paladin ends slightly ahead of the top threat instead of level with it.
- **Holy Strike triggers only some Seals.** It triggers Seal of Light, Justice and Wisdom, but not the damage Seals (Fury, Righteousness, Command). C17 makes this consistent for Retribution.

### Protection: beta test results

| Talent | Observed in the beta | Effect on the proposals |
| --- | --- | --- |
| Toughness | Only armor from items; nothing from Devotion Aura, scrolls, elixirs, potions or Mark of the Wild | Supports C9 |
| Redoubt | A blocked hit can trigger it without using a charge | C7 keeps the proc |
| Precision | Melee, ranged and spell hit; each ability uses the matching hit type | Confirms it as the shared hit talent |
| Anticipation | A raid boss stops critting at 440 Defense; Anticipation gives 20 | The stat targets assume this cap |
| Improved Seal of Fury | Mana return ignores the Seal's rank; no threat from the mana | Removed by C10 |
| Improved Righteous Fury | Applies after armor; multiplies with Iron Creed (×0.94 × 0.90) | Removed by C10 |
| Shield Specialization | Multiplies Shield Block Value; mana return is 4%; no threat from the mana | Stays Protection's main mana source; C13 shortens its limit to 2 sec |
| Sacred Duty | % of total Stamina, multiplies with Kings; shortens the cooldowns of Forbearance spells | None |
| Swift Judgement | Off the global cooldown | None |
| One-Handed Weapon Specialization | Melee, Seals, Judgements, Holy Strike and Twist of Light Echo | None |
| Templar's Bulwark | An absorb, not a heal: Mortal Strike effects don't reduce it | None |
| Reckoning | Stored attacks fire on the next melee hit; each can trigger Seals and Judgements | C11: charges are released by Holy Strike |
| Iron Creed | Holy Strike threat ×1.90 (Righteous Fury) × 1.25 | C8 keeps these multipliers |
| Holy Shield | Threat ×1.90 (Righteous Fury) × 1.20; more testing needed | None |

## Retribution

These changes link Retribution's melee to its Holy spells and cut the Seal-swapping load.

### Retribution layout after C16 and C17

| Row (points needed) | Talents | Points in the row |
| --- | --- | --- |
| 1 (0) | Deflection, Benediction | 10 |
| 2 (5) | Improved Judgement, Holy Conduit, Conviction | 9 |
| 3 (10) | Vindication, Sanctified Judgement, Seal of Command, Pursuit of Justice | 9 |
| 4 (15) | Eye for an Eye, Repentance (C17), Two-Handed Weapon Specialization (C16) | 6 |
| 5 (20) | Vengeance, Sacred Arbiter (C17) | 4 |
| 6 (25) | Champion of the Light, Instrument of Law | 5 |
| 7 (30) | Twist of Light | 1 |

Retribution stays at 44 points.

### C15. Conviction: attacks and spells

- **Proposed text.** "Improves your chance to get a critical strike with attacks and spells by 1/2/3/4/5%."
- **Model.** Shaman's Thundering Strikes made the same change.
- **Real change.** In the beta, Conviction already crits damaging Seals and Hammer of Wrath. The change only adds Holy Shock, Exorcism, Consecration and heals.
- **Cost for healers.** A Holy Paladin needs 10 Retribution points to get it (5 in row 1, then 5 in Conviction).

### C16. Two-Handed Weapon Specialization: 20 → 15 points

- **Model.** Warrior's version opens at 15 points.
- **Room.** Retribution row 4 has space after C17. Values stay at 2/4/6%.

### C17. Sacred Arbiter and Repentance: swap rows, make Sacred Arbiter stronger

- **Proposed text.** "Causes your Holy Strike ability to always trigger the effect of your active Seal and to refresh all Judgement effects on the target, including those of other Paladins. Does not trigger the stun of Seal of Justice."
- **Rows.** Sacred Arbiter moves from 15 to 20 points, Repentance from 20 to 15.
- **What it replaces.** The beta's +20% Holy Strike damage, worth about 5 damage per second with a typical two-hander. Holy Strike does not trigger Seals in the beta, so a Seal of Command effect on every Holy Strike adds about 22 (70% of a 300 swing, +6% from Two-Handed Weapon Specialization, every 10 sec).
- **Model.** Retribution's core payoff, as Stormstrike is for Enhancement.
- **Safety.** It triggers the Seal, not a second Judgement. The stun exception keeps a guaranteed stun every 10 sec out of PvP.
- **Tradeoffs.** Protection builds that take Sacred Arbiter for its Judgement refresh now need 20 Retribution points. Repentance becomes easier to reach for Holy and Protection in PvP.

### C18. Twist of Light: the Echo lasts 10 sec

- **Problem.** Each Echo lasts for one melee attack, so full value means swapping Seals before almost every swing. With a 3.5 sec two-hander, that is about 80% of the time in global cooldowns. Players on the beta forums cite a developer statement that rotations should stay around four buttons.
- **Proposed text.** "Reduces the Mana cost of your Seal spells by 20%. When you replace your Seal of Command, Seal of Righteousness, Seal of Fury, or Seal of Justice with a different Seal, you gain an Echo of that Seal for 10 sec. While the Echo lasts, your melee attacks also apply the replaced Seal's effects."
- **Same action, slower rhythm.** You still swap Seals, but once every 10 sec, next to Holy Strike and Judgement.

| Every 10 sec, 3.5 sec weapon | Beta | With C18 |
| --- | --- | --- |
| Seal casts | About 3 | 1 |
| Holy Strike | 1 | 1 |
| Judgement (8 sec cooldown with Improved Judgement 2/2) | 1.25 | 1.25 |
| Time in global cooldown (1.5 sec each, Judgement included) | About 79% | About 49% |
| Mana spent, single target | About 41.6 per sec | About 11.4 per sec |

- **Mana.** With one swap every 10 sec, Sanctified Judgement's refund covers most of the cost, so C18 is also Retribution's main mana fix (see Mana).

### Retribution: beta test results

| Talent | Observed in the beta | Effect on the proposals |
| --- | --- | --- |
| Benediction | Its cost cut multiplies with Purifying Power, Holy Conduit and Twist of Light | None |
| Holy Conduit | With Benediction, Consecration costs ×0.60 × 0.90 | None |
| Conviction | Also crits damaging Seals and Hammer of Wrath | C15 only adds Holy Shock, Exorcism, Consecration and heals |
| Vindication | About 5 procs per minute; ranks −67/136/204 target Attack Power and +1/2/3% yours | None |
| Sanctified Judgement | Refunds more than 60% of the Seal's base cost with Benediction | Probably a bug to report |
| Pursuit of Justice | 15% at 2/2; beats the 8% boot enchant | On the watch list |
| Eye for an Eye | Uses damage taken after armor and resistance | None |
| Sacred Arbiter | +20% Holy Strike damage; refreshes Light, Wisdom, Justice and Crusader | C17 replaces the +20% with the Seal trigger |
| Two-Handed Weapon Specialization | Melee, Seals, Judgements, Holy Strike and Twist of Light Echo | Supports C16 |
| Vengeance | Multiplies with other % damage; crits from procs add stacks | None |
| Repentance | Diminishing returns category not tested | None |
| Instrument of Law | Rank 2 makes Hammer of Wrath instant; the threat cut multiplies with Salvation | None |
| Twist of Light | Needs more testing; with Benediction, Seals cost ×0.72 | None |

## Judgements in raids

### The problem

- **The rule.** Each Paladin can have only one Judgement active on a target.
- **The conflict.** Since the October 15 patch, Salvation no longer uses a Blessing slot, so two Paladins cover a raid's Blessings. But raids prefer Judgement of Light and Wisdom, which help everyone, over Crusader, which mostly boosts the Paladins' own Holy damage. Crusader gets dropped, so Retribution loses damage and Protection loses threat.
- **Sacred Arbiter doesn't fix it.** Holy Strike refreshes all Judgements on the target, including other Paladins', but each Paladin still owns only one.

### C19. Personal Judgement of the Crusader (recommended)

- **Change.** Judgement of the Crusader no longer counts toward the one-Judgement limit, but it only increases Holy damage from the Paladin who applied it.
- **Precedent.** Salvation leaving the Blessing slot; Improved Seal of the Crusader made baseline.
- **Tradeoff.** Other Holy damage dealers lose the bonus.

**For Protection.** Judgement of Fury may remove the tank's own Judgement of the Crusader, because a Paladin can have only one Judgement active. With C19, Crusader stays up. It is worth about +50 threat per second for a Protection Paladin (see Threat).

### Alternatives to C19

| ID | Option | How it works | Precedent | Tradeoff |
| --- | --- | --- | --- | --- |
| C19a | Merge Light and Wisdom (fallback if C19 is rejected) | Judging Seal of Light or Wisdom applies one Judgement of Grace: attacks can heal the attacker for 61 and restore 59 mana | Weaponmaster merging four weapon talents | A single Paladin still has to choose |
| C19b | Judgement Echo (optional, with C19) | When your next Judgement replaces your Judgement of Light, Wisdom or Justice, the replaced Judgement stays on the target as an Echo for 40 sec | Twist of Light's Seal Echo | Needs a 30-point Retribution Paladin |

| Two-Paladin raid | Beta | C19 | C19a | C19b alone |
| --- | --- | --- | --- | --- |
| Holy + Holy | Light + Wisdom | Light + Wisdom | Grace | Light + Wisdom |
| Holy + Retribution | Two of three | All three | Grace + Crusader | All three |
| Holy + Protection | Two of three | All three | Grace + Crusader | Two of three |
| Protection + Retribution | Two of three | All three | Grace + Crusader | All three |

## Mana

### What we found

- **Spirit regen** (15 + Spirit ÷ 5 every 2 sec) stops for 5 sec after each cast, so in combat it is close to zero without a regen-while-casting talent.
- **Other classes** give their damage and hybrid specs 50% regen while casting at about 20 points (see What the other classes do). Protection and Retribution have none in the beta.
- **Protection's beta mana only comes from being hit** (Shield Specialization, Improved Seal of Fury). A Protection Paladin who is off-tanking or dealing damage has no income.
- **Retribution's mana problem is Seal swapping,** not missing regen.

### The fix

- **Reverence in row 2 (C4)** gives Protection and Retribution regen while casting for 8 Holy points, like Enhancement Shaman with Mindfulness: about 10 mana per sec at 50% (C1) and 120–130 Spirit.
- **Shield Specialization triggers once every 2 sec instead of 3 (C13).** It stays the tank's main source, with a Forever precedent in Shaman's Water Shield.
- **Improved Seal of Fury is removed (C10).**
- **C18 fixes Retribution.**

### Results

**Inputs.** 4,000 max mana; base mana 1,512 (Classic value, not confirmed for Forever); 130 Spirit for Protection, 120 for Retribution; boss swings every 2.0 sec; one-handed weapon at 2.7 sec. Level 60 costs from the Forever spellbook: Holy Shield rank 3 240, Holy Strike 20, Judgement 6% of base mana (91, 10 sec cooldown), Seal of Fury rank 7 200 every 30 sec, Seal of Command 210, Consecration rank 5 565 every 8 sec. The Retribution dip applies Benediction (×0.90 on all of these) and Holy Conduit (×0.60 on Consecration).

**Protection income per sec while tanking**

| Source | Beta | Proposed | How it is counted |
| --- | --- | --- | --- |
| Shield Specialization: 160 mana per block | 26.7 (once every 3 sec) | 48.0 (once every 2 sec, C13) | Beta: with a swing every 2 sec, the 3 sec limit skips the next swing; 50% block. Proposed: every blocked swing counts; 60% block with C7 |
| Improved Seal of Fury: 87 mana per shield used up | 23.3 | — (C10) | 60 mana +45% against a boss. Each of your swings makes a new shield; it pays out when a boss hit lands before your next swing (64% of boss swings land) |
| Reverence 50% (C1, C4) | — | 10.3 | Half of 41 mana every 2 sec at 130 Spirit |
| **Total** | **50.0** | **58.3** |  |

**Protection spending per sec.** 41.7 without Consecration and 112.4 with it. With the Retribution dip: 37.6 and 75.7.

| Protection, 4,000 mana | Beta | Proposed |
| --- | --- | --- |
| Tanking, no Consecration | +8.3 per sec, sustainable | +16.6 per sec, sustainable |
| Tanking, Consecration on cooldown | −62.4 per sec: 64 sec | −54.1 per sec: 74 sec |
| Tanking, Consecration on cooldown, Retribution dip | −25.7 per sec: 2 min 36 sec | −17.4 per sec: 3 min 50 sec |
| Not being hit, no Consecration | −41.7 per sec: 1 min 36 sec | −31.4 per sec: 2 min 7 sec |
| Not being hit, Consecration on cooldown | −112.4 per sec: 36 sec | −102.1 per sec: 39 sec |

| Retribution, single target | Spending | No regen | With Reverence 50% (9.75 per sec) |
| --- | --- | --- | --- |
| Beta Seal swapping (about 3 Seals every 10 sec) | 41.6 per sec | 1 min 36 sec | 2 min 6 sec |
| C18 (one Seal every 10 sec) | 11.4 per sec | 5 min 51 sec | About 40 min, close to sustainable |

Retribution spending assumes Sanctified Judgement returns 60% of the Seal's base cost (126 mana) per Judgement, as tested.

- **Tanking stays sustainable without Consecration:** +16.6 mana per sec, against +8.3 in the beta. Removing Improved Seal of Fury (C10) costs 23 mana per sec. Reverence, the extra blocks from C7 and the 2 sec limit (C13) give back 31.
- **Consecration on cooldown lasts a little longer than in the beta:** 74 sec against 64, or 3 min 50 sec with the Retribution dip. It stays a tool for packs, not a full-time rotation.
- **Reverence pays off when the Paladin is not being hit:** about 30 sec more without Consecration.
- **Raid buffs are not counted.** Blessing of Wisdom adds 8 mana per sec, and Judgement of Wisdom on the boss adds more.

## Tree balance review

Two checks: rows 1–2 must offer something to the other specs, and talents should match what other classes get.

| Tree | Rows 1–2 that tempt other specs | Who dips in | Cost |
| --- | --- | --- | --- |
| Holy | Improved Seals (+15% Seal damage), Divine Intellect, Infusion of Light, Reverence, Unyielding Faith | Retribution and Protection (Seal damage, regen, faster Holy Light); casters (Intellect) | 5–8 points |
| Retribution | Deflection, Benediction, Improved Judgement, Holy Conduit, Conviction | Protection (parry, crit, mana costs); Holy (Benediction, Holy Conduit) | 5–10 points |
| Protection | Divine Strength, Precision (+3% hit), Guardian's Favor | Everyone (Strength, hit); Holy (Guardian's Favor in PvP) | 5–8 points |

**Parity.** Divine Intellect matches Shaman's Ancestral Knowledge (+10%). Deflection matches Warrior's. Conviction matches Warrior's Cruelty (+5%). Benediction matches Shaman's Convection (−10%). Anticipation matches Warrior's (+20 Defense). Divine Strength matches Druid's Heart of the Wild.

**Points per tree.** Beta: Holy 46, Protection 48, Retribution 44. Proposed: Holy 44, Protection 47, Retribution 44.

### Watch list

These are risks to check in testing. None of them needs a change now.

| # | Risk | What to do if it happens |
| --- | --- | --- |
| W1 | Pursuit of Justice (+15% speed at 10 Retribution points) beats the boot enchant | Lower it to 10% if every Paladin dips for it |
| W2 | Sacred Duty gives Divine Shield −60 sec at 10 Protection points, a PvP dip | Cut it to −30 sec if it becomes mandatory |
| W3 | Retribution gets Strength and 3% hit in one 8-point Protection dip | Watch |
| W4 | A 7-point Retribution dip cuts Protection's spending with Consecration from about 112 to 76 mana per sec | Watch: it may become a mandatory Protection dip |
| W5 | Holy is the main dip for both other trees (Seal damage, Infusion of Light, Reverence, Consecrated Ground) | Watch: Retribution and Protection still offer parry, crit, mana costs, Strength and hit |
| W6 | Reckoning (C11): a 0/26/25 two-hander bursts for about 3,130 in one Hammer of Justice stun | Watch: below the beta's best case (about 3,700). Swift Judgement is about 17% of it |
| W7 | Iron Creed (C8) gives −10% damage taken to any spec with Righteous Fury and 25 Protection points | Watch in PvP; deliberate exception to the no-improved-buff rule |
| W8 | Fury's Reach (C12): a 15-point Protection dip plus Swift Judgement gives a 20 yard Judgement | Watch: the range only works with Seal of Fury |
| W9 | Repentance at 15 Retribution points and Templar's Bulwark (an absorb of 100% of health, three times Warrior's Last Stand) are strong PvP dips | Watch |
| W10 | Shield Specialization (C13) may make Consecration tanking too cheap against fast-hitting packs (up to 80 mana per sec) | Go back to 3 sec, or lower the return from 4% to 3% |
| W11 | Protection single-target threat in late raids depends on C14 and on block value in Forever gear (see Threat, Gear tiers) | Re-tune C14's 200%; then Iron Creed +100% Holy Strike threat; a shield attack only as a last step |

## Open questions

- [ ] Forever changed the spell hit cap. Did the crushing blow rules change too? A test against a raid boss would confirm the stat targets.
- [ ] Do regen-while-casting effects add together (capped at 100%) in Forever, as in Classic?
- [ ] Would C15 (Conviction for spells) make a Holy dip into Retribution too strong for healers?
- [ ] Should Retribution have a group contribution like Druid's Leader of the Pack, or is Vindication's Attack Power debuff enough?
- [ ] Is a 20 yard pull worth 3 Protection points (C12)?
- [ ] Does Judgement use the global cooldown in Forever? The C18 table assumes it does.
- [ ] Does Judgement of Fury remove your own Judgement of the Crusader?
- [ ] Does Holy Shield's damage scale with spell power, and by how much per block?
- [ ] Does Shield Slam have a threat multiplier, like Revenge's ×2.25? (Warrior testers)
- [ ] Do Heroic Strike and Maul hits give rage? (Warrior and Druid testers)
- [ ] Champion of the Light: the patch note of 16 October says 10/20/30% of Intellect, the client data of 18 October says 20/40/60%. Which is live?
- [ ] How much block value do Forever shields and tank gear give at each tier? C14's 200% is tuned on Classic-like values.

**Answered**

- [x] Vindication ranks: −67/136/204 target Attack Power and +1/2/3% yours.
- [x] Shield Specialization mana return: 4%.
- [x] Spell hit cap: 18%, with no unavoidable 1% miss.
- [x] Champion of the Light needs 28 Retribution points for 3/3 (row 6).
- [x] Level 60 costs (Forever spellbook): Seal of Fury rank 7 200 mana, Seal of Command 210, Consecration 565, Holy Shield rank 3 240.
- [x] Light's Vigil has 3 ranks: 730, 1,000 and 1,340 mana.

## Withdrawn ideas

These ideas were considered and dropped. They are not part of the proposals.

| Idea | Why it was dropped |
| --- | --- |
| Light's Vigil from 730 to about 500 mana | The estimate used rank 1. At level 60, rank 3 plus Holy Shock rank 4 costs 1,665 mana and heals about 3,840 across 5 players: 2.3 healing per mana, close to Holy Light rank 9 (2.4) on one target. At rank 1 (level 40) it already beats Holy Light rank 6 (2.0 against 1.8) |
| One-Handed Weapon Specialization boosts all damage while a shield is equipped | The beta talent already boosts all damage except Consecration and Retribution Aura |
| Unyielding Faith adds spell threat reduction | Not needed: Salvation no longer uses a Blessing slot, and a threat cut must not affect Protection |
| Holy Shield +35% or +40% block | With the Redoubt trigger, +30% already matches Warrior. +35% beats Warrior, and +40% also removes crits below 440 Defense |
| Holy Strike crits reset Hammer of Wrath | Hammer of Wrath's 6 sec cooldown is shorter than Holy Strike's 10 sec, and it only works below 20% health: about +1 damage per second |
| Champion of the Light adds healing | At 60% of Intellect it would match deep Holy's healing and pull Holy Paladins into Retribution. Could come back at 10/20/30%, now that C4 puts Healing Light out of a Retribution hybrid's reach |
| Sacred Ward (critical heals add a shield) | The same talent as Priest's Divine Aegis. Replaced by Lingering Light (C2) |
| Other ideas for the new Holy talent (smart heal splash, aura boost, Cleanse, Lay on Hands) | Too modern, or utility instead of engaging healing |
| Steadfast Faith (stun duration) in Protection row 1 | Two crowd-control reduction talents; other classes have one |
| Toughness that also gives Stamina | Replaced by Divine Strength from Holy (C9) |
| Hallowed Ground, or Shield Specialization, in Protection row 1 | Tank-only talents leave Holy and Retribution 5 wasted points before Precision |
| A regen talent in each tree (Iron Creed, Righteous Fury, Seal of Fury) | Reverence in row 2 does the same with one talent. The Righteous Fury and Seal of Fury versions could be used by Holy |
| Survive crushes with more armor, health and a stronger Seal of Fury absorb | Healers would still face the spikes. C7 removes the crushes instead |
| Holy Shield or Seal of Fury turns crushes into normal hits | Bypasses the attack table |
| Redoubt charges that each add a % of block | Block buffs with charges give one fixed bonus |
| Redoubt on every hit with a 6 sec cooldown | The Holy Shield trigger gives the same uptime with no new rule |
| Bring back Improved Blessing of Wisdom or Improved Lay on Hands | Forever removes improved-buff talents |
| Move Precision into Retribution | The Protection dip for hit is intended |
| Swap Light's Vigil and Holy Power | Every tree ends on a 1-point capstone |
| Cap Divine Precision below 18% | Priest's Holy Precision is the same, and the spell hit cap is 18% |
| Raise Two-Handed Weapon Specialization to 10% | Paladin's 6% is already above Warrior's 3% |
| Fix Vindication's flat ranks | Forever already reworked it |
| Reckoning only works with a shield | It would end the Classic two-handed Reckoning bomb |
| Holy Strike releases all 4 Reckoning charges | The 0/26/25 burst would be about 3,910 instead of 3,130 (+25%) |
| Reckoning at 40% chance, once every 1.5 sec | Too few charges on a boss (about 1.6 extra attacks per 10 sec) |
| Reckoning at 100% chance, once every 1.5 sec | Charges sit at the cap of 4; more than half the procs are lost and holding charges is no longer a choice |
| Swap Reckoning (row 5) and Iron Creed (row 6) | Makes Reckoning cost 25 points but does not stop a 0/30/21 hybrid. The 2-charge limit does the job without moving talents |
| Iron Creed without the Holy Strike threat bonus | Simpler wording, but loses about 10 threat per second |
| Aura Mastery or another improved aura talent for Protection | An improved-buff talent with low value (about −4% damage taken at 3 points). Fury's Reach (C12) covers the utility gap instead |
| Sacred Arbiter with +30% Holy Strike damage | About +8 damage per second: too small for a 20-point talent |
| Two Seals active at once (instead of C18) | Uses fewer global cooldowns but removes Seal swapping, the action the talent is built on |
| Two Judgements per Paladin | More global cooldowns, against C18 |
| Judgement of the Crusader moves into Retribution (Holy Strike applies it) | A raid without a Retribution Paladin loses the debuff |
| Holy Shield deals 3% of each blocked attack's damage (instead of C14) | Same result as C14, but based on damage taken instead of a stat, so it is hard to read and to gear for |
| Righteous Fury threat ×2.2 or ×2.5 (instead of ×1.9) | Flat: too strong early or too weak late. Also boosts Consecration on every target and changes a baseline spell Blizzard just tuned on 16 October |
| Holy Shield threat bonus +50% or +100% (instead of +20%) | Flat: +100% beats the Warrior at fresh level 60, +50% is too weak in late raids |
| Iron Creed: +25% threat on all Holy damage | Flat, and works like an improved Righteous Fury. Does not grow with content |
| Righteous Fury also boosts physical damage threat (×1.5) with a shield | Too weak in late raids (88% of the Druid) and changes Righteous Fury for every spec |

## Sources

- [WoW Forever Talents – Paladin](https://wowforevertalents.com/paladin/)
- [WoW Forever Talents – Paladin spellbook](https://wowforevertalents.com/abilities/paladin/)
- [WoW Forever Talents – Warrior](https://wowforevertalents.com/warrior/)
- [WoW Forever Talents – Druid](https://wowforevertalents.com/druid/)
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
- [Warcraft Tavern – Mage and Shaman deep dive](https://www.warcrafttavern.com/forever/news/scrolls-totems-mage-shaman-deep-dive-for-wow-forever/)
- [Outputlag – Seal of Fury tooltip](https://outputlag.com/news/world-of-warcraft-forevers-paladins-tank-with-seal-of-fury-and-a-10-yard-judgement-taunt/)
- [Notebookcheck – Blizzard on class simplicity](https://notebookcheck.net/WoW-Forever-won-t-modernize-Classic-classes-but-Blizzard-admits-some-were-too-simple.1424285.0.html)
- [Blizzard EU forums – WoW Forever Beta Development Notes, updated 15 October](https://eu.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-15-october/631316)
- [Blizzard forums – WoW Forever Beta Development Notes](https://us.forums.blizzard.com/en/wow/t/wow-classic-forever-beta-patch-notes/2360696)
- [Blizzard forums – No extra Rage on crit has been reverted](https://us.forums.blizzard.com/en/wow/t/warriors-rejoice-no-extra-rage-on-crit-has-been-reverted/2367562)
- [Icy Veins – WoW Forever reworked Warrior rage](https://www.icy-veins.com/wow-forever/news/wow-forever-just-reworked-warrior-rage-and-players-cant-stop-talking-about-it/)
- [Kami-labs – Consecration in WoW Forever](https://kami-labs.fr/en/wow-forever/consecration-wow-forever-quatre-cibles/)
- [WoW Forever Talents – Warrior spellbook](https://wowforevertalents.com/abilities/warrior/)
- [WoW Forever Talents – Druid spellbook](https://wowforevertalents.com/abilities/druid/)
- [Allakhazam – Spell coefficient (Classic)](<https://everquest.allakhazam.com/wiki/spell_coefficient_(WoW)>)
