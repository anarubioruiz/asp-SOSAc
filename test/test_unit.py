from unittest import TestCase, skip

from clorm import FactBase
from clorm import monkey
monkey.patch() # must call this before importing clingo

from utils import ClingoTest
import terms


class Observations(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup()

    def test_observes_inverse_of_isObservedBy(self):
        facts = FactBase([
            terms.observes(
                sensor="temp_sensor01",
                observable_property="temperature")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [
            terms.isObservedBy(
                observable_property="temperature",
                sensor="temp_sensor01")
        ]

        query = list(solution
            .query(terms.isObservedBy)
            .all()
        )

        self.assertEqual(expected, query)

    def test_isObservedBy_inverse_of_observes(self):
        facts = FactBase([
            terms.isObservedBy(
                observable_property="temperature",
                sensor="temp_sensor01")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [
            terms.isObservedBy(
                sensor="temp_sensor01",
                observable_property="temperature")
        ]

        query = list(solution
            .query(terms.isObservedBy)
            .all()
        )

        self.assertEqual(expected, query)

    def test_only_Sensor_observes_ObservableProperty(self):
        facts = FactBase([
            terms.observes(
                sensor="temp_sensor01",
                observable_property="temperature")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        sensors_query = list(solution
            .query(terms.Sensor)
            .all()
        )

        observable_properties_query = list(solution
            .query(terms.ObservableProperty)
            .all()
        )

        query = sensors_query + observable_properties_query
        expected = [
            terms.Sensor(id="temp_sensor01"),
            terms.ObservableProperty(id="temperature")
        ]

        self.assertCountEqual(expected, query)

    def test_only_ObservableProperty_isObservedBy_Sensor(self):
        facts = FactBase([
            terms.isObservedBy(
                observable_property="temperature",
                sensor="temp_sensor01")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        sensors_query = list(solution
            .query(terms.Sensor)
            .all()
        )

        observable_properties_query = list(solution
            .query(terms.ObservableProperty)
            .all()
        )

        query = sensors_query + observable_properties_query
        expected = [
            terms.Sensor(id="temp_sensor01"),
            terms.ObservableProperty(id="temperature")
        ]

        self.assertCountEqual(expected, query)
