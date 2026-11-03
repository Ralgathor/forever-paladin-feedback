# Open items

This tab gives the problems to report, the risks to check in tests and the open questions.

## Problems to report to Blizzard

- **Judgement of Fury: the damage hits before the taunt.** The taunt must apply first. Then the Paladin has a small threat lead, not only equal threat.
- **Holy Strike triggers only some Seals.** It triggers Seal of Light, Justice and Wisdom. It does not trigger Seal of Fury, Righteousness or Command. Blizzard can confirm if this is a bug or the design.

## Watch list

These are risks to check in tests. None of them needs a change now. A removed number stays reserved.

| # | Risk | Action if it occurs |
| --- | --- | --- |
| W1 | Pursuit of Justice (+15% speed at 10 Retribution points) is better than the boot enchant | Decrease it to 10% if all Paladins take it |
| W2 | Sacred Duty gives Divine Shield −60 sec and Forbearance −10 sec at 5 Protection points (row 2 in the live trees). This is a PvP dip | Decrease it to −30 sec if all players take it |
| W5 | Holy is the main dip for Retribution (Seal damage, Holy Conduit). Tanks dip Retribution for Benediction, Conviction and Sanctified Judgement (row 2) | Monitor: each tree still gives the other specs a reason for a dip |
| W6 | Reckoning: with Shieldsworn, Holy Strike comes each 6 sec. A Protection or hybrid build can store 4 extra attacks and use them in one Hammer of Justice stun. Blocks give a maximum of 1 charge each 1.5 sec | Modeled on the live version (see PvP burst check): the proposals do not change the Reckoning burst. Light's Vigil (C-H7) adds a Holy Shock burst (W30). Monitor in the live version |
| W7 | Iron Creed with Shieldsworn is always active: −6%. With Improved Righteous Fury 3/3, a tank has about −14.5% damage taken. Defensive Stance (Warrior) gives −10% | Monitor in raids and PvP. If it is too strong, decrease Improved Righteous Fury |
| W9 | Templar's Bulwark (an absorb of 100% of health, three times Last Stand) is in row 3 (10 points). This is a strong PvP dip. It is a Magic effect: a dispel removes it | Monitor |
| W13 | Light's Vigil: the Illumination text names it. Illumination can return mana for each critical heal of Light's Vigil (up to 5 for each cast) | Keep Illumination at 50% |
| W14 | The design goal of Holy is the best single-target healer. The development notes of 2 November 2026 change the Druid. With a 175% critical heal (main hypothesis since 3 November), the live Paladin is then 8–15% below the Druid on one tank (see Analysis, Healing). With Reverence 50% (C-H1), it is 3–7% below. At 225%, the Paladin is 5% below to 3% above the Druid, and 3–9% above with Reverence 50%. In raids, with Light's Vigil (C-H7) and Reverence 50%, the Paladin is 3–14% below the Druid | At 175%, the design goal is not reached: the Druid is the best healer on one target. This is an open design question. Compare the healing on one tank in live tests. A lead of more than 20% is too strong |
| W15 | With the game files of client 1.60.1.70707, Retribution has about 112% of the pure average at fresh level 60. In Naxxramas, it has about 107%. The development notes of 2 November 2026 give Two-Handed Weapon Specialization +2/4/6% Holy damage and Vengeance 5 stacks: +8.3% in wowsims (about 121%). The same notes increase the damage of most other classes. These are not in wowsims yet. The values come from wowsims of 1 November with the same item pool, enchants and consumables for each spec, and the model. The hybrid target is 95% | Compare Retribution with the pure average at each gear tier. If Retribution is above the pure average at the raid release, decrease the Sacred Arbiter bonus first (+20% → +10%). This change alone does not bring Retribution to 95%: −0.7% damage in wowsims |
| W16 | Consecration on cooldown gives Retribution more damage than its normal rotation. Consecrated Ground is in Holy row 5 | Mana is the balance. The 95% target is for the normal rotation, without Consecration |
| W17 | Holy Shock with Iron Creed: Righteous Fury stays active in PvP. With 25 Protection points, the build has Iron Creed, Templar's Bulwark, Holy Shield and Reckoning | Monitor in PvP with W7 and W9 |
| W18 | Lay on Hands with Devoted Sacrifice (C-P11) on yourself gives up to +550 mana below 1,100 mana (live: below 550). Paladins can use it for mana one time for each boss | If all Holy Paladins use it for mana, Lay on Hands does not restore mana when you are the target |
| W20 | Hand of Sacrifice (C4) with Divine Shield: the ally takes no damage and the Paladin takes no damage. In PvP, a Paladin can protect two allies for 825 each in one Divine Shield: 1,650 damage | Monitor in PvP. If it is too strong, Divine Shield removes Hand of Sacrifice |
| W22 | Divine Precision (live talent) is in Holy row 4 with no requirement: +8% spell hit with 15 Holy points | Monitor: Exorcism, Holy Wrath and Consecration use it |
| W24 | Holy Shield is in Protection row 5. Holy and Retribution can take it with 20 Protection points | Monitor hybrid builds in PvP |
| W25 | Shieldsworn: each Holy Strike lets the Paladin block spells for 6 sec. With a Holy Strike each 6 sec, the effect is always active | Monitor in PvP against casters |
| W26 | Swift Judgement is now a second Judgement with a 1 min cooldown, at 15 Protection points. Two Judgements of Command on a stunned target give a large burst | Monitor in PvP with W6 |
| W27 | Oath of Light gives a flat value (+400, +115, +229). Forever talents give a %. The value decreases with gear | Decision of 31 October: Oath of Light does not change. Compare its value with gear in live tests |
| W28 | The development notes of 2 November 2026 give Defensive Stance +80% threat, Defiance 20% and Bear Form +115%. The Paladin has no change. The live tank then has 70% of the Warrior threat with the same gear, and 71–82% from fresh level 60 to Naxxramas (83–98% with Consecration). Before the notes: 101–118% (see Analysis, Threat) | First, confirm the new Warrior and Druid values on the live realms. If they are correct, report the gap to Blizzard. Righteous Fury +33% → about +90% to all threat gives the Warrior threat again |
| W29 | Unsealed Wrath has no Seal cost decrease (Twist of Light had −20%). With the wowsims rotation (plan 1 + 3), the mana is empty after 3 min 43 sec at fresh level 60 (model). In wowsims of 1 November, the mana lasts 5 min with lean and full buffs, because the consumables include Major Mana Potion. In a 5 min fight at fresh level 60, the mana costs 2.5% damage (see Retribution, Mana with Unsealed Wrath) | Its spell data has a Seal cost effect at 0%. A −20% value gives 0% (2 min) to +2.6% (5 min) damage in the model, and 0% in wowsims. Watch the next patch values |
| W30 | Light's Vigil (C-H7) also removes the Holy Shock cooldown on enemies. With 3 stacks, three Holy Shocks hit in one Hammer of Justice stun (1,640–2,160 damage), and four as the stun ends (2,180–2,880). Live: one Holy Shock (550–720). The burst is ready each 18 sec, with no setup, at 20 yd (see Analysis, PvP burst check, part 6) | Decision of 3 November: keep the effect on enemies. Monitor in PvP with W6. If it is too strong, the next Holy Shock incurs no cooldown only when cast on allies. This change gives no healing loss |

