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
| W3 | Retribution receives Strength and 3% hit with one 8-point Protection dip | Monitor |
| W4 | A 10-point Retribution dip (Deflection 5, Holy Conduit 2, Benediction 3) decreases the mana that Protection uses with Consecration from about 112 to 76 per sec | Monitor: all Protection players can take this dip |
| W5 | Holy is the main dip for the two other trees (Seal damage, Infusion of Light, Reverence, Consecrated Ground) | Monitor: Retribution and Protection still give parry, critical hit, mana costs, Strength and hit |
| W6 | Reckoning (C11): a 0/26/25 two-handed build bursts for about 3,020 in one Hammer of Justice stun | Monitor: this is below the best beta case (about 3,700). Swift Judgement gives about 18% of it |
| W7 | Iron Creed (C7) gives −10% damage taken to all specs with Righteous Fury and 25 Protection points | Monitor in PvP. This is the one exception to the rule on talents that improve a buff |
| W8 | Fury's Reach (C12): a 15-point Protection dip with Swift Judgement gives a 20 yard Judgement | Monitor: the range works only with Seal of Fury |
| W9 | Templar's Bulwark (an absorb of 100% of health, three times Last Stand) is a strong PvP dip | Monitor |
| W10 | Shield Specialization (C13) can make Consecration too cheap against groups that hit fast (up to 58–98 mana per sec, related to maximum mana) | Go back to 3 sec, or decrease the return from 4% to 3% |
| W11 | Protection threat in late raids depends on C14 and on the block value of Forever gear (see Threat, part 2) | Change the 200% of C14. Then Iron Creed +100% Holy Strike threat. A shield attack only as the last step |
| W12 | Infusion of Light (C3): a 7-point Holy dip gives a 1.5 sec Holy Light after each Holy Strike in PvP | Holy Strike gives only −0.25/0.5 sec. Or only Holy Strike critical hits trigger it, as in the beta |
| W13 | Light's Vigil: the Illumination text names it. Illumination can return mana for each critical heal of Light's Vigil (up to 5 for each cast). Then the Paladin is −2% to +3% against the Shaman in raids (see Analysis, Healing, part 6) | Keep Illumination at 50% |
| W14 | The design goal of Holy is the best single-target healer. With the proposals, the Paladin is about equal to the Druid on one tank (−3% to +5%), and 11–27% above the Shaman and the Priest (see Analysis, Healing, part 5) | Compare the healing on one tank in beta tests. A lead of more than 20% is too strong |
| W15 | Retribution with C16 is about equal to Fury Warrior at fresh level 60 (101%). It falls to about 82% of Fury in Naxxramas (see Analysis, Damage, part 6) | Compare Retribution with Fury at each gear tier, not only at fresh level 60. If Retribution is above the pure damage classes in raids, decrease the Sacred Arbiter bonus first (+20% → +10%) |
| W16 | Consecrated Ground (2 Holy points) with Consecration on cooldown gives Retribution about +23% on one target. The mana lasts about 70 sec | If Retribution uses it on bosses, apply the +10% only to Holy spells, as the tooltip says, not to Seals and Judgements |
| W17 | Holy Shock with Iron Creed (21/30/0): Righteous Fury stays active in PvP. The build then has −10% damage taken, Templar's Bulwark, Reckoning and Holy Shock (see Analysis, Builds, part 5) | Monitor in PvP with W7 and W9 |
| W18 | Lay on Hands with C22 on yourself gives up to +550 mana below 1,100 mana (beta: below 550). Paladins can use it for mana one time for each boss | If all Holy Paladins use it for mana, Lay on Hands does not restore mana when you are the target |

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
- [ ] Champion of the Light: the patch note of 16 October gives 10/20/30% of Intellect. The client data of 18 October gives 20/40/60%. What is the live value?
- [ ] How much block value do Forever shields and tank gear give at each tier? The 200% of C14 uses Classic values.
- [ ] What is the healing power coefficient of the Light's Vigil party heal? Do Purification and Healing Way (Shaman) add or multiply?
- [ ] Does Holy Strike use the weapon speed (3.6 sec) or the normalized speed (3.3 sec) for the Seal of Command chance (C16)?
- [ ] Does MythicSim include Judgement of the Crusader in its raid debuffs? It changes the Retribution comparison by about 9% (see Analysis, Damage, part 7).
- [ ] What is the Slam cooldown in Forever? The Arms check in Analysis, Damage, uses one Slam each 3 sec at most.
- [ ] Does Righteous Fury increase the threat of heals in Forever? The text says "Holy attacks". If yes, a tank can use Flash of Light or Holy Light for threat (see Analysis, Builds, part 6).
- [ ] C8: Divine Strength gives almost no threat to a tank, and the tank builds skip it (see Analysis, Builds, part 3). Keep C8 as a talent for Retribution and change its reason? Or change Divine Strength so that tanks also use it?
- [ ] C22: when you cast Lay on Hands on yourself, does the drain occur before the 550 mana? If not, Lay on Hands gives you no mana.
- [ ] Light's Vigil: the Illumination text names it. Does Illumination return mana one time for each cast, or one time for each critical heal (up to 5)? With Illumination at 50%, the effect is small (W13).
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
