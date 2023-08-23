% ---- MOVEMENT
sosakc_observation(motion_ob).
sosakc_hasResult(motion_ob, "boolean").
sosakc_hasSimpleResult(motion_ob, "true").

sosakc_observesProperty(SENSOR_KLASS, motion)
    :- sosakc_makesObservation(SENSOR_KLASS, motion_ob).

sosakc_observation(not_motion_ob).
sosakc_hasResult(not_motion_ob, "boolean").
sosakc_hasSimpleResult(not_motion_ob, "false").

sosakc_observesProperty(SENSOR_KLASS, motion)
    :- sosakc_makesObservation(SENSOR_KLASS, not_motion_ob).

% ---- SOMETHING IS BROKEN
sosakc_observation(broken_ob).
sosakc_hasResult(broken_ob, "boolean").
sosakc_hasSimpleResult(broken_ob, "true").

sosakc_observesProperty(SENSOR_KLASS, broken)
    :- sosakc_makesObservation(SENSOR_KLASS, broken_ob).

% ---- SOMETHING IS OPEN OR CLOSED
sosakc_observation(open_ob).
sosakc_hasResult(open_ob, "boolean").
sosakc_hasSimpleResult(open_ob, "true").

sosakc_observesProperty(SENSOR_KLASS, open)
    :- sosakc_makesObservation(SENSOR_KLASS, open_ob).

sosakc_observation(closed_ob).
sosakc_hasResult(closed_ob, "boolean").
sosakc_hasSimpleResult(closed_ob, "false").

sosakc_observesProperty(SENSOR_KLASS, open)
    :- sosakc_makesObservation(SENSOR_KLASS, closed_ob).

% ---- ILLUMINANCE
sosakc_observation(illuminance_ob).
sosakc_hasResult(illuminance_ob, "number").

sosakc_observesProperty(SENSOR_KLASS, illuminance)
    :- sosakc_makesObservation(SENSOR_KLASS, illuminance_ob).

% ---- TEMPERATURE
sosakc_observation(temperature_ob).
sosakc_hasResult(temperature_ob, "number").

sosakc_observesProperty(SENSOR_KLASS, temperature)
    :- sosakc_makesObservation(SENSOR_KLASS, temperature_ob).
