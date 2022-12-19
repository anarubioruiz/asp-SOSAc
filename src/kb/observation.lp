% ---- MOVEMENT
observation(movement).
hasResult(movement, "true").

klass_observesProperty(SENSOR_KLASS, motion)
    :- klass_makesObservation(SENSOR_KLASS, movement).

observation(noMovement).
hasResult(noMovement, "false").

klass_observesProperty(SENSOR_KLASS, motion)
    :- klass_makesObservation(SENSOR_KLASS, noMovement).

% ---- SOMETHING IS BROKEN
observation(isBroken).
hasResult(isBroken, "true").

klass_observesProperty(SENSOR_KLASS, broken)
    :- klass_makesObservation(SENSOR_KLASS, isBroken).
