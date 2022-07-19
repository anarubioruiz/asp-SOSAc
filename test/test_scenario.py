from unittest import TestCase, skip

from clorm import FactBase
from clorm import monkey
monkey.patch() # must call this before importing clingo

from utils import ClingoTest
import terms


class LitOccupiedLocations(TestCase, ClingoTest):
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

    def test_lit_with_smart_bulb(self):
        scenario = [
            terms.InstanceOf(instance="motion_sensor1", klass="motion_sensor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="motion_sensor1"),

            terms.InstanceOf(instance="smart_bulb1", klass="smart_bulb"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="smart_bulb1"),
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
        ]

        self.assertCountEqual(expected, query)

    def test_lit_with_daylight(self):
        scenario = [
            terms.InstanceOf(instance="motion_sensor1", klass="motion_sensor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="motion_sensor1"),

            terms.InstanceOf(instance="blind_motor1", klass="blind_motor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="blind_motor1"),
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
        ]

        self.assertCountEqual(expected, query)


class SecurityAlertLocationIsInsecure(TestCase, ClingoTest):
    def setUp(self):
        self.clingo_setup()

        goals = [
            terms.Goal(id="goal_1", type="if", stateOf=terms.stateOf(thing_state="insecure", thing="location")),
            terms.Goal(id="goal_1", type="then", stateOf=terms.stateOf(thing_state="in_alert", thing="location")),
        ]

        transitions = [
            terms.TransitionTrigger(id=1, device_klass="window_sensor", state="broken"),
            terms.TransitionChange(id=1, target_klass="location", state="insecure"),

            terms.TransitionTrigger(id=2, device_klass="alarm_siren", state="on"),
            terms.TransitionChange(id=2, target_klass="location", state="in_alert"),
        ]

        facts = FactBase(goals+transitions)
        self.load_knowledge(facts)

    def test_turn_on_alarm_siren_when_window_is_broken_in_same_location(self):
        scenario = [
            terms.InstanceOf(instance="kitchen", klass="location"),
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
                id=terms.instructionId(goalID="goal_1", if_device="window_sensor1", then_device="none"),
                type="if",
                stateOf=terms.stateOf(thing_state="broken", thing="window_sensor1")),

            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="window_sensor1", then_device="alarm_siren1"),
                type="then",
                stateOf=terms.stateOf(thing_state="on", thing="alarm_siren1")),
        ]

        self.assertCountEqual(expected, query)

    def test_turn_on_alarm_siren_when_window_is_broken_in_different_location(self):
        # TODO: Alarm sirent and the broken window don't need to
        # be in the same location

        scenario = [
            terms.InstanceOf(instance="kitchen", klass="location"),
            terms.InstanceOf(instance="corridor", klass="location"),
            terms.InstanceOf(instance="window_sensor1", klass="window_sensor"),
            terms.PropertyValueOf(property="location", value="kitchen", owner="window_sensor1"),
            terms.InstanceOf(instance="alarm_siren1", klass="alarm_siren"),
            terms.PropertyValueOf(property="location", value="corridor", owner="alarm_siren1"),
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
                id=terms.instructionId(goalID="goal_1", if_device="window_sensor1", then_device="none"),
                type="if",
                stateOf=terms.stateOf(thing_state="broken", thing="window_sensor1")),

            terms.Instruction(
                id=terms.instructionId(goalID="goal_1", if_device="window_sensor1", then_device="alarm_siren1"),
                type="then",
                stateOf=terms.stateOf(thing_state="on", thing="alarm_siren1")),
        ]

        self.assertCountEqual(expected, query)


    # 2. Room's window is open when nobody is in the room.
    #  --------------------------------------------------
    # To generate:
    # instruction(id, if, stateOf(open, window_sensor))
    # instruction(id, when, stateOf(false, motion_sensor))
    # instruction(id, then, stateOf(on, alarm_siren))
