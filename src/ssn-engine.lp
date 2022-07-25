%  ---- Act

featureOfInterest(FEATURE) :- hasFeatureOfInterest(_, FEATURE).
isFeatureOfInterestOf(FEATURE, ACT) :- hasFeatureOfInterest(ACT, FEATURE).

:- hasFeatureOfInterest(OBSERVATION, FEATURE_1), hasFeatureOfInterest(OBSERVATION, FEATURE_2), FEATURE_1 != FEATURE_2.

% ---- FeatureOfInterest

act(ACT) :- isFeatureOfInterestOf(_, ACT).
hasFeatureOfInterest(ACT, FEATURE) :- isFeatureOfInterestOf(FEATURE, ACT).

% ---- Sensor

observableProperty(OBSERVABLE_PROPERTY) :- observes(_, OBSERVABLE_PROPERTY).
observation(OBSERVATION) :- makesObservation(_, OBSERVATION).

isObservedBy(OBSERVABLE_PROPERTY, SENSOR) :- observes(SENSOR, OBSERVABLE_PROPERTY).
madeBySensor(OBSERVATION, SENSOR) :- makesObservation(SENSOR, OBSERVATION).

% ---- ObservedProperty

sensor(SENSOR) :- isObservedBy(_, SENSOR).
observes(SENSOR, OBSERVABLE_PROPERTY) :- isObservedBy(OBSERVABLE_PROPERTY, SENSOR).

% ---- Observation

act(OBSERVATION) :- observation(OBSERVATION).

sensor(SENSOR) :- madeBySensor(_, SENSOR).
makesObservation(SENSOR, OBSERVATION) :- madeBySensor(OBSERVATION, SENSOR).

:- madeBySensor(OBSERVATION, SENSOR_1), madeBySensor(OBSERVATION, SENSOR_2), SENSOR_1 != SENSOR_2.

observableProperty(OBSERVABLE_PROPERTY) :- observedProperty(OBSERVATION, OBSERVABLE_PROPERTY).
observation(OBSERVATION) :- observedProperty(OBSERVATION, OBSERVABLE_PROPERTY).

% ---- Actuator

actuatableProperty(ACTUATABLE_PROPERTY) :- actsOnProperty(_, ACTUATABLE_PROPERTY).
actuation(ACTUATION) :- makesActuation(_, ACTUATION).

isActedOnBy(ACTUATABLE_PROPERTY, ACTUATOR) :- actsOnProperty(ACTUATOR, ACTUATABLE_PROPERTY).
madeByActuator(ACTUATION, ACTUATOR) :- makesActuation(ACTUATOR, ACTUATION).

% ---- ActuableProperty

actuator(ACTUATOR) :- isActedOnBy(_, ACTUATOR).
actsOnProperty(ACTUATOR, ACTUATABLE_PROPERTY) :- isActedOnBy(ACTUATABLE_PROPERTY, ACTUATOR).


% ---- Actuation

act(OBSERVATION) :- actuation(OBSERVATION).

actuator(ACTUATOR) :- madeByActuator(_, ACTUATOR).
makesActuation(ACTUATOR, ACTUATION) :- madeByActuator(ACTUATION, ACTUATOR).

:- madeByActuator(ACTUATION, ACTUATOR_1), madeByActuator(ACTUATION, ACTUATOR_2), ACTUATOR_1 != ACTUATOR_2.
