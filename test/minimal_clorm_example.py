#!/usr/bin/env python3

from clorm import monkey; monkey.patch() # must call this before importing clingo
from clorm import Predicate, ConstantField, ComplexTerm, FactBase, IntegerField
from clingo import Control
import argparse


class InstanceOf(Predicate):
    instance = ConstantField
    klass = ConstantField

class PropertyValueOf(Predicate):
    property_ = ConstantField
    value = ConstantField
    instance = ConstantField

class stateOf(ComplexTerm):
    attr_value = ConstantField
    klass_ = ConstantField

# example: instruction(1,then,stateOf(up,blind_motor1))
class Instruction(Predicate):
    id_ = IntegerField
    type_ = ConstantField
    stateOf_ = stateOf.Field

def check_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f",
                        "--files",
                        required=True,
                        nargs="+",
                        help="ASP file programs")
    return parser.parse_args()

def main():
    args = check_args()

    ctrl = Control(unifier=[InstanceOf, PropertyValueOf, Instruction, stateOf])

    for file in args.files:
        ctrl.load(file)

    instance = FactBase([InstanceOf(instance="kitchen", klass="location"), 
                        InstanceOf(instance="motion_sensor1", klass="motion_sensor"), 
                        InstanceOf(instance="blind_motor1", klass="blind_motor"),
                        PropertyValueOf(property_="location", value="kitchen", instance="motion_sensor1"),
                        PropertyValueOf(property_="location", value="kitchen", instance="blind_motor1")])

    ctrl.add_facts(instance)
    ctrl.ground([("base", [])])

    solution = None

    def on_model(model):
        nonlocal solution
        # print(model.facts(atoms=True))
        solution = model.facts(atoms=True)

    ctrl.solve(on_model=on_model)
    if not solution:
        raise ValueError("No solution found")

    query = solution.query(Instruction)

    for instruction in query.all():
        print(instruction)


if __name__ == "__main__":
    main()
