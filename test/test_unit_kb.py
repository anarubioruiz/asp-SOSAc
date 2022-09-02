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

        facts = FactBase([
            terms.Device(
                id="device01",
                klass="ANY"),
            terms.locatedAt(
                entity='device01',
                location='kitchen')
        ])

        self.load_knowledge(facts)

    def test_isHostedBy_its_location_by_default(self):
        solution = self.get_solution()

        expected = [
            terms.isHostedBy(
                hosted="device01",
                platform='kitchen')
        ]

        query = list(solution
            .query(terms.isHostedBy)
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
            # 'src/python.lp'
        )

        facts = FactBase([
            terms.Device(
                id="motion_sensor01",
                klass="_motionSensor_"),
            terms.locatedAt(
                entity='motion_sensor01',
                location='kitchen')
        ])

        self.load_knowledge(facts)

    def test_is_a_sensor(self):
        solution = self.get_solution()

        query = list(solution
            .query(terms.Sensor)
            .where(terms.Sensor.id == "motion_sensor01")
            .all()
        )

        self.assertEqual(len(query), 1)

    def test_observes_motion(self):
        solution = self.get_solution()

        query = list(solution
            .query(terms.observes)
            .where(terms.observes.sensor == "motion_sensor01")
            .all()
        )

        self.assertEqual(len(query), 1)

    def test_makesObservation_of_the_type_related_to_klass(self):
        solution = self.get_solution()

        expected = [
            terms.makesObservation(
                sensor="motion_sensor01",
                observation=terms.ActID(
                    device="motion_sensor01",
                    act="movement")
                )
        ]

        query = list(solution
            .query(terms.makesObservation)
            .all()
        )

        self.assertCountEqual(expected, query)

    def test_observation_observedProperty_equals_property_observedBy_sensor(self):
        solution = self.get_solution()

        expected = [
            terms.observedProperty(
                observation=terms.ActID(
                    device="motion_sensor01",
                    act="movement"),
                observable_property="motion")
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
                hosted="motion_sensor01",
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
                act=terms.ActID(device="motion_sensor01", act="movement"),
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
                act=terms.ActID(device="motion_sensor01", act="movement"),
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
                act=terms.ActID(device="motion_sensor01", act="movement"),
                result="true")
        ]

        query = list(solution
            .query(terms.hasSimpleResult)
            .all()
        )

        self.assertCountEqual(expected, query)
