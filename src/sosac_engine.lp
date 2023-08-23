%  ---- Act

sosac_featureOfInterest(FEATURE) :- sosac_hasFeatureOfInterest(_, FEATURE).
sosac_isFeatureOfInterestOf(FEATURE, ACT) :- sosac_hasFeatureOfInterest(ACT, FEATURE).

:- sosac_hasFeatureOfInterest(OBSERVATION, FEATURE_1), sosac_hasFeatureOfInterest(OBSERVATION, FEATURE_2), FEATURE_1 != FEATURE_2.

sosac_result(RESULT) :- hasResult(_, RESULT).
isResultOf(RESULT, ACT) :- hasResult(ACT, RESULT).

% ---- FeatureOfInterest

act(ACT) :- sosac_isFeatureOfInterestOf(_, ACT).
sosac_hasFeatureOfInterest(ACT, FEATURE) :- sosac_isFeatureOfInterestOf(FEATURE, ACT).

% ---- Sensor

sosac_observableProperty(OBSERVABLE_PROPERTY) :- sosac_observes(_, OBSERVABLE_PROPERTY).
sosac_observation(OBSERVATION) :- sosac_makesObservation(_, OBSERVATION).

sosac_isObservedBy(OBSERVABLE_PROPERTY, SENSOR) :- sosac_observes(SENSOR, OBSERVABLE_PROPERTY).
sosac_madeBySensor(OBSERVATION, SENSOR) :- sosac_makesObservation(SENSOR, OBSERVATION).

% ---- ObservedProperty

sosac_sensor(SENSOR) :- sosac_isObservedBy(_, SENSOR).
sosac_observes(SENSOR, OBSERVABLE_PROPERTY) :- sosac_isObservedBy(OBSERVABLE_PROPERTY, SENSOR).
sosac_observation(OBSERVATION) :- sosac_observedProperty(OBSERVATION, _).

% ---- Observation

act(OBSERVATION) :- sosac_observation(OBSERVATION).

sosac_sensor(SENSOR) :- sosac_madeBySensor(_, SENSOR).
sosac_makesObservation(SENSOR, OBSERVATION) :- sosac_madeBySensor(OBSERVATION, SENSOR).

:- sosac_madeBySensor(OBSERVATION, SENSOR_1), sosac_madeBySensor(OBSERVATION, SENSOR_2), SENSOR_1 != SENSOR_2.

sosac_observableProperty(OBSERVABLE_PROPERTY) :- sosac_observedProperty(_, OBSERVABLE_PROPERTY).

% ---- Actuator

sosac_actuatableProperty(ACTUATABLE_PROPERTY) :- sosac_actsOnProperty(_, ACTUATABLE_PROPERTY).
sosac_actuation(ACTUATION) :- sosac_makesActuation(_, ACTUATION).

sosac_isActedOnBy(ACTUATABLE_PROPERTY, ACTUATOR) :- sosac_actsOnProperty(ACTUATOR, ACTUATABLE_PROPERTY).
sosac_madeByActuator(ACTUATION, ACTUATOR) :- sosac_makesActuation(ACTUATOR, ACTUATION).

% ---- ActuatableProperty

sosac_actuation(ACTUATION) :- sosac_isActedOnBy(_, ACTUATION).
sosac_actsOnProperty(ACTUATION, ACTUATABLE_PROPERTY) :- sosac_isActedOnBy(ACTUATABLE_PROPERTY, ACTUATION).


% ---- Actuation

act(OBSERVATION) :- sosac_actuation(OBSERVATION).

sosac_actuator(ACTUATOR) :- sosac_madeByActuator(_, ACTUATOR).
sosac_makesActuation(ACTUATOR, ACTUATION) :- sosac_madeByActuator(ACTUATION, ACTUATOR).

:- sosac_madeByActuator(ACTUATION, ACTUATOR_1), sosac_madeByActuator(ACTUATION, ACTUATOR_2), ACTUATOR_1 != ACTUATOR_2.

% ---- Result

act(ACT) :- isResultOf(_, ACT).
hasResult(ACT, RESULT) :- isResultOf(RESULT, ACT).

% ---- Platform

sosac_platform(PLATFORM) :- isHostedBy(_, PLATFORM).
hosts(PLATFORM, HOSTED) :- isHostedBy(HOSTED, PLATFORM).
isHostedBy(HOSTED, PLATFORM) :- hosts(PLATFORM, HOSTED).
