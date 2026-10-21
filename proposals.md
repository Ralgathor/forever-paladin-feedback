# Forever Paladin Talent Proposals

This document proposes 15 talent changes, 2 new talents and 1 Judgement change for the WoW Forever Paladin. The goal is to follow the rules Forever already uses for the other hybrid classes, without changing what each tree is about. Each proposal follows a talent that another class already has in the same beta build.

## How to read this document

- **IDs.** H = Holy, P = Protection, R = Retribution, J = Judgements. Withdrawn proposals keep their ID and are listed under Withdrawn ideas.
- **Each proposal** gives the change, the proposed tooltip, the reason and the talent it follows.
- **Data.** Beta client build 1.60.1.70425 (16 October 2026). Talent text comes from wowforevertalents.com, except Vindication (ForeverChanges). Tested behavior comes from player tests shared on 19 October 2026.
- **Limits.** These are design ideas, not tested in play. Combat and mana numbers use Classic 1.12 rules unless a test says otherwise.

## Summary

| # | Talent | Tree, points | Beta | Proposed | Status |
| --- | --- | --- | --- | --- | --- |
| H1 | Reverence | Holy, 5 (row 2 with H6) | 10/20/30% regen while casting | 17/33/50% | Proposed |
| H3 | Light's Vigil | Holy, 30 | 730 mana | About 500 mana | Proposed |
| H4 | Lingering Light (new) | Holy, 20 (row 5 with H6) | — | Crit heals add a rolling heal over time of 15/30% of the heal | Proposed |
| H5 | Infusion of Light | Holy, 5 (row 2 with H6) | Holy Shock and Flash of Light crits speed up the next Holy Light | Holy Strike crits also trigger it | Proposed |
| H6 | Holy layout | Holy, rows 2–6 | — | Healing Light to row 6 (2 ranks); Infusion of Light and Reverence to row 2; Consecrated Ground to row 3; Spiritual Focus to row 4; Lingering Light in row 5 | Proposed |
| H7 | Divine Strength → Improved Seals | Holy, row 1 | Divine Strength in row 1; Improved Seals in row 2 (5/10/15%) | Improved Seals in row 1, 5 ranks, 3/6/9/12/15%; Divine Strength moves to Protection (P6) | Proposed |
| P2 | Improved Hammer of Justice | Protection, 10 (row 3) | Row 4, 3 ranks, −5/10/15 sec | Row 3, 3 ranks, −5/10/15 sec (beta values) | Proposed |
| P4 | Redoubt | Protection, row 1 | 10% chance on hit for +4–20% block | Same, and every Holy Shield cast also triggers it | Proposed |
| P5 | Iron Creed | Protection, 25 | Damage taken −2–10% for 6 sec after Holy Strike | Same threat; damage taken −2–10% while Righteous Fury is active, no timer | Proposed |
| P6 | Toughness → Divine Strength | Protection, row 1 | Armor from items +2–10% | Divine Strength (+2–10% Strength), moved from Holy | Proposed |
| P7 | Row 3 and 4 clean-up | Protection, 10–15 | Improved Seal of Fury, Improved Righteous Fury in row 3; Swift Judgement in row 4 | Both removed; Swift Judgement in row 3; new Righteous Defense (area taunt) in row 4 | Proposed |
| P8 | Reckoning | Protection, 20 | 8–40% on block, 20–100% on being crit, for an extra attack; stores up to 4 | 20–100% on block, dodge or parry (once every 4 sec) or on being crit, for a charge (up to 4); Holy Strike spends up to 2 charges as extra attacks | Proposed |
| P9 | Fury's Reach (new) | Protection, 15 | None: no ranged pull or taunt | 2 ranks: Judgement range +5/10 yards while Seal of Fury is active; requires Swift Judgement | Proposed |
| R1 | Conviction | Ret, 5 | Melee crit +1–5% | Attack and spell crit +1–5% | Proposed |
| R3 | Two-Handed Weapon Specialization | Ret, 20 → 15 | Opens at 20 points | Opens at 15 points | Proposed |
| R5 | Sacred Arbiter and Repentance | Ret, 15 and 20 | Sacred Arbiter at 15, Repentance at 20 | Rows swapped; Holy Strike always triggers your Seal | Proposed |
| R6 | Twist of Light | Ret, 30 | Echo applies to the next melee attack only | Echo applies to every melee attack for 10 sec | Proposed |
| J5 | Judgement of the Crusader | Baseline | Raid debuff, uses the Paladin's one Judgement | Personal debuff, outside the one-Judgement limit (recommended) | Proposed |
| J1 | Judgement of Light and Wisdom | Baseline | Two separate Judgements | Merged into Judgement of Grace (fallback to J5) | Proposed |
| J4 | Twist of Light | Ret, 30 | Echo for damage Seals only | Adds a 40-sec Judgement Echo (optional, on top of J5) | Proposed |

Withdrawn: P1, H2, P3, R2, R4. See Withdrawn ideas.

## Design rules

Forever builds its talent trees with five rules. Every proposal follows them.

1. **No improved-buff talents.** Buffs such as Blessing of Kings come from the trainer, not from talents.
2. **Rows 1–2 tempt the other specs.** Early talents should make the other two specs want to dip into the tree.
3. **Shared stats cover melee and spells.** Precision gives hit for both, like Thundering Strikes gives crit for both to Shaman.
4. **Each tree has 1-point signature talents** in rows 3 and 4, and ends on a 1-point capstone at 30 points.
5. **The class fantasy stays.** Holy heals with the Light. Protection holds the line with a shield. Retribution judges with a two-handed weapon and Seals.

### What the other classes do

| Pattern | Other classes | Paladin beta |
| --- | --- | --- |
| Mana regen while casting (healers) | Meditation (Priest), Reflection (Druid), Mindfulness (Shaman): 50% | Reverence: 30% |
| Mana regen while casting (damage and hybrid specs) | 50% at about 20 points: Bestial Discipline, Resourcefulness (Hunter), Improved Stormstrike (Shaman), Spirit Tap (Priest); Rapid Recuperation (Hunter) gives 100% for 15 sec | None for Protection or Ret |
| Deep healing bonus | Spiritual Healing (Priest, 25 points), Purification (Shaman, 25 points) | Healing Light (+12%) at 5 points |
| Healer capstone cost | Riptide 245 mana, Wild Growth 550, Prayer of Mending 210 | Light's Vigil 730, plus 160 for the Holy Shock that triggers it |
| Shared crit | Thundering Strikes (Shaman, row 1): all spells and attacks | Conviction: melee only |
| Two-handed weapon talent | Warrior: 15 points | 20 points |
| Stun cooldown talent | Brutal Impact (Druid): 2 ranks, −15/−30 sec on Bash | Improved Hammer of Justice: 3 ranks, −5/−10/−15 sec |
| Area taunt | Challenging Shout (Warrior), Challenging Roar (Druid): 10 yd, 6 sec, 10 min | None |

## Holy

Most saved Holy builds stop around 20 points. These changes make the path to Light's Vigil worth taking for a healer, and give Ret and Protection clear reasons to dip into Holy.

