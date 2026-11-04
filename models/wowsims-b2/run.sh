#!/bin/sh
# Checks on wowsims Forever, master branch (commit 6ee3c30f35, 4 November 2026, game files of client 1.60.1.70755).
# Usage: ./run.sh <wowsims clone>. Needs Go 1.25, Python 3 with grpcio-tools, protoc-gen-go v1.36.10.
set -e
W="$1"; D="$(cd "$(dirname "$0")" && pwd)"
cd "$W"
git checkout -q 6ee3c30f35
git apply "$D/patches/talents.patch" || true
git apply "$D/patches/notes-2-november.patch" || true
git apply "$D/patches/threat-options.patch" || true
git apply "$D/patches/burst-threat.patch" || true
cp "$D/apl/furyopen.apl.json" "$D/apl/furyopen1.apl.json" ui/specs/paladin/protection/apls/
cp "$D/apl/charge.apl.json" ui/specs/warrior/protection/apls/
cp "$D/go/proposals_sim.go" sim/paladin/
cp "$D/go/feedback_run_test.go" "$D/go/feedback_levelup_test.go" sim/paladin/retribution/
cp "$D/go/feedback_prot_test.go" sim/paladin/protection/feedback_run_test.go
cp "$D/go/feedback_warrior_test.go" sim/warrior/protection/feedback_run_test.go
cp "$D/go/feedback_bear_test.go" sim/druid/feralbear/
cp "$D/go/feedback_warrior_dps_test.go" sim/warrior/dps/feedback_dps_test.go
GRPC_PROTO="$(python3 -c 'import grpc_tools, os; print(os.path.join(os.path.dirname(grpc_tools.__file__), "_proto"))')"
python3 -m grpc_tools.protoc -I=./proto -I="$GRPC_PROTO" \
  --go_opt=Mgoogle/protobuf/descriptor.proto=google.golang.org/protobuf/types/descriptorpb --go_out=./sim/core ./proto/*.proto
cd sim/paladin/retribution
go test -tags with_db -c -o /tmp/rettest .
# Development notes of 2 November 2026: the N2H and V5 flags are for commit 895cd67f9 only.
# Commits d97252f2a and 6ee3c30f35 have both changes in the game data. Book ranks of Strength of Earth Totem and Grace of Air Totem:
FEEDBACK_BOOKTOTEMS=1 FEEDBACK_DUR=120 FEEDBACK_BUFFS=full /tmp/rettest -test.run TestFeedbackRun -test.v | grep RESULT
for b in full lean; do for d in 120 300; do for p in "" C1 UW20; do
  FEEDBACK_DUR=$d FEEDBACK_BUFFS=$b PROPOSE=$p /tmp/rettest -test.run TestFeedbackRun -test.v | grep RESULT
done; done; done
cd ../protection
go test -tags with_db -c -o /tmp/prottest .
for d in 120 180 300; do for p in "" CP1 CP1,RD20 RD20 NOTOUGH CP1,NOTOUGH CP1,RK100,RKICD4 CP1,NOTOUGH,RK100,RKICD4; do
  FEEDBACK_DUR=$d PROPOSE=$p /tmp/prottest -test.run TestFeedbackRun -test.v | grep RESULT
done; done
# Threat options after the notes of 2 November 2026 (threat-options.patch), 3 min
for e in "CP9_BV=1.0 PROPOSE=CP1,CP9" "CP9_BV=2.0 PROPOSE=CP1,CP9" "HS_THREAT=2.0 PROPOSE=CP1" "HS_THREAT=2.25 PROPOSE=CP1" \
         "HS_THREAT=2.5 PROPOSE=CP1" "CP6_ICD=2 PROPOSE=CP1,CP6A" "CP6_ICD=1 PROPOSE=CP1,CP6A" "HS_THREAT=2.0 CP9_BV=1.0 PROPOSE=CP1,CP9"; do
  env $e FEEDBACK_DUR=180 /tmp/prottest -test.run TestFeedbackRun -test.v | grep RESULT
done
cd ../../warrior/protection
go test -tags with_db -c -o /tmp/wartest .
FEEDBACK_DUR=120 /tmp/wartest -test.run TestFeedbackRun -test.v | grep RESULT
# Analysis, Threat, parts 7 and 8: 3 min, 1, 3 and 5 targets (each target hits for 1/3 of the boss when FEEDBACK_TARGETS is set)
cd ../../paladin/protection
# The C1 flag panics in this test on commits d97252f2a and 6ee3c30f35. The C1 and C-P12 (RK100) values come from commit 895cd67f9.
for p in "" CP1 CP1,NOTOUGH; do
  FEEDBACK_DUR=180 PROPOSE=$p /tmp/prottest -test.run TestFeedbackRun -test.v | grep -E "RESULT|TMI"
done
for n in 1 3 5; do for p in "" CP1; do
  FEEDBACK_DUR=180 FEEDBACK_TARGETS=$n PROPOSE=$p /tmp/prottest -test.run TestFeedbackRun -test.v | grep PERTARGET
done; done
cd ../../warrior/protection
FEEDBACK_DUR=180 /tmp/wartest -test.run TestFeedbackRun -test.v | grep -E "RESULT|TMI"
for n in 1 3 5; do FEEDBACK_DUR=180 FEEDBACK_TARGETS=$n /tmp/wartest -test.run TestFeedbackRun -test.v | grep PERTARGET; done
cd ../../druid/feralbear
go test -tags with_db -c -o /tmp/beartest .
FEEDBACK_DUR=180 /tmp/beartest -test.run TestFeedbackBear -test.v | grep RESULT
for n in 1 3 5; do FEEDBACK_DUR=180 FEEDBACK_TARGETS=$n /tmp/beartest -test.run TestFeedbackBear -test.v | grep PERTARGET; done
# Analysis, Damage, part 9: Fury and Arms, pre-raid set
cd ../../warrior/dps
go test -tags with_db -c -o /tmp/wardps .
for s in fury arms; do for d in 120 300; do
  FEEDBACK_DUR=$d FEEDBACK_SPEC=$s FEEDBACK_GEAR=prebis /tmp/wardps -test.run TestFeedbackDps -test.v | grep RESULT
done; done
# Analysis, Threat, part 8: burst threat, 3 min, threat on the boss in steps of 0.1 sec (BURST lines).
# Paladin openers: default (wowsims), furyopen (Fury opener, two Judgements at 0 sec), furyopen1 (one Judgement at 0 sec)
cd ../../paladin/protection
for a in default furyopen furyopen1; do for p in "" CP1; do
  FEEDBACK_APL=$a FEEDBACK_DUR=180 FEEDBACK_BURST="pal_${a}_${p:-live}" PROPOSE=$p /tmp/prottest -test.run TestFeedbackRun -test.v | grep -E "BURST|RESULT"
done; done
cd ../../warrior/protection
FEEDBACK_NOENG=1 FEEDBACK_DUR=180 FEEDBACK_BURST=war /tmp/wartest -test.run TestFeedbackRun -test.v | grep -E "BURST|RESULT"
FEEDBACK_NOENG=1 FEEDBACK_CHARGE=1 FEEDBACK_DUR=180 FEEDBACK_BURST=war_charge /tmp/wartest -test.run TestFeedbackRun -test.v | grep -E "BURST|RESULT"
FEEDBACK_DUR=180 FEEDBACK_BURST=war_sapper /tmp/wartest -test.run TestFeedbackRun -test.v | grep -E "BURST|RESULT"
cd ../../druid/feralbear
FEEDBACK_DUR=180 FEEDBACK_BURST=bear /tmp/beartest -test.run TestFeedbackBear -test.v | grep -E "BURST|RESULT"
# Analysis, Threat, parts 1 to 9: Righteous Fury (C25, RF_ALL=1.90) and the alternative C25a (RF_ALL=1.80).
# One boss, groups (1, 3 and 5 targets) and burst (default and Fury openers).
cd ../../paladin/protection
for rf in 1.90 1.80; do
  for p in C25 CP1,C25 CP1,NOTOUGH,C25; do
    RF_ALL=$rf FEEDBACK_DUR=180 PROPOSE=$p /tmp/prottest -test.run TestFeedbackRun -test.v | grep -E "RESULT|TMI"
  done
  for p in C25 CP1,C25; do
    for n in 1 3 5; do RF_ALL=$rf FEEDBACK_DUR=180 FEEDBACK_TARGETS=$n PROPOSE=$p /tmp/prottest -test.run TestFeedbackRun -test.v | grep PERTARGET; done
    for a in default furyopen; do
      RF_ALL=$rf FEEDBACK_APL=$a FEEDBACK_DUR=180 FEEDBACK_BURST="pal_${a}_${rf}_$p" PROPOSE=$p /tmp/prottest -test.run TestFeedbackRun -test.v | grep -E "BURST|RESULT"
    done
  done
done
