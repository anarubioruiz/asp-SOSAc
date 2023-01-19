% ---- MOTION SENSOR
klass_makesObservation(_motionSensor_, motion_ob).
klass_makesObservation(_motionSensor_, not_motion_ob).

%  ---- BROKEN WINDOW SENSOR
klass_makesObservation(_brokenWindowSensor_, broken_ob).
klass_hasFeatureOfInterest((_brokenWindowSensor_, broken_ob), host).

% ---- DOOR SENSOR
klass_makesObservation(_doorSensor_, open_ob).
klass_makesObservation(_doorSensor_, closed_ob).
klass_hasFeatureOfInterest((_doorSensor_, open_ob), host).
klass_hasFeatureOfInterest((_doorSensor_, closed_ob), host).

% ---- LIGHT SENSOR
klass_makesObservation(_lightSensor_, illuminance_ob).

% ---- TEMPERATURE SENSOR
klass_makesObservation(_temperatureSensor_, temperature_ob).
klass_makesObservation(_infraredTemperatureSensor_, temperature_ob).
