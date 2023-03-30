% ---- MOTION SENSOR
k_makesObservation(_motionSensor_, motion_ob).
k_makesObservation(_motionSensor_, not_motion_ob).

%  ---- BROKEN WINDOW SENSOR
k_makesObservation(_brokenWindowSensor_, broken_ob).
k_hasFeatureOfInterest((_brokenWindowSensor_, broken_ob), host).

% ---- DOOR SENSOR
k_makesObservation(_doorSensor_, open_ob).
k_makesObservation(_doorSensor_, closed_ob).
k_hasFeatureOfInterest((_doorSensor_, open_ob), host).
k_hasFeatureOfInterest((_doorSensor_, closed_ob), host).

% ---- LIGHT SENSOR
k_makesObservation(_lightSensor_, illuminance_ob).

% ---- TEMPERATURE SENSOR
k_makesObservation(_temperatureSensor_, temperature_ob).
k_makesObservation(_infraredTemperatureSensor_, temperature_ob).
