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

class BasicEngine(TestCase, Clingo):
    def setUp(self):
        self.clingo_setup()

    def test_property_value_is_instance_of_property(self):
        facts = FactBase([
            terms.PropertyValueOf(property="location", value="kitchen", owner="motion_sensor1")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [terms.InstanceOf(instance="kitchen", klass="location")]
        query = list(solution
            .query(terms.InstanceOf)
            .where(terms.InstanceOf.instance == "kitchen")
            .all()
        )

        self.assertEqual(expected, query)

class Inheritance(TestCase, Clingo):
    def setUp(self):
        self.clingo_setup()

        facts = FactBase([
            terms.SubclassOf(child_klass="actuator", parent_klass="device"),
            terms.SubclassOf(child_klass="smart_bulb", parent_klass="actuator"),
            terms.InstanceOf(instance="lamp1", klass="smart_bulb"),
        ])

        self.load_knowledge(facts)

    def test_subclass_relation_is_transitive(self):
        solution = self.get_solution()

        query = list(solution
            .query(terms.SubclassOf)
            .where(terms.SubclassOf.child_klass == "smart_bulb")
            .all()
        )

        expected = [
            terms.SubclassOf(child_klass="smart_bulb", parent_klass="device"),
            terms.SubclassOf(child_klass="smart_bulb", parent_klass="actuator")
        ]

        self.assertCountEqual(expected, query)

    def test_instance_is_member_of_all_its_parent_klasses(self):
        solution = self.get_solution()

        query = list(solution.query(terms.MemberOf).all())
        expected = [
            terms.MemberOf(instance="lamp1", klass="smart_bulb"),
            terms.MemberOf(instance="lamp1", klass="actuator"),
            terms.MemberOf(instance="lamp1", klass="device")
        ]

        self.assertCountEqual(expected, query)

class Transition(TestCase, Clingo):
    def setUp(self):
        self.clingo_setup()

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

            terms.InstanceOf(instance="blind_motor1", klass="blind_motor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="blind_motor1"),

            terms.InstanceOf(instance="smart_bulb1", klass="smart_bulb"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="smart_bulb1")
        ]

        facts = FactBase(transition+scenario)
        self.load_knowledge(facts)

    def test_instance_of_transition_trigger(self):
        solution = self.get_solution()

        klass_query = list(solution
            .query(terms.TransitionTrigger)
            .where(terms.TransitionTrigger.id == 1)
            .all())

        instance_query = list(solution
            .query(terms._TransitionTrigger)
            .where(terms._TransitionTrigger.id == 1)
            .all())

        query = klass_query + instance_query
        expected = [
            terms.TransitionTrigger(id=1, device_klass="motion_sensor", state="true"),
            terms._TransitionTrigger(id=1, device="motion_sensor1", state="true")
        ]

        self.assertCountEqual(expected, query)

    def test_instance_of_transition_change(self):
        solution = self.get_solution()

        klass_query = list(solution
            .query(terms.TransitionChange)
            .where(terms.TransitionChange.id == 1)
            .all())

        instance_query = list(solution
            .query(terms._TransitionChange)
            .where(terms._TransitionChange.id == 1)
            .all())

        query = klass_query + instance_query
        expected = [
            terms.TransitionChange(id=1, target_klass="location", state="occupied"),
            terms._TransitionChange(id=1, target="bathroom", state="occupied")
        ]

        self.assertCountEqual(expected, query)

    def test_not_instance_of_transition_change_when_not_apropiate_trigger(self):
        solution = self.get_solution()

        query = list(solution
            .query(terms._TransitionChange)
            .where(terms._TransitionChange.state == "lit")
            .all())

        not_expected = [
            terms._TransitionChange(id=2, target="bathroom", state="lit"),
            terms._TransitionChange(id=3, target="bathroom", state="lit"),
        ]

        self.assertFalse(any(i_transitionChange in query for i_transitionChange in not_expected))
