observation(movement).
hasResult(movement, "there's movement").
hasSimpleResult(movement, "true").

observation(noMovement).
hasResult(noMovement, "there's no movement").
hasSimpleResult(noMovement, "false").

observes(DEVICE, motion) :- makesObservation(DEVICE, movement).
observes(DEVICE, motion) :- makesObservation(DEVICE, noMovement).
