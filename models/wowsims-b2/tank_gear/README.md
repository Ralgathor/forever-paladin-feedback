# Item pool tank sets (4 November 2026, new searches on 6, 8, 9, 11, 12, 13, 15, 16 and 18 November, two on 12 November)

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

**Proc pass (11 November 2026, after the review).** The search above opens only the slots with an item outside the pool. Thus, a slot with a pool item of the default set does not try the proc items. The proc pass corrects this. Each other slot runs all pool items with an implemented effect, slot by slot, against the set so far (1,000 iterations).

An item replaces the item of the slot only if the score is more than 0.2% better. All sets ran this pass (`log_*_proc.txt`). Three more sets change:

- Warrior threat set: Hand of Justice replaces Demon's Blood. 1,632.4 threat each sec (was 1,604.0), score +1.0% at 3,000 iterations.
- Warrior survival set: Stoneform Shoulders, Magically Sealed Bracers, Force Imbued Gauntlets, Hand of Justice and Skullflame Shield. Score +3.9%.
- Shockadin set: Storm Gauntlets and The Needler replace Gauntlets of Elements and Shin Blade. 833.8 DPS (was 823.0), +1.3%.

The Paladin and Druid sets do not change. In the Paladin main hand, Hand of Edward the Odd stays first. The search logs of 9 November have the commit in the file name (`log_*_9f254e8d8.txt`).

**New search (12 November 2026).** Master commit `52471a100` (hotfixes of 11 and 12 November) adds 69 items, for example Darrowshire Strongguard and Warmaster Legguards. It also changes tank rules:

- Weapon procs no longer trigger from Shield Slam, Shield Bash, Thunder Clap and abilities with magic DefenseType.
- Lacerate gives 10/3 threat for each point of damage, from the hit and from the ticks. wowsims measured this rule in the game only on rank 2, at levels 38 to 50.
- Faerie Fire in Bear Form gives 2 × level threat.

First, the sets of 11 November ran on this commit (`../logs/checks_52471a100_pool_old_sets.log`, `../logs/checks_52471a100_pool_surv_old_sets.log`). The live Paladin does not change (1,133.4 threat each sec). The Warrior has 1,623.8 (was 1,632.4), and the Druid 2,302.2 (was 1,613.6, +43% from Lacerate).

The search then ran again for all tank sets and the Shockadin set, with the slot search and the proc pass in one run. The list of items with an implemented effect has 275 items on this commit (`effects_52471a100.txt`, 266 on commit 3633d376a). A new set replaces the old set only if its score is more than 0.5% better at 3,000 iterations. Two sets change:

- Warrior threat set: +1.0% score. Skullflame Shield and Deep Jungle Rifle replace Sacred Protector and Eaglehorn Long Bow. 1,650.2 threat each sec (1,623.8 with the old set).
- Warrior survival set: +0.65% score. New items: Talisman of Evasion, Girdle of Uther, Warmaster Legguards, Shalehusk Boots and Ezra's Seal of Authenticity. Also Royal Seal of Eldre'Thalas, Mark of Tyranny, Ironfoe and Carapace Spine Crossbow. 253.7 damage taken each sec (270.9 with the old set).

The Paladin threat set (−0.15%), the Paladin survival set (the same items), the Druid sets (the same items) and the Shockadin set (−0.13%) stay. The search logs of 11 November have the commit in the file name (`log_*_3633d376a.txt`, `log_*_proc_3633d376a.txt`).

**New search (12 November 2026, evening).** Master commit `129fcd89e` (hotfixes of 12 November and push 114027) changes two proc items and adds Blackhand's Breadth:

- Hand of Justice has its full proc chance (3%) only against Dwarves, and 1% against other targets. Ironfoe has 6% against Orcs and 3% against other targets.
- Weapon procs skip melee abilities with no DefenseType.
- wowsims gives the set bonuses of 113 item sets.

First, the sets of 12 November ran on this commit (`../logs/checks_129fcd89e_pool_old_sets.log`, `../logs/checks_129fcd89e_pool_surv_old_sets.log`). The live Paladin does not change (1,133.4 threat each sec): its sets have no Hand of Justice and no Ironfoe. The Warrior has 1,600.6 (was 1,650.2, −3.0%), and the Druid 2,276.8 (was 2,302.2, −1.1%). The Shockadin set has 823.8 DPS (was 833.8, −1.2%).

