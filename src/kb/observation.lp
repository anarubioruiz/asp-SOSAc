observation(movement).
hasResult(movement, "there's movement").
hasSimpleResult(movement, "true").

observation(noMovement).
hasResult(noMovement, "there's no movement").
hasSimpleResult(noMovement, "false").

klassObserves(SENSOR_KLASS, motion) :- makesObservationType(SENSOR_KLASS, movement).
klassObserves(SENSOR_KLASS, motion) :- makesObservationType(SENSOR_KLASS, noMovement).
