"""Talent strings (tree order of the sim) and PROPOSE flags. See README.md for the flags."""
RET = "ClassPaladin__default__default__default__Default"   # wowsims Retribution preset (beta talents)
RB1 = "0000320302-003-05225331201330321"
RET_PROP = "C1,C15,C16,C17,C26"
# Builds of Analysis, Builds, parts 4 and 5 (calculator version 5). RB6 needs the flags BZ2,MFM3 (new talents).
# Version 6 adds Burning Zeal 2/2 to RB1, RB2 and SHOCK_RET_DP (flag BZ2). See Analysis, Builds, part 4.
RB2 = "0200320302-003-05225531001330321"
RB6 = "02003-003-05225531201330321"
SHOCK_RET = "0502320322010105--0022533120133"              # 26/0/25, before Divine Precision in row 4 (M-H5)
SHOCK_RET_DP = "0500320302013125--0022533100133"        # 28/0/23: Divine Precision 3/3, Consecrated Ground 2/2.
# Divine Grace 1/2 (filler, no damage effect) is not in the beta string: the sim string has 50 points.
# Calculator version 6 (Analysis, Builds, part 4). Vindication has 3 ranks (VIN3), Burning Zeal 5 ranks (BZR5).
# Burning Zeal and Measure for Measure are not in the beta string: the flags BZ<n> and MFM<n> give their ranks.
RET6 = RET_PROP + ",VIN3,BZR5"
RB1_V6 = ("0000320101-003-05205331201330321", "BZ5,MFM2")    # 7/8/36: v6p000320101-030000000000005-020533120133032152
RB2_V6 = ("02003103-003-05205331001330321", "BZ5,MFM2")      # 9/8/34: v6p2003103-030000000000005-020533100133032152
RB6_V6 = ("02003-003-05215331201330321", "BZ5,MFM3")         # 5/8/38: v6p2003-030000000000005-021533120133032153
SR28_V6 = ("0500320322012123--0022510100133", "BZ5")         # 28/0/23: v6p50032032201212302--02251010013300005
HS21_V6 = ("05003203220101--0022530100133032", "BZ5")        # 21/0/30: v6p50032032201010002--02253010013303205
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
