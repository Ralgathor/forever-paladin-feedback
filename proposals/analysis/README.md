# Analysis

This part gives the calculations behind the proposals. Each sub-tab answers one question. Each sub-tab starts with a short answer. The details and the method come after it.

## Sub-tabs

| Sub-tab | Question |
| --- | --- |
| [Crushing blows](crushing-blows.md) | Why does the Paladin tank take crushing blows, and how does Redoubt (C-P1) stop them? |
| [Threat](threat.md) | Does the Paladin tank hold a boss and a group as well as the Warrior and the Druid? |
| [PvP burst check](pvp-burst-check.md) | Do the proposals make the PvP burst too high? |
| [Mana](mana.md) | How long does the mana of a Protection or Retribution Paladin last? |
| [Healing](healing.md) | How well does the Holy Paladin heal against the Priest, the Druid and the Shaman? |
| [Damage](damage.md) | How much damage does Retribution do against the other damage classes? |
| [Builds](builds.md) | What are the main builds of each spec, with the proposals? |
| [Tree balance](tree-balance.md) | Do the Paladin trees have the same number of strong talents as the other classes? |

## Trees

- **Live.** The live trees, with no proposal.
- **Proposed.** The live trees, with the kept proposals (calculator version 6).
- **Withdrawn proposals.** Some tabs also give values for proposals that were withdrawn. The Withdrawn ideas tab gives the reasons.

## Words in these tabs

| Word | Meaning |
| --- | --- |
| wowsims | wowsims Forever, a combat simulator for WoW Forever. It plays the fight many times with the game rules and gives the average |
| Model | A calculation in this repository (Python). It is simpler than wowsims. It is not a combat log |
| Iterations | The number of times wowsims plays the fight. 3,000 iterations give an average with an error of about 1 DPS |
| DPS | Damage each sec |
| TPS | Threat each sec. The tank with more threat keeps the enemy |
| Healing each sec | Healing each sec after overhealing. Overhealing is the part of a heal that the target does not need |
| TMI | A wowsims value for the danger of large damage spikes on a tank, in a 6 sec window. A lower TMI is better |
| Attack table | The list of results of a boss attack: miss, dodge, parry, block, critical hit, crushing blow and hit. The results share 100% |
| Crushing blow | A boss hit for 150% damage. It is in the attack table only when miss, dodge, parry and block are less than 100% |
| Fresh 60 | A new level 60 character with no buffs, no debuffs and no consumables |
| Raid | Full raid buffs and debuffs, with consumables |
| MP5 | Mana each 5 sec, from gear |
| Flag | A switch in the wowsims test files that adds one proposal to the sim |
