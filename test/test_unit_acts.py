from unittest import TestCase, skip

from clorm import FactBase
from clorm import monkey
monkey.patch() # must call this before importing clingo

from utils import ClingoTest
import terms


class Act(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup()

    # sosa:hasFeatureOfInterest - Domain: scott:Act, Range: sosa:FeatureOfInterest
    def test_Act_hasFeatureOfInterest_FeatureOfInterest(self):
        facts = FactBase([
            terms.hasFeatureOfInterest(
                act="observation01",
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
            terms.Act(id="observation01"),
            terms.FeatureOfInterest(id="kitchen")
        ]

        self.assertCountEqual(expected, query)


class FeatureOfInterest(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup()

    # sosa:isFeatureOfInterestOf - Domain: sosa:FeatureOfInterest, Range: scott:Act
    def test_FeatureOfInterest_isFeatureOfInterestOf_Act(self):
        facts = FactBase([
            terms.isFeatureOfInterestOf(
                feature_of_interest="kitchen",
                act="observation01")
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
            terms.Act(id="observation01"),
            terms.FeatureOfInterest(id="kitchen")
        ]

        self.assertCountEqual(expected, query)

    # sosa:isFeatureOfInterestOf inverse property of sosa:hasFeatureOfInterest
    def test_isFeatureOfInterestOf_inverse_of_hasFeatureOfInterest(self):
        facts = FactBase([
            terms.isFeatureOfInterestOf(
                feature_of_interest="kitchen",
                act="observation01")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        query = list(solution
            .query(terms.hasFeatureOfInterest)
            .all()
        )
        expected = [
            terms.hasFeatureOfInterest(
                act="observation01",
                feature_of_interest="kitchen")
        ]

        self.assertCountEqual(expected, query)