### Holy layout after H4, H6 and H7

| Row (level) | Talents | Points |
| --- | --- | --- |
| 1 (10) | Improved Seals (H7), Divine Intellect | 10 |
| 2 (15) | Infusion of Light, Reverence, Unyielding Faith | 7 |
| 3 (20) | Voice of Truth, Purifying Power, Consecrated Ground | 5 |
| 4 (25) | Spiritual Focus, Illumination, Divine Favor | 8 |
| 5 (30) | Divine Precision, Holy Shock, Lingering Light (H4) | 6 |
| 6 (35) | Holy Power, Healing Light | 7 |
| 7 (40) | Light's Vigil | 1 |

Holy goes from 46 to 44 points. Every talent can be used when its row opens, and Illumination still requires Reverence (straight arrow, column 2).

### H1. Reverence: 10/20/30% → 17/33/50%

- **Proposed text.** "Allows 17/33/50% of your Mana regeneration to continue while casting."
- **Model.** Meditation (Priest), Reflection (Druid) and Mindfulness (Shaman) all give 50% in 3 ranks.
- **Why Illumination is not enough.** Other healers also have a mana return on top of their 50% (Litany of Light, Water Shield, Mana Tide Totem). Forever also halved Illumination: it returns 50% of the base cost.
- **With H6.** Reverence moves to row 2, so it is also the regen talent for Protection and Ret (see Mana).
- **Fallback.** If it proves too strong, use 13/27/40%.

### H3. Light's Vigil: 730 mana → about 500

- **Cost today.** 730 mana, plus 160 for the Holy Shock that triggers it: 890 in total.
- **Healing.** 325–344 on each party member: about 1,670 on five players, plus about 115 from Holy Shock.
- **Problem.** Even with five players hurt, it gives about 2.0 healing per mana. Holy Light rank 9 gives about 2.4 (660 mana).
- **At about 500.** The full combo costs 660 mana, the same as Holy Light, and heals about 1,780 across the party. It stays a group heal that only pays off when several players are hurt.

### H4. New talent: Lingering Light (row 5, column 3, 2 ranks)

