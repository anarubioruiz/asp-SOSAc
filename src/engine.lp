% ----------------------------------------------------
% ---- OBSERVATIONS ----------------------------------

% ---- Sensor

observableProperty(OBSERVABLE_PROPERTY) :- observes(_, OBSERVABLE_PROPERTY).
observation(OBSERVATION) :- makesObservation(_, OBSERVATION).

isObservedBy(OBSERVABLE_PROPERTY, SENSOR) :- observes(SENSOR, OBSERVABLE_PROPERTY).
madeBySensor(OBSERVATION, SENSOR) :- makesObservation(SENSOR, OBSERVATION).

% ---- ObservedProperty

sensor(SENSOR) :- isObservedBy(_, SENSOR).
observes(SENSOR, OBSERVABLE_PROPERTY) :- isObservedBy(OBSERVABLE_PROPERTY, SENSOR).

% ---- Observation

sensor(SENSOR) :- madeBySensor(_, SENSOR).
makesObservation(SENSOR, OBSERVATION) :- madeBySensor(OBSERVATION, SENSOR).

:- madeBySensor(OBSERVATION, SENSOR_1), madeBySensor(OBSERVATION, SENSOR_2), SENSOR_1 != SENSOR_2.

:- hasFeatureOfInterest(OBSERVATION, FEATURE_1), hasFeatureOfInterest(OBSERVATION, FEATURE_2), FEATURE_1 != FEATURE_2.


% %%%%%%%%%%%%%%%%%%%%%%%%

% actuator(ACTUATOR) :- madeByActuator(_, ACTUATOR).
% makesActuation(ACTUATOR, ACTUATION) :- madeByActuator(ACTUATION, ACTUATOR).
