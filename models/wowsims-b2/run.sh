#!/bin/sh
# Retribution checks on wowsims Forever, branch paladin/hotfix-113554-port (commit db28d84a8).
# Usage: ./run.sh <wowsims clone>. Needs Go 1.25, Python 3 with grpcio-tools, protoc-gen-go v1.36.10.
set -e
W="$1"; D="$(cd "$(dirname "$0")" && pwd)"
cd "$W"
git checkout -q db28d84a8
git apply "$D/talents.patch" || true
cp "$D/proposals_sim.go" sim/paladin/
cp "$D/feedback_run_test.go" sim/paladin/retribution/
GRPC_PROTO="$(python3 -c 'import grpc_tools, os; print(os.path.join(os.path.dirname(grpc_tools.__file__), "_proto"))')"
python3 -m grpc_tools.protoc -I=./proto -I="$GRPC_PROTO" \
  --go_opt=Mgoogle/protobuf/descriptor.proto=google.golang.org/protobuf/types/descriptorpb --go_out=./sim/core ./proto/*.proto
cd sim/paladin/retribution
go test -tags with_db -c -o /tmp/rettest .
for b in full lean; do for d in 120 180 300; do for p in "" C1 BZ C1,BZ UW20 C1,BZ,UW20; do
  FEEDBACK_DUR=$d FEEDBACK_BUFFS=$b PROPOSE=$p /tmp/rettest -test.run TestFeedbackRun -test.v | grep RESULT
done; done; done
