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
	googleproto "google.golang.org/protobuf/proto"
)

func TestFeedbackBear(t *testing.T) {
	if os.Getenv("FEEDBACK_DUR") == "" {
		t.Skip()
	}
	dur, _ := strconv.ParseFloat(os.Getenv("FEEDBACK_DUR"), 64)
	player := &proto.Player{
		Name: "Bear", Race: proto.Race_RaceNightElf, Class: proto.Class_ClassDruid,
		Equipment:     feedbackItems(core.GetGearSet("../../../ui/specs/druid/feralbear/gear_sets", "default").GearSet),
		Consumables:   feedbackConsumes(),
		TalentsString: DefaultTalents,
		Spec:          DefaultSpecOptions,
		Rotation:      core.GetAplRotation("../../../ui/specs/druid/feralbear/apls", "adaptive").Rotation,
		Buffs:         core.FullTankIndividualBuffs,
		// 18 November 2026: the same professions as the Paladin tank test (Engineering for the Goblin Sapper Charge).
		Profession1: proto.Profession_Engineering, Profession2: proto.Profession_Enchanting,
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
	feedbackPrintStats(raid)
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
			thr, casts, dmg := 0.0, 0.0, 0.0
			for _, tm := range a.Targets {
				thr += tm.Threat
				casts += float64(tm.Casts)
				dmg += tm.Damage
			}
			if thr != 0 {
				fmt.Printf("SRC %v threat=%.1f casts=%.2f damage=%.1f\n", a.Id, thr/float64(rsr.SimOptions.Iterations), casts/float64(rsr.SimOptions.Iterations), dmg/float64(rsr.SimOptions.Iterations))
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
	return feedbackEnchants(feedbackItemIds(eq))
}

// feedbackEnchants: FEEDBACK_ENCHANTS is a comma list of 17 enchant ids, one for each slot (0 = no enchant, "-" = keep
// the enchant of the set). It replaces the enchants of the set (18 November 2026: the same enchant rules for all specs,
// ../tank_gear/enchants_<tank>[_surv].json, ../matched_gear/enchants_fair.json). An empty slot takes no enchant.
func feedbackEnchants(eq *proto.EquipmentSpec) *proto.EquipmentSpec {
	v := os.Getenv("FEEDBACK_ENCHANTS")
	if v == "" {
		return eq
	}
	for i, s := range strings.Split(v, ",") {
		s = strings.TrimSpace(s)
		if i >= len(eq.Items) || eq.Items[i] == nil || s == "-" {
			continue
		}
		e, _ := strconv.Atoi(s)
		if eq.Items[i].Id == 0 {
			e = 0
		}
		eq.Items[i].Enchant = int32(e)
	}
	return eq
}

func feedbackItemIds(eq *proto.EquipmentSpec) *proto.EquipmentSpec {
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
			if eq.Items[i].Id == it.Id { // the same item: keep its random suffix
				it.RandomSuffix = eq.Items[i].RandomSuffix
			}
		}
		out.Items = append(out.Items, it)
	}
	return out
}

// feedbackConsumes: the consumables of the tank test.
// FEEDBACK_CONSUMES: "" (the sets of 4 to 16 November: the Paladin has its tank consumables, the Warrior and the Druid
// the consumables of their wowsims tests), "full" (the full threat set of 17 November, the same rules for the three tanks),
// "default" (the wowsims test consumables only). FEEDBACK_CONSUMES_JSON: a ConsumesSpec as JSON, in place of all these.
// FEEDBACK_STATS=1 prints the final stats of the tank.
func feedbackConsumes() *proto.ConsumesSpec {
	if v := os.Getenv("FEEDBACK_CONSUMES_JSON"); v != "" {
		c := &proto.ConsumesSpec{}
		if err := protojson.Unmarshal([]byte(v), c); err != nil {
			panic(err)
		}
		return c
	}
	switch os.Getenv("FEEDBACK_CONSUMES") {
	case "default":
		return DefaultConsumables
	case "full":
		return feedbackFullConsumes
	case "fullsurv": // the survival sets (18 November 2026): the full set and Greater Stoneshield Potion, the same for the three tanks
		c := googleproto.Clone(feedbackFullConsumes).(*proto.ConsumesSpec)
		c.DefensivePotId = 13455
		return c
	}
	return DefaultConsumables
}

func feedbackPrintStats(raid *proto.Raid) {
	if os.Getenv("FEEDBACK_STATS") == "" {
		return
	}
	res := core.ComputeStats(&proto.ComputeStatsRequest{Raid: raid})
	st := res.RaidStats.Parties[0].Players[0].FinalStats.Stats
	fmt.Printf("STATS str=%.0f agi=%.0f sta=%.0f int=%.0f sp=%.0f holy=%.0f ap=%.0f hit=%.1f crit=%.1f def=%.0f armor=%.0f bv=%.0f\n",
		st[proto.Stat_StatStrength], st[proto.Stat_StatAgility], st[proto.Stat_StatStamina], st[proto.Stat_StatIntellect],
		st[proto.Stat_StatSpellDamage], st[proto.Stat_StatHolyDamage], st[proto.Stat_StatAttackPower], st[proto.Stat_StatHitRating],
		st[proto.Stat_StatCritRating], st[proto.Stat_StatDefenseRating], st[proto.Stat_StatArmor], st[proto.Stat_StatBlockValue])
}

// feedbackFullConsumes: the full threat set of 17 November 2026 (the rules are in the Paladin test). The Druid test
// consumables, with Flask of the Titans, Smoked Desert Dumplings in place of Dirge's Kickin' Chimaerok Chops, Major Frenzy
// Potion, the Elixirs of Ferocity, Greater Defense and the Phalanx, Juju Power, Juju Might, R.O.I.D.S., Dragonbreath Chili
// and Rumsey Rum. A Druid weapon takes no oil or stone in Bear Form. 18 November 2026: Greater Stoneshield Potion only in
// the survival sets (FEEDBACK_CONSUMES=fullsurv), the same as the Paladin and the Warrior.
var feedbackFullConsumes = &proto.ConsumesSpec{
	FlaskId:        13510,  // Flask of the Titans
	FoodId:         20452,  // Smoked Desert Dumplings
	OffensivePotId: 250943, // Major Frenzy Potion
	ConjuredId:     9421,   // Major Healthstone
	// 28 November 2026 (wowsims dc09e002f0): one elixir for each group, and only the strongest amount of each stat counts.
	// Elixir of Ferocity, Elixir of Greater Defense and the Scrolls of Agility IV, Strength IV and Protection IV give nothing
	// next to Juju Power, R.O.I.D.S., the Mongoose and the Phalanx, thus they are removed (logs/consumables_dc09e002f0.log).
	// Elixir of the Mongoose, Elixir of the Phalanx and Gift of Arthas
	ElixirIds: []int32{13452, 250329, 9088},
	// Goblin Sapper Charge, Rumsey Rum, Juju Power, Juju Might, R.O.I.D.S. and Dragonbreath Chili
	ExtraIds: []int32{10646, 17048, 12451, 12460, 8410, 12217},
}
