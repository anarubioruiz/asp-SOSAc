from unittest import TestCase, skip

from clorm import FactBase
from clorm import monkey; monkey.patch() # must call this before importing clingo
from clingo import Control

from terms import InstanceOf, SubclassOf, MemberOf


class Clingo:
    def clingo_setup(self):
        self.ctrl = Control(unifier=[InstanceOf, SubclassOf, MemberOf])
        self.ctrl.load("src/engine.lp")

    def load_knowledge(self, facts):
        self.ctrl.add_facts(facts)
        self.ctrl.ground([("base", [])])

    def get_solution(self):
        solution = None

        def on_model(model):
            nonlocal solution
            print(model)
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
