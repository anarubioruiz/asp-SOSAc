#!/usr/bin/env python3

import os
import sys
import time
import shutil

from clorm import FactBase

from scott_clingo import ScottClingo
import scott_terms as terms

KB_NAMES = [
    '_motionSensor_',
    '_brokenWindowSensor_',
    '_smartBulb_',
    '_alarmSiren_'
]

EVAL_SCENARIOS_DIR = 'eval_scenarios'
NUM_DEVICES = len(KB_NAMES)
DEVICES_WITH_HOST = [
    '_brokenWindowSensor_'
]


class Evaluation(ScottClingo):
    def __init__(self, size_from, size_offset, num_cases, filename):
        self.size_from = int(size_from)
        self.size_offset = int(size_offset)
        self.num_cases = int(num_cases)
        self.current_scenario = []
        self.current_size = 0

        self.file = open(filename, 'w')
        self.file.write('ROOMS; DEVICES; SIZE; TIME; LOAD_TIME; GROUND_TIME; SOLUTION_TIME\n')

        self.setUp()
        self.evaluate()

    def setUp(self):
        self.clingo_setup(
            'src/sosa_engine.lp',
            'src/engine.lp',
            'src/kb/sensor.lp',
            'src/kb/observation.lp',
            'src/kb/actuator.lp',
            'src/kb/actuation.lp'
        )

    def evaluate(self):
        print('Evaluating performance...')

        for i in range(self.num_cases):
            size = self.size_from + i * self.size_offset
            self.genScenario(size)
            facts = FactBase(self.current_scenario)
            self.current_size = size

            start_time = time.time()

            self.ctrl.add_facts(facts)
            finished_load_time = time.time()
            self.ctrl.ground([("base", [])])
            finished_ground_time = time.time()

            solution = self.get_solution(
                print_solution=False
            )

            end_time = time.time()

            self.saveResult(
                size,
                len(solution),
                start_time,
                finished_load_time,
                finished_ground_time,
                end_time
            )

        self.file.close()

    def genScenario(self, size):
        for i in range(self.current_size, size):
            for klass in KB_NAMES:
                instance = klass.replace('_', '')
                self.current_scenario.extend([
                    terms.Device(
                        id=f'{instance}_{i}',
                        klass=klass),
                    terms.x_is_the_y_of_z(
                        value=f'room_{i}',
                        property='location',
                        entity=f'{instance}_{i}')
                ])

                if klass in DEVICES_WITH_HOST:
                    self.current_scenario.extend([
                        terms.x_is_the_y_of_z(
                            value=f'host_{i}',
                            property='host',
                            entity=f'{instance}_{i}')
                    ])

    def saveResult(self, size, length, start_time, finished_load_time, finished_ground_time, end_time):
        exec_time = end_time - start_time
        load_time = finished_load_time - start_time
        ground_time = finished_ground_time - finished_load_time
        solution_time = end_time - finished_ground_time

        input = f'{size}; {NUM_DEVICES*size}; {length}; {exec_time}; {load_time}; {ground_time}; {solution_time}\n'
        self.file.writelines(input)


Evaluation(*sys.argv[1:])
print('Done!')
