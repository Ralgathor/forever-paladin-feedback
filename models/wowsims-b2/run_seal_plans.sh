#!/bin/sh
# Seal plans and Seal pairs of Retribution (W29) on the item pool Retribution set (matched_gear/set_Retribution.json).
# Usage: ./run_seal_plans.sh <wowsims clone>. Needs /tmp/bin/rettest (tank_gear/run_pool.sh builds it). 3,000 iterations.
set -e
W="$1"; D="$(cd "$(dirname "$0")" && pwd)"
python3 "$D/seal_plans_apl.py" "$W"
IR=$(python3 -c "import json,sys;print(','.join(str(x.get('id',0)) for x in json.load(open(sys.argv[1]))['items']))" "$D/matched_gear/set_Retribution.json")
OUT="$D/logs/seal_plans_8298ab833_pool.log"
echo "# wowsims Forever master 8298ab833, item pool Retribution set. APLs of seal_plans_apl.py." > "$OUT"
job() { echo "### $*" >> "$OUT"; (cd "$W/sim/paladin/retribution" && env FEEDBACK_ITEMS=$IR "$@" /tmp/bin/rettest -test.run TestFeedbackRun -test.v 2>&1 | grep -E "RESULT|panic" >> "$OUT") || true; }
for a in fb_r1c3 fb_r1c2 fb_r2c2 fb_r1c1 fb_r3c3 fb_r3c1; do job FEEDBACK_APL=$a FEEDBACK_DUR=120 FEEDBACK_BUFFS=full; done
for a in fb_r1c3 fb_F1C3 fb_L1C3 fb_W1C3 fb_J1C3 fb_onlyC fb_F1R3 fb_R1F1 fb_R1F3 fb_onlyR fb_W1R3 fb_onlyF; do
  job FEEDBACK_APL=$a FEEDBACK_DUR=120 FEEDBACK_BUFFS=full
  job FEEDBACK_APL=$a FEEDBACK_DUR=300 FEEDBACK_BUFFS=none
done
for a in fb_r1c3 fb_F1C3 fb_W1C3; do job FEEDBACK_APL=$a FEEDBACK_DUR=300 FEEDBACK_BUFFS=lean; done
for a in fb_r1c3 fb_W1C3; do job FEEDBACK_APL=$a FEEDBACK_DUR=120 FEEDBACK_BUFFS=none; done
echo DONE >> "$OUT"
