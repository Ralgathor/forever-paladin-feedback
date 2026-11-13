package paladin

import (
	"os"
	"strconv"
	"strings"
	"time"

	"github.com/wowsims/forever/sim/core"
	"github.com/wowsims/forever/sim/core/stats"
)

// Proposal flags for the feedback checks (PROPOSE=C1,BZ,UW20). Off by default.
func proposeFlag(f string) bool {
	for _, p := range strings.Split(os.Getenv("PROPOSE"), ",") {
		if p == f {
			return true
		}
	}
	return false
}

func (paladin *Paladin) applySimProposals() {
	// C25 Righteous Fury: all threat +90% (RF_ALL, default 1.90) in place of +33%. The Holy part (+90% more) does not change.
	// The sim tank always has Righteous Fury, thus a static multiplier gives the same result.
	if proposeFlag("C25") {
		rf := 1.90
		if v, err := strconv.ParseFloat(os.Getenv("RF_ALL"), 64); err == nil {
			rf = v
		}
		paladin.PseudoStats.ThreatMultiplier *= rf / 1.33
	}

	// W15 balance lever: Sacred Arbiter Holy Strike bonus +10% (SA10) or +0% (SA0) in place of +20%.
	if paladin.Talents.SacredArbiter && (proposeFlag("SA10") || proposeFlag("SA0")) {
		mult := 1.10 / 1.20
		if proposeFlag("SA0") {
			mult = 1.0 / 1.20
		}
		paladin.AddStaticMod(core.SpellModConfig{
			Kind:       core.SpellMod_DamageDone_Pct,
			ClassMask:  SpellMaskHolyStrike,
			FloatValue: mult - 1,
		})
	}

	// C-H1 Reverence 25/50% (REV50): +10% of the mana regeneration during casts for each rank (live: 15/30%).
	if proposeFlag("REV50") && paladin.Talents.Reverence > 0 {
		paladin.PseudoStats.SpiritRegenRateCasting += 0.10 * float64(paladin.Talents.Reverence)
	}

	// C-H7 Light's Vigil (CH7), the enemy part: Holy Shock, Judgement and Holy Strike give a stack for 30 sec, once each
	// 6 sec, up to 3 stacks. A Holy Shock cast uses one stack and then incurs no cooldown. The party heal is not modeled.
	if proposeFlag("CH7") && paladin.Talents.LightsVigil {
		stacks := paladin.RegisterAura(core.Aura{
			Label:     "CH7 Light's Vigil stacks" + paladin.Label,
			ActionID:  core.ActionID{SpellID: 1311595, Tag: 7},
			Duration:  30 * time.Second,
			MaxStacks: 3,
		})
		icd := core.Cooldown{Timer: paladin.NewTimer(), Duration: 6 * time.Second}
		core.MakePermanent(paladin.RegisterAura(core.Aura{
			Label: "CH7 Light's Vigil trigger" + paladin.Label,
			OnCastComplete: func(aura *core.Aura, sim *core.Simulation, spell *core.Spell) {
				if spell.Matches(SpellMaskHolyShock) && stacks.IsActive() && stacks.GetStacks() > 0 {
					stacks.RemoveStack(sim)
					spell.CD.Reset()
					if spell.SharedCD.Timer != nil {
						spell.SharedCD.Reset()
					}
				}
				if !spell.Matches(SpellMaskHolyShock|SpellMaskJudgement|SpellMaskHolyStrike) || !icd.IsReady(sim) {
					return
				}
				icd.Use(sim)
				stacks.Activate(sim)
				stacks.AddStack(sim)
			},
		}))
	}

	// C1: Holy Strike triggers your active Seal the same as a melee attack (Command, Righteousness, Fury).
	// It stores and consumes no Unsealed Wrath copy.
	if proposeFlag("C1") {
		paladin.MakeProcTriggerAura(core.ProcTrigger{
			Name:           "C1 Holy Strike Seal trigger" + paladin.Label,
			Callback:       core.CallbackOnSpellHitDealt,
			ClassSpellMask: SpellMaskHolyStrike,
			Outcome:        core.OutcomeLanded,
			Handler: func(sim *core.Simulation, _ *core.Spell, result *core.SpellResult) {
				seal := paladin.activeSeal()
				if seal == nil || seal.echo == nil {
					return
				}
				switch seal.echoID {
				case echoOfCommandID, echoOfRighteousnessID, echoOfFuryID:
					seal.echo(sim, result.Target)
				}
			},
		})
	}
	// C-R4 Burning Zeal 2/2: +20% critical damage bonus of Seals, Judgements and Holy Strike (as Impale).
	if proposeFlag("BZ") {
		paladin.AddStaticMod(core.SpellModConfig{
			ClassMask:  SpellMaskSealProcs | SpellMaskAllJudgements | SpellMaskHolyStrike,
			Kind:       core.SpellMod_CritMultiplier_Flat,
			FloatValue: 0.20,
		})
	}
	// C-R5 Measure for Measure (MFM1/MFM2/MFM3): when your target dodges or parries your attack, the remaining
	// cooldown of your Judgement is reduced by 1/2/3 sec.
	for rank := 1; rank <= 3; rank++ {
		if !proposeFlag("MFM" + string(rune('0'+rank))) {
			continue
		}
		cut := time.Duration(rank) * time.Second
		paladin.MakeProcTriggerAura(core.ProcTrigger{
			Name:     "C-R5 Measure for Measure" + paladin.Label,
			Callback: core.CallbackOnSpellHitDealt,
			ProcMask: core.ProcMaskMelee,
			Outcome:  core.OutcomeDodge | core.OutcomeParry,
			Handler: func(sim *core.Simulation, _ *core.Spell, _ *core.SpellResult) {
				if paladin.Judgement != nil && paladin.Judgement.CD.Timer != nil {
					paladin.Judgement.CD.Reduce(cut)
				}
			},
		})
	}
	// W29 option: Unsealed Wrath decreases the Seal cost by 20%.
	if proposeFlag("UW20") && paladin.Talents.UnsealedWrath {
		paladin.AddStaticMod(core.SpellModConfig{
			ClassMask:  SpellMaskAllSeals,
			Kind:       core.SpellMod_PowerCost_Pct,
			FloatValue: -0.20,
		})
	}
	// C-P1: each Holy Shield cast also starts Redoubt (full charges). RD20: Redoubt 4-20% (5/5 = 20%).
	if redoubt := paladin.GetAura("Redoubt" + paladin.Label); redoubt != nil {
		if proposeFlag("RD20") {
			redoubt.AttachStatBuff(stats.BlockPercent, -10)
		}
		if proposeFlag("CP1") {
			paladin.MakeProcTriggerAura(core.ProcTrigger{
				Name:           "C-P1 Holy Shield starts Redoubt" + paladin.Label,
				Callback:       core.CallbackOnCastComplete,
				ClassSpellMask: SpellMaskHolyShield,
				Handler: func(sim *core.Simulation, _ *core.Spell, _ *core.SpellResult) {
					redoubt.Activate(sim)
					redoubt.SetStacks(sim, redoubt.MaxStacks)
				},
			})
		}
	}
}