## Open questions

- [ ] Forever changed the spell hit cap. Did the crushing blow rules also change? A test against a raid boss can confirm the stat targets.
- [ ] Do the effects that keep regeneration during casts add together (maximum 100%) in Forever, as in Classic?
- [ ] Must Retribution have a group buff, as Leader of the Pack (Druid)? Or is the Attack Power debuff of Vindication sufficient?
- [ ] Does the Holy Shield damage increase with spell power? By how much for each block?
- [ ] Does Shield Slam have a threat multiplier, as Revenge (×2.25) has? (Warrior testers)
- [ ] Do Heroic Strike and Maul hits give rage? (Warrior and Druid testers)
- [ ] Do Maul and Swipe have the ×1.75 threat multiplier in Forever? The model uses ×1.75. The wowsims Forever data gives threat for the damage only. Without the multipliers of Maul and Primal Bite, the Druid loses about one third of its threat at the gear of Threat, part 1. It drops from 600 to 384 TPS. (Druid testers)
- [ ] Faerie Fire in Bear Form: the model uses 120 threat (2 × level) for each cast. The wowsims Forever data gives no threat. What is the value? (Druid testers)
- [ ] Primal Bite: the tooltip gives "a high amount of threat", with no number. The model uses ×3. The wowsims Forever data gives threat for the damage only. What is the multiplier? (Druid testers)
- [ ] Judgement of Fury: the game files give a third effect of 1,691 + 18% of spell power. Is this bonus threat, the taunt or a server value? If it is bonus threat, it adds about 200 TPS to the Paladin. The model does not use it.
- [ ] How much block value do Forever shields and tank gear give at each tier? Pre-raid gear gives 108 (Wowhead Forever values). The raid values of the model (140, 180 and 230) are estimates. Forever has no raid shields yet.
- [ ] What is the healing power coefficient of the Light's Vigil party heal? Do Purification and Healing Way (Shaman) add or multiply?
- [ ] Does Righteous Fury increase the threat of heals in Forever? The text says "Holy attacks". If yes, a tank can use Flash of Light or Holy Light for threat (see Analysis, Builds).
- [ ] Hand of Sacrifice (C4): does damage that moves to a Paladin in Divine Shield have no effect in Forever, as in Classic? Does it stop a Polymorph on the Paladin?
- [ ] Devoted Sacrifice (C-P11): when you cast Lay on Hands on yourself, does the drain occur before the 550 mana? If not, Lay on Hands gives you no mana.
- [ ] Light's Vigil: the Illumination text names it. Does Illumination return mana one time for each cast, or one time for each critical heal (up to 5)? With Illumination at 50%, it gives +13% to +19% raid healing against the Shaman (W13).
- [ ] What is the Spirit regeneration formula in Forever? Does Intellect change it? The DoubleZug tests agree with neither the Classic nor the TBC formula.
- [ ] Can heals start Omen of Clarity for a Druid? Can the Druid use it for Wild Growth? (Druid testers)
- [ ] How many targets does Prayer of Mending heal in a raid fight? The Priest result depends on it (Priest testers)
- [ ] Holy Power 5/5 (live talent): does a critical heal heal for 175%, 200% or 225%? The analysis uses 175%: +50% of the bonus, the rule of Ruin and Elemental Fury (decision of 3 November, the general view of the players). 225% is ×1.5 on the full critical heal (the main case on 2 November, the wowsims value). Holy Power is the only spell in the game files with its aura (A_MOD_CRITICAL_HEALING_AMOUNT). 200% is +50 points on the 150% critical heal (the main case from 1 to 2 November). With the Druid of the notes of 2 November, Holy is 8–15% below the Druid on one tank at 175%, 3–10% below at 200%, and 5% below to 3% above at 225%. The Light's Vigil (C-H7) party heal of 60% is for 175%. At 225%, decrease it to 35%. The development notes of 2 November 2026 say: "Increases the critical strike healing bonus of your Holy Spells by 10/20/30/40/50%". This text is nearer to 175% (the rule of Ruin). **Test:** take Holy Power 5/5. Cast Divine Favor, then Holy Light on a target with no Oath of Light. Compare the heal with the average of the tooltip. 2 times the average is 200%. 2.25 times the average is 225%. 1.75 times the average is 175%.
- [ ] Oath of Light gives "up to" +400 to Holy Light. Do the low ranks of Holy Light receive less?
- [ ] Shieldsworn: does a Holy Strike that misses still trigger Holy Shield and Shield Specialization?
- [ ] Unsealed Wrath: does Holy Strike store a Seal copy and consume the stored copies? In the wowsims spell data, Unsealed Wrath triggers only on auto attacks (proc flag 0x4). The model uses this. **Test:** turn off auto attack. Cast Seal of Righteousness, then Holy Strike. Cast Seal of Command, turn on auto attack and hit one time. A Seal of Righteousness hit shows that Holy Strike stored a copy.
- [ ] Holy Shield rank 4 (221 damage) has no cost and no level in the game files. What rank does a level 60 Paladin have?

