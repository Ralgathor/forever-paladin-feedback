#!/bin/sh
# Checks on wowsims Forever, master branch (commit 895cd67f9, 1 November 2026).
# Usage: ./run.sh <wowsims clone>. Needs Go 1.25, Python 3 with grpcio-tools, protoc-gen-go v1.36.10.
set -e
W="$1"; D="$(cd "$(dirname "$0")" && pwd)"
cd "$W"
git checkout -q 895cd67f9
git apply "$D/talents.patch" || true
git apply "$D/notes-2-november.patch" || true
git apply "$D/threat-options.patch" || true
cp "$D/proposals_sim.go" sim/paladin/
cp "$D/feedback_run_test.go" "$D/feedback_levelup_test.go" sim/paladin/retribution/
cp "$D/feedback_prot_test.go" sim/paladin/protection/feedback_run_test.go
cp "$D/feedback_warrior_test.go" sim/warrior/protection/feedback_run_test.go
cp "$D/feedback_bear_test.go" sim/druid/feralbear/
cp "$D/feedback_warrior_dps_test.go" sim/warrior/dps/feedback_dps_test.go
GRPC_PROTO="$(python3 -c 'import grpc_tools, os; print(os.path.join(os.path.dirname(grpc_tools.__file__), "_proto"))')"
python3 -m grpc_tools.protoc -I=./proto -I="$GRPC_PROTO" \
  --go_opt=Mgoogle/protobuf/descriptor.proto=google.golang.org/protobuf/types/descriptorpb --go_out=./sim/core ./proto/*.proto
cd sim/paladin/retribution
go test -tags with_db -c -o /tmp/rettest .
# Development notes of 2 November 2026: N2H, V5 (full buffs, 2 min)
for p in N2H V5 N2H,V5; do
  FEEDBACK_DUR=120 FEEDBACK_BUFFS=full PROPOSE=$p /tmp/rettest -test.run TestFeedbackRun -test.v | grep RESULT
done
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
for p in "" C1 CP1 CP1,RK100,RKICD4 CP1,RK100,RKICD4,C1 CP1,RK100,RKICD4,C1,NOTOUGH; do
  FEEDBACK_DUR=180 PROPOSE=$p /tmp/prottest -test.run TestFeedbackRun -test.v | grep -E "RESULT|TMI"
done
for n in 1 3 5; do for p in "" CP1,RK100,RKICD4,C1; do
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
