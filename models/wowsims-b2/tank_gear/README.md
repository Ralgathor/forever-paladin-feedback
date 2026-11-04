# Item pool tank sets (4 November 2026)

The tank sets of Analysis, Threat, parts 5 to 9, and Protection: a threat set and a survival set for each class (see Survival sets). Each set obeys the item pool rules of the damage sets (`../matched_gear/opt.py`, `pre_raid`):

- No raid drops.
- No items of the Zul'Gurub and Ahn'Qiraj patches (item ids 19000 to 23999).
- No PvP items.
- No Revered or Exalted reputation items.
- Item level 63 or lower.

The wowsims default tank sets have raid, PvP and reputation items. The sets of this folder replace these items. The wowsims links are on the [sets page](https://ralgathor.github.io/forever-paladin-feedback/sets/).

## Method

1. Dump the request of each tank test with `FEEDBACK_DUMP` (feedback_prot_test.go, feedback_warrior_test.go, feedback_bear_test.go, `FEEDBACK_DUR=180`).
2. Copy `zztank_main.go` to `cmd/zztank/main.go` in the wowsims clone and build it: `go build -tags with_db -o /tmp/zztank ./cmd/zztank`.
3. Run `python3 search_tank.py <prot|war|bear|shock> <dump>`. For each item that is not in the pool, it takes the 12 pool items of the same slot with the best tank stat sum. Each candidate runs in the full set, 1,000 iterations. The search keeps the candidate with the best score, slot by slot. The score is 40% threat, 20% damage, 20% damage taken and 20% TMI, each against the default set. No item is used two times. The enchants do not change. An item of the default set keeps its random suffix (for example Hyperion Helm of the Warrior). The final set runs with 3,000 iterations.
4. Run `./run_pool.sh <wowsims clone>`. It runs all tank jobs of `../logs/checks_8298ab833.log` again with the new sets (`FEEDBACK_ITEMS`), on master commit 9a8624af9. The output is `../logs/checks_9a8624af9_pool.log`. The Paladin has the tank consumables of `feedbackConsumables` (`../go/feedback_prot_test.go`).

`set_*.json` has the 17 item ids of each set. `log_*.txt` has the search output.

## Survival sets

`TANK_SCORE=survival python3 search_tank.py <prot|war|bear> <dump>` uses the same method with a survival score: 40% threat, 30% damage taken and 30% TMI, each against the default set. The dump must have the default set (no `FEEDBACK_ITEMS`). The sets are `set_*_surv.json`, the search output `log_*_surv.txt`. `./run_pool.sh <wowsims clone> surv` runs all tank jobs with these sets: `../logs/checks_9a8624af9_pool_surv.log`. `TANK_SET=surv python3 ../finals.py <codes>` runs the Protection builds with the Paladin survival set: `../logs/finals_surv.log`.

| Tank | Items that differ from the threat set (threat set → survival set) |
| --- | --- |
| Protection Paladin | Lightforge Gauntlets → Warder's Gloves, Vindicator's Belt → Redeemer's Waistcord, Warder's Sabatons → Lightforge Boots, Cleansed Vilebranch Icon → Volunteer's Lucky Seal, Cleansed Vilebranch Medallion → Enriched Seal, Grave Scepter → Elderwild Construction Hammer, Antique Bulwark → Sacred Protector |
| Protection Warrior | Horn of Ve'han → Artifact Seeker's Pendant, Legplates of Valor → Enriched Thorium Leggings, Volunteer's Lucky Seal → Smotts' Compass, Greatflank Flayer → Bagh Nakh |
| Bear Druid | Warden's Leather Bracers → Elven Chain Wristguards, Cleansed Vilebranch Medallion → Enriched Seal |

| Tank (master 9a8624af9) | Threat set: threat / damage taken / TMI | Survival set: threat / damage taken / TMI |
| --- | --- | --- |
| Protection Paladin, live | 1,136.9 / 342.7 / 54.0 | 1,081.0 / 333.1 / 45.8 |
| Protection Warrior | 1,447.7 / 299.7 / 41 | 1,382.3 / 292.4 / 41 |
| Bear Druid | 1,754.7 / 393.3 / 43.9 | 1,717.9 / 392.5 / 42.7 |

The sets were searched on master 8298ab833, with the Paladin without consumables. The items do not change on master 9a8624af9.

## Shockadin set

`search_tank.py shock` uses the same method for the Shockadin set of the Builds tab (`set_shock.json`, `log_shock.txt`). The score is damage only. The dump is the Shockadin test of feedback_run_test.go (`FEEDBACK_SHOCK=1`, `FEEDBACK_DUR=180`, full buffs). The item swap set (Manual Crowd Pummeler) does not change.

## Sets

| Tank | Replaced items | New items |
| --- | --- | --- |
| Protection Paladin | Premier Chevalier Shoulders, Heavy Thorium Gauntlets, Soulforge Belt, Depleted Thorium Sabatons, Ring of Awareness, Arena Grand Master, Defender's Grip Stabilizer, Dark Iron Destroyer, Force Reactive Disk, Libram of Fervor | Lightforge Spaulders, Lightforge Gauntlets, Vindicator's Belt, Warder's Sabatons, Initiate's Signet of Vigilance, Cleansed Vilebranch Icon, Cleansed Vilebranch Medallion, Grave Scepter, Antique Bulwark, Libram of Holy Alacrity |
| Protection Warrior | Beads of Ogre Might, Belt of Heroism, Hyperion Legplates, Commander's Boots, Ring of Awareness, Defender's Grip Stabilizer, Annihilator, Archstrike Bow | Horn of Ve'han, Valiant's Waistguard, Legplates of Valor, Boots of Valor, Initiate's Signet of Vigilance, Volunteer's Lucky Seal, Greatflank Flayer, Gorewood Bow |
| Bear Druid | Amulet of the Darkmoon, Theramore Pauldrons, Premier Knight-Captain's Beasthide Bracers, Timbermaw Brawlers, Sentinel's Leather Pants, Dunestalker's Boots, Signet Ring of the Bronze Dragonflight, Heavy Dark Iron Ring, Stormpike Insignia Rank 6, Rune of the Guard Captain, Premier Grand Marshal's Battle Hammer | Artifact Seeker's Pendant, Warden's Leather Shoulders, Warden's Leather Bracers, Warden's Leather Gauntlets, Warbear Woolies, Warden's Leather Boots, Ring of Protection, Initiate's Signet of Vigilance, Glimmering Mithril Insignia, Cleansed Vilebranch Medallion, Enchanted Battlehammer |
| Shockadin | Blessed Band of Light, Channeler's Ring, Jewel of the Guard Captain, Adaptive Combat Assistant, Libram of Law | Initiate's Signet of Ferocity, Initiate's Signet of Brilliance, Cleansed Vilebranch Icon, Frozen Heart of the Mountain, Libram of Holy Alacrity |

## Results (wowsims master 8298ab833, 3 min, 3,000 iterations)

These are the results of the search, on master 8298ab833, before the hotfixes of 4 November and with the Paladin without consumables. Threat each sec without the multipliers of the notes of 2 November. The values of master 9a8624af9 are in the table of Survival sets.

| Tank | Default set: threat / damage taken / TMI | Item pool set: threat / damage taken / TMI |
| --- | --- | --- |
| Protection Paladin, live | 980.1 / 337.9 / 57.5 | 1,029.3 / 383.8 / 68.6 |
| Protection Warrior | 964.7 / 286.1 / 47 | 1,002.1 / 299.7 / 41 |
| Bear Druid | 846.6 / 382.6 / 40.0 | 779.0 / 393.3 / 43.9 |

- **On master 9a8624af9** (native multipliers, Paladin tank consumables), the Warrior has 1,448, the Druid 1,755 (121% of the Warrior) and the live Paladin 1,137 (79%).
- **Shockadin:** 851.4 DPS with the default set, 839.9 with the item pool set (−1.4%).
- **The Druid loses the most.** Its default set has the most PvP and reputation items.
- **The search is greedy.** It changes one slot at a time and keeps the other items. A full search of all slots together can give a slightly better set.