**Answered**

- [x] Does Judgement of Fury remove your own Judgement of the Crusader? No (player test).
- [x] What is the Slam cooldown in Forever? 15 sec, and 10 sec with Improved Slam 2/2 (development notes of 2 November 2026). The Arms check in Analysis, Damage, uses one Slam each 3 sec at most. It must run again.
- [x] Vindication ranks: −67/136/204 Attack Power on the target and +1/2/3% on you.
- [x] Shield Specialization mana return: 4%.
- [x] Champion of the Light (live talent): 5 ranks, 12–60% of Intellect.
- [x] Spell hit cap: 18%, with no fixed 1% miss.
- [x] Champion of the Light needs 28 Retribution points for 3/3 (row 6).
- [x] Level 60 costs (Forever spellbook): Seal of Fury rank 7: 200 mana. Seal of Command: 210. Consecration: 565. Holy Shield rank 3: 240.
- [x] Light's Vigil has 3 ranks: 730, 1,000 and 1,340 mana.
- [x] Can heals over time be critical heals in Forever? Yes, each tick ([Warcraft Tavern](https://www.warcrafttavern.com/forever/guides/restoration-druid/)). Analysis, Healing uses this rule.
- [x] Does Swiftmend remove the Rejuvenation or Regrowth that it uses? No (player test).
- [x] Paladin critical chance from Intellect: 59.9 Intellect for 1% (0.0167% for each point). Base spell critical chance 3.5%, base melee critical chance 0.7% (game files, wowsims Forever). Not 54 Intellect and 3.3%.
