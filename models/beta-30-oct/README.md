# Models on the beta of 30 October 2026

These scripts run the models of the Analysis tabs on the beta trees of 30 October 2026 (hotfix push 113554). The first three use no proposal. They use the repository models with no change.

| Script | Run | What it gives |
| --- | --- | --- |
| healing_b2.py | `python3 healing_b2.py ../healing` | Holy Paladin against the Priest, the Druid and the Shaman: raid and one tank |
| recovery_b2.py | `python3 recovery_b2.py ../healing` | Healing in the first 3 and 6 sec after a large hit on one tank |
| threat_b2.py | `python3 threat_b2.py ..` | Protection threat and mana against the Warrior and the Druid |
| holy_proposals_b2.py | `python3 holy_proposals_b2.py` | Reverence 50% (C-H1) and Lingering Light (C-H2, withdrawn) against the Druid: raid and one tank |

The inputs come from wowsims Forever, branch `paladin/hotfix-113554-port`. Each script gives its inputs at the top. The results are in Beta test results.
