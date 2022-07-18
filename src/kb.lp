% GENERAL KNOWLEDGE
klass(location).
klass(sensor).

subclassOf(motion_sensor, sensor).

transition(1).
transitionTrigger(1, motion_sensor, true).
transitionChange(1, location, occupied).

subclassOf(blind_motor, actuator).
subclassOf(smart_bulb, actuator).

transition(2).
transitionTrigger(2, blind_motor, up).
transitionCondition(2, context, daylighted).
transitionChange(2, location, lit).  % The change always refers to a trigger property

transition(3).
transitionTrigger(3, smart_bulb, on).
transitionChange(3, location, lit).

transition(4).
transitionTrigger(4, window_sensor, broken).
transitionChange(4, location, insecure).

transition(5).
transitionTrigger(5, alarm_siren, on).
transitionChange(5, location, in_alert).

%

% transition(4).
% transitionTrigger(4, window_sensor, open).
% transitionCondition(4, location, unoccupied).
% transitionChange(4, location, insecure).

% transition(5).
% transitionTrigger(5, alarm_siren, on).
% transitionChange(5, home, in_alert).

%
