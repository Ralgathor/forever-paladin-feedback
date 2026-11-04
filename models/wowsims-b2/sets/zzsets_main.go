// zzsets makes a wowsims link for each default set that the threat and builds sims use.
// Steps: run the feedback tests (models/wowsims-b2/go) with FEEDBACK_DUMP=<dir>/<file>.json and no
// PROPOSE flag (see README.md), copy this file to cmd/zzsets/main.go, then:
// go run -tags with_db ./cmd/zzsets <dir> jobs.json
// It prints the links as JSON, decodes each link, runs it again and prints DPS and TPS as a check.
package main

import (
	"bytes"
	"compress/zlib"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"io"
	"os"

	"github.com/wowsims/forever/sim"
	"github.com/wowsims/forever/sim/core"
	"github.com/wowsims/forever/sim/core/proto"
	"google.golang.org/protobuf/encoding/protojson"
	googleProto "google.golang.org/protobuf/proto"
)

type job struct {
	Name string `json:"name"`
	File string `json:"file"`
	Path string `json:"path"`
}

func main() {
	dir := os.Args[1]
	var jobs []*job
	b, _ := os.ReadFile(os.Args[2])
	if err := json.Unmarshal(b, &jobs); err != nil {
		panic(err)
	}
	sim.RegisterAll()
	out := []map[string]string{}
	for _, j := range jobs {
		raw, err := os.ReadFile(dir + "/" + j.File)
		if err != nil {
			panic(err)
		}
		r := &proto.RaidSimRequest{}
		if err := protojson.Unmarshal(raw, r); err != nil {
			panic(err)
		}
		p := r.Raid.Parties[0].Players[0]
		s := &proto.IndividualSimSettings{
			ApiVersion: 2,
			Settings:   &proto.SimSettings{Iterations: 3000},
			RaidBuffs:  r.Raid.Buffs,
			PartyBuffs: r.Raid.Parties[0].Buffs,
			Debuffs:    r.Raid.Debuffs,
			Tanks:      r.Raid.Tanks,
			Player:     p,
			Encounter:  r.Encounter,
		}
		bin, err := googleProto.Marshal(s)
		if err != nil {
			panic(err)
		}
		var buf bytes.Buffer
		w := zlib.NewWriter(&buf)
		w.Write(bin)
		w.Close()
		enc := base64.StdEncoding.EncodeToString(buf.Bytes())
		url := "https://www.wowsims.com/forever/" + j.Path + "/#" + enc
		// Check: decode the link and run it.
		zr, _ := zlib.NewReader(bytes.NewReader(buf.Bytes()))
		bin2, _ := io.ReadAll(zr)
		s2 := &proto.IndividualSimSettings{}
		if err := googleProto.Unmarshal(bin2, s2); err != nil {
			panic(err)
		}
		req := &proto.RaidSimRequest{
			Raid:       &proto.Raid{Buffs: s2.RaidBuffs, Debuffs: s2.Debuffs, Tanks: s2.Tanks, Parties: []*proto.Party{{Players: []*proto.Player{s2.Player}, Buffs: s2.PartyBuffs}}},
			Encounter:  s2.Encounter,
			SimOptions: &proto.SimOptions{Iterations: 3000, RandomSeed: 101},
		}
		res := core.RunRaidSim(req)
		if res.Error != nil {
			fmt.Fprintln(os.Stderr, j.Name, res.Error.Message)
			continue
		}
		m := res.RaidMetrics.Parties[0].Players[0]
		fmt.Fprintf(os.Stderr, "%s DPS %.1f TPS %.1f\n", j.Name, m.Dps.Avg, m.Threat.Avg)
		out = append(out, map[string]string{"name": j.Name, "url": url})
	}
	o, _ := json.MarshalIndent(out, "", " ")
	fmt.Println(string(o))
}
