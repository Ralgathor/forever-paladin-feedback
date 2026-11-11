// Prints the ids of the items with an effect that the sim implements (core.HasItemEffect), one per line.
package main

import (
	"fmt"

	"github.com/wowsims/forever/sim"
	"github.com/wowsims/forever/sim/core"
)

func main() {
	sim.RegisterAll()
	for id := int32(1); id < 400000; id++ {
		if core.HasItemEffect(id) {
			fmt.Println(id)
		}
	}
}