- **Proposed text.** "Your non-periodic critical heals cause the target to be healed for an additional 15/30% of the amount healed over 6 sec. Refreshing this effect carries over any remaining healing."
- **Identity.** A heal over time from crits is a Paladin idea (WotLK's Sheath of Light). It is not Priest's Divine Aegis, which is a shield, and it is Holy's only heal over time.
- **Wording.** "Non-periodic critical heals" comes from Priest's Divine Aegis and Inspiration. "Refreshing this effect carries over any remaining healing" comes from Priest's Blessed Recovery, which already rolls its healing in Forever.
- **Why crit.** Healing Light already gives a flat healing bonus. The Holy tree invests in crit (Illumination, Infusion of Light, Divine Favor, Holy Power), and this talent pays it off.
- **Value.** About 25% crit × 30% ≈ +7.5% healing. Some of it overheals on full targets.

**How it rolls.** It follows Forever's Ignite and Blessed Recovery, not Deep Wounds.

|  | Ignite (Mage) | Deep Wounds (Warrior) | Lingering Light |
| --- | --- | --- | --- |
| Amount | 8–40% of the crit's damage | 20–60% of average weapon damage, the same for every crit | 15/30% of the crit heal |
| Duration | 4 sec, a tick every 2 sec | 12 sec | 6 sec, a tick every 2 sec |
| New crit while active | Remaining damage is kept and added | Refreshes the duration only | Remaining healing is added, then spread over a new 6 sec |
| Per caster | One per Mage per target | One per target | One per Paladin per target |

- **Amount.** Taken from the full crit heal, overhealing included.
- **No double bonus.** Healing bonuses apply once, to the crit. The heal over time is not increased again and cannot crit.
- **In play.** Repeated crits on the tank build a bigger heal over time. Divine Favor on Holy Light gives a planned large one. Holy Shock crits (+15% from Holy Power) add frequent small amounts.

### H5. Infusion of Light: Holy Strike crits also trigger it

- **Proposed text.** "Your Holy Shock, Holy Strike and Flash of Light critical hits reduce the cast time of your next Holy Light cast within 15 sec by 0.5/1 sec."
- **What changes.** Only Holy Strike is added. Values and duration stay as in the beta.
- **Synergy.** Holy Power gives +15% crit to both Holy Shock and Holy Strike, but only Holy Shock fed Infusion of Light.
- **In play.** A Holy Paladin who melees between heals gets a reason to use Holy Strike. Ret and Protection, who use Holy Strike in their rotation, get faster emergency Holy Lights.
- **Limit.** Holy Strike has a 10-sec cooldown, so at most one extra chance every 10 sec.
- **Risk.** With H6 it is in row 2, so a 7-point Holy dip gives Ret or Protection a faster self-heal in PvP. The 10-sec cooldown keeps it modest.

### H6. Holy layout: Healing Light moves to row 6

| Talent | Beta | Proposed | Why |
| --- | --- | --- | --- |
| Healing Light | Row 2, 3 ranks (4/8/12%) | Row 6, 2 ranks (6/12%) | Puts the +12% healing bonus at 25 points, like Spiritual Healing and Purification. A Holy Paladin with 28 points in Ret has only 23 for Holy and can't reach it |
| Infusion of Light | Row 4 | Row 2 | Ret and Protection keep a healing reason to dip into Holy. Faster heals, not bigger ones |
| Reverence | Row 3 | Row 2 | Gives Protection and Ret regen while casting for 8 Holy points, like Enhancement Shaman reaches Mindfulness with 8 Restoration points |
| Consecrated Ground | Row 5 | Row 3 | Row 3 opens at level 20, when Consecration is learned. Protection reaches it with 12 Holy points instead of 22, for AoE threat |
| Spiritual Focus | Row 2 | Row 4 | Makes room in row 2. Spell pushback only matters to healers |
| Lingering Light (H4) | — | Row 5 | Next to Holy Shock, whose crits trigger it |
| Unyielding Faith | Row 2, column 4 | Row 2, column 3 | Fills the gap left when Improved Seals moves to row 1 (H7), so row 2 has no empty slot between talents |

- **Deep Holy** keeps Healing Light, Holy Power, Lingering Light and Light's Vigil, so going deep stays clearly better for healing.
- **Cost.** A leveling Holy Paladin gets +12% healing at level 35 instead of 15.

### H7. Row 1: Improved Seals replaces Divine Strength

- **Proposed text.** "Increases the damage done by your Seals and Judgements by 3/6/9/12/15%."
- **What changes.** Improved Seals moves from row 2 (3 ranks, 5/10/15%) to row 1 with 5 ranks: the same 15% at max rank. Divine Strength leaves Holy and moves to Protection row 1 (P6).
- **Dip.** 5 Holy points now give +15% Seal and Judgement damage to Ret and Protection. Seals are the class's own damage, so the dip is more Paladin-specific than Strength.

### Holy: beta test results

| Talent | Observed in the beta | Effect on the proposals |
| --- | --- | --- |
| Divine Strength, Divine Intellect | % of base, gear and flat-buff stats; multiplies with Kings | Divine Strength moves to Protection (P6) |
| Healing Light | Boosts the whole heal, not just its base | Supports H4: a flat healing talent would overlap |
| Spiritual Focus | Adds to other pushback resistance (Concentration Aura 70% + 35% = immune) | None |
| Improved Seals | Boosts the whole damage, not just its base; doesn't affect Seal of the Crusader | None |
| Unyielding Faith | Diminishing returns not tested | None |
| Reverence | Keeps a % of Spirit regen while casting; the 5-second rule restarts when a cast ends | H1 still applies |
| Purifying Power | Multiplies with Benediction (×0.80 × 0.90) | None |
| Illumination | Returns 50% of the base cost, so discounts don't reduce the return | None |
| Divine Favor | Off the global cooldown | None |
| Divine Precision | The spell hit cap is 18% with no unavoidable 1% miss; 3/3 covers it alone | No change needed |
| Holy Shock | Damage scales with spell damage, healing with healing power; both at 42.9% | None |
| Consecrated Ground | Boosts all your Holy damage on those targets, including Retribution Aura and Consecration | None |
| Light's Vigil | Needs more testing | H3 still applies |

## Protection

Protection gets a fix for crushing blows (P4), its biggest gap with Warrior, a cleaner tree (P2, P5, P6, P7), a Reckoning that rewards avoidance and player choice (P8) and a ranged Judgement for pulls (P9).

### Protection layout after P2, P6, P7 and P9

| Row (level) | Talents | Points |
| --- | --- | --- |
| 1 (10) | Divine Strength (P6), Redoubt | 10 |
| 2 (15) | Precision, Guardian's Favor, Anticipation | 10 |
| 3 (20) | Swift Judgement, Improved Hammer of Justice (P2), Shield Specialization, Sacred Duty | 9 |
| 4 (25) | Fury's Reach (P9), One-Handed Weapon Specialization, Righteous Defense (P7) | 6 |
| 5 (30) | Templar's Bulwark, Reckoning | 6 |
| 6 (35) | Iron Creed | 5 |
| 7 (40) | Holy Shield | 1 |

Protection goes from 48 to 47 points. Rows 1–4 hold 35 points, more than the 20 needed to open row 5.

### P2. Improved Hammer of Justice: moves to row 3, beta values

- **Proposed text.** "Decreases the cooldown of your Hammer of Justice spell by 5/10/15 sec." (3 ranks, same as beta; only the row changes)
- **Model.** Druid's Brutal Impact on Bash, which also has a 60-sec base cooldown.
- **Why.** It is one of the least-taken Paladin talents. Values stay as in the beta and only the row changes. It moves to row 3 because P7 empties part of that row.
- **Watch in PvP.** Holy or Ret now reach the full −15 sec Hammer of Justice (a 45 sec cooldown) with 13 Protection points instead of 18. Druid has Brutal Impact in Feral row 2 (−30 sec on Bash), so this stays in line.

### P4. Redoubt: add a Holy Shield trigger

- **Proposed text.** "Damaging melee attacks against you have a 10% chance to increase your chance to block by 4/8/12/16/20%. Lasts 10 sec or 5 blocks. Casting Holy Shield also triggers this effect."
- **What changes.** Only the Holy Shield trigger is new. Triggering Redoubt while it is active resets it to 10 sec and 5 blocks.
- **Why.** It removes most crushing blows. See Crushing blows.
- **Blizzard's direction.** The October 1 patch moved block from Redoubt (6–30% → 4–20%) to Holy Shield (20% → 30%). P4 keeps those values; Redoubt only gains uptime.
- **Other specs.** Holy and Ret don't have Holy Shield, so their Redoubt doesn't change.
- **Side effects.** Block from talents goes from about 40% on average to about 50%: slightly more Reckoning procs, Shield Specialization mana and Holy Shield damage.

### P5. Iron Creed: damage reduction while Righteous Fury is active

- **Proposed text.** "Increases the threat generated by your Holy Strike ability by 5/10/15/20/25%. While Righteous Fury is active, reduces your damage taken by 2/4/6/8/10%."
- **Problem.** In the beta the buff lasts 6 sec after a Holy Strike that can be used every 10 sec, so at 5/5 it averages only about 6% damage reduction.
- **Result.** The reduction works whenever Righteous Fury is active. It has no timer and no Holy Strike condition, so Holy Strike keeps only the Reckoning release as an extra mechanic. The Holy Strike threat bonus stays. It is worth about 2.5-4.4 threat per second, while Reckoning adds about 27. This is a deliberate exception to the no-improved-buff rule: it works like the removed Improved Righteous Fury, but it needs 25 Protection points. Watch it in PvP, because any class can use Righteous Fury.
- **Total.** 10% damage reduction, the same as Warrior's Defensive Stance. Improved Righteous Fury, which stacked on top (about 15% in total), is removed by P7.

### P6. Toughness → Divine Strength (from Holy)

- **Proposed text.** "Increases your Strength by 2/4/6/8/10%." Unchanged from the beta; only its tree changes.
- **Why remove Toughness.** Forever moved away from flat armor talents for tanks: Warrior's Toughness was removed, Shaman's now gives Stamina, and Druid's Thick Hide grows with Defense. Paladin's Toughness was the last flat armor talent.
- **Why Divine Strength.** Strength is the Protection Paladin's stat: Attack Power for threat and some block value (20 Strength = 1). Holy no longer needs it (H7).
- **Row 1 for every spec.** Holy and Ret reach Precision through Protection row 1, and Divine Strength is useful to all three specs.
- **Parity.** One % Strength talent for the class, like Druid's Heart of the Wild. No extra Stamina: only Sacred Duty's +4%.
- **Watch.** Ret now gets Strength and 3% hit in one 8-point Protection dip.

### P7. Rows 3–4: remove two talents, add Righteous Defense

- **Improved Righteous Fury: removed.** With Iron Creed always up (P5), the two stacked to about 15% damage reduction. Iron Creed alone gives Warrior's 10%.
- **Improved Seal of Fury: removed.** It was a second "mana from being hit" talent, and its return ignores the Seal's rank. Reverence in row 2 (H6) covers mana instead (see Mana).
- **Swift Judgement moves to row 3** and no longer needs Improved Seal of Fury.
- **New: Righteous Defense (row 4, 1 point).** "Forces all enemies within 10 yards to attack you for 6 sec." Instant, 10-min cooldown.
  - It matches Warrior's Challenging Shout and Druid's Challenging Roar: same area, duration and cooldown.
  - Judgement of Fury stays the single-target taunt.
  - Every tree keeps a 1-point signature talent in rows 3 and 4: Holy has Voice of Truth and Divine Favor, Ret has Seal of Command and Repentance (after R5), Protection has Swift Judgement and Righteous Defense.
  - Holy and Ret can reach it with 15 points but have no use for an area taunt.
- **Unchanged.** Righteous Fury, Seal of Fury and its absorb stay baseline.

### P8. Reckoning: charges from avoidance, spent by Holy Strike

- **Proposed text.** "Gives you a 20/40/60/80/100% chance to gain an extra attack after Blocking, Dodging, Parrying or being the victim of a non-periodic critical strike. Cannot occur from Blocks, Dodges or Parries more than once every 4 sec. Stores up to 4 extra attacks. Your Holy Strike releases up to 2 stored extra attacks." Worded like Classic's extra-attack effects: Reckoning ("a 20% chance to gain an extra attack after being the victim of a critical strike"), Sword Specialization and Hand of Justice.
- **Beta text.** "Gives you a 8/16/24/32/40% chance after Blocking and a 20/40/60/80/100% chance after receiving a non-periodic critical strike to gain an extra attack. Stores up to 4 extra attacks. Cannot occur from Blocks more than once every 1.5 sec."
- **The crit trigger stays, for the Classic "Reckoning bomb".** Like the beta, the 4-sec limit applies only to block, dodge and parry. In raids it changes nothing: at 440 Defense bosses can't crit. While leveling and in PvP, crits fill charges fast, so a Paladin can store 4 and unload them with Holy Strike. Holy Strike releases at most 2 charges, so one Holy Strike is 3 hits at most.

**Problems in the beta.**

- **The crit trigger is dead at endgame.** At 440 Defense a boss can't crit (see Stat targets), so half the talent only works while leveling or in PvP.
- **Storage does nothing while tanking.** A tank attacks all the time, so stored attacks fire on the next swing. Storing only happens when you stop attacking (the Classic "Reckoning bomb").
- **No player choice,** and low value: about one extra attack every 8 sec, about +24 damage per second.

**What P8 changes.**

- **Trigger: block, dodge or parry.** It works at the crit cap, like Warrior's Master of Defense (Rage on dodge or parry). About 86% of boss swings are avoided at the stat targets.
- **Ranks raise the chance (20–100%); the 4-sec limit is fixed,** like other proc talents.
- **Holy Strike spends the charges.** Storage becomes a decision: spend every 10 sec, or hold charges for a target switch, a taunt or a dangerous add (up to 3 hits in one Holy Strike).
- **A shield-to-attack link,** like Warrior's Shield Slam, which the community discussion on Wowhead says Paladins lack.
- **The Reckoning bomb stays,** capped at 4 charges.

**Value at 5/5** (simulation: boss swings every 2 sec, 86% avoided, Holy Strike every 10 sec, about 200 damage per extra attack).

| Version | Charges per Holy Strike, 1 boss | Charges per Holy Strike, 3 attackers | Damage per sec, 1 boss |
| --- | --- | --- | --- |
| Beta (40% on block, crit trigger dead) | About 1.2, fired at once | — | About +24 |
| 40%, once per 1.5 sec (first draft) | 1.7 | 3.2 | +34 |
| 100%, once per 1.5 sec | 3.8, often wasted at the cap | 4.0 | +76: too strong, no choice left |
| **P8: 100%, once per 4 sec, Holy Strike spends 2** | **2.3** | **2.4** | **About +40** |

- **The 4-sec limit** keeps the rate the same on a boss and on a pack, and leaves room below the cap, so holding charges is a real choice.
- **About +30% of a tank's melee damage,** all of it on Holy Strike, whose threat Iron Creed already raises.
- **Risk.** In PvP, 4 stored charges is a big burst. Holy Strike releases at most 2, so one stun window gives Holy Strike plus 2 extra attacks (3 hits), and the other 2 charges wait for the next Holy Strike. The meme stays (4 crits taken, 4 charges stored), but it now takes two Holy Strikes to empty. For a tank this costs about 10-15% of Reckoning damage and almost no threat.

**PvP burst check, build 0/26/25 (two-hander).** This is the build p-5532000210215-50005031211331 in the calculator: Protection 26 (Reckoning 5/5, Swift Judgement, Improved Hammer of Justice 2/3) and Retribution 25 (Seal of Command, Sacred Arbiter, 2H Specialization 3/3, Vengeance 3/3, Conviction 5/5). The numbers are rough estimates, not a simulation.

**Assumptions.** A two-hander swing is 300 damage including Attack Power. Crit chance is 25%, and 30% of physical damage is lost to armor. Seal of Command procs 7 times per minute on a 3.5 sec weapon. The stun lasts 6 sec. Holy Strike is a full Holy attack (cooldown 10 sec). Seal of Command at max rank: 70% weapon damage per proc, Judgement 194-211 Holy damage, or 388-422 if the target is stunned. Swift Judgement has a 1 min cooldown, Hammer of Justice 50 sec (60 sec base, −10 sec with 2/3 ranks; 45 sec at 3/3). The build keeps its 26 Protection points, so it takes 2 of the 3 ranks. The calculator shows a lower Seal of Command rank (74, or 136-148 stunned) than the real tooltip.

| Part of the burst in one stun | Release all 4 | Release 2 (P8) |
| --- | --- | --- |
| Holy Strike with Sacred Arbiter | about 515 | about 515 |
| Extra attacks (about 395 each) | 4: about 1,580 | 2: about 790 |
| Two auto-attacks | about 590 | about 590 |
| Two stunned Judgements (with Swift Judgement, about 530 each) | about 1,060 | about 1,060 |
| **Total** | **about 3,750** | **about 2,960** |

The uncertainty is about 25%, so release 2 is roughly 2,200-3,700. When Swift Judgement is on cooldown (Swift Judgement 60 sec, Hammer of Justice 50 sec), the total is about 2,430.

| Beta comparison (same model) | Burst |
| --- | --- |
| Beta, nothing stored (usual case) | about 1,640 |
| Beta, 4 crits taken first (the Classic meme) | about 3,220 |
| Proposed, release 2, Swift Judgement up | about 2,960 |
| Proposed, release 2, Swift Judgement on cooldown | about 2,430 |

- **Result.** Release 2 cuts the burst by about 20% compared with releasing all 4. The proposal is about 80% above beta's usual burst and about 8% below beta's best case, and the 4-crit meme bomb is preserved.
- **Decision.** The shield requirement on Reckoning was rejected because it would end the Classic meme. The Reckoning/Iron Creed swap and a change to Swift Judgement were not applied. Improved Hammer of Justice stays at the beta values (3 ranks, −5/10/15 sec; only the row changes). Swift Judgement is about 18% of the burst, so it stays on the watch list.
- **Iron Creed does not change the burst.** It only reduces damage taken while Righteous Fury is active and adds Holy Strike threat. Reckoning adds about 27 threat per second over beta, while the Holy Strike bonus is worth 2.5-4.4, so the bonus is kept (option A).

### P9. Fury's Reach: a ranged pull for Protection

- **Proposed text.** "Increases the range of your Judgement by 5/10 yards while Seal of Fury is active." 2 ranks, row 4, column 1. Requires Swift Judgement (a straight arrow from row 3). Righteous Defense moves to column 3.
- **Why.** Protection has no ranged pull or taunt. Seal of Fury's Judgement already deals 163-178 Holy damage and taunts for 4 sec, but only from 10 yards. With 2 ranks it reaches 20 yards, double the base range.
- **Model.** Warrior has Vanguard (Charge in Defensive Stance, row 4, 1 point) and Druid has Feral Charge (row 3 perk) and a ranged pull in Feral. Paladin had nothing.
- **Why it needs ranks.** Row 4 already has a 1-point talent (Righteous Defense), so this one has 2 ranks like the rest of the row.
- **Why only with Seal of Fury.** Seal of Command Judgement deals 388-422 to a stunned target. Without the condition, that would be a 20 yard burst for hybrids in PvP. With it, Holy and Ret get almost nothing from the 15-point dip.
- **Threat and mana.** No change to threat per second: Judgement still costs 91 mana and has a 10 sec cooldown. Only the opener changes, since it pulls from range. Swift Judgement is the prerequisite, so the full path costs 3 points (Swift Judgement plus 2 ranks), and the range is also used by the Judgement it resets.
- **Open question.** Is a 20 yard pull enough to be worth 3 points? +5 yards per rank keeps it at only double the base range, which is the balance choice.

### Crushing blows

#### The problem

A raid boss is 3 levels above the player. In Classic rules, it has a 15% chance to land a crushing blow for 150% damage. Crushes only disappear when miss + dodge + parry + block reach 100% against the boss (about 102.4% on the character sheet). A tank can either push crushes off the attack table (Warrior) or survive them with armor and health (Druid).

| Tank | How crushes are handled | Result |
| --- | --- | --- |
| Warrior | Shield Block: +75% block, 2 blocks, 7 sec, 5-sec cooldown; Shield Specialization +5% block | Pushes crushes off the table with modest gear, but leaks after the 2 blocks |
| Druid | No shield; Thick Hide armor grows with Defense; Bear Form adds up to +20% Stamina | Always crushable, but has the armor and health to take it |
| Paladin (beta) | Holy Shield: +30% block, 4 charges, 10 sec, 10-sec cooldown; Redoubt is a 10% proc | Needs about 72% avoidance from gear: crushable like a Druid, without the Druid's armor and health |

**Two paths.** Path A pushes crushes off the table with block, the stat the tree already builds on. Path B adds armor, health and a stronger Seal of Fury absorb to survive them, but healers still face the spikes. **Path A was chosen.** That is P4.

#### The fix: Holy Shield also triggers Redoubt

- **Redoubt in the beta** is a block buff with charges: +4–20% block for 10 sec or 5 blocks. Only 10% of melee hits start it, so it is up about half the time.
- **With P4,** each Holy Shield cast (every 10 sec) restarts Redoubt, so both buffs are always up together.
- **Charges are enough.** A boss swinging every 2 sec swings 5 times in 10 sec, and about 3 of those are blocked: fewer than Redoubt's 5 blocks and Holy Shield's 4 charges.
- **First hit.** Casting Holy Shield before the pull covers the boss's first swing.
- **Holy Shield stays at +30%.** With the Redoubt trigger, +30% already matches Warrior. +35% and +40% were checked and dropped.

#### Stat targets

Against a level 63 boss (Defense skill 315), with Classic rules.

- **Crit immunity: 440 Defense.** The boss has 5.6% crit against a level 60, and each Defense point removes 0.04%. Anticipation gives 20, so gear and enchants must give +120.
- **Crush immunity: miss + dodge + parry + block = 100%.** At 440 Defense each roll gets +5% from Defense.

With 5/5 Deflection, Holy Shield and Redoubt up:

| Roll | Sources | Against the boss |
| --- | --- | --- |
| Miss | 5% base + 5% Defense | 10% |
| Dodge | About 0.7% base + 5% Defense + Agility ÷ 20 | 5.7% + Agi/20 |
| Parry | 5% base + 5% Deflection + 5% Defense | 15% |
| Block | 5% base + 5% Defense + 30% Holy Shield + 20% Redoubt | 60% |
| Total |  | 90.7% + Agi/20 |

- **Gap after the crit cap: about 9.3%,** about 186 Agility or 58 Defense above 440. Until it closes, the missing % is the crush chance: with about 100 Agility, about 4% of swings can crush, like a Warrior between Shield Blocks.
- **Holy Shield is the whole mechanism.** Without it, the Paladin is fully crushable.
- **Gaps.** A delayed Holy Shield leaves a short gap, and fast or dual-wielding bosses can use up the charges early.

#### Compared with Warrior

Both tanks at 440 Defense with about 100 Agility, against a boss swinging every 2 sec. Shield Block tooltip on Wowhead: "Increases chance to block by 75% for 7 sec, but will only block 2 attacks", 10 Rage, 5-sec cooldown.

|  | Swings covered | Crush chance on other swings | Swings that can crush |
| --- | --- | --- | --- |
| Warrior | About 80% (2 of 2.5 per cycle) | 15% | About 3% |
| Paladin, Holy Shield +30% (proposed) | About 100% | About 4.3% | About 4.3% |
| Paladin, +35% | About 100% | 0% | About 0% |
| Paladin, +40% | About 100% | 0% | 0%, and no crits even below 440 Defense |

At +30%, Paladin and Warrior are level. Paladin's gap closes with gear; Warrior's gaps depend on boss swing speed.

### Protection: beta test results

| Talent | Observed in the beta | Effect on the proposals |
| --- | --- | --- |
| Toughness | Only armor from items; nothing from Devotion Aura, scrolls, elixirs, potions or Mark of the Wild | Supports P6 |
| Redoubt | A blocked hit can trigger it without using a charge | P4 keeps the proc |
| Precision | Melee, ranged and spell hit; each ability uses the matching hit type | Confirms it as the shared hit talent |
| Anticipation | A raid boss stops critting at 440 Defense; Anticipation gives 20 | The stat targets assume this cap |
| Improved Seal of Fury | Mana return ignores the Seal's rank; no threat from the mana | Removed by P7 |
| Improved Righteous Fury | Applies after armor; multiplies with Iron Creed (×0.94 × 0.90) | Removed by P7 |
| Shield Specialization | Multiplies Shield Block Value; mana return is 4%; no threat from the mana | Stays: Protection's main mana source |
| Sacred Duty | % of total Stamina, multiplies with Kings; shortens the cooldowns of Forbearance spells | None |
| Swift Judgement | Off the global cooldown | None |
| One-Handed Weapon Specialization | Melee, Seals, Judgements, Holy Strike and Twist of Light Echo | Confirms P1's withdrawal |
| Templar's Bulwark | An absorb, not a heal: Mortal Strike effects don't reduce it | None |
| Reckoning | Stored attacks fire on the next melee hit; each can trigger Seals and Judgements | P8: charges come from avoidance and are spent by Holy Strike |
| Iron Creed | Holy Strike threat ×1.90 (Righteous Fury) × 1.25 | P5 keeps these multipliers |
| Holy Shield | Threat ×1.90 (Righteous Fury) × 1.20; more testing needed | None |

## Retribution

These changes link Ret's melee to its Holy spells and cut the Seal-swapping load.

### Retribution layout after R3 and R5

| Row (level) | Talents | Points |
| --- | --- | --- |
| 1 (10) | Deflection, Benediction | 10 |
| 2 (15) | Improved Judgement, Holy Conduit, Conviction | 9 |
| 3 (20) | Vindication, Sanctified Judgement, Seal of Command, Pursuit of Justice | 9 |
| 4 (25) | Eye for an Eye, Repentance (R5), Two-Handed Weapon Specialization (R3) | 6 |
| 5 (30) | Vengeance, Sacred Arbiter (R5) | 4 |
| 6 (35) | Champion of the Light, Instrument of Law | 5 |
| 7 (40) | Twist of Light | 1 |

Ret stays at 46 points.

### R1. Conviction: attacks and spells

- **Proposed text.** "Improves your chance to get a critical strike with attacks and spells by 1/2/3/4/5%."
- **Model.** Shaman's Thundering Strikes made the same change.
- **Real change.** In the beta, Conviction already crits damaging Seals and Hammer of Wrath. The change only adds Holy Shock, Exorcism, Consecration and heals.
- **Cost for healers.** A Holy dip costs 10 points (5 in row 1, then Conviction).

### R3. Two-Handed Weapon Specialization: 20 → 15 points

- **Model.** Warrior's version opens at 15 points.
- **Room.** Ret row 4 has space after R5. Values stay at 2/4/6%.

### R5. Sacred Arbiter and Repentance: swap rows, make Sacred Arbiter stronger

- **Proposed text.** "Causes your Holy Strike ability to always trigger the effect of your active Seal and to refresh all Judgement effects on the target, including those of other Paladins. Does not trigger the stun of Seal of Justice."
- **Rows.** Sacred Arbiter moves from 15 to 20 points, Repentance from 20 to 15.
- **What it replaces.** The beta's +20% Holy Strike damage. Holy Strike is too weak for that to matter: +30% would add only about 6 damage per second with a typical two-hander. A guaranteed Seal of Command effect adds about 16.
- **Model.** Ret's core payoff, as Stormstrike is for Enhancement.
- **Safety.** It triggers the Seal, not a second Judgement. The stun exception keeps a guaranteed stun every 10 sec out of PvP.
- **Tradeoffs.** Protection builds that take Sacred Arbiter for its Judgement refresh can't reach it at 20 points. Repentance becomes easier to reach for Holy and Protection in PvP.

### R6. Twist of Light: the Echo lasts 10 sec

- **Problem.** Each Echo lasts for one melee attack, so full value means swapping Seals before almost every swing: about 80% of the time in global cooldowns with a 3.5-sec two-hander. Players on the beta forums cite a developer statement that rotations should stay around four buttons.
- **Proposed text.** "Reduces the Mana cost of your Seal spells by 20%. When you replace your Seal of Command, Seal of Righteousness, Seal of Fury, or Seal of Justice with a different Seal, you gain an Echo of that Seal for 10 sec. While the Echo lasts, your melee attacks also apply the replaced Seal's effects."
- **Same action, slower rhythm.** You still swap Seals, but once every 10 sec, with Holy Strike and Judgement.

| Each 10 sec, 3.5-sec weapon | Beta | With R6 |
| --- | --- | --- |
| Seal casts | About 3 | 1 |
| Holy Strike | 1 | 1 |
| Judgement (8-sec cooldown) | 1.25 | 1.25 |
| Time in global cooldown | About 79% | About 49% |
| Mana spent (single target) | About 41.6 per sec | About 11.4 per sec |

- **Mana.** With one swap every 10 sec, Sanctified Judgement's refund covers most of the cost, so R6 is also Ret's main mana fix.
- **Alternative.** Two Seals active at once would use fewer global cooldowns but removes Seal swapping, the action the talent is built on.

### Retribution: beta test results

| Talent | Observed in the beta | Effect on the proposals |
| --- | --- | --- |
| Benediction | Its cost cut multiplies with Purifying Power, Holy Conduit and Twist of Light | None |
| Holy Conduit | With Benediction, instant spells cost ×0.60 × 0.90 | None |
| Conviction | Also crits damaging Seals and Hammer of Wrath | R1 only adds Holy Shock, Exorcism, Consecration and heals |
| Vindication | About 5 procs per minute; ranks −67/136/204 target Attack Power and +1/2/3% yours | None |
| Sanctified Judgement | Refunds more than 60% of the base cost with Benediction | Probably a bug to report |
| Pursuit of Justice | 15% at 2/2; beats the 8% boot enchant | Watch (F5) |
| Eye for an Eye | Uses damage taken after armor and resistance | None |
| Sacred Arbiter | +20% Holy Strike damage; refreshes Light, Wisdom, Justice and Crusader | R5 trades the +20% for the Seal trigger |
| Two-Handed Weapon Specialization | Melee, Seals, Judgements, Holy Strike and Twist of Light Echo | Supports R3 |
| Vengeance | Multiplies with other % damage; crits from procs add stacks | None |
| Repentance | Diminishing returns category not tested | None |
| Instrument of Law | Rank 2 makes Hammer of Wrath instant; the threat cut multiplies with Salvation | None |
| Twist of Light | Needs more testing; with Benediction, Seals cost ×0.72 | None |

## Mana

### What we found

- **Spirit regen** (15 + Spirit ÷ 5 every 2 sec) stops for 5 sec after each cast, so in combat it is close to zero without a regen-while-casting talent.
- **Other classes** give their damage and hybrid specs 50% regen while casting at about 20 points (see What the other classes do). Protection and Ret have none in the beta.
- **Protection's beta mana only comes from being hit** (Shield Specialization, Improved Seal of Fury). A Protection Paladin who is off-tanking or dealing damage has no income.
- **Ret's mana problem is Seal swapping,** not missing regen.

### The fix

- **Reverence in row 2 (H6)** gives Protection and Ret regen while casting for 8 Holy points, like Enhancement Shaman with Mindfulness: about 10 mana/sec at 50% (H1) and 120–130 Spirit.
- **Shield Specialization stays.** It is the tank's main source and has a Forever precedent in Shaman's Water Shield.
- **Improved Seal of Fury is removed (P7).**
- **R6 fixes Ret.**

### Results

**Inputs.** 4,000 max mana; base mana 1,512 (Classic value, not confirmed for Forever); 130 Spirit for Protection, 120 for Ret; boss swings every 2.0 sec; one-hand weapon at 2.7 sec; Holy Shield up. Costs from the Forever tooltips: Holy Shield 150, Holy Strike 20, Judgement 6% of base mana (91, 10-sec cooldown), Seal of Fury 200 every 30 sec, Seal of Command 210, Consecration 565 every 8 sec. The Ret dip applies Benediction (×0.90 on all of these) and Holy Conduit (×0.60 on Consecration).

**Income per second while tanking.**

| Source | Beta | Proposed | How it is counted |
| --- | --- | --- | --- |
| Shield Specialization: 160 mana per block, once every 3 sec | 26.7 | 30.0 | With a swing every 2 sec, the 3-sec cooldown skips the next swing; block chance about 50% in the beta, 60% with P4 |
| Improved Seal of Fury: 87 mana per shield fully absorbed | 18.7 | — (P7) | Each of your swings makes a new shield; it counts only if a boss hit lands before your next swing (36% of swings are avoided) |
| Reverence 50% (H1, H6) | — | 10.3 | Half of 41 mana every 2 sec at 130 Spirit |
| **Total** | **45.4** | **40.3** |  |

**Spending per second.** 32.7 without Consecration and 103.4 with it; with the Ret dip, 29.5 and 67.6.

| Protection | Beta | Proposed |
| --- | --- | --- |
| Tanking, no Consecration | +12.6/sec, sustainable | +7.5/sec, sustainable |
| Tanking, Consecration on cooldown | −58.0/sec → 69 sec | −63.1/sec → 63 sec |
| Tanking, Consecration on cooldown, Ret dip | −22.2/sec → 3 min | −27.4/sec → 2 min 26 sec |
| Not being hit, no Consecration | −32.7/sec → 2 min 2 sec | −22.5/sec → 2 min 58 sec |
| Not being hit, Consecration on cooldown | −103.4/sec → 39 sec | −93.1/sec → 43 sec |

| Ret, single target | Spending | No regen | With Reverence 50% |
| --- | --- | --- | --- |
| Beta Seal swapping (about 3 Seals every 10 sec) | 41.6/sec | 1 min 36 sec | 2 min 6 sec |
| R6 (one Seal every 10 sec) | 11.4/sec | 5 min 52 sec | About 41 min, close to sustainable |

- **Tanking stays sustainable without Consecration,** but the margin is thinner than first estimated: about +8 mana/sec instead of +13 in the beta. Removing Improved Seal of Fury (P7) costs more than Reverence gives back while tanking.
- **Reverence pays off when the Paladin is not being hit:** about 1 min more without Consecration.
- **Consecration on cooldown stays a tool for packs,** about 1 min either way, or about 2.5 min with the Ret dip.
- **Watch.** If tanking mana feels too tight in testing, the simplest fix is Shield Specialization's cooldown from 3 to 2 sec (+about 12 mana/sec at 60% block).

## Judgements in raids

### The problem

- **The rule.** Each Paladin can have only one Judgement active on a target.
- **The conflict.** Since the October 15 patch, Salvation no longer uses a Blessing slot, so two Paladins cover a raid's Blessings. But raids prefer Light and Wisdom, which help everyone, over Crusader, which mostly boosts the Paladins' own Holy damage. Crusader gets dropped, so Ret loses damage and Protection loses threat.
- **Sacred Arbiter doesn't fix it.** Holy Strike refreshes all Judgements on the target, "even those from other Paladins", but each Paladin still owns only one.

### Options

| Option | How it works | Precedent | Tradeoff |
| --- | --- | --- | --- |
| **J5. Personal Crusader (recommended)** | Judgement of the Crusader no longer counts toward the one-Judgement limit, but only increases Holy damage from the Paladin who applied it | Salvation leaving the Blessing slot; Improved Seal of the Crusader made baseline | Other Holy damage dealers lose the bonus |
| J1. Merge Light and Wisdom (fallback) | Judging Seal of Light or Wisdom applies one Judgement of Grace: attacks can heal the attacker for 61 and restore 59 mana | Weaponmaster merging four weapon talents | A single Paladin still has to choose |
| J4. Judgement Echo (optional) | When your next Judgement replaces your Judgement of Light, Wisdom or Justice, the replaced Judgement stays on the target as an Echo for 40 sec | Twist of Light's Seal Echo | Needs a 30-point Ret Paladin |
| J2. Two Judgements per Paladin (not chosen) | Each Paladin keeps two Judgements | None | More global cooldowns, against R6 |
| J3. Crusader moves into Ret (not chosen) | Holy Strike applies the Crusader debuff with Sacred Arbiter | Leader of the Pack | A raid without Ret loses the debuff |

| Two-Paladin raid | Beta | J1 | J4 | J5 |
| --- | --- | --- | --- | --- |
| Holy + Holy | Light + Wisdom | Grace | Light + Wisdom | Light + Wisdom |
| Holy + Ret | Two of three | Grace + Crusader | All three | All three |
| Holy + Protection | Two of three | Grace + Crusader | Two of three | All three |
| Protection + Ret | Two of three | Grace + Crusader | All three | All three |

## Tree balance review

Two checks: rows 1–2 must offer something to the other specs, and talents should match what other classes get.

| Tree | Rows 1–2 that tempt other specs | Who dips in | Cost |
| --- | --- | --- | --- |
| Holy | Improved Seals (+15% Seal damage), Divine Intellect, Infusion of Light, Reverence, Unyielding Faith | Ret and Protection (Seal damage, regen, faster Holy Light); casters (Intellect) | 5–8 points |
| Retribution | Deflection, Benediction, Improved Judgement, Holy Conduit, Conviction | Protection (parry, crit, mana costs); Holy (Benediction, Holy Conduit) | 5–10 points |
| Protection | Divine Strength, Precision (+3% hit), Guardian's Favor | Everyone (Strength, hit); Holy (Guardian's Favor in PvP) | 5–8 points |

