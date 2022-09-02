observation(movement).
hasResult(movement, "there's movement").
hasSimpleResult(movement, "true").

klassObservesProperty(SENSOR_KLASS, motion)
    :- makesObservationKlass(SENSOR_KLASS, movement).

observation(noMovement).
hasResult(noMovement, "there's no movement").
hasSimpleResult(noMovement, "false").

klassObservesProperty(SENSOR_KLASS, motion)
    :- makesObservationKlass(SENSOR_KLASS, noMovement).
