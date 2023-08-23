% ---- MOTION SENSOR
sosakc_makesObservation(_motionSensor_, motion_ob).
sosakc_makesObservation(_motionSensor_, not_motion_ob).

%  ---- BROKEN WINDOW SENSOR
sosakc_makesObservation(_brokenWindowSensor_, broken_ob).
sosakc_hasFeatureOfInterest((_brokenWindowSensor_, broken_ob), host).

% ---- DOOR SENSOR
sosakc_makesObservation(_doorSensor_, open_ob).
sosakc_makesObservation(_doorSensor_, closed_ob).
sosakc_hasFeatureOfInterest((_doorSensor_, open_ob), host).
sosakc_hasFeatureOfInterest((_doorSensor_, closed_ob), host).

% ---- LIGHT SENSOR
sosakc_makesObservation(_lightSensor_, illuminance_ob).

% ---- TEMPERATURE SENSOR
sosakc_makesObservation(_temperatureSensor_, temperature_ob).
sosakc_makesObservation(_infraredTemperatureSensor_, temperature_ob).
