% ---- MOVEMENT
observation(motion_ob).
hasResult(motion_ob, boolean).
hasSimpleResult(motion_ob, "true").

klass_observesProperty(SENSOR_KLASS, motion)
    :- klass_makesObservation(SENSOR_KLASS, motion_ob).

observation(not_motion_ob).
hasResult(not_motion_ob, boolean).
hasSimpleResult(not_motion_ob, "false").

klass_observesProperty(SENSOR_KLASS, motion)
    :- klass_makesObservation(SENSOR_KLASS, not_motion_ob).

% ---- SOMETHING IS BROKEN
observation(broken_ob).
hasResult(broken_ob, boolean).
hasSimpleResult(broken_ob, "true").

klass_observesProperty(SENSOR_KLASS, broken)
    :- klass_makesObservation(SENSOR_KLASS, broken_ob).

% ---- SOMETHING IS OPEN OR CLOSED
observation(open_ob).
hasResult(open_ob, boolean).
hasSimpleResult(open_ob, "true").

klass_observesProperty(SENSOR_KLASS, open)
    :- klass_makesObservation(SENSOR_KLASS, open_ob).

observation(closed_ob).
hasResult(closed_ob, boolean).
hasSimpleResult(closed_ob, "false").

klass_observesProperty(SENSOR_KLASS, open)
    :- klass_makesObservation(SENSOR_KLASS, closed_ob).

% ---- ILLUMINANCE
observation(illuminance_ob).
hasResult(illuminance_ob, number).

klass_observesProperty(SENSOR_KLASS, illuminance)
    :- klass_makesObservation(SENSOR_KLASS, illuminance_ob).

% ---- TEMPERATURE
observation(temperature_ob).
hasResult(temperature_ob, number).

klass_observesProperty(SENSOR_KLASS, temperature)
    :- klass_makesObservation(SENSOR_KLASS, temperature_ob).
