from unittest import TestCase, skip

from clorm import FactBase
from clorm import monkey
monkey.patch() # must call this before importing clingo

from utils import ClingoTest
import terms


class Act(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup('src/sosa_engine.lp')

    # sosa:hasFeatureOfInterest - Domain: scott:Act, Range: sosa:FeatureOfInterest
    def test_Act_hasFeatureOfInterest_FeatureOfInterest(self):
        facts = FactBase([
            terms.hasFeatureOfInterest(
                act=terms.ActID(device="ANY", act="ANY"),
                feature_of_interest="kitchen")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        acts_query = list(solution
            .query(terms.Act)
            .all()
        )

        features_of_interest_query = list(solution
            .query(terms.FeatureOfInterest)
            .all()
        )

        query = acts_query + features_of_interest_query
        expected = [
            terms.Act(id=terms.ActID(device="ANY", act="ANY")),
            terms.FeatureOfInterest(id="kitchen")
        ]

        self.assertCountEqual(expected, query)

    # sosa:hasFeatureOfInterest inverse property of sosa:isFeatureOfInterestOf
    def test_hasFeatureOfInterest_inverse_of_isFeatureOfInterestOf(self):
        facts = FactBase([
            terms.hasFeatureOfInterest(
                act=terms.ActID(device="ANY", act="ANY"),
                feature_of_interest="bathroom")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        query = list(solution
            .query(terms.isFeatureOfInterestOf)
            .all()
        )
        expected = [
            terms.isFeatureOfInterestOf(
                feature_of_interest="bathroom",
                act=terms.ActID(device="ANY", act="ANY"))
        ]

        self.assertCountEqual(expected, query)

    # scott:Act max 1 sosa:hasFeatureOfInterest
    def test_no_more_than_1_hasFeatureOfInterest(self):
        facts = FactBase([
            terms.hasFeatureOfInterest(
                act=terms.ActID(device="ANY", act="ANY"),
                feature_of_interest="kitchen"),
            terms.hasFeatureOfInterest(
                act=terms.ActID(device="ANY", act="ANY"),
                feature_of_interest="bathroom")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        self.assertEqual(solution, None)

    # sosa:hasResult inverse property of sosa:isResultOf
    def test_hasResult_inverse_of_isResultOf(self):
        facts = FactBase([
            terms.hasResult(
                act=terms.ActID(device="ANY", act="ANY"),
                result="open")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [
            terms.isResultOf(
                result="open",
                act=terms.ActID(device="ANY", act="ANY"))
        ]

        query = list(solution
            .query(terms.isResultOf)
            .all()
        )

        self.assertEqual(expected, query)

    # sosa:hasSimpleResult - Domain: scott:Act, Range: --
    def test_Act_hasSimpleResult(self):
        facts = FactBase([
            terms.hasSimpleResult(
                act=terms.ActID(device="ANY", act="ANY"),
                result="true")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [terms.Act(id=terms.ActID(device="ANY", act="ANY"))]
        query = list(solution
            .query(terms.Act)
            .all()
        )

        self.assertCountEqual(expected, query)


class FeatureOfInterest(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup('src/sosa_engine.lp')

    # sosa:isFeatureOfInterestOf - Domain: sosa:FeatureOfInterest, Range: scott:Act
    def test_FeatureOfInterest_isFeatureOfInterestOf_Act(self):
        facts = FactBase([
            terms.isFeatureOfInterestOf(
                feature_of_interest="kitchen",
                act=terms.ActID(device="ANY", act="ANY"))
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        acts_query = list(solution
            .query(terms.Act)
            .all()
        )

        features_of_interest_query = list(solution
            .query(terms.FeatureOfInterest)
            .all()
        )

        query = acts_query + features_of_interest_query
        expected = [
            terms.Act(id=terms.ActID(device="ANY", act="ANY")),
            terms.FeatureOfInterest(id="kitchen")
        ]

        self.assertCountEqual(expected, query)

    # sosa:isFeatureOfInterestOf inverse property of sosa:hasFeatureOfInterest
    def test_isFeatureOfInterestOf_inverse_of_hasFeatureOfInterest(self):
        facts = FactBase([
            terms.isFeatureOfInterestOf(
                feature_of_interest="kitchen",
                act=terms.ActID(device="ANY", act="ANY"))
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        query = list(solution
            .query(terms.hasFeatureOfInterest)
            .all()
        )
        expected = [
            terms.hasFeatureOfInterest(
                act=terms.ActID(device="ANY", act="ANY"),
                feature_of_interest="kitchen")
        ]

        self.assertCountEqual(expected, query)


class Sensor(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup('src/sosa_engine.lp')

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
                observation=terms.ActID(device="ANY", act="ANY"))
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
            terms.Observation(id=terms.ActID(device="ANY", act="ANY"))
        ]

        self.assertCountEqual(expected, query)

    # sosa:madeObservation inverse property of sosa:madeBySensor
    def test_makesObservation_inverse_of_madeBySensor(self):
        facts = FactBase([
            terms.makesObservation(
                sensor="temp_sensor01",
                observation=terms.ActID(device="ANY", act="ANY"))
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [
            terms.madeBySensor(
                observation=terms.ActID(device="ANY", act="ANY"),
                sensor="temp_sensor01")
        ]

        query = list(solution
            .query(terms.madeBySensor)
            .all()
        )

        self.assertEqual(expected, query)


class ObservableProperty(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup('src/sosa_engine.lp')

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

    # sosa:isObservedBy inverse property of sosa:observes
    def test_isObservedBy_inverse_of_observes(self):
        facts = FactBase([
            terms.isObservedBy(
                observable_property="temperature",
                sensor="temp_sensor01")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [
            terms.observes(
                sensor="temp_sensor01",
                observable_property="temperature")
        ]

        query = list(solution
            .query(terms.observes)
            .all()
        )

        self.assertEqual(expected, query)

class Observation(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup('src/sosa_engine.lp')

    # sosa:Observation sub class of scott:Act
    def test_Observations_are_Acts(self):
        facts = FactBase([
            terms.Observation(id=terms.ActID(device="ANY", act="ANY"))
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [terms.Act(id=terms.ActID(device="ANY", act="ANY"))]
        query = list(solution
            .query(terms.Act)
            .all()
        )

        self.assertCountEqual(expected, query)

    # sosa:madeBySensor - Domain: sosa:Observation, Range: sosa:Sensor
    def test_Observation_madeBySensor_Sensor(self):
        facts = FactBase([
            terms.madeBySensor(
                observation=terms.ActID(device="ANY", act="ANY"),
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
            terms.Observation(id=terms.ActID(device="ANY", act="ANY"))
        ]

        self.assertCountEqual(expected, query)

    # sosa:madeBySensor inverse property of sosa:madeObservation
    def test_madeBySensor_inverse_of_makesObservation(self):
        facts = FactBase([
            terms.madeBySensor(
                observation=terms.ActID(device="ANY", act="ANY"),
                sensor="temp_sensor01")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [
            terms.makesObservation(
                sensor="temp_sensor01",
                observation=terms.ActID(device="ANY", act="ANY"))
        ]

        query = list(solution
            .query(terms.makesObservation)
            .all()
        )

        self.assertEqual(expected, query)

    # sosa:Observation max 1 sosa:madeBySensor
    def test_no_more_than_1_madeBySensor(self):
        facts = FactBase([
            terms.madeBySensor(
                observation=terms.ActID(device="ANY", act="ANY"),
                sensor="temp_sensor01"),
            terms.madeBySensor(
                observation=terms.ActID(device="ANY", act="ANY"),
                sensor="temp_sensor02")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        self.assertEqual(solution, None)

    # sosa:observedProperty - Domain: sosa:Observation, Range: sosa:ObservableProperty
    def test_Observation_observedProperty_ObservableProperty(self):
        facts = FactBase([
            terms.observedProperty(
                observation=terms.ActID(device="ANY", act="ANY"),
                observable_property="occupancy",)
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        observable_properties_query = list(solution
            .query(terms.ObservableProperty)
            .all()
        )

        observations_query = list(solution
            .query(terms.Observation)
            .all()
        )

        query = observable_properties_query + observations_query
        expected = [
            terms.ObservableProperty(id="occupancy"),
            terms.Observation(id=terms.ActID(device="ANY", act="ANY"))
        ]

        self.assertCountEqual(expected, query)


class Actuator(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup('src/sosa_engine.lp')

    # sosa:madeActuation - Domain: sosa:Actuator, Range: sosa:Actuation
    def test_sensor_makesActuation_actuation(self):
        facts = FactBase([
            terms.makesActuation(
                actuator="smart_bulb01",
                actuation=terms.ActID(device="ANY", act="ANY"))
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
            terms.Actuation(id=terms.ActID(device="ANY", act="ANY"))
        ]

        self.assertCountEqual(expected, query)

    # sosa:madeActuation inverse property of sosa:madeByActuator
    def test_makesActuation_inverse_of_madeByActuator(self):
        facts = FactBase([
            terms.makesActuation(
                actuator="smart_bulb01",
                actuation=terms.ActID(device="ANY", act="ANY"))
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [
            terms.madeByActuator(
                actuation=terms.ActID(device="ANY", act="ANY"),
                actuator="smart_bulb01")
        ]

        query = list(solution
            .query(terms.madeByActuator)
            .all()
        )

        self.assertEqual(expected, query)

class actuatableProperty(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup('src/sosa_engine.lp')

    # sosa:isActedOnBy - Domain: sosa:actuatableProperty, Range: sosa:Actuation
    def test_actuatableProperty_isActedOnBy_Actuation(self):
        facts = FactBase([
            terms.isActedOnBy(
                actuatable_property="lighting",
                actuation=terms.ActID(device="ANY", act="ANY"))
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        actuations_query = list(solution
            .query(terms.Actuation)
            .all()
        )

        actuatable_properties_query = list(solution
            .query(terms.ActuatableProperty)
            .all()
        )

        query = actuations_query + actuatable_properties_query
        expected = [
            terms.Actuation(id=terms.ActID(device="ANY", act="ANY")),
            terms.ActuatableProperty(id="lighting")
        ]

        self.assertCountEqual(expected, query)

    # sosa:isActedOnBy invserse property of sosa:actsOnProperty
    def test_isActedOnBy_inverse_actsOnProperty(self):
        facts = FactBase([
            terms.isActedOnBy(
                actuatable_property="lighting",
                actuation=terms.ActID(device="ANY", act="ANY"))
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [
            terms.actsOnProperty(
                actuation=terms.ActID(device="ANY", act="ANY"),
                actuatable_property="lighting")
        ]

        query = list(solution
            .query(terms.actsOnProperty)
            .all()
        )

        self.assertEqual(expected, query)


class Actuation(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup('src/sosa_engine.lp')

    # sosa:Actuation sub class of scott:Act
    def test_Actuations_are_Acts(self):
        facts = FactBase([
            terms.Actuation(id=terms.ActID(device="ANY", act="ANY"))
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [terms.Act(id=terms.ActID(device="ANY", act="ANY"))]
        query = list(solution
            .query(terms.Act)
            .all()
        )

        self.assertCountEqual(expected, query)

    # sosa:madeByActuator - Domain: sosa:Actuation, Range: sosa:Actuator
    def test_Actuation_madeByActuator_Actuator(self):
        facts = FactBase([
            terms.madeByActuator(
                actuation=terms.ActID(device="ANY", act="ANY"),
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
            terms.Actuation(id=terms.ActID(device="ANY", act="ANY"))
        ]

        self.assertCountEqual(expected, query)

    # sosa:madeByActuator inverse property of sosa:makesActuation
    def test_madeByActuator_inverse_of_makesActuation(self):
        facts = FactBase([
            terms.madeByActuator(
                actuation=terms.ActID(device="ANY", act="ANY"),
                actuator="smart_bulb01",)
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [
            terms.makesActuation(
                actuator="smart_bulb01",
                actuation=terms.ActID(device="ANY", act="ANY"))
        ]

        query = list(solution
            .query(terms.makesActuation)
            .all()
        )

        self.assertEqual(expected, query)

    # sosa:Actuation max 1 sosa:madeByActuator
    def test_no_more_than_1_madeByActuator(self):
        facts = FactBase([
            terms.madeByActuator(
                actuation=terms.ActID(device="ANY", act="ANY"),
                actuator="smart_bulb01"),
            terms.madeByActuator(
                actuation=terms.ActID(device="ANY", act="ANY"),
                actuator="smart_bulb02")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        self.assertEqual(solution, None)


class Result(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup('src/sosa_engine.lp')

    # sosa:isResultOf - Domain: sosa:Result, Range: scott:Act
    def test_Result_isResultOf_Act(self):
        facts = FactBase([
            terms.isResultOf(
                result="open",
                act=terms.ActID(device="ANY", act="ANY"))
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        acts_query = list(solution
            .query(terms.Act)
            .all()
        )

        results_query = list(solution
            .query(terms.Result)
            .all()
        )

        query = acts_query + results_query
        expected = [
            terms.Act(id=terms.ActID(device="ANY", act="ANY")),
            terms.Result(id="open")
        ]

        self.assertCountEqual(expected, query)

    # sosa:isResultOf inverse property of sosa:hasResult
    def test_isResultOf_inverse_of_hasResult(self):
        facts = FactBase([
            terms.isResultOf(
                result="open",
                act=terms.ActID(device="ANY", act="ANY"))
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [
            terms.hasResult(
                act=terms.ActID(device="ANY", act="ANY"),
                result="open")
        ]

        query = list(solution
            .query(terms.hasResult)
            .all()
        )

        self.assertEqual(expected, query)


class Platform(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup('src/sosa_engine.lp')

    # sosa:hosts - Domain: sosa:Platform, Range: --
    def test_Platform_hosts(self):
        facts = FactBase([
            terms.hosts(
                platform="Joey",
                hosted="smart_watch01")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [terms.Platform(id="Joey")]
        query = list(solution
            .query(terms.Platform)
            .all()
        )

        self.assertCountEqual(expected, query)

    # sosa:hosts inverse property of sosa:isHostedBy
    def test_hosts_inverse_of_isHostedBy(self):
        facts = FactBase([
            terms.hosts(
                platform="Joey",
                hosted="smart_watch01")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [
            terms.isHostedBy(
                hosted="smart_watch01",
                platform="Joey")
        ]

        query = list(solution
            .query(terms.isHostedBy)
            .all()
        )

        self.assertEqual(expected, query)

    # sosa:isHostedBy inverse property of sosa:hosts
    def test_isHostedBy_inverse_of_hosts(self):
        facts = FactBase([
            terms.isHostedBy(
                hosted="smart_watch01",
                platform="Joey")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [
            terms.hosts(
                platform="Joey",
                hosted="smart_watch01")
        ]

        query = list(solution
            .query(terms.hosts)
            .all()
        )

        self.assertEqual(expected, query)
