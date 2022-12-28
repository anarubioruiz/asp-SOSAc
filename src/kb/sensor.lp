% ---- MOTION SENSOR
klass_makesObservation(_motionSensor_, movement).

%  ---- BROKEN WINDOW SENSOR
klass_makesObservation(_brokenWindowSensor_, isBroken).
klass_hasFeatureOfInterest((_brokenWindowSensor_, isBroken), host).

% ---- DOOR SENSOR
klass_makesObservation(_doorSensor_, open).
klass_makesObservation(_doorSensor_, closed).
klass_hasFeatureOfInterest((_doorSensor_, open), host).
klass_hasFeatureOfInterest((_doorSensor_, closed), host).
