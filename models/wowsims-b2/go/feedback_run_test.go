package retribution

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"testing"

	"github.com/wowsims/forever/sim/core"
	"github.com/wowsims/forever/sim/core/proto"
	"github.com/wowsims/forever/sim/core/stats"
	googleproto "google.golang.org/protobuf/proto"
)

// FEEDBACK_DUR (sec), FEEDBACK_BUFFS (full|lean|none), FEEDBACK_SHOCK (Holy Shock build), PROPOSE flags. Prints DPS, time to OOM and sec OOM.
func TestFeedbackRun(t *testing.T) {
	if os.Getenv("FEEDBACK_DUR") == "" {
		t.Skip()
	}
	dur, _ := strconv.ParseFloat(os.Getenv("FEEDBACK_DUR"), 64)
	raid, party, indiv := core.FullRaidBuffs, core.FullPartyBuffs, core.FullIndividualBuffs
	if os.Getenv("FEEDBACK_BUFFS") == "lean" {
		raid = &proto.RaidBuffs{MarkOfTheWild: true, BattleShout: 1}
		party = &proto.PartyBuffs{}
		indiv = &proto.IndividualBuffs{GreaterBlessingOfKings: true, GreaterBlessingOfWisdom: 1, GreaterBlessingOfMight: 1}
	}
	if os.Getenv("FEEDBACK_BOOKTOTEMS") != "" { // rank 2: the Ruins of Ahn'Qiraj book ranks of Strength of Earth and Grace of Air
		rb := googleproto.Clone(raid).(*proto.RaidBuffs)
		rb.StrengthOfEarthTotem, rb.GraceOfAirTotem = 2, 2
		raid = rb
	}
	debuffs, cons := core.FullDebuffs, DefaultConsumables
	gear, apl, talents := "default", envOr("FEEDBACK_APL", "default"), UnsealedWrathTalents
	var swap *proto.ItemSwap
	if os.Getenv("FEEDBACK_SHOCK") != "" { // the wowsims shockadinSuite: Holy Shock set, item swap set, APL and consumables
		gear, apl, talents = "holy_shock", "holy_shock", HolyShockTalents
		swap = core.GetItemSwapGearSet("../../../ui/specs/paladin/retribution/gear_sets", "holy_shock_item_swap").ItemSwap
		c := googleproto.Clone(DefaultConsumables).(*proto.ConsumesSpec)
		c.ElixirIds[0] = 8423  // Cerebral Cortex Compound
		c.SwapMhImbueId = 3829 // Frost Oil
		cons = c
	}
	if os.Getenv("FEEDBACK_BUFFS") == "none" { // fresh level 60: no buffs, no debuffs, no consumables
		raid, party, indiv = &proto.RaidBuffs{}, &proto.PartyBuffs{}, &proto.IndividualBuffs{}
		debuffs, cons = &proto.Debuffs{}, &proto.ConsumesSpec{}
	}
	player := &proto.Player{
		Name: "Ret", Race: proto.Race_RaceHuman, Class: proto.Class_ClassPaladin,
		Equipment:     core.GetGearSet("../../../ui/specs/paladin/retribution/gear_sets", gear).GearSet,
		Consumables:   cons,
		TalentsString: talentsOr(talents),
		Spec:          DefaultSpecOptions,
		Rotation:      core.GetAplRotation("../../../ui/specs/paladin/retribution/apls", apl).Rotation,
		ItemSwap:       swap,
		EnableItemSwap: swap != nil,
		BonusStats:    feedbackBonus(),
		Buffs:         indiv,
		Profession1:   proto.Profession_Engineering, Profession2: proto.Profession_Blacksmithing,
		DistanceFromTarget: 25,
	}
	enc := core.MakeSingleTargetEncounter(5)
	enc.Duration = dur
	rsr := &proto.RaidSimRequest{
		Raid:       core.SinglePlayerRaidProto(player, party, raid, debuffs),
		Encounter:  enc,
		SimOptions: &proto.SimOptions{Iterations: feedbackIter(), RandomSeed: 101},
	}
	res := core.RunRaidSim(rsr)
	if res.Error != nil {
		t.Fatal(res.Error.Message)
	}
	u := res.RaidMetrics.Parties[0].Players[0]
	fmt.Printf("RESULT dur=%.0f buffs=%s propose=%q dps=%.1f tto=%.1f oom=%.1f\n", dur, os.Getenv("FEEDBACK_BUFFS"),
		os.Getenv("PROPOSE"), u.Dps.Avg, u.Tto.Avg, u.SecondsOomAvg)
}

func talentsOr(d string) string {
	if v := os.Getenv("FEEDBACK_TALENTS"); v != "" {
		return v
	}
	return d
}

// FEEDBACK_ITER: iterations (default 3000). FEEDBACK_BONUS: bonus stats "index:value,..." (proto Stat order).
func feedbackIter() int32 {
	if v := os.Getenv("FEEDBACK_ITER"); v != "" {
		n, _ := strconv.Atoi(v)
		return int32(n)
	}
	return 3000
}

func feedbackBonus() *proto.UnitStats {
	v := os.Getenv("FEEDBACK_BONUS")
	if v == "" {
		return nil
	}
	st := make([]float64, stats.SimStatsLen)
	for _, kv := range strings.Split(v, ",") {
		p := strings.SplitN(kv, ":", 2)
		i, _ := strconv.Atoi(p[0])
		x, _ := strconv.ParseFloat(p[1], 64)
		st[i] += x
	}
	return &proto.UnitStats{Stats: st}
}

func envOr(k, d string) string {
	if v := os.Getenv(k); v != "" {
		return v
	}
	return d
}
