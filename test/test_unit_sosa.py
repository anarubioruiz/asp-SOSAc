from unittest import TestCase, skip
from clorm import FactBase

from sosac_clingo import SosaCClingo
import sosac_terms as terms


class Act(TestCase, SosaCClingo):
    def setUp(self):
        self.clingo_setup('src/sosac_engine.lp')

    # sosa:hasFeatureOfInterest - Domain: sosac:Act, Range: sosa:FeatureOfInterest
    def test_Act_hasFeatureOfInterest_FeatureOfInterest(self):
        facts = FactBase([
            terms.hasFeatureOfInterest(
                act=terms.ActID(device='ANY', act='ANY'),
                feature_of_interest='kitchen')
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        acts_query = list(solution
            .query(terms.Act)
            .all()
        )

        features_of_interest_query = list(solution
            .query(terms.sosac_featureOfInterest)
            .all()
        )

        query = acts_query + features_of_interest_query
        expected = [
            terms.Act(id=terms.ActID(device='ANY', act='ANY')),
            terms.sosac_featureOfInterest(id='kitchen')
        ]

        self.assertCountEqual(expected, query)

    # sosa:hasFeatureOfInterest inverse property of sosa:isFeatureOfInterestOf
    def test_hasFeatureOfInterest_inverse_of_isFeatureOfInterestOf(self):
        facts = FactBase([
            terms.hasFeatureOfInterest(
                act=terms.ActID(device='ANY', act='ANY'),
                feature_of_interest='bathroom')
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        query = list(solution
            .query(terms.isFeatureOfInterestOf)
            .all()
        )
        expected = [
            terms.isFeatureOfInterestOf(
                feature_of_interest='bathroom',
                act=terms.ActID(device='ANY', act='ANY'))
        ]

        self.assertCountEqual(expected, query)

    # sosac:Act max 1 sosa:hasFeatureOfInterest
    def test_no_more_than_1_hasFeatureOfInterest(self):
        facts = FactBase([
            terms.hasFeatureOfInterest(
                act=terms.ActID(device='ANY', act='ANY'),
                feature_of_interest='kitchen'),
            terms.hasFeatureOfInterest(
                act=terms.ActID(device='ANY', act='ANY'),
                feature_of_interest='bathroom')
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        self.assertEqual(solution, None)

    # sosa:hasResult inverse property of sosa:isResultOf
    def test_hasResult_inverse_of_isResultOf(self):
        facts = FactBase([
            terms.hasResult(
                act=terms.ActID(device='ANY', act='ANY'),
                result='open_ob')
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [
            terms.isResultOf(
                result='open_ob',
                act=terms.ActID(device='ANY', act='ANY'))
        ]

        query = list(solution
            .query(terms.isResultOf)
            .all()
        )

        self.assertEqual(expected, query)


class sosac_featureOfInterest(TestCase, SosaCClingo):
    def setUp(self):
        self.clingo_setup('src/sosac_engine.lp')

        facts = FactBase([
            terms.isFeatureOfInterestOf(
                feature_of_interest='kitchen',
                act=terms.ActID(device='ANY', act='ANY'))
        ])

        self.load_knowledge(facts)

    # sosa:isFeatureOfInterestOf - Domain: sosa:FeatureOfInterest, Range: sosac:Act
    def test_FeatureOfInterest_isFeatureOfInterestOf_Act(self):
        solution = self.get_solution()

        acts_query = list(solution
            .query(terms.Act)
            .all()
        )

        features_of_interest_query = list(solution
            .query(terms.sosac_featureOfInterest)
            .all()
        )

        query = acts_query + features_of_interest_query
        expected = [
            terms.Act(id=terms.ActID(device='ANY', act='ANY')),
            terms.sosac_featureOfInterest(id='kitchen')
        ]

        self.assertCountEqual(expected, query)

    # sosa:isFeatureOfInterestOf inverse property of sosa:hasFeatureOfInterest
    def test_isFeatureOfInterestOf_inverse_of_hasFeatureOfInterest(self):
        solution = self.get_solution()

        query = list(solution
            .query(terms.hasFeatureOfInterest)
            .all()
        )
        expected = [
            terms.hasFeatureOfInterest(
                act=terms.ActID(device='ANY', act='ANY'),
                feature_of_interest='kitchen')
        ]

        self.assertCountEqual(expected, query)


class sosac_sensor(TestCase, SosaCClingo):
    def setUp(self):
        self.clingo_setup('src/sosac_engine.lp')

    # sosa:observes - Domain: sosa:Sensor, Range: sosa:ObservableProperty
    def test_sensor_observes_ObservableProperty(self):
        facts = FactBase([
            terms.sosac_observes(
                sensor='temp_sensor01',
                observable_property='temperature')
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        sensors_query = list(solution
            .query(terms.sosac_sensor)
            .all()
        )

        observable_properties_query = list(solution
            .query(terms.sosac_observableProperty)
            .all()
        )

        query = sensors_query + observable_properties_query
        expected = [
            terms.sosac_sensor(id='temp_sensor01'),
            terms.sosac_observableProperty(id='temperature')
        ]

        self.assertCountEqual(expected, query)

    # sosa:observes inverse property of sosa:isObservedBy
    def test_observes_inverse_of_isObservedBy(self):
        facts = FactBase([
            terms.sosac_observes(
                sensor='temp_sensor01',
                observable_property='temperature')
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [
            terms.sosac_isObservedBy(
                observable_property='temperature',
                sensor='temp_sensor01')
        ]

        query = list(solution
            .query(terms.sosac_isObservedBy)
            .all()
        )

        self.assertEqual(expected, query)

    # sosa:madeObservation - Domain: sosa:Sensor, Range: sosa:Observation
    def test_sensor_makesObservation_observation(self):
        facts = FactBase([
            terms.sosac_makesObservation(
                sensor='temp_sensor01',
                observation=terms.ActID(device='ANY', act='ANY'))
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        sensors_query = list(solution
            .query(terms.sosac_sensor)
            .all()
        )

        observations_query = list(solution
            .query(terms.sosac_observation)
            .all()
        )

        query = sensors_query + observations_query
        expected = [
            terms.sosac_sensor(id='temp_sensor01'),
            terms.sosac_observation(id=terms.ActID(device='ANY', act='ANY'))
        ]

        self.assertCountEqual(expected, query)

    # sosa:madeObservation inverse property of sosa:madeBySensor
    def test_makesObservation_inverse_of_madeBySensor(self):
        facts = FactBase([
            terms.sosac_makesObservation(
                sensor='temp_sensor01',
                observation=terms.ActID(device='ANY', act='ANY'))
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [
            terms.sosac_madeBySensor(
                observation=terms.ActID(device='ANY', act='ANY'),
                sensor='temp_sensor01')
        ]

        query = list(solution
            .query(terms.sosac_madeBySensor)
            .all()
        )

        self.assertEqual(expected, query)


class sosac_observableProperty(TestCase, SosaCClingo):
    def setUp(self):
        self.clingo_setup('src/sosac_engine.lp')

        facts = FactBase([
            terms.sosac_isObservedBy(
                observable_property='temperature',
                sensor='temp_sensor01')
        ])

        self.load_knowledge(facts)

    # sosa:isObservedBy - Domain: sosa:ObservableProperty, Range: sosa:Sensor
    def test_ObservableProperty_isObservedBy_Sensor(self):
        solution = self.get_solution()

        sensors_query = list(solution
            .query(terms.sosac_sensor)
            .all()
        )

        observable_properties_query = list(solution
            .query(terms.sosac_observableProperty)
            .all()
        )

        query = sensors_query + observable_properties_query
        expected = [
            terms.sosac_sensor(id='temp_sensor01'),
            terms.sosac_observableProperty(id='temperature')
        ]

        self.assertCountEqual(expected, query)

    # sosa:isObservedBy inverse property of sosa:observes
    def test_isObservedBy_inverse_of_observes(self):
        solution = self.get_solution()

        expected = [
            terms.sosac_observes(
                sensor='temp_sensor01',
                observable_property='temperature')
        ]

        query = list(solution
            .query(terms.sosac_observes)
            .all()
        )

        self.assertEqual(expected, query)

class sosac_observation(TestCase, SosaCClingo):
    def setUp(self):
        self.clingo_setup('src/sosac_engine.lp')

    # sosa:Observation sub class of sosac:Act
    def test_Observations_are_Acts(self):
        facts = FactBase([
            terms.sosac_observation(id=terms.ActID(device='ANY', act='ANY'))
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [terms.Act(id=terms.ActID(device='ANY', act='ANY'))]
        query = list(solution
            .query(terms.Act)
            .all()
        )

        self.assertCountEqual(expected, query)

    # sosa:madeBySensor - Domain: sosa:Observation, Range: sosa:Sensor
    def test_Observation_madeBySensor_Sensor(self):
        facts = FactBase([
            terms.sosac_madeBySensor(
                observation=terms.ActID(device='ANY', act='ANY'),
                sensor='temp_sensor01',)
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        sensors_query = list(solution
            .query(terms.sosac_sensor)
            .all()
        )

        observations_query = list(solution
            .query(terms.sosac_observation)
            .all()
        )

        query = sensors_query + observations_query
        expected = [
            terms.sosac_sensor(id='temp_sensor01'),
            terms.sosac_observation(id=terms.ActID(device='ANY', act='ANY'))
        ]

        self.assertCountEqual(expected, query)

    # sosa:madeBySensor inverse property of sosa:madeObservation
    def test_madeBySensor_inverse_of_makesObservation(self):
        facts = FactBase([
            terms.sosac_madeBySensor(
                observation=terms.ActID(device='ANY', act='ANY'),
                sensor='temp_sensor01')
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [
            terms.sosac_makesObservation(
                sensor='temp_sensor01',
                observation=terms.ActID(device='ANY', act='ANY'))
        ]

        query = list(solution
            .query(terms.sosac_makesObservation)
            .all()
        )

        self.assertEqual(expected, query)

    # sosa:Observation max 1 sosa:madeBySensor
    def test_no_more_than_1_madeBySensor(self):
        facts = FactBase([
            terms.sosac_madeBySensor(
                observation=terms.ActID(device='ANY', act='ANY'),
                sensor='temp_sensor01'),
            terms.sosac_madeBySensor(
                observation=terms.ActID(device='ANY', act='ANY'),
                sensor='temp_sensor02')
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        self.assertEqual(solution, None)

    # sosa:observedProperty - Domain: sosa:Observation, Range: sosa:ObservableProperty
    def test_Observation_observedProperty_ObservableProperty(self):
        facts = FactBase([
            terms.sosac_observedProperty(
                observation=terms.ActID(device='ANY', act='ANY'),
                observable_property='occupancy',)
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        observable_properties_query = list(solution
            .query(terms.sosac_observableProperty)
            .all()
        )

        observations_query = list(solution
            .query(terms.sosac_observation)
            .all()
        )

        query = observable_properties_query + observations_query
        expected = [
            terms.sosac_observableProperty(id='occupancy'),
            terms.sosac_observation(id=terms.ActID(device='ANY', act='ANY'))
        ]

        self.assertCountEqual(expected, query)


class Actuator(TestCase, SosaCClingo):
    def setUp(self):
        self.clingo_setup('src/sosac_engine.lp')

        facts = FactBase([
            terms.sosac_makesActuation(
                actuator='smart_bulb01',
                actuation=terms.ActID(device='ANY', act='ANY'))
        ])

        self.load_knowledge(facts)

    # sosa:madeActuation - Domain: sosa:Actuator, Range: sosa:Actuation
    def test_sensor_sosac_makesActuation_actuation(self):
        solution = self.get_solution()

        actuators_query = list(solution
            .query(terms.sosac_actuator)
            .all()
        )

        actuations_query = list(solution
            .query(terms.sosac_actuation)
            .all()
        )

        query = actuators_query + actuations_query
        expected = [
            terms.sosac_actuator(id='smart_bulb01'),
            terms.sosac_actuation(id=terms.ActID(device='ANY', act='ANY'))
        ]

        self.assertCountEqual(expected, query)

    # sosa:madeActuation inverse property of sosa:madeByActuator
    def test_sosac_makesActuation_inverse_of_madeByActuator(self):
        solution = self.get_solution()

        expected = [
            terms.sosac_madeByActuator(
                actuation=terms.ActID(device='ANY', act='ANY'),
                actuator='smart_bulb01')
        ]

        query = list(solution
            .query(terms.sosac_madeByActuator)
            .all()
        )

        self.assertEqual(expected, query)

class sosac_actuatableProperty(TestCase, SosaCClingo):
    def setUp(self):
        self.clingo_setup('src/sosac_engine.lp')

        facts = FactBase([
            terms.sosac_isActedOnBy(
                actuatable_property='lighting',
                actuation=terms.ActID(device='ANY', act='ANY'))
        ])

        self.load_knowledge(facts)

    # sosa:isActedOnBy - Domain: sosa:actuatableProperty, Range: sosa:Actuation
    def test_actuatableProperty_isActedOnBy_Actuation(self):
        solution = self.get_solution()

        actuations_query = list(solution
            .query(terms.sosac_actuation)
            .all()
        )

        actuatable_properties_query = list(solution
            .query(terms.sosac_actuatableProperty)
            .all()
        )

        query = actuations_query + actuatable_properties_query
        expected = [
            terms.sosac_actuation(id=terms.ActID(device='ANY', act='ANY')),
            terms.sosac_actuatableProperty(id='lighting')
        ]

        self.assertCountEqual(expected, query)

    # sosa:isActedOnBy invserse property of sosa:actsOnProperty
    def test_isActedOnBy_inverse_actsOnProperty(self):
        solution = self.get_solution()

        expected = [
            terms.sosac_actsOnProperty(
                actuation=terms.ActID(device='ANY', act='ANY'),
                actuatable_property='lighting')
        ]

        query = list(solution
            .query(terms.sosac_actsOnProperty)
            .all()
        )

        self.assertEqual(expected, query)


class sosac_actuation(TestCase, SosaCClingo):
    def setUp(self):
        self.clingo_setup('src/sosac_engine.lp')

    # sosa:Actuation sub class of sosac:Act
    def test_Actuations_are_Acts(self):
        facts = FactBase([
            terms.sosac_actuation(id=terms.ActID(device='ANY', act='ANY'))
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [terms.Act(id=terms.ActID(device='ANY', act='ANY'))]
        query = list(solution
            .query(terms.Act)
            .all()
        )

        self.assertCountEqual(expected, query)

    # sosa:madeByActuator - Domain: sosa:Actuation, Range: sosa:Actuator
    def test_Actuation_madeByActuator_Actuator(self):
        facts = FactBase([
            terms.sosac_madeByActuator(
                actuation=terms.ActID(device='ANY', act='ANY'),
                actuator='smart_bulb01',)
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        actuators_query = list(solution
            .query(terms.sosac_actuator)
            .all()
        )

        actuations_query = list(solution
            .query(terms.sosac_actuation)
            .all()
        )

        query = actuators_query + actuations_query
        expected = [
            terms.sosac_actuator(id='smart_bulb01'),
            terms.sosac_actuation(id=terms.ActID(device='ANY', act='ANY'))
        ]

        self.assertCountEqual(expected, query)

    # sosa:madeByActuator inverse property of sosa:sosac_makesActuation
    def test_madeByActuator_inverse_of_sosac_makesActuation(self):
        facts = FactBase([
            terms.sosac_madeByActuator(
                actuation=terms.ActID(device='ANY', act='ANY'),
                actuator='smart_bulb01',)
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [
            terms.sosac_makesActuation(
                actuator='smart_bulb01',
                actuation=terms.ActID(device='ANY', act='ANY'))
        ]

        query = list(solution
            .query(terms.sosac_makesActuation)
            .all()
        )

        self.assertEqual(expected, query)

    # sosa:Actuation max 1 sosa:madeByActuator
    def test_no_more_than_1_madeByActuator(self):
        facts = FactBase([
            terms.sosac_madeByActuator(
                actuation=terms.ActID(device='ANY', act='ANY'),
                actuator='smart_bulb01'),
            terms.sosac_madeByActuator(
                actuation=terms.ActID(device='ANY', act='ANY'),
                actuator='smart_bulb02')
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        self.assertEqual(solution, None)


class Result(TestCase, SosaCClingo):
    def setUp(self):
        self.clingo_setup('src/sosac_engine.lp')

        facts = FactBase([
            terms.isResultOf(
                result='boolean',
                act=terms.ActID(device='ANY', act='ANY'))
        ])

        self.load_knowledge(facts)

    # sosa:isResultOf - Domain: sosa:Result, Range: sosac:Act
    def test_Result_isResultOf_Act(self):
        solution = self.get_solution()

        acts_query = list(solution
            .query(terms.Act)
            .all()
        )

        results_query = list(solution
            .query(terms.sosac_result)
            .all()
        )

        query = acts_query + results_query
        expected = [
            terms.Act(id=terms.ActID(device='ANY', act='ANY')),
            terms.sosac_result(id='boolean')
        ]

        self.assertCountEqual(expected, query)

    # sosa:isResultOf inverse property of sosa:hasResult
    def test_isResultOf_inverse_of_hasResult(self):
        solution = self.get_solution()

        expected = [
            terms.hasResult(
                act=terms.ActID(device='ANY', act='ANY'),
                result='boolean')
        ]

        query = list(solution
            .query(terms.hasResult)
            .all()
        )

        self.assertEqual(expected, query)


class sosac_platform(TestCase, SosaCClingo):
    def setUp(self):
        self.clingo_setup('src/sosac_engine.lp')

    # sosa:hosts - Domain: sosa:Platform, Range: --
    def test_Platform_hosts(self):
        facts = FactBase([
            terms.hosts(
                platform='Joey',
                hosted='smart_watch01')
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [terms.sosac_platform(id='Joey')]
        query = list(solution
            .query(terms.sosac_platform)
            .all()
        )

        self.assertCountEqual(expected, query)

    # sosa:hosts inverse property of sosa:isHostedBy
    def test_hosts_inverse_of_isHostedBy(self):
        facts = FactBase([
            terms.hosts(
                platform='Joey',
                hosted='smart_watch01')
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [
            terms.isHostedBy(
                hosted='smart_watch01',
                platform='Joey')
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
                hosted='smart_watch01',
                platform='Joey')
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [
            terms.hosts(
                platform='Joey',
                hosted='smart_watch01')
        ]

        query = list(solution
            .query(terms.hosts)
            .all()
        )

        self.assertEqual(expected, query)
