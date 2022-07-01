% GENERAL KNOWLEDGE
klass(location).
klass(sensor).

subclassOf(motion_sensor, sensor).
targetPropertyOf(occupancy, location, motion_sensor).
deviceStateImplies(motion_sensor, true, occupied).

transition(1).
antecedent(1, motion_sensor, true).
consecuent(1, location, occupied).

subclassOf(blind_motor, actuator).
targetPropertyOf(lighting, location, blind_motor).
deviceStateImplies(blind_motor, up, lit).

transition(2).
antecedent(2, blind_motor, up).
antecedent(2, context, daylighted).
consecuent(2, location, lit).
