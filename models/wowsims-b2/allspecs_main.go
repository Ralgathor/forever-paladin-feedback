// All damage specs on the current wowsims (Analysis, Damage, part 7). Run from the wowsims clone:
//  1. Dump the "Average-Default" request of each spec test suite: add to sim/core/test_suite.go (TestDPS, before RunRaidSim)
//     a write of protojson.Marshal(rsr) to $ZZDUMP/<testName>.json, then run each spec test with ZZDUMP=/tmp/zzdump.
//  2. Copy this file to cmd/zzrun/main.go, build with -tags with_db, and run:
//     PREBIS=1 NOCONS=1 GEARFIX=1 WARGEAR=prebis_fury zzrun run
//     PREBIS: Balance pre-raid set. NOCONS: no consumables (class weapon items stay). GEARFIX: raid and PvP items out.
//     WARGEAR: the Warrior gear set. SWAP: Ret and Warrior armor swap. All runs: Ret raid buffs, 2 min, 3,000 iterations.
package main

import (
	"fmt"
	"os"
	"path/filepath"
	"sort"
	"strings"

	"github.com/wowsims/forever/sim"
	"github.com/wowsims/forever/sim/core"
	"github.com/wowsims/forever/sim/core/proto"
	"google.golang.org/protobuf/encoding/protojson"
)

func load(f string) *proto.RaidSimRequest {
	b, _ := os.ReadFile(f)
	r := &proto.RaidSimRequest{}
	if err := protojson.Unmarshal(b, r); err != nil { panic(err) }
	return r
}

func main() {
	sim.RegisterAll()
	ret := load("/tmp/zzdump/TestRetribution-Average-Default.json")
	files, _ := filepath.Glob("/tmp/zzdump/*.json")
	sort.Strings(files)
	mode := os.Args[1]
	war := load("/tmp/zzdump/TestDpsWarrior-Average-Default.json")
	if os.Getenv("SWAP") != "" {
		a := ret.Raid.Parties[0].Players[0].Equipment.Items
		b := war.Raid.Parties[0].Players[0].Equipment.Items
		for i := 0; i < 13; i++ { a[i], b[i] = b[i], a[i] }
		files = []string{"ret", "war"}
	}
	for _, f := range files {
		var r *proto.RaidSimRequest
		if f == "ret" { r = ret } else if f == "war" { r = war } else { r = load(f) }
		p := r.Raid.Parties[0].Players[0]
		if mode == "names" {
			var n []string
			for _, it := range p.Equipment.Items {
				if i := core.GetItemByID(it.Id); i != nil { n = append(n, i.Name) }
			}
			fmt.Println(filepath.Base(f), "|", strings.Join(n, "; "))
			continue
		}
		if strings.Contains(f, "Balance") && os.Getenv("PREBIS") != "" {
			p.Equipment = core.GetGearSet("/tmp/wowsims-forever/ui/specs/druid/balance/gear_sets", "prebis").GearSet
		}
		if w := os.Getenv("WARGEAR"); w != "" && strings.Contains(f, "DpsWarrior") {
			p.Equipment = core.GetGearSet("/tmp/wowsims-forever/ui/specs/warrior/dps/gear_sets", w).GearSet
		}
		if os.Getenv("ONLY") != "" && !strings.Contains(f, os.Getenv("ONLY")) { continue }
		if os.Getenv("NOCONS") != "" {
			c := p.Consumables
			n := &proto.ConsumesSpec{}
			if c != nil {
				n.MhWeaponImbueId = c.MhWeaponImbueId
				n.OhWeaponImbueId = c.OhWeaponImbueId
			}
			p.Consumables = n
		}
		if os.Getenv("GEARFIX") != "" {
			fix := map[string]map[int32]int32{
				"DpsWarrior": {18404: 22150, 18821: 19325, 12798: 17016, 19491: 22150},
				"FeralCat":   {18404: 22150},
				"Hunter":     {19618: 22150, 19619: 22150, 19620: 22150},
				"Affliction": {19518: 272406}, "Demonology": {19518: 272406}, "Destruction": {19518: 272406},
				"Elemental":  {19147: 272406, 20047: 18405},
				"Arcane":     {23057: 22149, 21415: 272413, 18543: 272407, 18820: 272438, 19379: 270225, 23451: 22379, 19366: 15968},
			}
			for _, k := range []string{"Fire", "Frost", "FFB"} { fix[k] = fix["Arcane"] }
			for k, m := range fix {
				if !strings.Contains(f, k) { continue }
				for _, it := range p.Equipment.Items {
					if n, ok := m[it.Id]; ok { it.Id = n; it.RandomSuffix = 0 }
				}
			}
			for _, it := range p.Equipment.Items {
				if i := core.GetItemByID(it.Id); i != nil && (it.Id == 18404 || it.Id == 18821 || it.Id == 18820 || it.Id == 19379 || it.Id == 23057 || it.Id == 19147 || it.Id == 20047 || it.Id == 23451 || it.Id == 19366 || it.Id == 21415 || it.Id == 18543 || it.Id == 19518 || it.Id == 19618 || it.Id == 19619 || it.Id == 19620) {
					fmt.Println("  LEFT", f, i.Name)
				}
			}
		}
		r.Raid.Buffs = ret.Raid.Buffs
		r.Raid.Debuffs = ret.Raid.Debuffs
		r.Raid.Parties[0].Buffs = ret.Raid.Parties[0].Buffs
		p.Buffs = ret.Raid.Parties[0].Players[0].Buffs
		r.Encounter.Duration = 120
		r.Encounter.DurationVariation = 5
		r.SimOptions.Iterations = 3000
		res := core.RunRaidSim(r)
		if res.Error != nil { fmt.Println(filepath.Base(f), "ERR", res.Error.Message); continue }
		fmt.Printf("%-45s %8.1f\n", filepath.Base(f), res.RaidMetrics.Dps.Avg)
	}
}
