from unittest import TestCase, skip

from clorm import FactBase
from clorm import monkey
monkey.patch() # must call this before importing clingo
from clingo import Control

import terms


class Clingo:
    def clingo_setup(self):
        self.ctrl = Control(unifier=[
            terms.InstanceOf,
            terms.SubclassOf,
            terms.PropertyValueOf,
            terms.MemberOf,
            terms.TransitionTrigger,
            terms._TransitionTrigger,
            terms.TransitionChange,
            terms._TransitionChange,
            terms.instructionId,
            terms.stateOf,
            terms.Instruction,
            terms.Goal
        ])

        self.ctrl.load("src/engine.lp")

    def load_knowledge(self, facts):
        self.ctrl.add_facts(facts)
        self.ctrl.ground([("base", [])])

    def get_solution(self):
        solution = None

        def on_model(model):
            nonlocal solution
            solution = model.facts(atoms=True)
            for item in solution.query(terms._TransitionChange).all():
                print(item)

        self.ctrl.solve(on_model=on_model)
        return solution

class Instruction(TestCase, Clingo):
    def setUp(self):
        self.clingo_setup()

        goals = [
            terms.Goal(id="goal_1", type="if", stateOf=terms.stateOf(thing_state="occupied", thing="location")),
            terms.Goal(id="goal_1", type="then", stateOf=terms.stateOf(thing_state="lit", thing="location")),
        ]

        transition = [
            terms.TransitionTrigger(id=1, device_klass="motion_sensor", state="true"),
            terms.TransitionChange(id=1, target_klass="location", state="occupied"),

            terms.TransitionTrigger(id=2, device_klass="blind_motor", state="up"),
            terms.TransitionChange(id=2, target_klass="location", state="lit"),

            terms.TransitionTrigger(id=3, device_klass="smart_bulb", state="on"),
            terms.TransitionChange(id=3, target_klass="location", state="lit")
        ]

        scenario = [
            terms.InstanceOf(instance="motion_sensor1", klass="motion_sensor"),
            terms.PropertyValueOf(property="location", value="bathroom", owner="motion_sensor1"),

            terms.InstanceOf(instance="smart_bulb1", klass="smart_bulb"),
            terms.PropertyValueOf(property="location", value="bathroom", owner="smart_bulb1"),

            terms.InstanceOf(instance="motion_sensor2", klass="motion_sensor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="motion_sensor2"),

            terms.InstanceOf(instance="blind_motor1", klass="blind_motor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="blind_motor1"),

            terms.InstanceOf(instance="smart_bulb2", klass="smart_bulb"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="smart_bulb2")
        ]

        facts = FactBase(goals+transition+scenario)
        self.load_knowledge(facts)

    def test_(self):
        solution = self.get_solution()