**Parity.** Divine Intellect matches Shaman's Ancestral Knowledge (+10%), Deflection matches Warrior's, Conviction matches Warrior's Cruelty (+5%), Benediction matches Shaman's Convection (−10%), Anticipation matches Warrior's (+20 Defense), Divine Strength matches Druid's Heart of the Wild.

**Points per tree.** Beta: Holy 46, Protection 48, Ret 46. Proposed: Holy 44, Protection 47, Ret 46.

| # | Flag | Verdict |
| --- | --- | --- |
| F1 | Protection row 1 had flat armor (Toughness) | Done: P6 |
| F2 | Protection's hit dip costs 8 points, other trees' dips 5 | Keep: hit is the strongest dip stat |
| F3 | Ret row 4 held only 3 points | Done: R3 and R5 (6 points) |
| F4 | Holy row 6 held only Holy Power | Done: H4 and H6 |
| F5 | Pursuit of Justice (+15% speed at 10 Ret points) beats the boot enchant | Watch: lower to 10% if every Paladin dips for it |
| F6 | Sacred Duty: Divine Shield −60 sec at 10 Protection points, a PvP dip | Watch: cut to −30 sec if it becomes mandatory |
| F7 | Holy has no early threat-reduction talent | Leave: Salvation no longer uses a Blessing slot |
| F8 | Ret gets Strength and hit in one 8-point Protection dip | Watch |
| F9 | Improved Seal of Fury: about 40% of Protection's tanking mana, ignores the Seal's rank | Done: removed by P7 |
| F10 | A 7-point Ret dip cuts Protection's Consecration cost from about 103 to 68 mana/sec | Watch: may become a mandatory Protection dip |
| F11 | Holy is the main dip for both other trees (Seal damage, Infusion of Light, Reverence, Consecrated Ground) | Watch: Ret and Protection still offer parry, crit, mana costs, Strength and hit |
| F12 | Reckoning stores up to 4 attacks: a 0/26/25 two-hander bursts for about 2,960 in one Hammer of Justice stun | Watch: Holy Strike releases only 2 at a time. Beta's best case is about 3,220 |
| F13 | Iron Creed gives −10% damage taken to any class that uses Righteous Fury and has 25 Protection points | Watch in PvP; deliberate exception to the no-improved-buff rule |
| F14 | Fury's Reach: a 15-point Protection dip plus Swift Judgement gives a 20 yard Judgement | Watch: the range only works with Seal of Fury |
| F15 | Repentance at 15 Ret points and Templar's Bulwark (an absorb of 100% of health, three times Warrior's Last Stand) are strong for PvP dips | Watch |

