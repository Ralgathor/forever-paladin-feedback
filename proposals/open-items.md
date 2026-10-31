# Open items

This tab gives the problems to report, the risks to check in tests and the open questions.

## Problems to report to Blizzard

- **Judgement of Fury: the damage hits before the taunt.** The taunt must apply first. Then the Paladin has a small threat lead, not only equal threat.
- **Holy Strike triggers only some Seals.** It triggers Seal of Light, Justice and Wisdom. It does not trigger Seal of Fury, Righteousness or Command. Holy Strike Seal trigger (C1) makes this consistent for all specs.

## Watch list

These are risks to check in tests. None of them needs a change now. A removed number stays reserved.

| # | Risk | Action if it occurs |
| --- | --- | --- |
| W1 | Pursuit of Justice (+15% speed at 10 Retribution points) is better than the boot enchant | Decrease it to 10% if all Paladins take it |
| W2 | Sacred Duty gives Divine Shield −60 sec and Forbearance −10 sec at 5 Protection points (beta of 30 October: row 2). This is a PvP dip | Decrease it to −30 sec if all players take it |
| W5 | Holy is the main dip for Retribution (Seal damage, Holy Conduit). Tanks dip Retribution for Benediction, Conviction and Sanctified Judgement (row 2) | Monitor: each tree still gives the other specs a reason for a dip |
| W6 | Reckoning: with Shieldsworn, Holy Strike comes each 6 sec. A Protection or hybrid build can store 4 extra attacks and use them in one Hammer of Justice stun | Model the PvP burst again on the beta of 30 October (see PvP burst check) |
| W7 | Iron Creed with Shieldsworn is always active: −6%. With Improved Righteous Fury 3/3, a tank has about −14.5% damage taken. Defensive Stance (Warrior) gives −10% | Monitor in raids and PvP. If it is too strong, decrease Improved Righteous Fury |
| W9 | Templar's Bulwark (an absorb of 100% of health, three times Last Stand) is in row 3 (10 points). This is a strong PvP dip | Monitor |
| W13 | Light's Vigil: the Illumination text names it. Illumination can return mana for each critical heal of Light's Vigil (up to 5 for each cast) | Keep Illumination at 50% |
| W14 | The design goal of Holy is the best single-target healer. In the beta of 30 October, the Paladin is 3–12% above the Druid on one tank (see Beta test results). In raids, it is 18–26% below the Druid. This is accepted: raid healing is not the goal of Holy | Compare the healing on one tank in beta tests. A lead of more than 20% is too strong |
| W15 | Retribution in the beta of 30 October has about 96% of the pure average with pre-raid gear, and about 88–89% in Naxxramas (estimate). The hybrid target is 95%. Holy Strike Seal trigger (C1) and Burning Zeal (C-R4) add damage | Compare Retribution with the pure average at each gear tier. If Retribution is above the pure average at the raid release, decrease the Sacred Arbiter bonus first (+20% → +10%) |
| W16 | Consecration on cooldown gives Retribution more damage than its normal rotation. Consecrated Ground is in Holy row 5 | Mana is the balance. The 95% target is for the normal rotation, without Consecration |
| W17 | Holy Shock with Iron Creed: Righteous Fury stays active in PvP. With 25 Protection points, the build has Iron Creed, Templar's Bulwark, Holy Shield and Reckoning | Monitor in PvP with W7 and W9 |
| W18 | Lay on Hands with Devoted Sacrifice (C-P11) on yourself gives up to +550 mana below 1,100 mana (beta: below 550). Paladins can use it for mana one time for each boss | If all Holy Paladins use it for mana, Lay on Hands does not restore mana when you are the target |
| W20 | Hand of Sacrifice (C4) with Divine Shield: the ally takes no damage and the Paladin takes no damage. In PvP, a Paladin can protect two allies for 825 each in one Divine Shield: 1,650 damage | Monitor in PvP. If it is too strong, Divine Shield removes Hand of Sacrifice |
| W22 | Divine Precision (beta of 30 October) is in Holy row 4 with no requirement: +8% spell hit with 15 Holy points | Monitor: Exorcism, Holy Wrath and Consecration use it |
| W24 | Holy Shield is in Protection row 5. Holy and Retribution can take it with 20 Protection points | Monitor hybrid builds in PvP |
| W25 | Shieldsworn: each Holy Strike lets the Paladin block spells for 6 sec. With a Holy Strike each 6 sec, the effect is always active | Monitor in PvP against casters |
| W26 | Swift Judgement is now a second Judgement with a 1 min cooldown, at 15 Protection points. Two Judgements of Command on a stunned target give a large burst | Monitor in PvP with W6 |
| W27 | Oath of Light gives a flat value (+400, +115, +229). Forever talents give a %. The value decreases with gear | Decision of 31 October: Oath of Light keeps its beta version. Compare its value with gear in beta tests |
| W28 | The tank of the beta of 30 October has 101–118% of the Warrior threat, and 120–142% with Consecration (see Beta test results) | Compare tank threat in raids. If it is too high, decrease the Righteous Fury bonus (+33%) first |
| W29 | Unsealed Wrath has no Seal cost decrease (Twist of Light had −20%). Retribution mana can be lower in long fights | Model the Retribution mana again |

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
- [ ] Holy Strike Seal trigger (C1): what sets the Seal of Command chance? Is it the weapon speed (3.6 sec) or the normalized speed (3.3 sec)?
- [ ] Does MythicSim include Judgement of the Crusader in its raid debuffs? It changes the Retribution comparison by about 10% (see Analysis, Damage, part 7).
- [ ] What is the Slam cooldown in Forever? The Arms check in Analysis, Damage, uses one Slam each 3 sec at most.
- [ ] Does Righteous Fury increase the threat of heals in Forever? The text says "Holy attacks". If yes, a tank can use Flash of Light or Holy Light for threat (see Analysis, Builds, part 6).
- [ ] Hand of Sacrifice (C4): does damage that moves to a Paladin in Divine Shield have no effect in Forever, as in Classic? Does it stop a Polymorph on the Paladin?
- [ ] Devoted Sacrifice (C-P11): when you cast Lay on Hands on yourself, does the drain occur before the 550 mana? If not, Lay on Hands gives you no mana.
- [ ] Light's Vigil: the Illumination text names it. Does Illumination return mana one time for each cast, or one time for each critical heal (up to 5)? With Illumination at 50%, it gives +13% to +19% raid healing against the Shaman (W13).
- [ ] What is the Spirit regeneration formula in Forever? Does Intellect change it? The DoubleZug tests agree with neither the Classic nor the TBC formula.
- [ ] Can heals start Omen of Clarity for a Druid? Can the Druid use it for Wild Growth? (Druid testers)
- [ ] How many targets does Prayer of Mending heal in a raid fight? The Priest result depends on it (Priest testers)
- [ ] Holy Power 5/5 (beta of 30 October): does a critical heal heal for 225% (×1.5 on the full critical heal, the wowsims value) or for 175% (+50% of the bonus, the Classic rule of Ice Shards and Ruin)? At 225%, Holy is 3–10% above the Druid on one tank. At 175%, it is 7% below to 1% above. **Test:** take Holy Power 5/5. Cast Divine Favor, then Holy Light on a target with no Oath of Light. Compare the heal with the average of the tooltip. 2.25 times the average is 225%. 1.75 times the average is 175%.
- [ ] Oath of Light gives "up to" +400 to Holy Light. Do the low ranks of Holy Light receive less?
- [ ] Shieldsworn: does a Holy Strike that misses still trigger Holy Shield and Shield Specialization?
- [ ] Unsealed Wrath: does Holy Strike store a Seal copy and consume the stored copies?
- [ ] Holy Shield rank 4 (221 damage) has no cost and no level in the game files. What rank does a level 60 Paladin have?

