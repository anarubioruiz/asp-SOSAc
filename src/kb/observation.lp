% ---- MOVEMENT
observation(movement).
hasResult(movement, "there's movement").
hasSimpleResult(movement, "true").

klass_observesProperty(SENSOR_KLASS, motion)
    :- klass_makesObservation(SENSOR_KLASS, movement).

observation(noMovement).
hasResult(noMovement, "there's no movement").
hasSimpleResult(noMovement, "false").

klass_observesProperty(SENSOR_KLASS, motion)
    :- klass_makesObservation(SENSOR_KLASS, noMovement).

% ---- SOMETHING IS BROKEN
observation(isBroken).
hasResult(isBroken, "is broken").
hasSimpleResult(isBroken, "true").

klass_observesProperty(SENSOR_KLASS, integrity)
    :- klass_makesObservation(SENSOR_KLASS, isBroken).