The search then ran again for all tank sets and the Shockadin set, with the slot search and the proc pass in one run. The list of items with an implemented effect has 296 items on this commit (`effects_129fcd89e.txt`). A new set replaces the old set only if its score is more than 0.5% better at 3,000 iterations. One set changes:

- Warrior survival set: +0.69% score. Hammer of the Vesper, Naglering and Sentinel's Gloves replace Ironfoe, Ring of Protection and Force Imbued Gauntlets. 1,385.9 threat each sec, 250.9 damage taken each sec and TMI 38.8 (old set: 1,417.5, 253.6 and 40.1).

The other sets stay. Two sets gain less than the run noise: the Paladin survival set (+0.41%, Cloudkeeper Legplates) and the Shockadin set (+0.43%, Blackhand's Breadth). The Paladin threat set (+0.06%), the Warrior threat set (−0.30%) and the Druid sets (−0.02% and the same items) also stay. The search logs of 12 November have the commit in the file name (`log_*_52471a100.txt`).

**New search (13 November 2026).** Master commit `8c7b5a5f5` (client 1.60.1.70938, hotfixes of 13 November) adds 46 items, for example The Lion Horn of Stormwind, Bolt's Charged Eyeball and Scaleguard Scimitar. It also changes tank rules:

- Redoubt and Shieldsworn: each melee swing or ability against the Paladin rolls the 10% Redoubt chance, avoided attacks included. Before, only hits rolled it.
- The Lion Horn of Stormwind: when struck, 10% chance to give 725 armor to the party for 30 sec (60 sec cooldown).
- Since this round, Judgement of Righteousness and Judgement of Fury are ranged attacks (`../patches/judgement-ranged.patch`). They no longer trigger melee weapon procs. Judgement of Command is a melee attack again since the late hotfix of 13 November.

First, the sets of 12 November, evening ran on this commit (`../logs/checks_8c7b5a5f5_pool_old_sets.log`, `../logs/checks_8c7b5a5f5_pool_surv_old_sets.log`). The live Paladin has 1,141.1 threat each sec (was 1,133.4, +0.7%) and takes 328.2 damage each sec (was 336.1, −2.4%). The Warrior and the Druid do not change. The Shockadin set has 815.5 DPS (was 823.8, −1.0%, from the ranged judgements).

The search then ran again for all tank sets and the Shockadin set, with the slot search and the proc pass in one run. The list of items with an implemented effect has 308 items on this commit (`effects_8c7b5a5f5.txt`). A new set replaces the old set only if its score is more than 0.5% better at 3,000 iterations. Four sets change. The Lion Horn of Stormwind is in all four:

- Paladin threat set: +0.60% score. Stockade Pauldrons, Storm Gauntlets, Sentinel's Waistguard, Cloudkeeper Legplates, Initiate's Signet of Ferocity, The Lion Horn of Stormwind, Bolt's Charged Eyeball and Draconian Deflector. 1,138.9 threat each sec, 315.5 damage taken each sec and TMI 50.4 (old set: 1,141.1, 328.2 and 50.0). The set has no Argent Defender now.
- Paladin survival set: +2.32% score. Cloudkeeper Legplates, Naglering, The Lion Horn of Stormwind, Ragged John's Neverending Cup and Draconian Deflector. 1,089.7, 300.2 and 43.6 (old set: 1,088.3, 316.9 and 44.7).
- Warrior threat set: +1.95% score. Stoneform Shoulders, Magically Sealed Bracers, Sabatons of Heroism, The Lion Horn of Stormwind, Scaleguard Scimitar and Blackcrow. 1,525.0, 269.1 and 38.2 (old set: 1,600.6, 295.1 and 44.4). The set gives 4.7% less threat and 8.8% less damage taken.
- Druid survival set: +1.54% score. Feralheart Grips and The Lion Horn of Stormwind. 2,162.9, 334.2 and 35.1 (old set: 2,192.6, 346.7 and 35.9).

The other sets stay: the Druid threat set (+0.46%), the Shockadin set (+0.32%) and the Warrior survival set (−0.46%). The search logs of 12 November, evening have the commit in the file name (`log_*_129fcd89e.txt`).

**New search (15 November 2026).** Master commit `6084403a9` (hotfixes of 15 November) adds 98 items, for example the Soulforge and Heroism items of dungeon set 0.5. It also changes tank rules:

- Spell damage, periodic damage and special attacks give a Warrior or a Druid two times the rage of a melee swing.
- Shield Slam and Cleave have new flat threat values. Damage shields reflect no damage on a full block.
- wowsims now makes Judgement of Righteousness and Judgement of Fury ranged attacks itself. Thus, `../patches/judgement-ranged.patch` is not necessary.

First, the sets of 13 November ran on this commit (`../logs/checks_6084403a9_pool_old_sets.log`, `../logs/checks_6084403a9_pool_surv_old_sets.log`). The live Paladin has 1,150.8 threat each sec (was 1,138.9, +1.0%) and takes 316.6 damage each sec (was 315.5). The Warrior threat set has 1,569.2 (was 1,525.0, +2.9%), and the Druid threat set 2,428.3 (was 2,276.8, +6.7%). The Shockadin set has 819.0 DPS (was 815.5, +0.4%).

The search then ran again for all tank sets and the Shockadin set, with the slot search and the proc pass in one run. The list of items with an implemented effect has 316 items on this commit (`effects_6084403a9.txt`). A new set replaces the old set only if its score is more than 0.5% better at 3,000 iterations. Three sets change:

- Warrior threat set: +3.97% score. New items: Lionheart Helm, Phantasmal Cloak, Chestguard of Heroism, Sentinel's Wristguards, Force Imbued Gauntlets and Sentinel's Waistguard. Also Cloudkeeper Legplates, Furbolg Berserker's Boots, Blackstone Ring, Naglering, Volunteer's Lucky Seal, Scarlet Kris and Deep Jungle Rifle. 1,677.5 threat each sec, 295.7 damage taken each sec and TMI 38.2 (old set: 1,569.2, 287.2 and 40.2). The set gives 6.9% more threat and 3.0% more damage taken.
- Warrior survival set: +6.7% score. The same new items as the threat set, with Shifting Cloak, Wraithplate Leggings, Ring of Saviors, Intricately Runed Shield and Eaglehorn Long Bow. 1,590.2, 282.0 and 36.2 (old set: 1,426.3, 269.4 and 41).
- Druid threat set: +1.21% score. Feralheart Grips, Feralheart Treads, Ring of Protection and Counterattack Lodestone. 2,439.0, 354.5 and 37.1 (old set: 2,428.3, 360.9 and 38.1).

The other sets stay: the Paladin threat set (+0.16%), the Shockadin set (+0.22%), the Paladin survival set and the Druid survival set (less than 0.5%). The search logs of 13 November have the commit in the file name (`log_*_8c7b5a5f5.txt`).

**Open search (16 November 2026).** The slot search of `search_tank.py` changes one slot at a time from the default set. It keeps a new item only if the score is 0.5% better. Thus, it can stop at a set that is not the best. `search_open.py` searches again from the current sets on the same commit (6084403a9):

- Each slot tries the 12 pool items with the best tank stat sum and all pool items with an implemented effect. For the Paladin, it also tries all pool items with spell damage and Defense.
- It makes up to 3 passes over the 17 slots. A new item must improve the score by more than 0.2% at 1,000 iterations. The final set runs with 3,000 iterations.
- It also requires item level 45 or higher. No item of item level 31 to 44 with an effect improved a set in a test run.

Usage: `[TANK_SCORE=survival SUF=_surv] python3 search_open.py <prot|war|bear> <dump> pool`. All six tank sets change. The search logs of the first sets of 15 November are `log_*_6084403a9_first.txt`.

| Set | Score (old → new) | New items | Threat / damage taken / TMI (old set) |
| --- | --- | --- | --- |
| Paladin, threat | 1.0032 → 1.0422 | Shifting Cloak, Soulforge Chestguards, Warder's Wristguards, Warder's Waistguard, Initiate's Signet of Vigilance, Myrmidon's Signet, Flamebreak Talisman | 1,179.7 / 300.2 / 46.9 (1,150.8 / 316.6 / 50.5) |
| Warrior, threat | 1.0394 → 1.1107 | Lightforge Spaulders, Stoneskin Gargoyle Cape, Breastplate of Heroism, Gargantuan Wristguards, Handguards of Heroism, Valiant's Waistguard, Legplates of Valor, Myrmidon's Signet, Royal Seal of Eldre'Thalas, The Lion Horn of Stormwind (other slot), Ironfoe | 1,838.0 / 293.6 / 37.3 (1,677.5 / 295.7 / 38.2) |
| Druid, threat | 0.9775 → 0.9886 | Horn of Ve'han, Death's Clutch, Cloak of Warding | 2,453.8 / 346.8 / 36.7 (2,439.0 / 354.5 / 37.1) |
| Paladin, survival | 1.0043 → 1.0405 | Enriched Thorium Helm, Shifting Cloak, Soulforge Chestguards, Vigorsteel Vambraces, Warder's Waistguard, Enriched Thorium Leggings | 1,078.8 / 293.9 / 39.1 (1,102.4 / 302.1 / 43.9) |
| Warrior, survival | 1.0915 → 1.2068 | 11 items, for example Faceguard of Heroism, Spaulders of Valor, Handguards of Heroism and Krol Blade (`log_war_surv.txt`) | 1,540.5 / 254.6 / 29.5 (1,590.2 / 282.0 / 36.2) |
| Druid, survival | 1.0274 → 1.0619 | Cloak of Warding, Songbird Blouse, Dinosaur Hide Belt, Feralheart Treads | 2,232.4 / 331.3 / 31.4 (2,319.2 / 336.6 / 35.3) |

- The Warrior threat set gains 9.6% threat, the Paladin threat set 2.5% and the Druid threat set 0.6%. Thus, the live Paladin goes from 69% to 64% of the Warrior threat.
- The Paladin threat set takes 5% less damage. Soulforge Chestguards and the Warder's pieces give Defense and dodge.
- All checks and builds ran again with the new sets: `../logs/checks_6084403a9_pool.log`, `../logs/checks_6084403a9_pool_surv.log`, `../logs/finals.log` and `../logs/finals_surv.log`. The runs with the first sets of 15 November have `_6084403a9_first` in the file name.

**New search (18 November 2026).** Master commit `ad6b13af8` (hotfixes of 16 and 17 November) changes the proc rates of many items. Unbridled Wrath now also procs from melee abilities, thus the Warrior receives more rage. First, the sets of 16 November ran on this commit with the full threat consumables (`../logs/checks_ad6b13af8_pool_full_old_sets.log`, `../logs/checks_ad6b13af8_pool_surv_full_old_sets.log`). The live Paladin has 1,396 threat each sec (no change), the Warrior 1,914 (+0.8%) and the Druid 2,611 (no change).

`search_open.py` then ran again for all six tank sets, from the sets of 16 November, with the full threat consumables. It uses the `EFFECTS` list of this commit (`effects_ad6b13af8.txt`, 368 items). `EFFECTS=<list>` is now an option of `search_open.py`. A new set replaces the old set only if its score is more than 0.5% better at 3,000 iterations. Four sets change:

| Set | Score (old → new) | New items | Threat / damage taken / TMI (old set) |
| --- | --- | --- | --- |
| Paladin, threat | 1.0485 → 1.0579 | Vigorsteel Vambraces, Warder's Gloves, Frozen Heart of the Mountain | 1,383.5 / 290.6 / 43.5 (1,396.1 / 296.3 / 46.4) |
| Paladin, survival | 1.0412 → 1.0556 | Warder's Wristguards, Soulforge Sabatons, Initiate's Signet of Vigilance | 1,292.2 / 288.2 / 37.7 (1,282.0 / 290.6 / 38.6) |
| Druid, threat | 0.9879 → 1.0109 | Feralheart Faceguard, Truestrike Shoulders, Feralheart Armor, Cloudrunner Girdle | 2,573.3 / 316.4 / 25.7 (2,610.8 / 329.9 / 28.2) |
| Druid, survival | 1.0515 → 1.0939 | Feralheart Faceguard, Horn of Ve'han, Feralheart Armor | 2,389.1 / 300.3 / 23.2 (2,379.0 / 315.9 / 24.7) |

- The Warrior sets (+0.2%) and the Shockadin set (+0.05%) stay.
- The new Paladin threat set has 0.9% less threat, but takes 1.9% less damage and has a 6% better TMI. The new Druid threat set has 1.4% less threat and takes 4% less damage.
- All checks and builds ran again with the new sets: `../logs/checks_ad6b13af8_pool*.log` and `../logs/finals*.log`. The search logs of 16 November have `_6084403a9` in the file name.

## Method

1. Dump the request of each tank test with `FEEDBACK_DUMP` (feedback_prot_test.go, feedback_warrior_test.go, feedback_bear_test.go, `FEEDBACK_DUR=180`).
2. Copy `zztank_main.go` to `cmd/zztank/main.go` in the wowsims clone and build it: `go build -tags with_db -o /tmp/zztank ./cmd/zztank`.
3. Run `EFFECTS=effects_ad6b13af8.txt python3 search_tank.py <prot|war|bear|shock> <dump>`. For each item that is not in the pool, it takes the 12 pool items of the same slot with the best tank stat sum. It also takes all pool items of the slot with an effect that wowsims implements (`EFFECTS`, since 11 November). Make the list with `zzeffects_main.go` (copy to `cmd/zzeffects/main.go`, `go run -tags with_db ./cmd/zzeffects > effects.txt`).

   After the slot search, the proc pass tests all pool items with an implemented effect in each other slot. `START=<set file>` runs only the proc pass, from that set. Each candidate runs in the full set, 1,000 iterations. The search keeps the candidate with the best score, slot by slot. The score is 40% threat, 20% damage, 20% damage taken and 20% TMI, each against the default set.

   No item is used two times. The enchants do not change. An item of the default set keeps its random suffix (for example Hyperion Helm of the Warrior). The final set runs with 3,000 iterations.
4. Run `./run_pool.sh <wowsims clone>`. It runs all tank jobs of `../logs/checks_8298ab833.log` again with the new sets (`FEEDBACK_ITEMS`), on master commit ad6b13af8 (Go 1.27). The output is `../logs/checks_ad6b13af8_pool.log`. Earlier outputs:

   - 15 and 16 November, master commit 6084403a9: `../logs/checks_6084403a9_pool.log`
   - 13 November, master commit 8c7b5a5f5: `../logs/checks_8c7b5a5f5_pool.log`
   - 12 November, evening, master commit 129fcd89e: `../logs/checks_129fcd89e_pool.log`
   - 12 November, master commit 52471a100: `../logs/checks_52471a100_pool.log`
   - 11 November, master commit 3633d376a: `../logs/checks_3633d376a_pool.log`
   - 9 November, master commit 9f254e8d8: `../logs/checks_9f254e8d8_pool.log`
   - 4 November, master commit 9a8624af9: `../logs/checks_9a8624af9_pool.log`

   The Paladin has the tank consumables of `feedbackConsumables` (`../go/feedback_prot_test.go`).

`set_*.json` has the 17 item ids of each set. `log_*.txt` has the search output.

## Survival sets

`TANK_SCORE=survival python3 search_tank.py <prot|war|bear> <dump>` uses the same method with a survival score. The score is 40% threat, 30% damage taken and 30% TMI, each against the default set. The dump must have the default set (no `FEEDBACK_ITEMS`). The sets are `set_*_surv.json`, the search output `log_*_surv.txt`. `./run_pool.sh <wowsims clone> surv` runs all tank jobs with these sets: `../logs/checks_ad6b13af8_pool_surv.log`. `TANK_SET=surv python3 ../finals.py <codes>` runs the Protection builds with the Paladin survival set: `../logs/finals_surv.log`.

| Tank | Items that differ from the threat set (threat set → survival set) |
| --- | --- |
| Protection Paladin | Stalwart Helm → Enriched Thorium Helm, Vigorsteel Vambraces → Warder's Wristguards, Warder's Gloves → Force Imbued Gauntlets, Cloudkeeper Legplates → Enriched Thorium Leggings, Warder's Sabatons → Soulforge Sabatons, Frozen Heart of the Mountain → Ragged John's Neverending Cup |
| Protection Warrior | 15 items, for example Breastplate of Heroism → Chestguard of Heroism, Ironfoe → Krol Blade, Skullflame Shield → Intricately Runed Shield (`set_war.json`, `set_war_surv.json`) |
| Bear Druid | Truestrike Shoulders → Warden's Leather Shoulders, Cloudrunner Girdle → Dinosaur Hide Belt, Warbear Woolies → Warstrife Leggings, Counterattack Lodestone → Glimmering Mithril Insignia, Glimmering Mithril Insignia → The Lion Horn of Stormwind |

| Tank (master ad6b13af8, sets of 18 November, consumables of 16 November) | Threat set: threat / damage taken / TMI | Survival set: threat / damage taken / TMI |
| --- | --- | --- |
| Protection Paladin, live | 1,164.4 / 295.1 / 44.4 | 1,083.4 / 293.1 / 38.4 |
| Protection Warrior | 1,846.0 / 294.4 / 37 | 1,553.8 / 255.2 / 30 |
| Bear Druid | 2,423.7 / 331.9 / 33.0 | 2,243.1 / 314.5 / 29.6 |

With the full threat consumables of 17 November, see the table of 18 November above and Analysis, Threat, part 6.

The sets of 4 November were searched on master 8298ab833, with the Paladin without consumables. The search of 8 November ran on master ae9b8c23a. The search of 9 November ran on master 9f254e8d8. The searches of 11, 12, 13, 15, 16 and 18 November ran on masters 3633d376a, 52471a100, 129fcd89e, 8c7b5a5f5, 6084403a9 (15 and 16 November) and ad6b13af8. The earlier values (threat set and survival set, threat / damage taken / TMI) are:

| Master (sets) | Paladin, live | Warrior | Druid |
| --- | --- | --- | --- |
| 6084403a9 (sets of 16 November) | 1,179.7 / 300.2 / 46.9 and 1,078.8 / 293.9 / 39.1 | 1,838.0 / 293.6 / 37 and 1,540.5 / 254.6 / 30 | 2,453.8 / 346.8 / 36.7 and 2,232.4 / 331.3 / 31.4 |
| 6084403a9 (sets of 15 November) | 1,150.8 / 316.6 / 50.5 and 1,102.4 / 302.1 / 44.0 | 1,677.5 / 295.7 / 38 and 1,590.2 / 282.0 / 36 | 2,439.0 / 354.5 / 37.1 and 2,319.2 / 336.6 / 35.3 |
| 8c7b5a5f5 (sets of 13 November) | 1,138.9 / 315.5 / 50.4 and 1,089.7 / 300.2 / 43.6 | 1,525.0 / 269.1 / 38 and 1,385.9 / 250.9 / 39 | 2,276.8 / 358.6 / 37.9 and 2,162.9 / 334.2 / 35.1 |
| 129fcd89e (sets of 12 November, evening) | 1,133.4 / 336.1 / 51.0 and 1,082.3 / 323.4 / 45.7 | 1,600.6 / 295.1 / 44 and 1,385.9 / 250.9 / 39 | 2,276.8 / 358.6 / 37.9 and 2,192.6 / 346.7 / 35.9 |
| 52471a100 (sets of 12 November) | 1,133.4 / 336.1 / 51.0 and 1,082.3 / 323.4 / 45.7 | 1,650.2 / 297.0 / 45 and 1,452.4 / 253.7 / 40 | 2,302.2 / 359.4 / 38.1 and 2,192.6 / 346.7 / 35.9 |
| 3633d376a (sets of 11 November) | 1,133.4 / 336.1 / 51.0 and 1,082.3 / 323.4 / 45.7 | 1,632.4 / 299.4 / 44 and 1,448.4 / 270.3 / 38 | 1,613.6 / 358.3 / 37.9 and 1,524.8 / 347.5 / 36.1 |
| 9f254e8d8 (sets of 9 November) | 1,187.4 / 316.2 / 47.1 and 1,172.7 / 316.6 / 45.5 | 1,511.8 / 306.1 / 43 and 1,388.6 / 292.8 / 41 | 1,582.3 / 359.4 / 38.2 and 1,514.6 / 345.3 / 35.8 |
| ae9b8c23a (sets of 8 November) | 1,228.5 / 329.2 / 49.0 and 1,204.1 / 317.6 / 45.5 | 1,488.9 / 305.9 / 43 and 1,368.8 / 292.4 / 41 | 1,756.1 / 361.5 / 38.6 and 1,673.4 / 355.9 / 36.2 |
| 9a8624af9 (sets of 4 November; Warrior threat set of 6 November) | 1,136.9 / 342.7 / 54.0 and 1,081.0 / 333.1 / 45.8 | 1,503.0 / 305.8 / 43 and 1,382.3 / 292.4 / 41 | 1,754.7 / 393.3 / 43.9 and 1,717.9 / 392.5 / 42.7 |

## Shockadin set

`search_tank.py shock` uses the same method for the Shockadin set of the Builds tab (`set_shock.json`, `log_shock.txt`). The score is damage only. The dump is the Shockadin test of feedback_run_test.go (`FEEDBACK_SHOCK=1`, `FEEDBACK_DUR=180`, full buffs). The item swap set (Manual Crowd Pummeler) does not change. On 18 November (master ad6b13af8), the search gives +0.05%, less than the 0.5% rule. Thus, the set of 11 November stays (817.6 DPS).

## Sets

| Tank | Replaced items | New items |
| --- | --- | --- |
| Protection Paladin | Premier Chevalier Shoulders, Heavy Thorium Gauntlets, Soulforge Belt, Enchanted Thorium Leggings (since 13 November), Depleted Thorium Sabatons, Ring of Awareness, Arena Grand Master, Defender's Grip Stabilizer, Dark Iron Destroyer, Force Reactive Disk, Libram of Fervor | Stockade Pauldrons, Storm Gauntlets, Sentinel's Waistguard, Cloudkeeper Legplates, Warder's Sabatons, Initiate's Signet of Ferocity, The Lion Horn of Stormwind, Bolt's Charged Eyeball, Hand of Edward the Odd, Draconian Deflector, Libram of Holy Alacrity. Until 13 November: Lightforge Spaulders, Warder's Gloves (Justicar's Gloves until 9 November), Lightforge Belt, Initiate's Signet of Vigilance, Scalding Flamehoof, Volunteer's Lucky Seal (Enriched Seal until 9 November) and Argent Defender |
| Protection Warrior | Beads of Ogre Might, Hermit's Pauldron and Mighty Armsplints (since 13 November), Hyperion Legplates, Commander's Boots, Ring of Awareness, Defender's Grip Stabilizer, Demon's Blood, Annihilator, Sacred Protector (since 12 November), Archstrike Bow (and Belt of Heroism until 9 November) | Horn of Ve'han, Stoneform Shoulders, Magically Sealed Bracers, Legplates of Valor, Sabatons of Heroism, Myrmidon's Signet, Royal Seal of Eldre'Thalas, The Lion Horn of Stormwind, Scaleguard Scimitar, Skullflame Shield, Blackcrow. Until 13 November: Grimy Metal Boots, Hand of Justice, Ironfoe and Deep Jungle Rifle. Until 12 November: Eaglehorn Long Bow. Until 11 November: Valiant's Waistguard, Boots of Valor, Initiate's Signet of Vigilance, Volunteer's Lucky Seal, Scarlet Kris (Greatflank Flayer until 6 November) and Gorewood Bow. The belt is now Girdle of Uther, the belt of the default set since 9 November |
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
- **Shockadin:** on master 8c7b5a5f5, with the ranged judgements, 814.5 DPS with the default set and 815.5 with the item pool set of 11 November (+0.1%). On master 129fcd89e, 820.6 DPS with the default set and 823.8 with the item pool set of 11 November (+0.4%). The Hand of Justice change costs the item pool set 1.2%. On masters 3633d376a and 52471a100: 820.6 and 833.8 (+1.6%).

  On master 9f254e8d8: 820.6 and 823.0 (+0.3%). On master ae9b8c23a: 846.9 and 848.6 (+0.2%). On master 8298ab833: 851.4 and 839.9 (−1.4%).
- **The Druid loses the most.** Its default set has the most PvP and reputation items.
- **The search is greedy.** It changes one slot at a time and keeps the other items. A full search of all slots together can give a slightly better set.