## Open questions

- [ ] Forever changed the spell hit cap. Did the crushing blow rules change too? A test against a raid boss would confirm the stat targets.
- [ ] Do regen-while-casting effects add together (capped at 100%) in Forever, as in Classic?
- [ ] Would R1 (Conviction for spells) make a Holy dip into Ret too strong for healers?
- [ ] Should Ret have a group contribution like Druid's Leader of the Pack, or is Vindication's Attack Power debuff enough?

**Answered**

- [x] Vindication ranks: −67/136/204 target Attack Power and +1/2/3% yours.
- [x] Shield Specialization mana return: 4%.
- [x] Spell hit cap: 18%, with no unavoidable 1% miss.
- [x] Champion of the Light needs 28 Ret points for 3/3 (row 6).
- [x] Mana costs at level 60 (Forever tooltips): Seal of Fury rank 7 200 mana, Seal of Command 210, Consecration 565.

## Withdrawn ideas

| Idea | Why it was dropped |
| --- | --- |
| P1. One-Handed Weapon Specialization boosts all damage with a shield | The beta talent already boosts all damage except Consecration and Retribution Aura |
| H2. Unyielding Faith adds spell threat −10/20% | Depended on R2 moving Instrument of Law's threat cut into Holy |
| P3. Holy Shield +35% or +40% | With the Redoubt trigger, +30% already matches Warrior; +35% beats it, +40% also removes crits below 440 Defense |
| R2. Holy Strike crits reset Hammer of Wrath | Hammer of Wrath's 6-sec cooldown is shorter than Holy Strike's 10 sec and it only works below 20% health: about +1 damage per second |
| R4. Champion of the Light adds healing | At 60% of Intellect it would match deep Holy's healing and pull Holy Paladins into Ret. To revisit: healing at 10/20/30% would stay below deep Holy, now that H6 puts Healing Light out of reach |
| H4 as Sacred Ward (crit heals add a shield) | The same talent as Priest's Divine Aegis |
| H4 alternatives (smart heal splash, Aura boost, Cleanse, Lay on Hands) | Too modern, or utility instead of engaging healing |
| P6 as Steadfast Faith (stun duration) | Two crowd-control reduction talents; other classes have one |
| P6 as Toughness with Stamina | Replaced by Divine Strength from Holy |
| P6 as Hallowed Ground, or Shield Specialization in row 1 | Tank-only talents leave Holy and Ret 5 wasted points before Precision |
| Regen talent in each tree (Iron Creed, Righteous Fury, Seal of Fury) | Reverence in row 2 does the same with one talent; the Righteous Fury and Seal of Fury versions could be used by Holy |
| Holy Shield or Seal of Fury turns crushes into normal hits | Bypasses the attack table |
| Redoubt charges that each add a % of block | Block buffs with charges give one fixed bonus |
| Redoubt on every hit with a 6-sec cooldown | The Holy Shield trigger gives the same uptime with no new rule |
| Bring back Improved Blessing of Wisdom or Improved Lay on Hands | Forever removes improved-buff talents |
| Move Precision into Ret | The Protection dip for hit is intended |
| Swap Light's Vigil and Holy Power | Every tree ends on a 1-point capstone |
| Cap Divine Precision below 18% | Priest's Holy Precision is the same, and the spell hit cap is 18% |
| Raise Two-Handed Weapon Specialization to 10% | Paladin's 6% is already above Warrior's 3% |
| Fix Vindication's flat ranks | Forever already reworked it |
| Reckoning only works with a shield | It would end the Classic two-handed "Reckoning bomb". Releasing 2 charges per Holy Strike limits the burst instead |
| Swap Reckoning (row 6) and Iron Creed (row 5) | Makes Reckoning cost 25 points but does not stop a 0/30/21 hybrid. The release limit does the job without moving talents |
| Iron Creed without the Holy Strike threat bonus (option B) | Simpler wording, but loses 2.5-4.4 threat per second; kept as a small, separate effect |
| Aura Mastery or an improved aura talent for Protection | An improved-buff talent with low value (about −4% damage taken at 3 points). Fury's Reach covers the utility gap instead |
| A shield strike attack in row 4 (like Shield Slam or Primal Bite) | Not chosen for now; about +38 threat per second at a 10 sec cooldown. Can come back if Protection threat is too low |

