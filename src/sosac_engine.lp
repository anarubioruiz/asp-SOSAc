%  ---- Act

sosac_featureOfInterest(FEATURE) :- hasFeatureOfInterest(_, FEATURE).
isFeatureOfInterestOf(FEATURE, ACT) :- hasFeatureOfInterest(ACT, FEATURE).

:- hasFeatureOfInterest(OBSERVATION, FEATURE_1), hasFeatureOfInterest(OBSERVATION, FEATURE_2), FEATURE_1 != FEATURE_2.

result(RESULT) :- hasResult(_, RESULT).
isResultOf(RESULT, ACT) :- hasResult(ACT, RESULT).

% ---- FeatureOfInterest

act(ACT) :- isFeatureOfInterestOf(_, ACT).
hasFeatureOfInterest(ACT, FEATURE) :- isFeatureOfInterestOf(FEATURE, ACT).

% ---- Sensor

sosac_observableProperty(OBSERVABLE_PROPERTY) :- observes(_, OBSERVABLE_PROPERTY).
sosac_observation(OBSERVATION) :- makesObservation(_, OBSERVATION).

isObservedBy(OBSERVABLE_PROPERTY, SENSOR) :- observes(SENSOR, OBSERVABLE_PROPERTY).
madeBySensor(OBSERVATION, SENSOR) :- makesObservation(SENSOR, OBSERVATION).

% ---- ObservedProperty

sosac_sensor(SENSOR) :- isObservedBy(_, SENSOR).
observes(SENSOR, OBSERVABLE_PROPERTY) :- isObservedBy(OBSERVABLE_PROPERTY, SENSOR).
sosac_observation(OBSERVATION) :- observedProperty(OBSERVATION, _).

% ---- Observation

act(OBSERVATION) :- sosac_observation(OBSERVATION).

sosac_sensor(SENSOR) :- madeBySensor(_, SENSOR).
makesObservation(SENSOR, OBSERVATION) :- madeBySensor(OBSERVATION, SENSOR).

:- madeBySensor(OBSERVATION, SENSOR_1), madeBySensor(OBSERVATION, SENSOR_2), SENSOR_1 != SENSOR_2.

sosac_observableProperty(OBSERVABLE_PROPERTY) :- observedProperty(_, OBSERVABLE_PROPERTY).

% ---- Actuator

actuatableProperty(ACTUATABLE_PROPERTY) :- actsOnProperty(_, ACTUATABLE_PROPERTY).
actuation(ACTUATION) :- makesActuation(_, ACTUATION).

isActedOnBy(ACTUATABLE_PROPERTY, ACTUATOR) :- actsOnProperty(ACTUATOR, ACTUATABLE_PROPERTY).
madeByActuator(ACTUATION, ACTUATOR) :- makesActuation(ACTUATOR, ACTUATION).

% ---- ActuatableProperty

actuation(ACTUATION) :- isActedOnBy(_, ACTUATION).
actsOnProperty(ACTUATION, ACTUATABLE_PROPERTY) :- isActedOnBy(ACTUATABLE_PROPERTY, ACTUATION).


% ---- Actuation

act(OBSERVATION) :- actuation(OBSERVATION).

actuator(ACTUATOR) :- madeByActuator(_, ACTUATOR).
makesActuation(ACTUATOR, ACTUATION) :- madeByActuator(ACTUATION, ACTUATOR).

:- madeByActuator(ACTUATION, ACTUATOR_1), madeByActuator(ACTUATION, ACTUATOR_2), ACTUATOR_1 != ACTUATOR_2.

% ---- Result

act(ACT) :- isResultOf(_, ACT).
hasResult(ACT, RESULT) :- isResultOf(RESULT, ACT).

% ---- Platform

platform(PLATFORM) :- isHostedBy(_, PLATFORM).
hosts(PLATFORM, HOSTED) :- isHostedBy(HOSTED, PLATFORM).
isHostedBy(HOSTED, PLATFORM) :- hosts(PLATFORM, HOSTED).
