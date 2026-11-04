#!/bin/sh
# Tank and Retribution jobs of logs/checks_8298ab833.log again, with the item pool sets (FEEDBACK_ITEMS):
# the tank sets of this folder and the Retribution set of ../matched_gear (set_Retribution.json).
# Usage: ./run_pool.sh <wowsims clone> [surv]. Set up the clone first with ../run.sh (master commit 8298ab833).
# With "surv", the tank jobs use the survival tank sets (set_*_surv.json) and write checks_8298ab833_pool_surv.log (no R jobs).
set -e
W="$1"; V="${2:+_$2}"; D="$(cd "$(dirname "$0")/.." && pwd)"
cp "$D/go/feedback_prot_test.go" "$W/sim/paladin/protection/feedback_run_test.go"
cp "$D/go/feedback_warrior_test.go" "$W/sim/warrior/protection/feedback_run_test.go"
cp "$D/go/feedback_bear_test.go" "$W/sim/druid/feralbear/"
cp "$D/go/feedback_run_test.go" "$W/sim/paladin/retribution/feedback_run_test.go"
(cd "$W/sim/paladin/retribution" && go test -tags with_db -c -o /tmp/bin/rettest .)
(cd "$W/sim/paladin/protection" && go test -tags with_db -c -o /tmp/prottest .)
(cd "$W/sim/warrior/protection" && go test -tags with_db -c -o /tmp/wartest .)
(cd "$W/sim/druid/feralbear" && go test -tags with_db -c -o /tmp/beartest .)
ids() { python3 -c "import json,sys;print(','.join(map(str,json.load(open(sys.argv[1])))))" "$D/tank_gear/$1"; }
IR=$(python3 -c "import json,sys;print(','.join(str(x.get('id',0)) for x in json.load(open(sys.argv[1]))['items']))" "$D/matched_gear/set_Retribution.json")
IP=$(ids set_prot$V.json); IW=$(ids set_war$V.json); ID=$(ids set_bear$V.json)
OUT="$D/logs/checks_8298ab833_pool$V.log"
echo "# wowsims Forever master 8298ab833, item pool sets${2:+, $2 tank sets} (FEEDBACK_ITEMS). Tank and Retribution jobs of checks_8298ab833.log." > "$OUT"
J="PWDR"; [ -n "$V" ] && J="PWD"
grep "^### [$J] " "$D/logs/checks_8298ab833.log" | while IFS= read -r line; do
  t=$(echo "$line" | sed 's/^### \(.\) | .*/\1/'); e=$(echo "$line" | sed 's/^### . | //')
  case $t in
    P) b=/tmp/prottest; dir=sim/paladin/protection; r=TestFeedbackRun; I=$IP;;
    W) b=/tmp/wartest; dir=sim/warrior/protection; r=TestFeedbackRun; I=$IW;;
    R) b=/tmp/bin/rettest; dir=sim/paladin/retribution; r=TestFeedbackRun; I=$IR;;
    D) b=/tmp/beartest; dir=sim/druid/feralbear; r=TestFeedbackBear; I=$ID;;
  esac
  echo "$line" >> "$OUT"
  (cd "$W/$dir" && env FEEDBACK_ITEMS=$I $e $b -test.run $r -test.v 2>&1 | grep -E "RESULT|TMI|PERTARGET|BURST|panic" >> "$OUT") || true
done
# Extra job for Analysis, Crushing blows, part 3 (normal boss, C-P1 with 4-20%, no Toughness)
echo "### P | FEEDBACK_DUR=180 PROPOSE=CP1,RD20,NOTOUGH" >> "$OUT"
(cd "$W/sim/paladin/protection" && env FEEDBACK_ITEMS=$IP FEEDBACK_DUR=180 PROPOSE=CP1,RD20,NOTOUGH /tmp/prottest -test.run TestFeedbackRun -test.v 2>&1 | grep -E "RESULT|TMI" >> "$OUT")
echo DONE >> "$OUT"
