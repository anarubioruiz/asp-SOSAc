#!/usr/bin/env python3

import sys
import time

from clorm import FactBase

from scott_clingo import ScottClingo
import scott_terms as terms

KB_NAMES = [
    '_motionSensor_',
    '_brokenWindowSensor_',
    # '_smartBulb_',
    # '_alarmSiren_'
]

NUM_DEVICES = len(KB_NAMES)
DEVICES_WITH_HOST = [
    '_brokenWindowSensor_'
]


class Evaluation(ScottClingo):
    def __init__(self, size_from, size_offset, num_cases, filename):
        self.size_from = int(size_from)
        self.size_offset = int(size_offset)
        self.num_cases = int(num_cases)
        self.file = open(filename, 'w')

        self.current_size = 0
        self.current_scenario = []

        self.file.write('FROM SIZE, OFFSET\n')
        self.file.write(f'{self.size_from}, {self.size_offset}\n\n')
        self.file.write('ROOMS, DEVICES, SIZE, TIME\n')

        self.setUp()
        self.evaluate()

    def setUp(self):
        self.clingo_setup(
            'sosa_engine.lp',
            'engine.lp',
            'kb/sensor.lp',
            'kb/observation.lp',
            'kb/actuator.lp',
            'kb/actuation.lp'
        )

    def evaluate(self):
        print('Evaluating performance...')

        for i in range(self.num_cases):
            size = self.size_from + i * self.size_offset
            self.genScenario(size)
            facts = FactBase(self.current_scenario)
            self.current_size = size

            start_time = time.time()

            self.load_knowledge(facts)
            solution = self.get_solution(
                print_solution=False
            )

            exec_time = time.time() - start_time

            self.saveResult(size, exec_time, len(solution))

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

    def saveResult(self, size, exec_time, length):
        input = f'{size}, {NUM_DEVICES*size}, {length}, {exec_time}\n'
        self.file.writelines(input)


Evaluation(*sys.argv[1:])
print('Done!')
