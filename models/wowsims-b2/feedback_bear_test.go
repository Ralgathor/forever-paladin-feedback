package feralbear

import (
	"fmt"
	"os"
	"strconv"
	"testing"

	"github.com/wowsims/forever/sim/core"
	"github.com/wowsims/forever/sim/core/proto"
)

func TestFeedbackBear(t *testing.T) {
	if os.Getenv("FEEDBACK_DUR") == "" {
		t.Skip()
	}
	dur, _ := strconv.ParseFloat(os.Getenv("FEEDBACK_DUR"), 64)
	player := &proto.Player{
		Name: "Bear", Race: proto.Race_RaceNightElf, Class: proto.Class_ClassDruid,
		Equipment:     core.GetGearSet("../../../ui/specs/druid/feralbear/gear_sets", "default").GearSet,
		Consumables:   DefaultConsumables,
		TalentsString: DefaultTalents,
		Spec:          DefaultSpecOptions,
		Rotation:      core.GetAplRotation("../../../ui/specs/druid/feralbear/apls", "adaptive").Rotation,
		Buffs:         core.FullTankIndividualBuffs,
		DistanceFromTarget: 5,
		HealingModel:       &proto.HealingModel{BurstWindow: 6},
		InFrontOfTarget:    true,
	}
	for _, it := range player.Equipment.Items {
		if it.Id != 0 && core.GetItemByID(it.Id) == nil {
			fmt.Printf("DROP %d\n", it.Id)
			it.Id = 0; it.Enchant = 0
		}
	}
	enc := core.MakeSingleTargetEncounter(5)
	enc.Duration = dur
	ntg := 1
	if v := os.Getenv("FEEDBACK_TARGETS"); v != "" {
		ntg, _ = strconv.Atoi(v)
		t0 := core.FreshDefaultTargetConfig()
		t0.MinBaseDamage *= 1.0 / 3
		enc.Targets = nil
		for i := 0; i < ntg; i++ {
			enc.Targets = append(enc.Targets, t0)
		}
	}
	raid := core.SinglePlayerRaidProto(player, core.FullPartyBuffs, core.FullRaidBuffs, core.FullDebuffs)
	raid.Tanks = append(raid.Tanks, &proto.UnitReference{Type: proto.UnitReference_Player, Index: 0})
	rsr := &proto.RaidSimRequest{Raid: raid, Encounter: enc, SimOptions: &proto.SimOptions{Iterations: 3000, RandomSeed: 101}}
	res := core.RunRaidSim(rsr)
	if res.Error != nil {
		t.Fatal(res.Error.Message)
	}
	u := res.RaidMetrics.Parties[0].Players[0]
	per := make([]float64, ntg)
	for _, a := range u.Actions {
		for _, tm := range a.Targets {
			if int(tm.UnitIndex) < ntg {
				per[tm.UnitIndex] += tm.Threat / 3000 / dur
			}
		}
	}
	fmt.Printf("PERTARGET %v\n", per)
	var casts, crush float64
	for _, a := range res.EncounterMetrics.Targets[0].Actions {
		for _, tm := range a.Targets {
			crush += float64(tm.Crushes)
			casts += float64(tm.Casts)
		}
	}
	tmi := 0.0
	if u.Tmi != nil {
		tmi = u.Tmi.Avg
	}
	fmt.Printf("RESULT druid dur=%.0f tps=%.1f dtps=%.1f tmi=%.2f crush=%.1f%%\n", dur, u.Threat.Avg, u.Dtps.Avg, tmi, 100*crush/casts)
}
