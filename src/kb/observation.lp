% ---- MOVEMENT
k_observation(motion_ob).
k_hasResult(motion_ob, "boolean").
k_hasSimpleResult(motion_ob, "true").

k_observesProperty(SENSOR_KLASS, motion)
    :- k_makesObservation(SENSOR_KLASS, motion_ob).

k_observation(not_motion_ob).
k_hasResult(not_motion_ob, "boolean").
k_hasSimpleResult(not_motion_ob, "false").

k_observesProperty(SENSOR_KLASS, motion)
    :- k_makesObservation(SENSOR_KLASS, not_motion_ob).

% ---- SOMETHING IS BROKEN
k_observation(broken_ob).
k_hasResult(broken_ob, "boolean").
k_hasSimpleResult(broken_ob, "true").

k_observesProperty(SENSOR_KLASS, broken)
    :- k_makesObservation(SENSOR_KLASS, broken_ob).

% ---- SOMETHING IS OPEN OR CLOSED
k_observation(open_ob).
k_hasResult(open_ob, "boolean").
k_hasSimpleResult(open_ob, "true").

k_observesProperty(SENSOR_KLASS, open)
    :- k_makesObservation(SENSOR_KLASS, open_ob).

k_observation(closed_ob).
k_hasResult(closed_ob, "boolean").
k_hasSimpleResult(closed_ob, "false").

k_observesProperty(SENSOR_KLASS, open)
    :- k_makesObservation(SENSOR_KLASS, closed_ob).

% ---- ILLUMINANCE
k_observation(illuminance_ob).
k_hasResult(illuminance_ob, "number").

k_observesProperty(SENSOR_KLASS, illuminance)
    :- k_makesObservation(SENSOR_KLASS, illuminance_ob).

% ---- TEMPERATURE
k_observation(temperature_ob).
k_hasResult(temperature_ob, "number").

k_observesProperty(SENSOR_KLASS, temperature)
    :- k_makesObservation(SENSOR_KLASS, temperature_ob).
