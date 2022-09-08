from unittest import TestCase, skip

from clorm import FactBase
from clorm import monkey
monkey.patch() # must call this before importing clingo

from utils import ClingoTest
import terms


class Device(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup(
            'src/sosa_engine.lp',
            'src/engine.lp',
        )

        self.facts = FactBase([
            terms.Device(
                id='device01',
                klass='ANY')
        ])

    def test_isHostedBy_its_location_by_default(self):
        self.facts.add(
            terms.x_is_the_y_of_z(
                value='kitchen',
                property='location',
                entity='device01')
        )

        self.load_knowledge(self.facts)
        solution = self.get_solution()

        expected = [
            terms.isHostedBy(
                hosted='device01',
                platform='kitchen')
        ]

        query = list(solution
            .query(terms.isHostedBy)
            .all()
        )

        self.assertCountEqual(expected, query)

    def test_is_not_hosted_by_its_location_if_host_is_specified(self):
        self.facts.add([
            terms.x_is_the_y_of_z(
                value='kitchen',
                property='location',
                entity='device01'),
            terms.x_is_the_y_of_z(
                value='window01',
                property='host',
                entity='device01')
        ])

        self.load_knowledge(self.facts)
        solution = self.get_solution()

        expected = [
            terms.isHostedBy(
                hosted='device01',
                platform='window01')
        ]

        query = list(solution
            .query(terms.isHostedBy)
            .all()
        )

        self.assertCountEqual(expected, query)

    def test_is_located_at_host_location(self):
        self.facts.add([
            terms.x_is_the_y_of_z(
                value='window01',
                property='host',
                entity='device01'),
            terms.x_is_the_y_of_z(
                value='kitchen',
                property='location',
                entity='window01')
        ])

        self.load_knowledge(self.facts)
        solution = self.get_solution()

        expected = [
            terms.x_is_the_y_of_z(
                value='kitchen',
                property='location',
                entity='device01')
        ]

        query = list(solution
            .query(terms.x_is_the_y_of_z)
            .where(
                terms.x_is_the_y_of_z.entity == 'device01',
                terms.x_is_the_y_of_z.property == 'location')
            .all()
        )

        self.assertCountEqual(expected, query)

    def test_host_is_located_at_device_location(self):
        self.facts.add([
            terms.x_is_the_y_of_z(
                value='window01',
                property='host',
                entity='device01'),
            terms.x_is_the_y_of_z(
                value='kitchen',
                property='location',
                entity='device01')
        ])

        self.load_knowledge(self.facts)
        solution = self.get_solution()

        expected = [
            terms.x_is_the_y_of_z(
                value='kitchen',
                property='location',
                entity='window01')
        ]

        query = list(solution
            .query(terms.x_is_the_y_of_z)
            .where(
                terms.x_is_the_y_of_z.entity == 'window01',
                terms.x_is_the_y_of_z.property == 'location')
            .all()
        )

        self.assertCountEqual(expected, query)

class Sensor(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup(
            'src/sosa_engine.lp',
            'src/engine.lp',
            'src/kb/observation.lp'
        )

        facts = FactBase([
            terms.makesObservationKlass(
                klass='_motionSensor_',
                observation_klass='movement'
            ),
            terms.Device(
                id='motion_sensor01',
                klass='_motionSensor_'),
            terms.x_is_the_y_of_z(
                value='kitchen',
                property='location',
                entity='motion_sensor01')
        ])

        self.load_knowledge(facts)

    def test_observation_observedProperty_equals_klassObservesProperty(self):
        solution = self.get_solution()

        klass_property_query = list(solution
            .query(terms.klassObservesProperty)
            .all()
        )

        self.assertEqual(len(klass_property_query), 1)
        klassObservesProperty = klass_property_query[0]

        property_query = list(solution
            .query(terms.observedProperty)
            .all()
        )

        self.assertEqual(len(property_query), 1)
        observedProperty = property_query[0]

        self.assertEqual(
            observedProperty.observable_property,
            klassObservesProperty.observable_property
        )

    def test_observedProperty_is_a_property_of_the_sensor_featureOfInterest(self):
        solution = self.get_solution()

        expected = [
            terms.hasProperty(
                feature_of_interest='kitchen',
                property='motion')
        ]

        query = list(solution
            .query(terms.hasProperty)
            .all()
        )

        self.assertCountEqual(expected, query)


class Actuator(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup(
            'src/sosa_engine.lp',
            'src/engine.lp',
            'src/kb/actuation.lp'
        )

        facts = FactBase([
            terms.makesActuationKlass(
                klass='_smartBulb_',
                actuation_klass='illuminate'
            ),
            terms.Device(
                id='smart_bulb01',
                klass='_smartBulb_'),
            terms.x_is_the_y_of_z(
                value='kitchen',
                property='location',
                entity='smart_bulb01')
        ])

        self.load_knowledge(facts)

    def test_actuation_actsOnProperty_equals_klassActsOnProperty(self):
        solution = self.get_solution()

        klass_property_query = list(solution
            .query(terms.klassActsOnProperty)
            .all()
        )

        self.assertEqual(len(klass_property_query), 1)
        klassActsOnProperty = klass_property_query[0]

        property_query = list(solution
            .query(terms.actsOnProperty)
            .all()
        )

        self.assertEqual(len(property_query), 1)
        actsOnProperty = property_query[0]

        self.assertEqual(
            actsOnProperty.actuatable_property,
            klassActsOnProperty.actuatable_property
        )

    def test_actsOnProperty_is_a_property_of_the_actuator_featureOfInterest(self):
        solution = self.get_solution()

        expected = [
            terms.hasProperty(
                feature_of_interest='kitchen',
                property='illumination')
        ]

        query = list(solution
            .query(terms.hasProperty)
            .all()
        )

        self.assertCountEqual(expected, query)


class MotionSensor(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup(
            'src/sosa_engine.lp',
            'src/engine.lp',
            'src/kb/sensor.lp',
            'src/kb/observation.lp',
        )

        facts = FactBase([
            terms.Device(
                id='motion_sensor01',
                klass='_motionSensor_'),
            terms.x_is_the_y_of_z(
                value='kitchen',
                property='location',
                entity='motion_sensor01')
        ])

        self.load_knowledge(facts)

    def test_is_a_sensor(self):
        solution = self.get_solution()

        query = list(solution
            .query(terms.Sensor)
            .where(terms.Sensor.id == 'motion_sensor01')
            .all()
        )

        self.assertEqual(len(query), 1)

    def test_observes_motion(self):
        solution = self.get_solution()

        expected = [
            terms.observes(
                sensor='motion_sensor01',
                observable_property='motion')
        ]

        query = list(solution
            .query(terms.observes)
            .all()
        )

        self.assertCountEqual(expected, query)

    def test_makesObservation_of_the_movement_klass(self):
        solution = self.get_solution()

        expected = [
            terms.makesObservation(
                sensor='motion_sensor01',
                observation=terms.ActID(
                    device='motion_sensor01',
                    act='movement')
                )
        ]

        query = list(solution
            .query(terms.makesObservation)
            .all()
        )

        self.assertEqual(expected, query)

    def test_observation_observedProperty_is_motion(self):
        solution = self.get_solution()

        expected = [
            terms.observedProperty(
                observation=terms.ActID(
                    device='motion_sensor01',
                    act='movement'),
                observable_property='motion')
        ]

        query = list(solution
            .query(terms.observedProperty)
            .all()
        )

        self.assertCountEqual(expected, query)

    def test_isHostedBy_its_location_by_default(self):
        solution = self.get_solution()

        expected = [
            terms.isHostedBy(
                hosted='motion_sensor01',
                platform='kitchen')
        ]

        query = list(solution
            .query(terms.isHostedBy)
            .all()
        )

        self.assertCountEqual(expected, query)

    def test_host_is_the_observation_featureOfInterest(self):
        solution = self.get_solution()

        expected = [
            terms.hasFeatureOfInterest(
                act=terms.ActID(device='motion_sensor01', act='movement'),
                feature_of_interest='kitchen')
        ]

        query = list(solution
            .query(terms.hasFeatureOfInterest)
            .all()
        )

        self.assertCountEqual(expected, query)

    def test_motion_is_a_host_property(self):
        solution = self.get_solution()

        expected = [
            terms.hasProperty(
                feature_of_interest='kitchen',
                property='motion')
        ]

        query = list(solution
            .query(terms.hasProperty)
            .all()
        )

        self.assertCountEqual(expected, query)

    def test_movement_observation_hasResult_thereIsMovement(self):
        solution = self.get_solution()

        expected = [
            terms.hasResult(
                act=terms.ActID(device='motion_sensor01', act='movement'),
                result="there's movement")
        ]

        query = list(solution
            .query(terms.hasResult)
            .all()
        )

        self.assertCountEqual(expected, query)

    def test_movement_observation_hasSimpleResult_true(self):
        solution = self.get_solution()

        expected = [
            terms.hasSimpleResult(
                act=terms.ActID(device='motion_sensor01', act='movement'),
                result='true')
        ]

        query = list(solution
            .query(terms.hasSimpleResult)
            .all()
        )

        self.assertCountEqual(expected, query)


class BrokenWindowSensor(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup(
            'src/sosa_engine.lp',
            'src/engine.lp',
            'src/kb/sensor.lp',
            'src/kb/observation.lp',
        )

        facts = FactBase([
            terms.Device(
                id='broken_window_sensor01',
                klass='_brokenWindowSensor_'),
            terms.x_is_the_y_of_z(
                value='kitchen',
                property='location',
                entity='broken_window_sensor01'),
            terms.x_is_the_y_of_z(
                value='window01',
                property='host',
                entity='broken_window_sensor01')
        ])

        self.load_knowledge(facts)

    def test_is_a_sensor(self):
        solution = self.get_solution()

        query = list(solution
            .query(terms.Sensor)
            .where(terms.Sensor.id == 'broken_window_sensor01')
            .all()
        )

        self.assertEqual(len(query), 1)

    def test_observes_integrity(self):
        solution = self.get_solution()

        expected = [
            terms.observes(
                sensor='broken_window_sensor01',
                observable_property='integrity')
        ]

        query = list(solution
            .query(terms.observes)
            .all()
        )

        self.assertCountEqual(expected, query)

    def test_makesObservation_of_the_isBroken_klass(self):
        solution = self.get_solution()

        expected = [
            terms.makesObservation(
                sensor='broken_window_sensor01',
                observation=terms.ActID(
                    device='broken_window_sensor01',
                    act='isBroken')
                )
        ]

        query = list(solution
            .query(terms.makesObservation)
            .all()
        )

        self.assertEqual(expected, query)

    def test_observation_observedProperty_is_integrity(self):
        solution = self.get_solution()

        expected = [
            terms.observedProperty(
                observation=terms.ActID(
                    device='broken_window_sensor01',
                    act='isBroken'),
                observable_property='integrity')
        ]

        query = list(solution
            .query(terms.observedProperty)
            .all()
        )

        self.assertCountEqual(expected, query)

    def test_isHostedBy_a_window(self):
        solution = self.get_solution()

        expected = [
            terms.isHostedBy(
                hosted='broken_window_sensor01',
                platform='window01')
        ]

        query = list(solution
            .query(terms.isHostedBy)
            .all()
        )

        self.assertCountEqual(expected, query)

    def test_host_is_the_observation_featureOfInterest(self):
        solution = self.get_solution()

        expected = [
            terms.hasFeatureOfInterest(
                act=terms.ActID(device='broken_window_sensor01', act='isBroken'),
                feature_of_interest='window01')
        ]

        query = list(solution
            .query(terms.hasFeatureOfInterest)
            .all()
        )

        self.assertCountEqual(expected, query)

    def test_integrity_is_a_host_property(self):
        solution = self.get_solution()

        expected = [
            terms.hasProperty(
                feature_of_interest='window01',
                property='integrity')
        ]

        query = list(solution
            .query(terms.hasProperty)
            .all()
        )

        self.assertCountEqual(expected, query)

    def test_isBroken_observation_hasResult_isBroken(self):
        solution = self.get_solution()

        expected = [
            terms.hasResult(
                act=terms.ActID(device='broken_window_sensor01', act='isBroken'),
                result='is broken')
        ]

        query = list(solution
            .query(terms.hasResult)
            .all()
        )

        self.assertCountEqual(expected, query)

    def test_isBroken_observation_hasSimpleResult_true(self):
        solution = self.get_solution()

        expected = [
            terms.hasSimpleResult(
                act=terms.ActID(device='broken_window_sensor01', act='isBroken'),
                result='true')
        ]

        query = list(solution
            .query(terms.hasSimpleResult)
            .all()
        )

        self.assertCountEqual(expected, query)


class SmartBulb(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup(
            'src/sosa_engine.lp',
            'src/engine.lp',
            'src/kb/actuator.lp',
            'src/kb/actuation.lp',
        )

        facts = FactBase([
            terms.Device(
                id='smart_bulb01',
                klass='_smartBulb_'),
            terms.x_is_the_y_of_z(
                value='kitchen',
                property='location',
                entity='smart_bulb01')
        ])

        self.load_knowledge(facts)

    def test_is_an_actuator(self):
        solution = self.get_solution()

        query = list(solution
            .query(terms.Actuator)
            .where(terms.Actuator.id == 'smart_bulb01')
            .all()
        )

        self.assertEqual(len(query), 1)

    def test_makesActuation_of_the_illuminate_klass(self):
        solution = self.get_solution()

        expected = [
            terms.makesActuation(
                actuator='smart_bulb01',
                actuation=terms.ActID(
                    device='smart_bulb01',
                    act='illuminate')
                )
        ]

        query = list(solution
            .query(terms.makesActuation)
            .all()
        )

        self.assertEqual(expected, query)

    def test_actuation_actsOnProperty_illumination(self):
        solution = self.get_solution()

        expected = [
            terms.actsOnProperty(
                actuation=terms.ActID(
                    device='smart_bulb01',
                    act='illuminate'),
                actuatable_property='illumination')
        ]

        query = list(solution
            .query(terms.actsOnProperty)
            .all()
        )

        self.assertCountEqual(expected, query)

    def test_isHostedBy_its_location_by_default(self):
        solution = self.get_solution()

        expected = [
            terms.isHostedBy(
                hosted='smart_bulb01',
                platform='kitchen')
        ]

        query = list(solution
            .query(terms.isHostedBy)
            .all()
        )

        self.assertCountEqual(expected, query)

    def test_host_is_the_actuation_featureOfInterest(self):
        solution = self.get_solution()

        expected = [
            terms.hasFeatureOfInterest(
                act=terms.ActID(device='smart_bulb01', act='illuminate'),
                feature_of_interest='kitchen')
        ]

        query = list(solution
            .query(terms.hasFeatureOfInterest)
            .all()
        )

        self.assertCountEqual(expected, query)

    def test_illumination_is_a_host_property(self):
        solution = self.get_solution()

        expected = [
            terms.hasProperty(
                feature_of_interest='kitchen',
                property='illumination')
        ]

        query = list(solution
            .query(terms.hasProperty)
            .all()
        )

        self.assertCountEqual(expected, query)

    def test_illuminate_actuation_hasResult_illuminating(self):
        solution = self.get_solution()

        expected = [
            terms.hasResult(
                act=terms.ActID(device='smart_bulb01', act='illuminate'),
                result='illuminating')
        ]

        query = list(solution
            .query(terms.hasResult)
            .all()
        )

        self.assertCountEqual(expected, query)

    def test_illuminate_actuation_hasSimpleResult_true(self):
        solution = self.get_solution()

        expected = [
            terms.hasSimpleResult(
                act=terms.ActID(device='smart_bulb01', act='illuminate'),
                result='on')
        ]

        query = list(solution
            .query(terms.hasSimpleResult)
            .all()
        )

        self.assertCountEqual(expected, query)
