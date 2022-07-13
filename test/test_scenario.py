from unittest import TestCase, skip

from clorm import FactBase
from clorm import monkey
monkey.patch() # must call this before importing clingo

from utils import ClingoTest
import terms


class OneLocationOneGoal(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup()

        goals = [
            terms.Goal(id="goal_1", type="if", stateOf=terms.stateOf(thing_state="occupied", thing="location")),
            terms.Goal(id="goal_1", type="then", stateOf=terms.stateOf(thing_state="lit", thing="location")),
        ]

        transitions = [
            terms.TransitionTrigger(id=1, device_klass="motion_sensor", state="true"),
            terms.TransitionChange(id=1, target_klass="location", state="occupied"),

            terms.TransitionTrigger(id=2, device_klass="blind_motor", state="up"),
            terms.TransitionCondition(id=2, thing_klass="context", state="daylighted"),
            terms.TransitionChange(id=2, target_klass="location", state="lit"),

            terms.TransitionTrigger(id=3, device_klass="smart_bulb", state="on"),
            terms.TransitionChange(id=3, target_klass="location", state="lit")
        ]

        facts = FactBase(goals+transitions)
        self.load_knowledge(facts)

    def test_no_devices(self):
        scenario = [
            terms.InstanceOf(instance="kitchen", klass="location")
        ]

        facts = FactBase(scenario)
        self.load_knowledge(facts)

        solution = self.get_solution()

        query = list(solution
            .query(terms.Instruction)
            .all()
        )

        self.assertEqual([], query)

    @skip
    def test_sensor_and_no_actuator(self):
        scenario = [
            terms.InstanceOf(instance="motion_sensor1", klass="motion_sensor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="motion_sensor1")
        ]

        facts = FactBase(scenario)
        self.load_knowledge(facts)

        solution = self.get_solution()

        query = list(solution
            .query(terms.Instruction)
            .all()
        )

        self.assertEqual([], query)

    def test_actuator_without_condition_and_no_sensor(self):
        scenario = [
            terms.InstanceOf(instance="smart_bulb1", klass="smart_bulb"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="smart_bulb1")
        ]

        facts = FactBase(scenario)
        self.load_knowledge(facts)

        solution = self.get_solution()

        query = list(solution
            .query(terms.Instruction)
            .all()
        )

        self.assertEqual([], query)

    def test_actuator_with_condition_and_no_sensor(self):
        scenario = [
            terms.InstanceOf(instance="blind_motor1", klass="blind_motor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="blind_motor1")
        ]

        facts = FactBase(scenario)
        self.load_knowledge(facts)

        solution = self.get_solution()

        query = list(solution
            .query(terms.Instruction)
            .all()
        )

        self.assertEqual([], query)

    def test_sensor_and_actuator_without_condition(self):
        scenario = [
            terms.InstanceOf(instance="motion_sensor1", klass="motion_sensor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="motion_sensor1"),

            terms.InstanceOf(instance="smart_bulb1", klass="smart_bulb"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="smart_bulb1")
        ]

        facts = FactBase(scenario)
        self.load_knowledge(facts)

        solution = self.get_solution()

        query = list(solution
            .query(terms.Instruction)
            .all()
        )

        expected = [
            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor1", then_device="none"),
                type="if",
                stateOf=terms.stateOf(thing_state="true", thing="motion_sensor1")),
            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor1", then_device="smart_bulb1"),
                type="then",
                stateOf=terms.stateOf(thing_state="on", thing="smart_bulb1"))
        ]

        self.assertCountEqual(expected, query)

    def test_sensor_and_actuator_with_condition(self):
        scenario = [
            terms.InstanceOf(instance="motion_sensor1", klass="motion_sensor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="motion_sensor1"),

            terms.InstanceOf(instance="blind_motor1", klass="blind_motor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="blind_motor1")
        ]

        facts = FactBase(scenario)
        self.load_knowledge(facts)

        solution = self.get_solution()

        query = list(solution
            .query(terms.Instruction)
            .all()
        )

        expected = [
            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor1", then_device="none"),
                type="if",
                stateOf=terms.stateOf(thing_state="true", thing="motion_sensor1")),
            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor1", then_device="blind_motor1"),
                type="then",
                stateOf=terms.stateOf(thing_state="up", thing="blind_motor1")),
            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor1", then_device="blind_motor1"),
                type="when",
                stateOf=terms.stateOf(thing_state="daylighted", thing="_context"))
        ]

        self.assertCountEqual(expected, query)

    def test_repeated_sensors_and_actuators(self):
        scenario = [
            terms.InstanceOf(instance="motion_sensor1", klass="motion_sensor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="motion_sensor1"),

            terms.InstanceOf(instance="motion_sensor2", klass="motion_sensor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="motion_sensor2"),

            terms.InstanceOf(instance="blind_motor1", klass="blind_motor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="blind_motor1"),

            terms.InstanceOf(instance="blind_motor2", klass="blind_motor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="blind_motor2")
        ]

        facts = FactBase(scenario)
        self.load_knowledge(facts)

        solution = self.get_solution()

        query = list(solution
            .query(terms.Instruction)
            .all()
        )

        expected = [
            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor1", then_device="none"),
                type="if",
                stateOf=terms.stateOf(thing_state="true", thing="motion_sensor1")),
            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor2", then_device="none"),
                type="if",
                stateOf=terms.stateOf(thing_state="true", thing="motion_sensor2")),

            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor1", then_device="blind_motor1"),
                type="then",
                stateOf=terms.stateOf(thing_state="up", thing="blind_motor1")),
            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor2", then_device="blind_motor1"),
                type="then",
                stateOf=terms.stateOf(thing_state="up", thing="blind_motor1")),
            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor1", then_device="blind_motor1"),
                type="when",
                stateOf=terms.stateOf(thing_state="daylighted", thing="_context")),
            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor2", then_device="blind_motor1"),
                type="when",
                stateOf=terms.stateOf(thing_state="daylighted", thing="_context")),

            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor2", then_device="blind_motor2"),
                type="then",
                stateOf=terms.stateOf(thing_state="up", thing="blind_motor2")),
            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor1", then_device="blind_motor2"),
                type="then",
                stateOf=terms.stateOf(thing_state="up", thing="blind_motor2")),
            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor2", then_device="blind_motor2"),
                type="when",
                stateOf=terms.stateOf(thing_state="daylighted", thing="_context")),
            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor1", then_device="blind_motor2"),
                type="when",
                stateOf=terms.stateOf(thing_state="daylighted", thing="_context"))
        ]

        self.assertCountEqual(expected, query)


