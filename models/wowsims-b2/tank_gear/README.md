# Item pool tank sets (4 November 2026, new searches on 6, 8, 9 and 11 November)

The tank sets of Analysis, Threat, parts 5 to 9, and Protection: a threat set and a survival set for each class (see Survival sets). Each set obeys the item pool rules of the damage sets (`../matched_gear/opt.py`, `pre_raid`):

- No raid drops.
- No items of the Zul'Gurub and Ahn'Qiraj patches (item ids 19000 to 23999).
- No PvP items.
- No Revered or Exalted reputation items.
- Item level 63 or lower.

The wowsims default tank sets have raid, PvP and reputation items. The sets of this folder replace these items.

**New search (6 November 2026).** Master commit `df57e2571` (hotfix push 113693) adds 2,447 items to the database. The search ran again for all tank sets and the Shockadin set on this commit, with the same rules and steps. Only the Warrior threat set changes: Scarlet Kris (a new dagger, item level 63, no source in the game data) replaces Greatflank Flayer. The Warrior threat increases by 3.8% (1,447.7 → 1,503.0). The other sets give the same items and the same values. The Paladin survival search changed the belt (Warder's Waistguard in place of Redeemer's Waistcord) by less than the run noise (+0.3% score), with no new item. Thus, the Paladin survival set stays. `log_war.txt` has the new Warrior search, `log_war_8298ab833.txt` the search of 4 November. The Warrior runs on commit df57e2571: `../logs/checks_df57e2571_pool.log`. The wowsims links are on the [sets page](https://ralgathor.github.io/forever-paladin-feedback/sets/).

**New search (8 November 2026).** Master commit `ae9b8c23a` (hotfixes of 7 and 8 November) adds 362 items that obey the pool rules for a Paladin. The search ran again for all tank sets and the Shockadin set on this commit, with the same rules and steps. The Paladin threat set takes Justicar's Gloves, Lightforge Belt, Volunteer's Lucky Seal, Enriched Seal, Hand of Edward the Odd and Argent Defender: +8.1% threat (1,136.9 → 1,228.5) and 4% less damage taken. The Paladin survival set takes Warder's Waistguard, Hand of Edward the Odd and Argent Defender. The Druid threat set takes Counterattack Lodestone and Unyielding Maul, and the Druid survival set Warstrife Leggings and Unyielding Maul. The Shockadin set takes Hand of Justice and Smolderweb's Eye. The Warrior sets do not change. A test with Argent Defender in the Warrior threat set gave only +0.2%. The search keeps the pool items of the default set, thus it did not offer this shield to the Warrior. The old search logs have the commit in the file name (`log_*_8298ab833.txt`, `log_war_df57e2571.txt`, `log_*_ae9b8c23a.txt`).

**New search (9 November 2026).** Master commit `9f254e8d8` (hotfix push 113823) adds 262 items, for example Scalding Flamehoof (a trinket, item level 62) and Thrall's Resolve. It also changes the Windfury Totem rule, the Druid threat (Maul and Omen of Clarity, the Enrage armor rule) and the Warrior threat rules. First, the sets of 8 November ran on this commit (`../logs/checks_9f254e8d8_pool_old_sets.log`): live Paladin 1,194.5 threat each sec (was 1,228.5), Warrior 1,511.8 (was 1,488.9), Druid 1,582.3 (was 1,756.1). The search then ran again for all tank sets and the Shockadin set, with the same rules and steps. A new set replaces the old set only if its score is more than 0.5% better (the run noise). Two sets change. The Paladin threat set takes Warder's Gloves, Scalding Flamehoof and Volunteer's Lucky Seal in place of Justicar's Gloves and Enriched Seal: +1.0% score, 0.6% less threat (1,194.5 → 1,187.4) and 3.9% less damage taken (329.1 → 316.2). The Druid survival set takes Warden's Leather Bracers, Thrall's Resolve and Scalding Flamehoof in place of Elven Chain Wristguards, Initiate's Signet of Vigilance and Enriched Seal: +1.0% score. The other searches gave a lower score than the old set (Warrior −2.2% and −1.9%, Shockadin −0.9%, Paladin survival −0.8%) or less than the run noise (Druid threat +0.4%). Thus, these sets stay.

**New search (11 November 2026).** Master commit `3633d376a` (client 1.60.1.70888, hotfixes of 10 and 11 November) adds 464 items, for example Ironfoe, Intricately Runed Shield and Ouroboros Ring. It also changes tank rules: Shield Slam ranks 2 to 4 have flat threat, Shield Slam and Shield Bash are main-hand abilities, and Rake ticks use live Attack Power. First, the sets of 9 November ran on this commit (`../logs/checks_3633d376a_pool_old_sets.log`, `../logs/checks_3633d376a_pool_surv_old_sets.log`): live Paladin 1,133.4 threat each sec (was 1,187.4), Warrior 1,591.8 (was 1,511.8), Druid 1,592.9 (was 1,582.3).

- **Argent Defender.** The Paladin loses 4.5% threat and takes 6.3% more damage (316.2 → 336.1). Block goes from 55.0% to 41.2%, and crushing blows from 5.6% to 12.0%. Until this commit, wowsims applied the proc buff of Argent Defender (Argent Dawn, +18% block for 10 sec) all the time, by error. Now wowsims lists this proc as not implemented (commit 3134971ec). The shield gives only its stats.
- **Proc items.** The search now also takes all pool items of the slot with an effect that wowsims implements (`EFFECTS`: the list of `zzeffects_main.go`, `effects_3633d376a.txt`). Before, a proc weapon such as Flurry Axe was not a candidate, because its stat sum is low. In the Paladin main hand, Flurry Axe is second (score 0.760) and Ironfoe third (0.752), after Hand of Edward the Odd (0.766). In the Warrior main hand, Ironfoe is first (1.063, Scarlet Kris 1.045).

The search then ran again for all tank sets and the Shockadin set. A new set replaces the old set only if its score is more than 0.5% better. Both sets run at 3,000 iterations, with the same default set as reference. Three sets change:

- Paladin survival set: +1.6% score. Stockade Pauldrons, Force Imbued Gauntlets, Sentinel's Waistguard, Warder's Sabatons, Myrmidon's Signet, Ragged John's Neverending Cup, Volunteer's Lucky Seal and Intricately Runed Shield.
- Warrior threat set: +1.1% score. Girdle of Uther, Grimy Metal Boots, Myrmidon's Signet, Royal Seal of Eldre'Thalas, Ironfoe and Eaglehorn Long Bow.
- Druid threat set: +1.3% score. Thrall's Resolve, Ouroboros Ring, Hand of Justice and Glimmering Mithril Insignia.

The Paladin threat set (−0.2%), the Warrior survival set (0%), the Druid survival set (the same items) and the Shockadin set (−0.1%) stay. The Paladin threat set keeps Argent Defender: its 2,121 armor and 39 block value still give the best score.

**Proc pass (11 November 2026, after the review).** The search above opens only the slots with an item outside the pool. Thus, a slot with a pool item of the default set does not try the proc items. The proc pass corrects this. Each other slot runs all pool items with an implemented effect, slot by slot, against the set so far (1,000 iterations). An item replaces the item of the slot only if the score is more than 0.2% better. All sets ran this pass (`log_*_proc.txt`). Three more sets change:

- Warrior threat set: Hand of Justice replaces Demon's Blood. 1,632.4 threat each sec (was 1,604.0), score +1.0% at 3,000 iterations.
- Warrior survival set: Stoneform Shoulders, Magically Sealed Bracers, Force Imbued Gauntlets, Hand of Justice and Skullflame Shield. Score +3.9%.
- Shockadin set: Storm Gauntlets and The Needler replace Gauntlets of Elements and Shin Blade. 833.8 DPS (was 823.0), +1.3%.

The Paladin and Druid sets do not change. In the Paladin main hand, Hand of Edward the Odd stays first. The search logs of 9 November have the commit in the file name (`log_*_9f254e8d8.txt`).

## Method

1. Dump the request of each tank test with `FEEDBACK_DUMP` (feedback_prot_test.go, feedback_warrior_test.go, feedback_bear_test.go, `FEEDBACK_DUR=180`).
2. Copy `zztank_main.go` to `cmd/zztank/main.go` in the wowsims clone and build it: `go build -tags with_db -o /tmp/zztank ./cmd/zztank`.
3. Run `EFFECTS=effects_3633d376a.txt python3 search_tank.py <prot|war|bear|shock> <dump>`. For each item that is not in the pool, it takes the 12 pool items of the same slot with the best tank stat sum. It also takes all pool items of the slot with an effect that wowsims implements (`EFFECTS`, since 11 November). Make the list with `zzeffects_main.go` (copy to `cmd/zzeffects/main.go`, `go run -tags with_db ./cmd/zzeffects > effects.txt`). After the slot search, the proc pass tests all pool items with an implemented effect in each other slot. `START=<set file>` runs only the proc pass, from that set. Each candidate runs in the full set, 1,000 iterations. The search keeps the candidate with the best score, slot by slot. The score is 40% threat, 20% damage, 20% damage taken and 20% TMI, each against the default set. No item is used two times. The enchants do not change. An item of the default set keeps its random suffix (for example Hyperion Helm of the Warrior). The final set runs with 3,000 iterations.
4. Run `./run_pool.sh <wowsims clone>`. It runs all tank jobs of `../logs/checks_8298ab833.log` again with the new sets (`FEEDBACK_ITEMS`), on master commit 3633d376a (Go 1.27). The output is `../logs/checks_3633d376a_pool.log` (9 November, master commit 9f254e8d8: `../logs/checks_9f254e8d8_pool.log`; 4 November, master commit 9a8624af9: `../logs/checks_9a8624af9_pool.log`). The Paladin has the tank consumables of `feedbackConsumables` (`../go/feedback_prot_test.go`).

`set_*.json` has the 17 item ids of each set. `log_*.txt` has the search output.

## Survival sets

`TANK_SCORE=survival python3 search_tank.py <prot|war|bear> <dump>` uses the same method with a survival score: 40% threat, 30% damage taken and 30% TMI, each against the default set. The dump must have the default set (no `FEEDBACK_ITEMS`). The sets are `set_*_surv.json`, the search output `log_*_surv.txt`. `./run_pool.sh <wowsims clone> surv` runs all tank jobs with these sets: `../logs/checks_3633d376a_pool_surv.log`. `TANK_SET=surv python3 ../finals.py <codes>` runs the Protection builds with the Paladin survival set: `../logs/finals_surv.log`.

| Tank | Items that differ from the threat set (threat set → survival set) |
| --- | --- |
| Protection Paladin | Lightforge Spaulders → Stockade Pauldrons, Warder's Gloves → Force Imbued Gauntlets, Lightforge Belt → Sentinel's Waistguard, Initiate's Signet of Vigilance → Myrmidon's Signet, Scalding Flamehoof → Ragged John's Neverending Cup, Argent Defender → Intricately Runed Shield |
| Protection Warrior | Horn of Ve'han → Artifact Seeker's Pendant, Girdle of Uther → Valiant's Waistguard, Legplates of Valor → Enriched Thorium Leggings, Grimy Metal Boots → Boots of Valor, Hermit's Pauldron → Stoneform Shoulders, Mighty Armsplints → Magically Sealed Bracers, Sentinel's Gloves → Force Imbued Gauntlets, Myrmidon's Signet → Initiate's Signet of Vigilance, Royal Seal of Eldre'Thalas → Smotts' Compass, Ironfoe → Bagh Nakh, Sacred Protector → Skullflame Shield, Eaglehorn Long Bow → Gorewood Bow |
| Bear Druid | Warbear Woolies → Warstrife Leggings, Ouroboros Ring → Ring of Protection, Hand of Justice → Glimmering Mithril Insignia, Glimmering Mithril Insignia → Scalding Flamehoof |

| Tank (master 3633d376a) | Threat set: threat / damage taken / TMI | Survival set: threat / damage taken / TMI |
| --- | --- | --- |
| Protection Paladin, live | 1,133.4 / 336.1 / 51.0 | 1,082.3 / 323.4 / 45.7 |
| Protection Warrior | 1,632.4 / 299.4 / 44 | 1,448.4 / 270.3 / 38 |
| Bear Druid | 1,613.6 / 358.3 / 37.9 | 1,524.8 / 347.5 / 36.1 |

The sets of 4 November were searched on master 8298ab833, with the Paladin without consumables. The search of 8 November ran on master ae9b8c23a. The search of 9 November ran on master 9f254e8d8, and the search of 11 November on master 3633d376a. The earlier values (threat set and survival set, threat / damage taken / TMI) are:

| Master (sets) | Paladin, live | Warrior | Druid |
| --- | --- | --- | --- |
| 9f254e8d8 (sets of 9 November) | 1,187.4 / 316.2 / 47.1 and 1,172.7 / 316.6 / 45.5 | 1,511.8 / 306.1 / 43 and 1,388.6 / 292.8 / 41 | 1,582.3 / 359.4 / 38.2 and 1,514.6 / 345.3 / 35.8 |
| ae9b8c23a (sets of 8 November) | 1,228.5 / 329.2 / 49.0 and 1,204.1 / 317.6 / 45.5 | 1,488.9 / 305.9 / 43 and 1,368.8 / 292.4 / 41 | 1,756.1 / 361.5 / 38.6 and 1,673.4 / 355.9 / 36.2 |
| 9a8624af9 (sets of 4 November; Warrior threat set of 6 November) | 1,136.9 / 342.7 / 54.0 and 1,081.0 / 333.1 / 45.8 | 1,503.0 / 305.8 / 43 and 1,382.3 / 292.4 / 41 | 1,754.7 / 393.3 / 43.9 and 1,717.9 / 392.5 / 42.7 |

## Shockadin set

`search_tank.py shock` uses the same method for the Shockadin set of the Builds tab (`set_shock.json`, `log_shock.txt`). The score is damage only. The dump is the Shockadin test of feedback_run_test.go (`FEEDBACK_SHOCK=1`, `FEEDBACK_DUR=180`, full buffs). The item swap set (Manual Crowd Pummeler) does not change.

## Sets

| Tank | Replaced items | New items |
| --- | --- | --- |
| Protection Paladin | Premier Chevalier Shoulders, Heavy Thorium Gauntlets, Soulforge Belt, Depleted Thorium Sabatons, Ring of Awareness, Arena Grand Master, Defender's Grip Stabilizer, Dark Iron Destroyer, Force Reactive Disk, Libram of Fervor | Lightforge Spaulders, Warder's Gloves (Justicar's Gloves until 9 November), Lightforge Belt, Warder's Sabatons, Initiate's Signet of Vigilance, Scalding Flamehoof, Volunteer's Lucky Seal (Enriched Seal until 9 November), Hand of Edward the Odd, Argent Defender, Libram of Holy Alacrity |
| Protection Warrior | Beads of Ogre Might, Hyperion Legplates, Commander's Boots, Ring of Awareness, Defender's Grip Stabilizer, Demon's Blood, Annihilator, Archstrike Bow (and Belt of Heroism until 9 November) | Horn of Ve'han, Legplates of Valor, Grimy Metal Boots, Myrmidon's Signet, Royal Seal of Eldre'Thalas, Hand of Justice, Ironfoe, Eaglehorn Long Bow. Until 11 November: Valiant's Waistguard, Boots of Valor, Initiate's Signet of Vigilance, Volunteer's Lucky Seal, Scarlet Kris (Greatflank Flayer until 6 November) and Gorewood Bow. The belt is now Girdle of Uther, the belt of the default set since 9 November |
| Bear Druid | Amulet of the Darkmoon, Theramore Pauldrons, Premier Knight-Captain's Beasthide Bracers, Timbermaw Brawlers, Sentinel's Leather Pants, Dunestalker's Boots, Signet Ring of the Bronze Dragonflight, Heavy Dark Iron Ring, Stormpike Insignia Rank 6, Rune of the Guard Captain, Premier Grand Marshal's Battle Hammer | Artifact Seeker's Pendant, Warden's Leather Shoulders, Warden's Leather Bracers, Warden's Leather Gauntlets, Warbear Woolies, Warden's Leather Boots, Ring of Protection, Initiate's Signet of Vigilance, Glimmering Mithril Insignia, Counterattack Lodestone, Unyielding Maul |
| Shockadin | Gauntlets of Elements, Blessed Band of Light, Channeler's Ring, Jewel of the Guard Captain, Adaptive Combat Assistant, Shin Blade, Libram of Law | Storm Gauntlets, Initiate's Signet of Ferocity, Initiate's Signet of Brilliance, Hand of Justice, Smolderweb's Eye, The Needler, Libram of Holy Alacrity |

## Results (wowsims master 8298ab833, 3 min, 3,000 iterations)

These are the results of the first search, on master 8298ab833, before the hotfixes of 4 November and with the Paladin without consumables. Threat each sec without the multipliers of the notes of 2 November. The values of master ae9b8c23a are in the table of Survival sets.

| Tank | Default set: threat / damage taken / TMI | Item pool set: threat / damage taken / TMI |
| --- | --- | --- |
| Protection Paladin, live | 980.1 / 337.9 / 57.5 | 1,029.3 / 383.8 / 68.6 |
| Protection Warrior | 964.7 / 286.1 / 47 | 1,002.1 / 299.7 / 41 |
| Bear Druid | 846.6 / 382.6 / 40.0 | 779.0 / 393.3 / 43.9 |

- **On master 9a8624af9** (native multipliers, Paladin tank consumables), the Warrior had 1,448, the Druid 1,755 (121% of the Warrior) and the live Paladin 1,137 (79%). On master df57e2571, the Warrior has 1,503 with Scarlet Kris. The Druid then has 117% of the Warrior and the live Paladin 76%. On master ae9b8c23a, with the sets of 8 November, the Warrior has 1,489, the Druid 1,756 (118%) and the live Paladin 1,229 (83%). With the default sets, the Warrior has 1,380, the Druid 1,918 and the live Paladin 1,078. On master 9f254e8d8, with the sets of 9 November, the Warrior has 1,512, the Druid 1,582 (105%) and the live Paladin 1,187 (79%). With the default sets, the Warrior has 1,396, the Druid 1,728 and the live Paladin 1,039.
- **Shockadin:** on master 3633d376a, 820.6 DPS with the default set and 833.8 with the item pool set of 11 November (+1.6%). On master 9f254e8d8: 820.6 and 823.0 (+0.3%). On master ae9b8c23a: 846.9 and 848.6 (+0.2%). On master 8298ab833: 851.4 and 839.9 (−1.4%).
- **The Druid loses the most.** Its default set has the most PvP and reputation items.
- **The search is greedy.** It changes one slot at a time and keeps the other items. A full search of all slots together can give a slightly better set.
