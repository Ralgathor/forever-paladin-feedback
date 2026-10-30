"""Talent strings (tree order of the sim) and PROPOSE flags. See README.md for the flags."""
RET = "ClassPaladin__default__default__default__Default"   # wowsims Retribution preset (beta talents)
RB1 = "0000320302-003-05225331201330321"
RET_PROP = "C1,C15,C16,C17,C26"
# Builds of Analysis, Builds, parts 4 and 5 (calculator version 5). RB6 needs the flags BZ2,MFM3 (new talents).
RB2 = "0200320302-003-05225531001330321"
RB6 = "02003-003-05225531201330321"
SHOCK_RET = "0502320322010105--0022533120133"              # 26/0/25, before Divine Precision in row 4 (M-H5)
SHOCK_RET_DP = "0500320302013125--0022533100133"        # 28/0/23: Divine Precision 3/3, Consecrated Ground 2/2.
# Divine Grace 1/2 (filler, no damage effect) is not in the beta string: the sim string has 50 points.
PB1 = "00003-0530500321301551-5022103"                     # Julien's beta build is in data/julien_prot.json
PROT_PROP = "C6,C7,C11,C13,C14"
PT3 = "00003-0530300321301551-50215200001"                # best proposed tank, builds/protection.md
BT4b = "50003-5230513021301351-50201"                      # best beta tank, builds/protection.md
PROT_ALL = "C1,C6,C7,C11,C13,C14,C15,C16,C17,C26,VIN5"    # all proposals of the tank build search
HOLY_BETA = "05320013025101051--05"
HOLY_PROP_TALENTS = "05320013025101051--05005"             # + Conviction 5
HOLY_PROP = "C1,C15,C15H,HL30,IOL,LL20"
PRIEST = "00000503103000000-03505003030120531"
WARRIOR_TANK = "ClassWarrior__prebis__default__default__Protection"
BEAR = "druid_feralbear/ClassDruid__default__default__default__Standard"
