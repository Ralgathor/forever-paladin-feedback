package retribution

import (
	"fmt"
	"os"
	"strconv"
	"testing"

	"github.com/wowsims/forever/sim/core"
	"github.com/wowsims/forever/sim/core/proto"
	"github.com/wowsims/forever/sim/core/stats"
)

// Level-up check: one level 60 humanoid (3,000 armor) that attacks you, fights of 15 sec +-25%, no buffs, no
// consumables, the default Retribution gear and rotation. FEEDBACK_TALENTS, FEEDBACK_HIT (base damage of the
// enemy, default 400), FEEDBACK_ITER. Prints DPS, damage taken each sec and mana spent each sec.
func TestFeedbackLevelUp(t *testing.T) {
	if os.Getenv("FEEDBACK_LEVELUP") == "" {
		t.Skip()
	}
	hit := 400.0
	if v := os.Getenv("FEEDBACK_HIT"); v != "" {
		hit, _ = strconv.ParseFloat(v, 64)
	}
	player := &proto.Player{
		Name: "Ret", Race: proto.Race_RaceHuman, Class: proto.Class_ClassPaladin,
		Equipment:     core.GetGearSet("../../../ui/specs/paladin/retribution/gear_sets", "default").GearSet,
		Consumables:   &proto.ConsumesSpec{},
		TalentsString: talentsOr(UnsealedWrathTalents),
		Spec:          DefaultSpecOptions,
		Rotation:      core.GetAplRotation("../../../ui/specs/paladin/retribution/apls", "default").Rotation,
		Buffs:         &proto.IndividualBuffs{},
		Profession1:   proto.Profession_Engineering, Profession2: proto.Profession_Blacksmithing,
		DistanceFromTarget: 5,
		InFrontOfTarget:    true,
	}
	target := &proto.Target{
		Level:         60,
		Stats:         stats.Stats{stats.Armor: 3000, stats.AttackPower: 320}.ToProtoArray(),
		MobType:       proto.MobType_MobTypeHumanoid,
		SwingSpeed:    2,
		MinBaseDamage: hit,
		DamageSpread:  0.3,
	}
	enc := &proto.Encounter{Duration: 15, DurationVariation: 3.75, ExecuteProportion_20: 0.2, ExecuteProportion_35: 0.35,
		Targets: []*proto.Target{target}}
	raid := core.SinglePlayerRaidProto(player, &proto.PartyBuffs{}, &proto.RaidBuffs{}, &proto.Debuffs{})
	raid.Tanks = append(raid.Tanks, &proto.UnitReference{Type: proto.UnitReference_Player, Index: 0})
	it := feedbackIter()
	res := core.RunRaidSim(&proto.RaidSimRequest{Raid: raid, Encounter: enc, SimOptions: &proto.SimOptions{Iterations: it, RandomSeed: 101}})
	if res.Error != nil {
		t.Fatal(res.Error.Message)
	}
	u := res.RaidMetrics.Parties[0].Players[0]
	spent := 0.0
	for _, r := range u.Resources {
		if r.Type == proto.ResourceType_ResourceTypeMana && r.Gain < 0 {
			spent -= r.Gain
		}
	}
	fmt.Printf("LEVELUP dps=%.1f dtps=%.1f mps=%.2f\n", u.Dps.Avg, u.Dtps.Avg, spent/float64(it)/15)
}