// C-P6: Reckoning charges from blocks, dodges and parries (20-100%, once each 4 sec) and from critical hits
// taken (no limit). Stores up to 4. Holy Strike releases up to 2 stored extra attacks; auto attacks spend none.
func (paladin *Paladin) applyReckoningCP6(stored *core.Aura, gain func(*core.Simulation, *core.Spell, *core.SpellResult), tag int32, newTriggers bool, release bool) {
	chance := 0.20 * float64(paladin.Talents.Reckoning)
	if newTriggers {
		paladin.MakeProcTriggerAura(core.ProcTrigger{
			Name:       "C-P6 Reckoning - Avoid" + paladin.Label,
			Callback:   core.CallbackOnSpellHitTaken,
			Outcome:    core.OutcomeBlock | core.OutcomeDodge | core.OutcomeParry,
			ProcChance: chance,
			ICD:        cp6ICD(),
			Handler:    gain,
		})
		paladin.MakeProcTriggerAura(core.ProcTrigger{
			Name:       "C-P6 Reckoning - Crit" + paladin.Label,
			Callback:   core.CallbackOnSpellHitTaken,
			Outcome:    core.OutcomeCrit,
			ProcChance: chance,
			Handler:    gain,
		})
	}
	if !release {
		return
	}
	var extraAttack *core.Spell
	paladin.MakeProcTriggerAura(core.ProcTrigger{
		Name:               "C-P6 Reckoning - Holy Strike" + paladin.Label,
		Callback:           core.CallbackOnSpellHitDealt,
		ClassSpellMask:     SpellMaskHolyStrike,
		TriggerImmediately: true,
		ExtraCondition: func(_ *core.Simulation, _ *core.Spell, _ *core.SpellResult) bool {
			return extraAttack != nil && stored.IsActive()
		},
		Handler: func(sim *core.Simulation, _ *core.Spell, result *core.SpellResult) {
			count := min(stored.GetStacks(), 2)
			if stored.GetStacks() > count {
				stored.SetStacks(sim, stored.GetStacks()-count)
			} else {
				stored.Deactivate(sim)
			}
			target := result.Target
			sim.RunAfterCurrentEvent(func(sim *core.Simulation) {
				mainHand := paladin.AutoAttacks.MHAuto()
				extraAttack.SetSpellSchool(mainHand.SpellSchool)
				extraAttack.BonusCoefficient = mainHand.BonusCoefficient
				for range count {
					extraAttack.Cast(sim, target)
				}
			})
		},
	}).ApplyOnInit(func(_ *core.Aura, _ *core.Simulation) {
		if paladin.AutoAttacks.MHAuto() == nil {
			return
		}
		swing := *paladin.AutoAttacks.MHConfig()
		swing.ActionID = swing.ActionID.WithTag(tag)
		extraAttack = paladin.GetOrRegisterSpell(swing)
	})
}

func cp9BlockValueMult() float64 {
	if v, err := strconv.ParseFloat(os.Getenv("CP9_BV"), 64); err == nil {
		return v
	}
	return 2.0
}

func cp6ICD() time.Duration {
	if v, err := strconv.ParseFloat(os.Getenv("CP6_ICD"), 64); err == nil {
		return time.Duration(v * float64(time.Second))
	}
	return 4 * time.Second
}

func holyShieldThreat() float64 {
	if v, err := strconv.ParseFloat(os.Getenv("HS_THREAT"), 64); err == nil {
		return v
	}
	return 1.2
}

// Judgement is a ranged attack since the hotfixes of 11 November 2026: it uses the ranged hit chance
// and no longer triggers melee item or effect procs. wowsims master still makes the damaging
// judgements melee. JMELEE keeps the old melee judgements.
func (paladin *Paladin) judgementProcMask() core.ProcMask {
	if proposeFlag("JMELEE") {
		return core.ProcMaskMeleeMHSpecial
	}
	return core.ProcMaskRangedSpecial
}
