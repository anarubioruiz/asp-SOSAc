from clorm import monkey
monkey.patch() # must call this before importing clingo
from clingo import Control

import sosac_terms as terms


class SosaCClingo:
    def clingo_setup(self, *files):
        self.ctrl = Control(unifier=[
            terms.sosac_device,
            terms.x_is_the_y_of_z,
            terms.x_is_the_interest_of_z,

            terms.sosakc_observesProperty,
            terms.sosakc_makesObservation,
            terms.sosakc_actsOnProperty,
            terms.sosakc_makesActuation,
            terms.sosakc_hasFeatureOfInterest,

            # CLINGO TERMS ---------

            terms.sosac_sensor,
            terms.sosac_observableProperty,
            terms.sosac_observation,
            terms.Act,
            terms.sosac_actuator,
            terms.sosac_actuation,
            terms.sosac_actuatableProperty,
            terms.sosac_featureOfInterest,
            terms.sosac_result,
            terms.sosac_platform,

            terms.sosac_isObservedBy,
            terms.sosac_observes,
            terms.sosac_makesObservation,
            terms.sosac_madeBySensor,
            terms.sosac_observedProperty,
            terms.sosac_makesActuation,
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