class TwoLocationOneGoal(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup()

        goals = [
            terms.Goal(id="goal_1", type="if", stateOf=terms.stateOf(thing_state="occupied", thing="location")),
            terms.Goal(id="goal_1", type="then", stateOf=terms.stateOf(thing_state="lit", thing="location")),
        ]

        transitions = [
            terms.TransitionTrigger(id=1, device_klass="motion_sensor", state="true"),
            terms.TransitionChange(id=1, target_klass="location", state="occupied"),

            terms.TransitionTrigger(id=2, device_klass="blind_motor", state="up"),
            terms.TransitionCondition(id=2, thing_klass="context", state="daylighted"),
            terms.TransitionChange(id=2, target_klass="location", state="lit"),

            terms.TransitionTrigger(id=3, device_klass="smart_bulb", state="on"),
            terms.TransitionChange(id=3, target_klass="location", state="lit")
        ]

        facts = FactBase(goals+transitions)
        self.load_knowledge(facts)

    @skip
    def test_location1_sensor_location2_actuator_with_condition(self):
        scenario = [
            terms.InstanceOf(instance="motion_sensor1", klass="motion_sensor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="motion_sensor1"),

            terms.InstanceOf(instance="blind_motor1", klass="blind_motor"),
            terms.PropertyValueOf(property="location", value="bathroom", owner="blind_motor1")
        ]

        facts = FactBase(scenario)
        self.load_knowledge(facts)

        solution = self.get_solution()

        query = list(solution
            .query(terms.Instruction)
            .all()
        )

        self.assertCountEqual([], query)

    def test_location1_sensor_and_actuator_without_condition_location2_actuator_with_condition(self):
        scenario = [
            terms.InstanceOf(instance="motion_sensor1", klass="motion_sensor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="motion_sensor1"),

            terms.InstanceOf(instance="smart_bulb1", klass="smart_bulb"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="smart_bulb1"),

            terms.InstanceOf(instance="blind_motor1", klass="blind_motor"),
            terms.PropertyValueOf(property="location", value="bathroom", owner="blind_motor1")
        ]

        facts = FactBase(scenario)
        self.load_knowledge(facts)

        solution = self.get_solution()

        query = list(solution
            .query(terms.Instruction)
            .all()
        )

        expected = [
            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor1", then_device="none"),
                type="if",
                stateOf=terms.stateOf(thing_state="true", thing="motion_sensor1")),      

            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor1", then_device="smart_bulb1"),
                type="then",
                stateOf=terms.stateOf(thing_state="on", thing="smart_bulb1"))
        ]

        self.assertCountEqual(expected, query)

    def test_location1_sensor_and_actuator_without_condition_location2_sensor_and_actuator_with_condition(self):
        scenario = [
            terms.InstanceOf(instance="motion_sensor1", klass="motion_sensor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="motion_sensor1"),

            terms.InstanceOf(instance="smart_bulb1", klass="smart_bulb"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="smart_bulb1"),

            terms.InstanceOf(instance="motion_sensor2", klass="motion_sensor"),
            terms.PropertyValueOf(property="location", value="bathroom", owner="motion_sensor2"),

            terms.InstanceOf(instance="blind_motor1", klass="blind_motor"),
            terms.PropertyValueOf(property="location", value="bathroom", owner="blind_motor1")
        ]

        facts = FactBase(scenario)
        self.load_knowledge(facts)

        solution = self.get_solution()

        query = list(solution
            .query(terms.Instruction)
            .all()
        )

        expected = [
            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor1", then_device="none"),
                type="if",
                stateOf=terms.stateOf(thing_state="true", thing="motion_sensor1")),      

            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor1", then_device="smart_bulb1"),
                type="then",
                stateOf=terms.stateOf(thing_state="on", thing="smart_bulb1")),

            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor2", then_device="none"),
                type="if",
                stateOf=terms.stateOf(thing_state="true", thing="motion_sensor2")),      

            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor2", then_device="blind_motor1"),
                type="then",
                stateOf=terms.stateOf(thing_state="up", thing="blind_motor1")),

            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor2", then_device="blind_motor1"),
                type="when",
                stateOf=terms.stateOf(thing_state="daylighted", thing="_context"))
        ]

        self.assertCountEqual(expected, query)

    def test_location1_sensor_actuator_without_condition_and_actuator_with_condition_location2_no_device(self):
        scenario = [
            terms.InstanceOf(instance="motion_sensor1", klass="motion_sensor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="motion_sensor1"),

            terms.InstanceOf(instance="smart_bulb1", klass="smart_bulb"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="smart_bulb1"),

            terms.InstanceOf(instance="blind_motor1", klass="blind_motor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="blind_motor1")
        ]

        facts = FactBase(scenario)
        self.load_knowledge(facts)

        solution = self.get_solution()

        query = list(solution
            .query(terms.Instruction)
            .all()
        )

        expected = [
            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor1", then_device="none"),
                type="if",
                stateOf=terms.stateOf(thing_state="true", thing="motion_sensor1")),      

            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor1", then_device="smart_bulb1"),
                type="then",
                stateOf=terms.stateOf(thing_state="on", thing="smart_bulb1")),     

            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor1", then_device="blind_motor1"),
                type="then",
                stateOf=terms.stateOf(thing_state="up", thing="blind_motor1")),

            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor1", then_device="blind_motor1"),
                type="when",
                stateOf=terms.stateOf(thing_state="daylighted", thing="_context"))
        ]

        self.assertCountEqual(expected, query)

    def test_location1_sensor_actuator_without_condition_and_actuator_with_condition_location2_sensor_actuator_without_condition_and_actuator_with_condition(self):
        scenario = [
            terms.InstanceOf(instance="motion_sensor1", klass="motion_sensor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="motion_sensor1"),

            terms.InstanceOf(instance="smart_bulb1", klass="smart_bulb"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="smart_bulb1"),

            terms.InstanceOf(instance="blind_motor1", klass="blind_motor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="blind_motor1"),


            terms.InstanceOf(instance="motion_sensor2", klass="motion_sensor"),
            terms.PropertyValueOf(property="location", value="bathroom", owner="motion_sensor2"),

            terms.InstanceOf(instance="smart_bulb2", klass="smart_bulb"),
            terms.PropertyValueOf(property="location", value="bathroom", owner="smart_bulb2"),

            terms.InstanceOf(instance="blind_motor2", klass="blind_motor"),
            terms.PropertyValueOf(property="location", value="bathroom", owner="blind_motor2")
        ]

        facts = FactBase(scenario)
        self.load_knowledge(facts)

        solution = self.get_solution()

        query = list(solution
            .query(terms.Instruction)
            .all()
        )

        expected = [
            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor1", then_device="none"),
                type="if",
                stateOf=terms.stateOf(thing_state="true", thing="motion_sensor1")),      

            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor1", then_device="smart_bulb1"),
                type="then",
                stateOf=terms.stateOf(thing_state="on", thing="smart_bulb1")),

            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor1", then_device="blind_motor1"),
                type="then",
                stateOf=terms.stateOf(thing_state="up", thing="blind_motor1")),

            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor1", then_device="blind_motor1"),
                type="when",
                stateOf=terms.stateOf(thing_state="daylighted", thing="_context")),


            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor2", then_device="none"),
                type="if",
                stateOf=terms.stateOf(thing_state="true", thing="motion_sensor2")),      

            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor2", then_device="smart_bulb2"),
                type="then",
                stateOf=terms.stateOf(thing_state="on", thing="smart_bulb2")),

            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor2", then_device="blind_motor2"),
                type="then",
                stateOf=terms.stateOf(thing_state="up", thing="blind_motor2")),

            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor2", then_device="blind_motor2"),
                type="when",
                stateOf=terms.stateOf(thing_state="daylighted", thing="_context"))
        ]

        self.assertCountEqual(expected, query)



# Basics TestCase:
# 1 GOAL:
# 1 location, 1 motion_sensor
# 1 location, 1 smart_bulb, 1 blind_motor
# 1 location, 1 motion_sensor, 1 smart_bulb, 1 blind_motor

# ScenarioA TestCase
# 1 GOAL:
# 2 location:
#    (el escenario que ya tenemos)

# ScenarioB TestCase
# 1 GOAL:
# 2 location:
#   - bathroom: 1 motion_sensor, 1 smart_bulb
#   - kitchen: 1 door_sensor, 1 smart_bulb

# Scenario C TestCase
# 2 GOAL:
#   - lit location when it is occupied
#   - notify user when location insecure
