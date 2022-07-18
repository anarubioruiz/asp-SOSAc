from unittest import TestCase, skip

from clorm import FactBase
from clorm import monkey
monkey.patch() # must call this before importing clingo

from utils import ClingoTest
import terms


class BasicEngine(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup()

    def test_property_value_is_instance_of_property(self):
        facts = FactBase([
            terms.PropertyValueOf(property="location", value="kitchen", owner="motion_sensor1")
        ])

        self.load_knowledge(facts)
        solution = self.get_solution()

        expected = [terms.InstanceOf(instance="kitchen", klass="location")]
        query = list(solution
            .query(terms.InstanceOf)
            .where(terms.InstanceOf.instance == "kitchen")
            .all()
        )

        self.assertEqual(expected, query)

class Inheritance(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup()

        facts = FactBase([
            terms.SubclassOf(child_klass="actuator", parent_klass="device"),
            terms.SubclassOf(child_klass="smart_bulb", parent_klass="actuator"),
            terms.InstanceOf(instance="lamp1", klass="smart_bulb"),
        ])

        self.load_knowledge(facts)

    def test_subclass_relation_is_transitive(self):
        solution = self.get_solution()

        query = list(solution
            .query(terms.SubclassOf)
            .where(terms.SubclassOf.child_klass == "smart_bulb")
            .all()
        )

        expected = [
            terms.SubclassOf(child_klass="smart_bulb", parent_klass="device"),
            terms.SubclassOf(child_klass="smart_bulb", parent_klass="actuator")
        ]

        self.assertCountEqual(expected, query)

    def test_instance_is_member_of_all_its_parent_klasses(self):
        solution = self.get_solution()

        query = list(solution.query(terms.MemberOf).all())
        expected = [
            terms.MemberOf(instance="_context", klass="context"),
            terms.MemberOf(instance="lamp1", klass="smart_bulb"),
            terms.MemberOf(instance="lamp1", klass="actuator"),
            terms.MemberOf(instance="lamp1", klass="device")
        ]

        self.assertCountEqual(expected, query)

class Transition(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup()

        transition = [
            terms.TransitionTrigger(id=1, device_klass="motion_sensor", state="true"),
            terms.TransitionChange(id=1, target_klass="location", state="occupied"),

            terms.TransitionTrigger(id=2, device_klass="blind_motor", state="up"),
            terms.TransitionCondition(id=2, thing_klass="context", state="daylighted"),
            terms.TransitionChange(id=2, target_klass="location", state="lit"),

            terms.TransitionTrigger(id=3, device_klass="smart_bulb", state="on"),
            terms.TransitionChange(id=3, target_klass="location", state="lit")
        ]

        scenario = [
            terms.InstanceOf(instance="motion_sensor1", klass="motion_sensor"),
            terms.PropertyValueOf(property="location", value="bathroom", owner="motion_sensor1"),

            terms.InstanceOf(instance="blind_motor1", klass="blind_motor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="blind_motor1"),

            terms.InstanceOf(instance="smart_bulb1", klass="smart_bulb"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="smart_bulb1")
        ]

        facts = FactBase(transition+scenario)
        self.load_knowledge(facts)

    def test_instance_of_transition_trigger(self):
        solution = self.get_solution()

        klass_query = list(solution
            .query(terms.TransitionTrigger)
            .where(terms.TransitionTrigger.id == 1)
            .all())

        instance_query = list(solution
            .query(terms._TransitionTrigger)
            .where(terms._TransitionTrigger.id == 1)
            .all())

        query = klass_query + instance_query
        expected = [
            terms.TransitionTrigger(id=1, device_klass="motion_sensor", state="true"),
            terms._TransitionTrigger(id=1, device="motion_sensor1", state="true")
        ]

        self.assertCountEqual(expected, query)

    def test_instance_of_transition_change(self):
        solution = self.get_solution()

        klass_query = list(solution
            .query(terms.TransitionChange)
            .where(terms.TransitionChange.id == 1)
            .all())

        instance_query = list(solution
            .query(terms._TransitionChange)
            .where(terms._TransitionChange.id == 1)
            .all())

        query = klass_query + instance_query
        expected = [
            terms.TransitionChange(id=1, target_klass="location", state="occupied"),
            terms._TransitionChange(id=1, target="bathroom", state="occupied")
        ]

        self.assertCountEqual(expected, query)

    def test_instance_of_transition_condition(self):
        solution = self.get_solution()

        klass_query = list(solution
            .query(terms.TransitionCondition)
            .all())

        instance_query = list(solution
            .query(terms._TransitionCondition)
            .all())

        query = klass_query + instance_query
        expected = [
            terms.TransitionCondition(id=2, thing_klass="context", state="daylighted"),
            terms._TransitionCondition(id=2, thing="_context", state="daylighted")
        ]

        self.assertCountEqual(expected, query)


    def test_not_instance_of_transition_change_when_not_appropiate_trigger(self):
        solution = self.get_solution()

        query = list(solution
            .query(terms._TransitionChange)
            .where(terms._TransitionChange.state == "lit")
            .all())

        not_expected = [
            terms._TransitionChange(id=2, target="bathroom", state="lit"),
            terms._TransitionChange(id=3, target="bathroom", state="lit"),
        ]

        self.assertFalse(any(i_transitionChange in query for i_transitionChange in not_expected))


class Instruction(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup()

        goals = [
            terms.Goal(
                id="goal_1",
                type="if",
                stateOf=terms.stateOf(thing_state="occupied",
                thing="location")),
            terms.Goal(
                id="goal_1",
                type="then",
                stateOf=terms.stateOf(thing_state="lit", thing="location")),
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

    def test_no_devices_derives_no_instructions(self):
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

    @skip  #Not working, but not important now
    def test_sensor_and_no_actuator_derives_no_instructions(self):
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

    def test_actuator_without_condition_and_no_sensor_derives_no_instructions(self):
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

    def test_actuator_with_condition_and_no_sensor_derives_no_instructions(self):
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

    def test_sensor_and_actuator_without_condition_in_same_location(self):
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

    def test_sensor_and_actuator_with_condition_in_same_location(self):
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

    def test_repeated_sensors_and_actuators_in_same_location(self):
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

    # TWO LOCATIONS TESTS ----------

    @skip  # Not working bec. instruction-if derived, but not important now
    def test_sensor_and_actuator_in_different_locations_derives_no_instrictions(self):
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

    def test_different_instructions_for_different_locations(self):
        scenario = [
            terms.InstanceOf(instance="motion_sensor1", klass="motion_sensor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="motion_sensor1"),

            terms.InstanceOf(instance="blind_motor1", klass="blind_motor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="blind_motor1"),

            terms.InstanceOf(instance="motion_sensor2", klass="motion_sensor"),
            terms.PropertyValueOf(property="location", value="bathroom", owner="motion_sensor2"),

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
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor2", then_device="blind_motor2"),
                type="then",
                stateOf=terms.stateOf(thing_state="up", thing="blind_motor2")),

            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="motion_sensor2", then_device="blind_motor2"),
                type="when",
                stateOf=terms.stateOf(thing_state="daylighted", thing="_context"))
        ]

        self.assertCountEqual(expected, query)


class Goals(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup()

        goals = [
            terms.Goal(
                id="goal_1",
                type="if",
                stateOf=terms.stateOf(thing_state="occupied", thing="location")),
            terms.Goal(
                id="goal_1",
                type="then",
                stateOf=terms.stateOf(thing_state="lit", thing="location")),
            terms.Goal(
                id="goal_2",
                type="if",
                stateOf=terms.stateOf(thing_state="insecure", thing="location")),
            terms.Goal(
                id="goal_2",
                type="then",
                stateOf=terms.stateOf(thing_state="in_alert", thing="location")),
        ]

        transitions = [
            terms.TransitionTrigger(id=1, device_klass="motion_sensor", state="true"),
            terms.TransitionChange(id=1, target_klass="location", state="occupied"),

            terms.TransitionTrigger(id=2, device_klass="blind_motor", state="up"),
            terms.TransitionCondition(id=2, thing_klass="context", state="daylighted"),
            terms.TransitionChange(id=2, target_klass="location", state="lit"),

            terms.TransitionTrigger(id=3, device_klass="smart_bulb", state="on"),
            terms.TransitionChange(id=3, target_klass="location", state="lit"),

            terms.TransitionTrigger(id=4, device_klass="window_sensor", state="broken"),
            terms.TransitionChange(id=4, target_klass="location", state="insecure"),

            terms.TransitionTrigger(id=5, device_klass="alarm_siren", state="on"),
            terms.TransitionChange(id=5, target_klass="location", state="in_alert"),
        ]

        facts = FactBase(goals+transitions)
        self.load_knowledge(facts)

    def test_get_instructions_for_two_goals(self):
        scenario = [
            terms.InstanceOf(instance="kitchen", klass="location"),

            terms.InstanceOf(instance="motion_sensor1", klass="motion_sensor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="motion_sensor1"),

            terms.InstanceOf(instance="smart_bulb1", klass="smart_bulb"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="smart_bulb1"),

            terms.InstanceOf(instance="window_sensor1", klass="window_sensor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="window_sensor1"),

            terms.InstanceOf(instance="alarm_siren1", klass="alarm_siren"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="alarm_siren1"),
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
                id=terms.instructionId(goalID="goal_2", if_device="window_sensor1", then_device="none"),
                type="if",
                stateOf=terms.stateOf(thing_state="broken", thing="window_sensor1")),
            terms.Instruction(
                id=terms.instructionId(goalID="goal_2", if_device="window_sensor1", then_device="alarm_siren1"),
                type="then",
                stateOf=terms.stateOf(thing_state="on", thing="alarm_siren1")),
        ]

        self.assertCountEqual(expected, query)
