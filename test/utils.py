from clorm import monkey
monkey.patch() # must call this before importing clingo
from clingo import Control

import terms


class ClingoTest:
    def clingo_setup(self):
        self.ctrl = Control(unifier=[
            terms.InstanceOf,
            terms.SubclassOf,
            terms.PropertyValueOf,
            terms.MemberOf,
            terms.TransitionTrigger,
            terms._TransitionTrigger,
            terms.TransitionChange,
            terms._TransitionChange,
            terms.instructionId,
            terms.stateOf,
            terms.Instruction,
            terms.Goal,
            terms.TransitionCondition,
            terms._TransitionCondition
        ])

        self.ctrl.load("src/engine.lp")

    def load_knowledge(self, facts):
        self.ctrl.add_facts(facts)
        self.ctrl.ground([("base", [])])

    def get_solution(self):
        solution = None

        def on_model(model):
            nonlocal solution
            solution = model.facts(atoms=True)
            for item in solution.query(terms.Instruction).all():
                print(item)
            # print(solution)

        self.ctrl.solve(on_model=on_model)
        return solution