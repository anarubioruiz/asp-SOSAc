from unittest import TestCase, skip

from clorm import FactBase
from clorm import monkey
monkey.patch() # must call this before importing clingo

from utils import ClingoTest
import terms


class Actuator(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup()

    # sosa:madeActuation - Domain: 	sosa:Actuation, Range: 	sosa:Actuator
    def test_sensor_makesActuation_actuation(self):
        facts = FactBase([
            terms.makesActuation(
                actuator="smart_bulb01",
                actuation="actuation01")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        actuators_query = list(solution
            .query(terms.Actuator)
            .all()
        )

        actuations_query = list(solution
            .query(terms.Actuation)
            .all()
        )

        query = actuators_query + actuations_query
        expected = [
            terms.Actuator(id="smart_bulb01"),
            terms.Actuation(id="actuation01")
        ]

        self.assertCountEqual(expected, query)

    # sosa:madeActuation inverse property of sosa:madeByActuator
    def test_makesActuation_inverse_of_madeByActuatorr(self):
        facts = FactBase([
            terms.makesActuation(
                actuator="smart_bulb01",
                actuation="actuation01")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [
            terms.madeByActuator(
                actuation="actuation01",
                actuator="smart_bulb01")
        ]

        query = list(solution
            .query(terms.madeByActuator)
            .all()
        )

        self.assertEqual(expected, query)

class ActuatableProperty(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup()

    # sosa:isActedOnBy - Domain: sosa:ActuatableProperty, Range: sosa:Actuation
    def test_ActuatableProperty_isActedOnBy_Actuator(self):
        facts = FactBase([
            terms.isActedOnBy(
                actuatable_property="lighting",
                actuator="smart_bulb01")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        actuators_query = list(solution
            .query(terms.Actuator)
            .all()
        )

        actuable_properties_query = list(solution
            .query(terms.ActuatableProperty)
            .all()
        )

        query = actuators_query + actuable_properties_query
        expected = [
            terms.Actuator(id="smart_bulb01"),
            terms.ActuatableProperty(id="lighting")
        ]

        self.assertCountEqual(expected, query)

    # sosa:isActedOnBy invserse property of sosa:actsOnProperty
    def test_isActedOnBy_inverse_actsOnProperty(self):
        facts = FactBase([
            terms.isActedOnBy(
                actuatable_property="lighting",
                actuator="smart_bulb01")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [
            terms.actsOnProperty(
                actuator="smart_bulb01",
                actuatable_property="lighting")
        ]

        query = list(solution
            .query(terms.actsOnProperty)
            .all()
        )

        self.assertEqual(expected, query)


class Actuation(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup()

    # sosa:madeByActuator - Domain: sosa:Actuation, Range: sosa:Actuator
    def test_Actuation_madeByActuator_Actuator(self):
        facts = FactBase([
            terms.madeByActuator(
                actuation="actuation01",
                actuator="smart_bulb01",)
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        actuators_query = list(solution
            .query(terms.Actuator)
            .all()
        )

        actuations_query = list(solution
            .query(terms.Actuation)
            .all()
        )

        query = actuators_query + actuations_query
        expected = [
            terms.Actuator(id="smart_bulb01"),
            terms.Actuation(id="actuation01")
        ]

        self.assertCountEqual(expected, query)

    # sosa:madeByActuator inverse property of sosa:makesActuation
    def test_madeByActuator_inverse_of_makesActuation(self):
        facts = FactBase([
            terms.madeByActuator(
                actuation="actuation01",
                actuator="smart_bulb01",)
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [
            terms.makesActuation(
                actuator="smart_bulb01",
                actuation="actuation01")
        ]

        query = list(solution
            .query(terms.makesActuation)
            .all()
        )

        self.assertEqual(expected, query)

    def test_no_more_than_1_madeByActuator(self):
        facts = FactBase([
            terms.madeByActuator(
                actuation="actuation01",
                actuator="smart_bulb01"),
            terms.madeByActuator(
                actuation="actuation01",
                actuator="smart_bulb02")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        self.assertEqual(solution, None)