**Answered**

- [x] Does Judgement of Fury remove your own Judgement of the Crusader? No (player test).
- [x] Vindication ranks: −67/136/204 Attack Power on the target and +1/2/3% on you.
- [x] Shield Specialization mana return: 4%.
- [x] Champion of the Light (beta of 30 October): 5 ranks, 12–60% of Intellect.
- [x] Spell hit cap: 18%, with no fixed 1% miss.
- [x] Champion of the Light needs 28 Retribution points for 3/3 (row 6).
- [x] Level 60 costs (Forever spellbook): Seal of Fury rank 7: 200 mana. Seal of Command: 210. Consecration: 565. Holy Shield rank 3: 240.
- [x] Light's Vigil has 3 ranks: 730, 1,000 and 1,340 mana.
- [x] Can heals over time be critical heals in Forever? Yes, each tick ([Warcraft Tavern](https://www.warcrafttavern.com/forever/guides/restoration-druid/)). Analysis, Healing uses this rule.
- [x] Does Swiftmend remove the Rejuvenation or Regrowth that it uses? No (player test).
- [x] Paladin critical chance from Intellect: 59.9 Intellect for 1% (0.0167% for each point). Base spell critical chance 3.5%, base melee critical chance 0.7% (game files, wowsims Forever). Not 54 Intellect and 3.3%.
