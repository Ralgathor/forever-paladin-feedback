# Models on the beta of 30 October 2026

These scripts run the models of the Analysis tabs on the live trees (hotfix push 113554, beta of 30 October 2026). The first three use no proposal. They use the repository models with no change. Run each script from any folder, with no argument. Each script also takes the path of its model folder (`../healing`, `../damage` or `..`) as an argument. The healing scripts need numpy and scipy: `pip install -r requirements.txt` in the root folder.

| Script | Run | What it gives |
| --- | --- | --- |
| healing_b2.py | `python3 healing_b2.py` | Holy Paladin against the Priest, the Druid and the Shaman: raid and one tank |
| recovery_b2.py | `python3 recovery_b2.py` | Healing in the first 3 and 6 sec after a large hit on one tank |
| threat_b2.py | `python3 threat_b2.py` | Protection threat and mana against the Warrior and the Druid |
| mana_tables_b2.py | `python3 mana_tables_b2.py` | All Protection tables of Analysis, Mana: income, gear tiers, Consecration, talents, Sanctified Judgement by rank and Lay on Hands |
| threat_tables_b2.py | `python3 threat_tables_b2.py` | All tables of Analysis, Threat: beta and proposed Paladin, gear tiers, flatter gear and groups of enemies |
| holy_proposals_b2.py | `python3 holy_proposals_b2.py` | Reverence 50% (C-H1, proposal since 2 November) and Lingering Light (C-H2, withdrawn) against the Druid: raid and one tank |
| light_vigil_ch7.py | `python3 light_vigil_ch7.py` | Light's Vigil (C-H7): raid and one tank against the Druid and the Shaman, with and without Reverence 50% (C-H1). Party heal % and cooldown options, group burst |
| oath_light_ch8.py | `python3 oath_light_ch8.py` | Oath of Light (C-H8): 20/25/30/35% in place of the flat values, with C-H1 and C-H7. One tank against the Druid, the Shaman and the Priest, raid, maximum, recovery after a large hit, the Oath bonus by healing power, the HB1 and HB2 values, the talent value, healing for each mana point and the case where Healing Light and Oath of Light add |
| retribution_b2.py | `python3 retribution_b2.py` | Retribution with Unsealed Wrath: Holy Strike Seal trigger (C1, withdrawn on 2 November 2026), Burning Zeal (C-R4), Seal plans and mana (W29), against the pure average. Start value: wowsims of 1 November (906 DPS), build 14/6/31 |
| damage_tables_b2.py | `python3 damage_tables_b2.py` | Analysis, Damage: stats, sources, increase with gear, % of Fury, the C1 review, Judgement of the Crusader and stat values |
| pvp_burst_b2.py | `python3 pvp_burst_b2.py` | PvP burst in one Hammer of Justice stun, and Reckoning charges in PvP (W6), beta and proposed |
| healing_sens_b2.py | `python3 healing_sens_b2.py` | Analysis, Healing, parts 5, 6 and 9: cost values, Holy Power cases and limits. NOTES_OFF=1 runs it without the development notes of 2 November |
| holy_builds_b2.py | `python3 holy_builds_b2.py` | builds/holy.md: the value of each healing talent and the stat weights of HB1 (model) |
| threat_options_b2.py | `python3 threat_options_b2.py` | Threat options after the development notes of 2 November (not proposals): % of the Warrior at each gear tier |

The talent and spell inputs come from wowsims Forever (branch `paladin/hotfix-113554-port`, 30 October 2026). The wowsims start values (Retribution DPS, Protection TPS) come from master commit `895cd67f9` (1 November 2026, models/wowsims-b2). Each script gives its inputs at the top. The results are in Beta test results and in the Analysis tabs.
