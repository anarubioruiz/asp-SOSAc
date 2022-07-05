% GENERAL KNOWLEDGE
klass(location).
klass(sensor).

subclassOf(motion_sensor, sensor).
% targetPropertyOf(occupancy, location, motion_sensor).
% deviceStateImplies(motion_sensor, true, occupied). %REMOVE

transition(1).
transitionTrigger(1, motion_sensor, true).
transitionChange(1, location, occupied).

subclassOf(blind_motor, actuator).
subclassOf(smart_bulb, actuator).
% targetPropertyOf(lighting, location, blind_motor).
% deviceStateImplies(blind_motor, up, lit). %REMOVE

transition(2).
transitionTrigger(2, blind_motor, up).
transitionCondition(2, context, daylighted).
transitionChange(2, location, lit).  % The change always refers to a trigger property

transition(3).
transitionTrigger(3, smart_bulb, on).
transitionChange(3, location, lit).
