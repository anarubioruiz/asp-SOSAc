% ---- MOTION SENSOR
sosakc_makesObservation(motionSensor, motion_ob).
sosakc_makesObservation(motionSensor, not_motion_ob).

% ---- MOTION SENSOR
sosakc_makesObservation(occupancySensor, occuppied_ob).
sosakc_makesObservation(occupancySensor, not_occupied_ob).

%  ---- BROKEN WINDOW SENSOR
sosakc_makesObservation(brokenWindowSensor, broken_ob).
sosakc_hasFeatureOfInterest((brokenWindowSensor, broken_ob), host).

% ---- DOOR SENSOR
sosakc_makesObservation(doorSensor, open_ob).
sosakc_makesObservation(doorSensor, closed_ob).
sosakc_hasFeatureOfInterest((doorSensor, open_ob), host).
sosakc_hasFeatureOfInterest((doorSensor, closed_ob), host).

% ---- LIGHT SENSOR
sosakc_makesObservation(lightSensor, illuminance_ob).

% ---- TEMPERATURE SENSOR
sosakc_makesObservation(temperatureSensor, temperature_ob).
sosakc_makesObservation(infraredTemperatureSensor, temperature_ob).
