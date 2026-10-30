# wowsims check

These scripts run the [wowsims Forever](https://github.com/wowsims/forever) simulator with the proposals. They check the Python models of this folder (damage, threat, healing). The Python models give the explanation. wowsims gives a second calculation with the full rules of the game.

## Setup

Requirements: git, Go 1.25 or later, Python 3, and grpcio-tools (`pip install grpcio-tools`).

```
./setup.sh
```

The script does these steps:

1. It clones wowsims Forever at commit `69e0e5b` into `.work/forever`. Set `WOWSIMS_WORK` to use a different folder.
2. It applies `proposals.patch`. The patch adds the proposals to the sim. Each proposal is off until you set its flag.
3. It makes the Go code of the protobuf files and builds the `wowsimcli` program.
4. It writes the player presets of each spec (gear, talents, rotation, consumables) to `.work/dump`.

A new wowsims commit can change the results. Change the commit in `setup.sh` only with a new check of all results.

## Scripts

| Script | What it gives | Analysis tab |
| --- | --- | --- |
| `run_damage.py` | Retribution against the other damage specs, and the value of each Retribution proposal. The new talents (Burning Zeal, Measure for Measure), RB6, Shock-Retribution and the Retribution tank, with the Holy Shock rotation (`data/shock_ret.apl.json`) | Damage, parts 10 and 11. Builds, parts 4 and 5 |
| `run_threat.py` | Protection against the Warrior and the Druid, with tuned values of Holy Shield and Iron Creed. The best tank builds with their pre-raid gear (`data/tank_path_gear.json`), and groups of 3 and 5 enemies. Epic shields use the Wowhead Forever block value (`WOWHEAD_BV` in `wowsims.py`). `WOWHEAD_BV=0` gives the wowsims values | Threat, parts 7 and 8 |
| `run_healing.py` | Holy Paladin and Holy Priest, one heal plan each: healing for each point of mana | Healing, part 9 |
| `tests.py` | One check for each proposal in the patch. The result must show the proposal text | — |
| `check.py` | The same values from the Python models and from wowsims, and the difference | Damage, Threat, Healing |

The scripts keep each sim result in `.work/out`. A new request or a new flag list starts a new sim. If you change the patch, delete `.work/out`.

`check.py` marks a difference above 5% with "check". The Analysis tab must explain each "check" value.

## Flags

Set the flags in the `PROPOSE` environment variable, with commas: `PROPOSE=C6,C14,HSBV150`. The scripts set the flags for you. The flags keep the proposal numbers of the first version of the patch.

| Flag | Proposal | Change in the sim |
| --- | --- | --- |
| `C1` | Reverence (C-H1) | 17/33/50% of the Spirit regeneration continues during casts |
| `C6` | Redoubt (C-P1) | Each Holy Shield cast gives Redoubt at full stacks (more blocks, no crushing blows) |
| `C7` | Iron Creed (C-P2) | Righteous Fury decreases all damage taken by the Iron Creed value |
| `IC<n>` | Iron Creed (C-P2) | With `C7`: Iron Creed at n% |
| `C11` | Reckoning (C-P6) | Reckoning charges also from blocks, dodges and parries (one time each 4 sec), and from critical hits |
| `C13` | Shield Specialization (C-P8) | Each block restores 2/4/6% of maximum mana, one time each 2 sec |
| `C14` | Holy Shield (C-P9) | Holy Shield damage adds a part of block value |
| `HSBV<n>` | Holy Shield (C-P9) | With `C14`: n% of block value (default 100) |
| `C15` | Conviction (C-R1) | Conviction critical chance on melee and spell damage |
| `C15H` | Conviction (C-R1) | With `C15`: Conviction also on Holy Light, Flash of Light and Holy Shock heals |
| `C16` | Holy Strike Seal trigger (C1) | Holy Strike triggers the active Seal (Seal of Fury, Seal of Command, Seal of Righteousness) |
| `C17` | Twist of Light (C-R2) | The Seal Echo has a duration, and Holy Strike refreshes it |
| `ECHO<n>` | Twist of Light (C-R2) | With `C17`: Echo duration of n sec |
| `C26` | Sanctified Judgement (C-R3) | The mana return occurs on each Judgement |
| `SA10` | Sacred Arbiter | Holy Strike damage +10%, not the beta value |
| `HL30` | Healing Light (C-H4) | Healing Light 10/20/30% on Holy Light, Flash of Light and Holy Shock |
| `IOL` | Infusion of Light (C-H3) | Each Flash of Light, Holy Shock and Holy Strike hit gives Infusion of Light, with no critical hit necessary |
| `LL<n>` | Lingering Light (C-H2) | Each critical heal heals n% more in 3 ticks of 2 sec. Ticks can be critical heals |
| `BOL` | Blessing of Light (C3) | The Blessing of Light heal bonus on the target. The wowsims buff does not add the bonus |
| `VIN5` | Vindication (C-P3) | Vindication has 5 ranks: +1% Attack Power for each rank |
| `BZ<n>` | Burning Zeal (C-R4) | n ranks: the critical damage bonus of Seals, Judgements and Holy Strike increases by 10% for each rank |
| `MFM<n>` | Measure for Measure (C-R5) | n ranks: a dodge or parry of a melee attack decreases the remaining Judgement cooldown by n sec |

`builds.py` gives the talent strings and the flag lists of each spec. The new talents of calculator version 5 are not in the beta talent string. The flags `BZ<n>` and `MFM<n>` give their ranks. Divine Grace and Merciful Light have no damage effect and no flag. A talent string uses the tree order of the sim, not the order of the game client.

## Limits

- The sim heals only the caster. It has no overhealing. Thus, the healing values are raw healing.
- The Druid has no heal spells in wowsims. The Shaman heal file is not part of the build. Thus, only the Paladin and the Priest have heal results.
- The Holy plans use one target and one or two spells. Holy Shock, Divine Favor and Light's Vigil are not in the plans.
- A Priest plan with one spell has no Litany of Light return. The Python model uses the return on about 80% of the casts.