## Sources

- [WoW Forever Talents – Paladin](https://wowforevertalents.com/paladin/)
- [WoW Forever Talents – Warrior](https://wowforevertalents.com/warrior/)
- [WoW Forever Talents – Druid](https://wowforevertalents.com/druid/)
- [WoW Forever Talents – Priest](https://wowforevertalents.com/priest/)
- [WoW Forever Talents – Shaman](https://wowforevertalents.com/shaman/)
- [WoW Forever Talents – Hunter](https://wowforevertalents.com/hunter/)
- [WoW Forever Talents – Mage](https://wowforevertalents.com/mage/)
- [WoW Forever Talents – Changes from Classic](https://wowforevertalents.com/talent-changes/)
- [WoW Forever Talents – Paladin abilities](https://wowforevertalents.com/abilities/paladin/)
- [ForeverChanges – Paladin talents](https://foreverchanges.pro/talents/paladin)
- [Wowhead – Shield Block tooltip (Forever)](https://nether.wowhead.com/forever/tooltip/spell/2565)
- [Wowhead – Hammer of Wrath tooltip (Forever)](https://nether.wowhead.com/forever/tooltip/spell/24239)
- [RankedBoost – WoW Forever block and patch notes](https://rankedboost.com/world-of-warcraft/forever/stats/block/)
- [Blizzard – WoW Forever Paladin deep dive](https://news.blizzard.com/en-us/article/24302099/world-of-warcraft-forever-class-deep-dives-paladin)
- [Warcraft Tavern – Mage and Shaman deep dive](https://www.warcrafttavern.com/forever/news/scrolls-totems-mage-shaman-deep-dive-for-wow-forever/)
- [Outputlag – Seal of Fury tooltip](https://outputlag.com/news/world-of-warcraft-forevers-paladins-tank-with-seal-of-fury-and-a-10-yard-judgement-taunt/)
- [Notebookcheck – Blizzard on class simplicity](https://notebookcheck.net/WoW-Forever-won-t-modernize-Classic-classes-but-Blizzard-admits-some-were-too-simple.1424285.0.html)
