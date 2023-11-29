#!/usr/bin/env python3

import sys
import time

from clorm import FactBase

from sosac_clingo import SosaCClingo
import sosac_terms as terms

KB_NAMES = [
    'motionSensor',
    'brokenWindowSensor',
    'smartLight',
    'alarmSiren'
]

EVAL_SCENARIOS_DIR = 'eval_scenarios'
NUM_DEVICES = len(KB_NAMES)
DEVICES_WITH_HOST = [
    'brokenWindowSensor'
]


class Evaluation(SosaCClingo):
    def __init__(self, size_from, size_offset, num_cases, iterations, filename):
        self.filename = filename
        self.iterations = int(iterations)
        self.size_from = int(size_from)
        self.size_offset = int(size_offset)
        self.num_cases = int(num_cases)
        self.current_scenario = []
        self.current_size = 0

        with open(filename, 'w') as f:
            f.write('ROOMS; DEVICES; SOLUTION_SIZE; TIME; LOAD_TIME; GROUNDING_TIME; SOLUTION_TIME\n')

        self.setUp()
        self.evaluate()

    def setUp(self):
        self.clingo_setup(
            'src/sosac_engine.lp',
            'src/engine.lp',
            'src/kb/sensor.lp',
            'src/kb/observation.lp',
            'src/kb/actuator.lp',
            'src/kb/actuation.lp'
        )

    def evaluate(self):
        print('Evaluating performance...')

        for i in range(self.num_cases):
            print(f'----- Case {i+1}/{self.num_cases}')

            size = self.size_from + i * self.size_offset
            self.genScenario(size)
            facts = FactBase(self.current_scenario)
            self.current_size = size

            for i in range(self.iterations):
                print(f'Iteration {i+1}/{self.iterations}')
                start_time = time.time()

                self.ctrl.add_facts(facts)
                finished_load_time = time.time()
                self.ctrl.ground([("base", [])])
                finished_GROUNDING_TIME = time.time()

                solution = self.get_solution(
                    print_solution=False
                )

                end_time = time.time()

                self.saveResult(
                    size,
                    len(solution),
                    start_time,
                    finished_load_time,
                    finished_GROUNDING_TIME,
                    end_time
                )

    def genScenario(self, size):
        for i in range(self.current_size, size):
            for klass in KB_NAMES:
                instance = klass.replace('_', '')
                self.current_scenario.extend([
                    terms.sosac_Device(
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

    def saveResult(self, size, length, start_time, finished_load_time, finished_GROUNDING_TIME, end_time):
        exec_time = end_time - start_time
        load_time = finished_load_time - start_time
        GROUNDING_TIME = finished_GROUNDING_TIME - finished_load_time
        solution_time = end_time - finished_GROUNDING_TIME

        input = f'{size}; {NUM_DEVICES*size}; {length}; {exec_time}; {load_time}; {GROUNDING_TIME}; {solution_time}\n'
        with open(self.filename, 'a') as f:
            f.writelines(input)


Evaluation(*sys.argv[1:])
print('Done!')
