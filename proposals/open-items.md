# Open items

This tab gives the problems to report, the risks to check in tests and the open questions.

## Problems to report to Blizzard

- **Judgement of Fury: the damage hits before the taunt.** The taunt must apply first. Then the Paladin has a small threat lead, not only equal threat.
- **Holy Strike triggers only some Seals.** It triggers Seal of Light, Justice and Wisdom. It does not trigger Seal of Fury, Righteousness or Command. C16 makes this consistent for all specs.
- **Sanctified Judgement with Benediction** returns more than 60% of the base cost of the Seal. This is possibly a bug.

## Watch list

These are risks to check in tests. None of them needs a change now.

| # | Risk | Action if it occurs |
| --- | --- | --- |
| W1 | Pursuit of Justice (+15% speed at 10 Retribution points) is better than the boot enchant | Decrease it to 10% if all Paladins take it |
| W2 | Sacred Duty gives Divine Shield −60 sec at 10 Protection points. This is a PvP dip | Decrease it to −30 sec if all players take it |
| W3 | Retribution receives 3% hit, Blessing of Protection each 3 min and Holy Conduit with one 7-point Protection dip (C8) | Monitor |
| W4 | Holy Conduit is in Protection row 2 (C8). With Consecration on cooldown, a tank uses about 84 mana per sec with no dip (beta: 112). Benediction from a Retribution dip decreases it to about 76 | Monitor: the Retribution dip now saves only about 8 mana per sec |
| W5 | Holy is the main dip for the two other trees (Seal damage, Infusion of Light, Reverence, Consecrated Ground) | Monitor: Retribution and Protection still give parry, critical hit, mana costs, hit and saves |
| W6 | Reckoning (C11): a 0/26/25 two-handed build bursts for about 3,020 in one Hammer of Justice stun | Monitor: this is below the best beta case (about 3,700). Swift Judgement gives about 18% of it |
| W7 | Iron Creed (C7) gives −10% damage taken to all specs with Righteous Fury and 25 Protection points | Monitor in PvP. This is the one exception to the rule on talents that improve a buff |
| W8 | Fury's Reach (C12): a 15-point Protection dip with Swift Judgement gives a 20 yard Judgement | Monitor: the range works only with Seal of Fury |
| W9 | Templar's Bulwark (an absorb of 100% of health, three times Last Stand) is a strong PvP dip | Monitor |
| W10 | Shield Specialization (C13) can make Consecration too cheap against groups that hit fast (up to 58–98 mana per sec, related to maximum mana) | Go back to 3 sec, or decrease the return from 4% to 3% |
| W11 | Protection threat in late raids depends on C14 and on the block value of Forever gear (see Threat, part 2) | Change the 200% of C14. Then Iron Creed +100% Holy Strike threat. A shield attack only as the last step |
| W12 | Infusion of Light (C3): a 7-point Holy dip gives a 1.5 sec Holy Light after each Holy Strike in PvP | Holy Strike gives only −0.25/0.5 sec. Or only Holy Strike critical hits trigger it, as in the beta |
| W13 | Light's Vigil: the Illumination text names it. Illumination can return mana for each critical heal of Light's Vigil (up to 5 for each cast). Then the Paladin is 13–19% above the Shaman in raids (see Analysis, Healing, part 6) | Keep Illumination at 50% |
| W14 | The design goal of Holy is the best single-target healer. With the proposals, the Paladin is first on one tank: 1–9% above the Druid, and 14–32% above the Shaman and the Priest (see Analysis, Healing, part 5) | Compare the healing on one tank in beta tests. A lead of more than 20% is too strong |
| W15 | Retribution with C16 is 103% of the pure average at fresh level 60 (101% of Fury). In Naxxramas, it is about 95% of the pure average and 92% of Fury. The hybrid target is 95% of the pure average (see Analysis, Damage, part 6) | Compare Retribution with the pure average at each gear tier, not only with Fury. If Retribution is above the pure average at the raid release, decrease the Sacred Arbiter bonus first (+20% → +10%). Ask for spell damage on Paladin plate items at each tier |
| W16 | Consecration on cooldown on one boss gives Retribution 108–118% of the pure average (normal rotation: 95–103%). Consecration gives 67% of the increase, Consecrated Ground (2 Holy points) 33%. Seals and Judgements do Holy damage, thus the +10% applies to them, as the tooltip says. With Holy Conduit, the mana is zero after 1 min 23 sec at fresh level 60 and 1 min 58 sec in Naxxramas (see Analysis, Damage, part 8) | Mana is the balance. The 95% target is for the normal rotation, without Consecration. Do not change Consecrated Ground. If raids use Consecration on all bosses, compare the 3 min average with the pure average |
| W17 | Holy Shock with Iron Creed (21/30/0): Righteous Fury stays active in PvP. The build then has −10% damage taken, Templar's Bulwark, Reckoning and Holy Shock (see Analysis, Builds, part 5) | Monitor in PvP with W7 and W9 |
| W18 | Lay on Hands with C22 on yourself gives up to +550 mana below 1,100 mana (beta: below 550). Paladins can use it for mana one time for each boss | If all Holy Paladins use it for mana, Lay on Hands does not restore mana when you are the target |
| W19 | Guardian's Favor is in Protection row 1 (C8). All specs take Blessing of Protection each 3 min and the C22 Lay on Hands for 2 points (see W18). No other class has a save talent in row 1 | Monitor in PvP. If all PvP builds take it, move it back to row 2 |

