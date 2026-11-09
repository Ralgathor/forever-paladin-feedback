# Item pool tank sets (4 November 2026, new searches on 6 and 8 November)

The tank sets of Analysis, Threat, parts 5 to 9, and Protection: a threat set and a survival set for each class (see Survival sets). Each set obeys the item pool rules of the damage sets (`../matched_gear/opt.py`, `pre_raid`):

- No raid drops.
- No items of the Zul'Gurub and Ahn'Qiraj patches (item ids 19000 to 23999).
- No PvP items.
- No Revered or Exalted reputation items.
- Item level 63 or lower.

The wowsims default tank sets have raid, PvP and reputation items. The sets of this folder replace these items.

**New search (6 November 2026).** Master commit `df57e2571` (hotfix push 113693) adds 2,447 items to the database. The search ran again for all tank sets and the Shockadin set on this commit, with the same rules and steps. Only the Warrior threat set changes: Scarlet Kris (a new dagger, item level 63, no source in the game data) replaces Greatflank Flayer. The Warrior threat increases by 3.8% (1,447.7 → 1,503.0). The other sets give the same items and the same values. The Paladin survival search changed the belt (Warder's Waistguard in place of Redeemer's Waistcord) by less than the run noise (+0.3% score), with no new item. Thus, the Paladin survival set stays. `log_war.txt` has the new Warrior search, `log_war_8298ab833.txt` the search of 4 November. The Warrior runs on commit df57e2571: `../logs/checks_df57e2571_pool.log`. The wowsims links are on the [sets page](https://ralgathor.github.io/forever-paladin-feedback/sets/).

**New search (8 November 2026).** Master commit `ae9b8c23a` (hotfixes of 7 and 8 November) adds 362 items that obey the pool rules for a Paladin. The search ran again for all tank sets and the Shockadin set on this commit, with the same rules and steps. The Paladin threat set takes Justicar's Gloves, Lightforge Belt, Volunteer's Lucky Seal, Enriched Seal, Hand of Edward the Odd and Argent Defender: +8.1% threat (1,136.9 → 1,228.5) and 4% less damage taken. The Paladin survival set takes Warder's Waistguard, Hand of Edward the Odd and Argent Defender. The Druid threat set takes Counterattack Lodestone and Unyielding Maul, and the Druid survival set Warstrife Leggings and Unyielding Maul. The Shockadin set takes Hand of Justice and Smolderweb's Eye. The Warrior sets do not change. A test with Argent Defender in the Warrior threat set gave only +0.2%. The search keeps the pool items of the default set, thus it did not offer this shield to the Warrior. The old search logs have the commit in the file name (`log_*_8298ab833.txt`, `log_war_df57e2571.txt`).

## Method

1. Dump the request of each tank test with `FEEDBACK_DUMP` (feedback_prot_test.go, feedback_warrior_test.go, feedback_bear_test.go, `FEEDBACK_DUR=180`).
2. Copy `zztank_main.go` to `cmd/zztank/main.go` in the wowsims clone and build it: `go build -tags with_db -o /tmp/zztank ./cmd/zztank`.
3. Run `python3 search_tank.py <prot|war|bear|shock> <dump>`. For each item that is not in the pool, it takes the 12 pool items of the same slot with the best tank stat sum. Each candidate runs in the full set, 1,000 iterations. The search keeps the candidate with the best score, slot by slot. The score is 40% threat, 20% damage, 20% damage taken and 20% TMI, each against the default set. No item is used two times. The enchants do not change. An item of the default set keeps its random suffix (for example Hyperion Helm of the Warrior). The final set runs with 3,000 iterations.
4. Run `./run_pool.sh <wowsims clone>`. It runs all tank jobs of `../logs/checks_8298ab833.log` again with the new sets (`FEEDBACK_ITEMS`), on master commit ae9b8c23a. The output is `../logs/checks_ae9b8c23a_pool.log` (4 November, master commit 9a8624af9: `../logs/checks_9a8624af9_pool.log`). The Paladin has the tank consumables of `feedbackConsumables` (`../go/feedback_prot_test.go`).

`set_*.json` has the 17 item ids of each set. `log_*.txt` has the search output.

## Survival sets

`TANK_SCORE=survival python3 search_tank.py <prot|war|bear> <dump>` uses the same method with a survival score: 40% threat, 30% damage taken and 30% TMI, each against the default set. The dump must have the default set (no `FEEDBACK_ITEMS`). The sets are `set_*_surv.json`, the search output `log_*_surv.txt`. `./run_pool.sh <wowsims clone> surv` runs all tank jobs with these sets: `../logs/checks_ae9b8c23a_pool_surv.log`. `TANK_SET=surv python3 ../finals.py <codes>` runs the Protection builds with the Paladin survival set: `../logs/finals_surv.log`.

| Tank | Items that differ from the threat set (threat set → survival set) |
| --- | --- |
| Protection Paladin | Justicar's Gloves → Warder's Gloves, Lightforge Belt → Warder's Waistguard, Warder's Sabatons → Lightforge Boots |
| Protection Warrior | Horn of Ve'han → Artifact Seeker's Pendant, Legplates of Valor → Enriched Thorium Leggings, Volunteer's Lucky Seal → Smotts' Compass, Scarlet Kris → Bagh Nakh |
| Bear Druid | Warden's Leather Bracers → Elven Chain Wristguards, Warbear Woolies → Warstrife Leggings, Counterattack Lodestone → Enriched Seal |

| Tank (master ae9b8c23a) | Threat set: threat / damage taken / TMI | Survival set: threat / damage taken / TMI |
| --- | --- | --- |
| Protection Paladin, live | 1,228.5 / 329.2 / 49.0 | 1,204.1 / 317.6 / 45.5 |
| Protection Warrior | 1,488.9 / 305.9 / 43 | 1,368.8 / 292.4 / 41 |
| Bear Druid | 1,756.1 / 361.5 / 38.6 | 1,673.4 / 355.9 / 36.2 |

The sets of 4 November were searched on master 8298ab833, with the Paladin without consumables. The search of 8 November ran on master ae9b8c23a. On master 9a8624af9 (sets of 4 November; Warrior threat set of 6 November), the values were: Paladin 1,136.9 / 342.7 / 54.0 and 1,081.0 / 333.1 / 45.8, Warrior 1,503.0 / 305.8 / 43 and 1,382.3 / 292.4 / 41, Druid 1,754.7 / 393.3 / 43.9 and 1,717.9 / 392.5 / 42.7.

## Shockadin set

`search_tank.py shock` uses the same method for the Shockadin set of the Builds tab (`set_shock.json`, `log_shock.txt`). The score is damage only. The dump is the Shockadin test of feedback_run_test.go (`FEEDBACK_SHOCK=1`, `FEEDBACK_DUR=180`, full buffs). The item swap set (Manual Crowd Pummeler) does not change.

## Sets

| Tank | Replaced items | New items |
| --- | --- | --- |
| Protection Paladin | Premier Chevalier Shoulders, Heavy Thorium Gauntlets, Soulforge Belt, Depleted Thorium Sabatons, Ring of Awareness, Arena Grand Master, Defender's Grip Stabilizer, Dark Iron Destroyer, Force Reactive Disk, Libram of Fervor | Lightforge Spaulders, Justicar's Gloves, Lightforge Belt, Warder's Sabatons, Initiate's Signet of Vigilance, Volunteer's Lucky Seal, Enriched Seal, Hand of Edward the Odd, Argent Defender, Libram of Holy Alacrity |
| Protection Warrior | Beads of Ogre Might, Belt of Heroism, Hyperion Legplates, Commander's Boots, Ring of Awareness, Defender's Grip Stabilizer, Annihilator, Archstrike Bow | Horn of Ve'han, Valiant's Waistguard, Legplates of Valor, Boots of Valor, Initiate's Signet of Vigilance, Volunteer's Lucky Seal, Scarlet Kris (Greatflank Flayer until 6 November), Gorewood Bow |
| Bear Druid | Amulet of the Darkmoon, Theramore Pauldrons, Premier Knight-Captain's Beasthide Bracers, Timbermaw Brawlers, Sentinel's Leather Pants, Dunestalker's Boots, Signet Ring of the Bronze Dragonflight, Heavy Dark Iron Ring, Stormpike Insignia Rank 6, Rune of the Guard Captain, Premier Grand Marshal's Battle Hammer | Artifact Seeker's Pendant, Warden's Leather Shoulders, Warden's Leather Bracers, Warden's Leather Gauntlets, Warbear Woolies, Warden's Leather Boots, Ring of Protection, Initiate's Signet of Vigilance, Glimmering Mithril Insignia, Counterattack Lodestone, Unyielding Maul |
| Shockadin | Blessed Band of Light, Channeler's Ring, Jewel of the Guard Captain, Adaptive Combat Assistant, Libram of Law | Initiate's Signet of Ferocity, Initiate's Signet of Brilliance, Hand of Justice, Smolderweb's Eye, Libram of Holy Alacrity |

## Results (wowsims master 8298ab833, 3 min, 3,000 iterations)

These are the results of the first search, on master 8298ab833, before the hotfixes of 4 November and with the Paladin without consumables. Threat each sec without the multipliers of the notes of 2 November. The values of master ae9b8c23a are in the table of Survival sets.

| Tank | Default set: threat / damage taken / TMI | Item pool set: threat / damage taken / TMI |
| --- | --- | --- |
| Protection Paladin, live | 980.1 / 337.9 / 57.5 | 1,029.3 / 383.8 / 68.6 |
| Protection Warrior | 964.7 / 286.1 / 47 | 1,002.1 / 299.7 / 41 |
| Bear Druid | 846.6 / 382.6 / 40.0 | 779.0 / 393.3 / 43.9 |

- **On master 9a8624af9** (native multipliers, Paladin tank consumables), the Warrior had 1,448, the Druid 1,755 (121% of the Warrior) and the live Paladin 1,137 (79%). On master df57e2571, the Warrior has 1,503 with Scarlet Kris. The Druid then has 117% of the Warrior and the live Paladin 76%. On master ae9b8c23a, with the sets of 8 November, the Warrior has 1,489, the Druid 1,756 (118%) and the live Paladin 1,229 (83%). With the default sets, the Warrior has 1,380, the Druid 1,918 and the live Paladin 1,078.
- **Shockadin:** on master ae9b8c23a, 846.9 DPS with the default set and 848.6 with the item pool set (+0.2%). On master 8298ab833: 851.4 and 839.9 (−1.4%).
- **The Druid loses the most.** Its default set has the most PvP and reputation items.
- **The search is greedy.** It changes one slot at a time and keeps the other items. A full search of all slots together can give a slightly better set.
