from clorm import monkey
monkey.patch() # must call this before importing clingo
from clingo import Control

import sosac_terms as terms


class SosaCClingo:
    def clingo_setup(self, *files):
        self.ctrl = Control(unifier=[
            terms.Device,
            terms.x_is_the_y_of_z,
            terms.x_is_the_interest_of_z,

            terms.k_observesProperty,
            terms.k_makesObservation,
            terms.k_actsOnProperty,
            terms.k_makesActuation,
            terms.k_hasFeatureOfInterest,

            # CLINGO TERMS ---------

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
            terms.isHostedBy,
            terms.hasProperty
        ])

        if not files:
            self.ctrl.load("src/engine.lp")
            self.ctrl.load("src/sosac_engine.lp")
            return

        for f in files:
            self.ctrl.load(f)

    def load_knowledge(self, facts):
        self.ctrl.add_facts(facts)
        self.ctrl.ground([("base", [])])

    def get_solution(self, print_solution=True):
        solution = None

        def on_model(model):
            nonlocal solution
            solution = model.facts(atoms=True)

            if print_solution:
                print(solution)

        self.ctrl.solve(on_model=on_model)
        return solution