## Open questions

- [ ] Forever changed the spell hit cap. Did the crushing blow rules also change? A test against a raid boss can confirm the stat targets.
- [ ] Do the effects that keep regeneration while casting add together (maximum 100%) in Forever, as in Classic?
- [ ] Does C15 (Conviction for spells) make a Holy dip into Retribution too strong for healers?
- [ ] Must Retribution have a group buff, as Leader of the Pack (Druid)? Or is the Attack Power debuff of Vindication sufficient?
- [ ] Does Vindication stack with Demoralizing Shout (Warrior) and Demoralizing Roar (Druid) in Forever? If not, a tank with Vindication adds nothing in a raid with a Warrior or a Druid (C8).
- [ ] Is a 20 yard pull worth 3 Protection points (C12)?
- [ ] Does Judgement use the global cooldown in Forever? The C17 table assumes that it does.
- [ ] Does the Holy Shield damage increase with spell power? By how much for each block?
- [ ] Does Shield Slam have a threat multiplier, as Revenge (×2.25) has? (Warrior testers)
- [ ] Do Heroic Strike and Maul hits give rage? (Warrior and Druid testers)
- [ ] Do Maul and Swipe have the ×1.75 threat multiplier in Forever? Our model uses ×1.75. The wowsims Forever data gives threat for the damage only. Without the multipliers of Maul, Swipe and Primal Bite, the Druid loses about half of its threat at the gear of Threat, part 1. (Druid testers)
- [ ] Primal Bite: the tooltip gives "a high amount of threat", with no number. Our model uses ×3. The wowsims Forever data gives threat for the damage only. What is the multiplier? (Druid testers)
- [ ] Judgement of Fury: the game files give a third effect of 1,691 + 18% of spell power. Is this bonus threat, the taunt or a server value? If it is bonus threat, it adds about 200 TPS to the Paladin. The model does not use it.
- [ ] Champion of the Light: the patch note of 16 October gives 10/20/30% of Intellect. The client data of 18 October gives 20/40/60%. What is the live value?
- [ ] How much block value do Forever shields and tank gear give at each tier? The 200% of C14 uses Classic values.
- [ ] What is the healing power coefficient of the Light's Vigil party heal? Do Purification and Healing Way (Shaman) add or multiply?
- [ ] Does Holy Strike use the weapon speed (3.6 sec) or the normalized speed (3.3 sec) for the Seal of Command chance (C16)?
- [ ] Does MythicSim include Judgement of the Crusader in its raid debuffs? It changes the Retribution comparison by about 10% (see Analysis, Damage, part 7).
- [ ] What is the Slam cooldown in Forever? The Arms check in Analysis, Damage, uses one Slam each 3 sec at most.
- [ ] Does Righteous Fury increase the threat of heals in Forever? The text says "Holy attacks". If yes, a tank can use Flash of Light or Holy Light for threat (see Analysis, Builds, part 6).
- [ ] C22: when you cast Lay on Hands on yourself, does the drain occur before the 550 mana? If not, Lay on Hands gives you no mana.
- [ ] Light's Vigil: the Illumination text names it. Does Illumination return mana one time for each cast, or one time for each critical heal (up to 5)? With Illumination at 50%, it gives +13% to +19% raid healing against the Shaman (W13).
- [ ] Does the Light's Vigil heal use the +15% critical chance of Holy Power for Holy Shock? Does Healing Light increase it? Both make Light's Vigil stronger (see Analysis, Healing, part 6).
- [ ] What is the Spirit regeneration formula in Forever? Does Intellect change it? The DoubleZug tests agree with neither the Classic nor the TBC formula.
- [ ] Can heals start Omen of Clarity for a Druid? Can the Druid use it for Wild Growth? (Druid testers)
- [ ] How many targets does Prayer of Mending heal in a raid fight? The Priest result depends on it (Priest testers)

**Answered**

- [x] Does Judgement of Fury remove your own Judgement of the Crusader? No (player test).
- [x] Vindication ranks: −67/136/204 Attack Power on the target and +1/2/3% on you.
- [x] Shield Specialization mana return: 4%.
- [x] Spell hit cap: 18%, with no fixed 1% miss.
- [x] Champion of the Light needs 28 Retribution points for 3/3 (row 6).
- [x] Level 60 costs (Forever spellbook): Seal of Fury rank 7: 200 mana. Seal of Command: 210. Consecration: 565. Holy Shield rank 3: 240.
- [x] Light's Vigil has 3 ranks: 730, 1,000 and 1,340 mana.
- [x] Can heals over time be critical heals in Forever? Yes, each tick ([Warcraft Tavern](https://www.warcrafttavern.com/forever/guides/restoration-druid/)). Analysis, Healing uses this rule.
- [x] Does Swiftmend remove the Rejuvenation or Regrowth that it uses? No (player test).
- [x] Paladin critical chance from Intellect: 59.9 Intellect for 1% (0.0167% for each point). Base spell critical chance 3.5%, base melee critical chance 0.7% (game files, wowsims Forever). Not 54 Intellect and 3.3%.
