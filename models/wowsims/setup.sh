#!/usr/bin/env bash
# Builds the wowsims Forever CLI with the proposals patch, and writes the player presets of all specs.
# Requirements: git, Go 1.24 or later, Python 3 with grpcio-tools (pip install grpcio-tools).
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
WORK="${WOWSIMS_WORK:-$HERE/.work}"
COMMIT=69e0e5b
mkdir -p "$WORK"
if [ ! -d "$WORK/forever" ]; then
  git clone https://github.com/wowsims/forever.git "$WORK/forever"
fi
cd "$WORK/forever"
git checkout -q -f "$COMMIT"
git clean -qfd sim
git apply "$HERE/proposals.patch"

# Go code for the protobuf files (the repository does not keep it).
go install google.golang.org/protobuf/cmd/protoc-gen-go@v1.36.10   # the protobuf version of go.mod
PATH="$PATH:$(go env GOPATH)/bin"
GRPC_PROTO="$(python3 -c 'import grpc_tools, os; print(os.path.join(os.path.dirname(grpc_tools.__file__), "_proto"))')"
python3 -m grpc_tools.protoc -I=./proto -I="$GRPC_PROTO" \
  --go_opt=Mgoogle/protobuf/descriptor.proto=google.golang.org/protobuf/types/descriptorpb \
  --go_out=./sim/core ./proto/*.proto

go build -tags with_db -o "$WORK/wowsimcli" ./cmd/wowsimcli

# Player presets of each test suite (gear, talents, rotation, consumables), one JSON file each.
rm -rf "$WORK/dump"
mkdir -p "$WORK/dump"
for p in paladin/retribution paladin/protection warrior/dps warrior/protection rogue hunter mage warlock priest; do
  ZZDUMP="$WORK/dump" go test -tags with_db -count=1 "./sim/$p/" > /dev/null
done
for p in druid/feralbear druid/feralcat druid/balance shaman/elemental shaman/enhancement; do
  ZZDUMP="$WORK/dump/$(echo "$p" | tr / _)" go test -tags with_db -count=1 "./sim/$p/" > /dev/null
done
echo "wowsimcli: $WORK/wowsimcli"
