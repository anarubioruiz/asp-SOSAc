from unittest import TestCase, skip

from clorm import FactBase
from clorm import monkey
monkey.patch() # must call this before importing clingo

from utils import ClingoTest
import terms


class MotionSensor(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup(
            'src/sosa_engine.lp',
            'src/kb/motion_sensor.lp',
            # 'src/python.lp'
        )

        facts = FactBase([
            terms.MotionSensor(
                id="motion_sensor01"),
            terms.locatedAt(
                entity='motion_sensor01',
                location='kitchen')
        ])

        self.load_knowledge(facts)

    def test_is_a_sensor(self):
        solution = self.get_solution()

        expected = [terms.Sensor(id="motion_sensor01")]
        query = list(solution
            .query(terms.Sensor)
            .all()
        )

        self.assertCountEqual(expected, query)

    def test_observes_motion(self):
        solution = self.get_solution()

        expected = [
            terms.observes(
                sensor="motion_sensor01",
                observable_property='motion')
        ]

        query = list(solution
            .query(terms.observes)
            .all()
        )

        self.assertCountEqual(expected, query)

    def test_hosted_by_its_location(self):
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

    def test_observation_created_when_host_is_known(self):
        solution = self.get_solution()

        query = list(solution
            .query(terms.makesObservation)
            .all()
        )

        self.assertEqual(len(query), 1)
        makesObservation = query[0]
        self.assertEqual(makesObservation.sensor, 'motion_sensor01')

    def test_host_is_the_observation_featureOfInterest(self):
        solution = self.get_solution()

        expected = [
            terms.hasFeatureOfInterest(
                act="motion_sensor01",
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
