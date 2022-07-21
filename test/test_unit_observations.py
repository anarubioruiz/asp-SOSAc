from unittest import TestCase, skip

from clorm import FactBase
from clorm import monkey
monkey.patch() # must call this before importing clingo

from utils import ClingoTest
import terms


class Sensor(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup()

    # sosa:observes - Domain: sosa:Sensor, Range: sosa:ObservableProperty
    def test_sensor_observes_ObservableProperty(self):
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

    # sosa:observes inverse property of sosa:isObservedBy
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

    # sosa:madeObservation - Domain: sosa:Sensor, Range: sosa:Observation
    def test_sensor_makesObservation_observation(self):
        facts = FactBase([
            terms.makesObservation(
                sensor="temp_sensor01",
                observation="observation01")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        sensors_query = list(solution
            .query(terms.Sensor)
            .all()
        )

        observations_query = list(solution
            .query(terms.Observation)
            .all()
        )

        query = sensors_query + observations_query
        expected = [
            terms.Sensor(id="temp_sensor01"),
            terms.Observation(id="observation01")
        ]

        self.assertCountEqual(expected, query)

    # sosa:madeObservation inverse property of sosa:madeBySensor
    def test_makesObservation_inverse_of_madeBySensor(self):
        facts = FactBase([
            terms.makesObservation(
                sensor="temp_sensor01",
                observation="observation01")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [
            terms.madeBySensor(
                observation="observation01",
                sensor="temp_sensor01")
        ]

        query = list(solution
            .query(terms.madeBySensor)
            .all()
        )

        self.assertEqual(expected, query)


class ObservableProperty(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup()

    # sosa:isObservedBy - Domain: sosa:ObservableProperty, Range: sosa:Sensor
    def test_ObservableProperty_isObservedBy_Sensor(self):
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

    # sosa:ObservableProperty inverse property of sosa:observes
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

class Observation(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup()

    # sosa:madeBySensor - Domain: sosa:Observation, Range: sosa:Sensor
    def test_Observation_madeBySensor_Sensor(self):
        facts = FactBase([
            terms.madeBySensor(
                observation="observation01",
                sensor="temp_sensor01",)
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        sensors_query = list(solution
            .query(terms.Sensor)
            .all()
        )

        observations_query = list(solution
            .query(terms.Observation)
            .all()
        )

        query = sensors_query + observations_query
        expected = [
            terms.Sensor(id="temp_sensor01"),
            terms.Observation(id="observation01")
        ]

        self.assertCountEqual(expected, query)

    # sosa:madeBySensor inverse property of sosa:madeObservation
    def test_madeBySensor_inverse_of_makesObservation(self):
        facts = FactBase([
            terms.madeBySensor(
                observation="observation01",
                sensor="temp_sensor01")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [
            terms.makesObservation(
                sensor="temp_sensor01",
                observation="observation01")
        ]

        query = list(solution
            .query(terms.makesObservation)
            .all()
        )

        self.assertEqual(expected, query)

    def test_no_more_than_1_madeBySensor(self):
        facts = FactBase([
            terms.madeBySensor(
                observation="observation01",
                sensor="temp_sensor01"),
            terms.madeBySensor(
                observation="observation01",
                sensor="temp_sensor02")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        self.assertEqual(solution, None)
