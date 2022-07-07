from unittest import TestCase, skip

from clorm import FactBase
from clorm import monkey; monkey.patch() # must call this before importing clingo
from clingo import Control

from terms import InstanceOf, SubclassOf, MemberOf, TransitionTrigger, TransitionChange, PropertyValueOf


class Clingo:
    def clingo_setup(self):
        self.ctrl = Control(unifier=[InstanceOf, SubclassOf, MemberOf, TransitionTrigger, TransitionChange, PropertyValueOf])
        self.ctrl.load("src/engine.lp")
        self.ctrl.load("src/kb.lp")

    def load_knowledge(self, facts):
        self.ctrl.add_facts(facts)
        self.ctrl.ground([("base", [])])

    def get_solution(self):
        solution = None

        def on_model(model):
            nonlocal solution
            # print(model)
            solution = model.facts(atoms=True)

        self.ctrl.solve(on_model=on_model)
        return solution


class Inheritance(TestCase, Clingo):
    def setUp(self):
        self.clingo_setup()

        facts = FactBase([
            SubclassOf(child_klass="actuator", parent_klass="device"),
            SubclassOf(child_klass="smart_bulb", parent_klass="actuator"),
            InstanceOf(instance="lamp1", klass="smart_bulb"),
        ])

        self.load_knowledge(facts)

    def test_subclass_relation_is_transitive(self):
        solution = self.get_solution()

        query = list(solution
            .query(SubclassOf)
            .where(SubclassOf.child_klass == "smart_bulb")
            .all()
        )

        expected = [
            SubclassOf(child_klass="smart_bulb", parent_klass="device"),
            SubclassOf(child_klass="smart_bulb", parent_klass="actuator")
        ]

        self.assertCountEqual(expected, query)

    def test_instance_is_member_of_all_its_parent_klasses(self):
        solution = self.get_solution()

        query = list(solution.query(MemberOf).all())
        expected = [
            MemberOf(instance="lamp1", klass="smart_bulb"),
            MemberOf(instance="lamp1", klass="actuator"),
            MemberOf(instance="lamp1", klass="device")
        ]

        self.assertCountEqual(expected, query)

class Transition(TestCase, Clingo):
    def setUp(self):
        self.clingo_setup()

        facts = FactBase([
            SubclassOf(child_klass="actuator", parent_klass="device"),
            SubclassOf(child_klass="motion_sensor", parent_klass="actuator"),
            InstanceOf(instance="motion_sensor1", klass="motion_sensor"),
            PropertyValueOf(property="location", value="kitchen", target="motion_sensor1")
        ])

        self.load_knowledge(facts)

    def test_instance_of_transition_trigger(self):
        solution = self.get_solution()

        query = list(solution
            .query(TransitionTrigger)
            .where(TransitionTrigger.id == 1)
            .all())

        expected = [
            TransitionTrigger(id=1, device="motion_sensor", device_state="true"),
            TransitionTrigger(id=1, device="motion_sensor1", device_state="true")
        ]

        self.assertCountEqual(expected, query)

    def test_instance_of_transition_change(self):
        solution = self.get_solution()

        query = list(solution
            .query(TransitionChange)
            .where(TransitionChange.id == 1)
            .all())

        expected = [
            TransitionChange(id=1, target="location", target_state="occupied"),
            TransitionChange(id=1, target="kitchen", target_state="occupied")
        ]

        self.assertCountEqual(expected, query)