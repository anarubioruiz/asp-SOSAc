from unittest import TestCase, skip

from clorm import FactBase
from clorm import monkey
monkey.patch() # must call this before importing clingo

from utils import ClingoTest
import terms


class InstanceInferences(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup(
            'src/sosa_engine.lp',
            'src/engine.lp',
        )

    def test_device_isHostedBy_its_location_by_default(self):
        facts = FactBase([
            terms.Device(
                id="motion_sensor01",
                klass="ANY"),
            terms.locatedAt(
                entity='motion_sensor01',
                location='kitchen')
        ])

        self.load_knowledge(facts)
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

    def test_observedProperty_is_a_property_of_the_sensor_featureOfInterest(self):
        facts = FactBase([
            terms.observes(
                sensor="motion_sensor01",
                observable_property="motion"),
            terms.makesObservation(
                sensor='motion_sensor01',
                observation=terms.ActID(
                    device="motion_sensor01",
                    act="observation01")),
            terms.hasFeatureOfInterest(
                act=terms.ActID(
                    device="motion_sensor01",
                    act="observation01"),
                feature_of_interest='kitchen'
            )
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [
            terms.hasProperty(
                feature_of_interest="kitchen",
                property='motion')
        ]

        query = list(solution
            .query(terms.hasProperty)
            .all()
        )

        self.assertCountEqual(expected, query)
