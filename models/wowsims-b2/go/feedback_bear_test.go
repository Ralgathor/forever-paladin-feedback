package feralbear

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"testing"

	"github.com/wowsims/forever/sim/core"
	"github.com/wowsims/forever/sim/core/proto"
	"google.golang.org/protobuf/encoding/protojson"
)

func TestFeedbackBear(t *testing.T) {
	if os.Getenv("FEEDBACK_DUR") == "" {
		t.Skip()
	}
	dur, _ := strconv.ParseFloat(os.Getenv("FEEDBACK_DUR"), 64)
	player := &proto.Player{
		Name: "Bear", Race: proto.Race_RaceNightElf, Class: proto.Class_ClassDruid,
		Equipment:     feedbackItems(core.GetGearSet("../../../ui/specs/druid/feralbear/gear_sets", "default").GearSet),
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
	if os.Getenv("FEEDBACK_BURST") != "" {
		enc.DurationVariation = 0 // the burst windows need the same fight length
		core.BurstStart()
	}
	if os.Getenv("FEEDBACK_LOG") != "" {
		rsr.SimOptions.Debug = true
		rsr.SimOptions.Iterations = 1
	}
	if d := os.Getenv("FEEDBACK_DUMP"); d != "" { // the request as JSON, for the wowsims links of sets/ (models/wowsims-b2/sets)
		b, _ := protojson.Marshal(rsr)
		os.WriteFile(d, b, 0644)
	}
	res := core.RunRaidSim(rsr)
	if os.Getenv("FEEDBACK_LOG") != "" {
		fmt.Println(res.Logs)
	}
	if os.Getenv("FEEDBACK_SRC") != "" {
		for _, a := range res.RaidMetrics.Parties[0].Players[0].Actions {
			thr, casts := 0.0, 0.0
			for _, tm := range a.Targets {
				thr += tm.Threat
				casts += float64(tm.Casts)
			}
			if thr != 0 {
				fmt.Printf("SRC %v threat=%.1f casts=%.2f\n", a.Id, thr/float64(rsr.SimOptions.Iterations), casts/float64(rsr.SimOptions.Iterations))
			}
		}
	}
	if os.Getenv("FEEDBACK_BURST") != "" {
		core.BurstReport(os.Getenv("FEEDBACK_BURST"), int(rsr.SimOptions.Iterations), []float64{1.5, 3, 4.5, 6, 8, 10, 15, 20, 30}, []float64{3, 6, 10})
	}
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

// feedbackItems: FEEDBACK_ITEMS is a comma list of 17 item ids (0 = empty slot), for example the pool sets of
// tank_gear/. The enchants of the default set stay on their slots.
func feedbackItems(eq *proto.EquipmentSpec) *proto.EquipmentSpec {
	v := os.Getenv("FEEDBACK_ITEMS")
	if v == "" {
		return eq
	}
	out := &proto.EquipmentSpec{}
	for i, s := range strings.Split(v, ",") {
		id, _ := strconv.Atoi(strings.TrimSpace(s))
		it := &proto.ItemSpec{Id: int32(id)}
		if i < len(eq.Items) && eq.Items[i] != nil && id != 0 {
			it.Enchant = eq.Items[i].Enchant
		}
		out.Items = append(out.Items, it)
	}
	return out
}
