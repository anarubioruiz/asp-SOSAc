from clorm import monkey
monkey.patch() # must call this before importing clingo
from clingo import Control

import terms


class ClingoTest:
    def clingo_setup(self):
        self.ctrl = Control(unifier=[
            terms.Sensor,
            terms.ObservableProperty,
            terms.Observation,
            terms.Act,
            terms.Actuator,
            terms.Actuation,
            terms.ActuatableProperty,
            terms.FeatureOfInterest,
            terms.Result,
            terms.Platform,

            terms.isObservedBy,
            terms.observes,
            terms.makesObservation,
            terms.madeBySensor,
            terms.observedProperty,
            terms.makesActuation,
            terms.isActedOnBy,
            terms.madeByActuator,
            terms.actsOnProperty,
            terms.hasFeatureOfInterest,
            terms.isFeatureOfInterestOf,
            terms.hasResult,
            terms.isResultOf,
            terms.hasSimpleResult,
            terms.hosts,
            terms.isHostedBy
        ])

        self.ctrl.load("src/ssn-engine.lp")

    def load_knowledge(self, facts):
        self.ctrl.add_facts(facts)
        self.ctrl.ground([("base", [])])

    def get_solution(self):
        solution = None

        def on_model(model):
            nonlocal solution
            solution = model.facts(atoms=True)
            # for item in solution.query(term...).all():
            #     print(item)
            print(solution)

        self.ctrl.solve(on_model=on_model)
        return solution
