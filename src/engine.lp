
%  ---- DEVICE INSTANCES

isHostedBy(DEVICE, LOCATION)
    :- device(DEVICE, _),
       x_is_the_y_of_z(LOCATION, location, DEVICE),
       not x_is_the_y_of_z(_, host, DEVICE).

isHostedBy(DEVICE, SPECIFIED_HOST)
    :- device(DEVICE, _),
       x_is_the_y_of_z(SPECIFIED_HOST, host, DEVICE).

% ---- SENSOR INSTANCES

sensor(SENSOR) :- makesObservation(SENSOR, _).

makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS))
    :- device(SENSOR, SENSOR_KLASS),
       makesObservationKlass(SENSOR_KLASS, OBSERVATION_KLASS).

observedProperty(actID(SENSOR, OBSERVATION_KLASS), OBSERVABLE_PROPERTY)
    :- device(SENSOR, SENSOR_KLASS),
       makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)),
       klassObservesProperty(SENSOR_KLASS, OBSERVABLE_PROPERTY).

observes(SENSOR, OBSERVABLE_PROPERTY)
    :- observedProperty(actID(SENSOR, _), OBSERVABLE_PROPERTY).

hasFeatureOfInterest(OBSERVATION, HOST)
    :- device(SENSOR, SENSOR_KLASS),
       isHostedBy(SENSOR, HOST),
       makesObservation(SENSOR, OBSERVATION).

hasProperty(FEATURE, OBSERVABLE_PROPERTY)
    :- observedProperty(OBSERVATION, OBSERVABLE_PROPERTY),
       hasFeatureOfInterest(OBSERVATION, FEATURE).

hasResult(actID(SENSOR, OBSERVATION_KLASS), RESULT)
    :- makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)),
       hasResult(OBSERVATION_KLASS, RESULT).

hasSimpleResult(actID(SENSOR, OBSERVATION_KLASS), RESULT)
    :- device(SENSOR, SENSOR_KLASS),
       makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)),
       hasSimpleResult(OBSERVATION_KLASS, RESULT).

% ---- ACTUATOR INSTANCES

actuator(ACTUATOR) :- makesActuation(ACTUATOR, _).

makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS))
    :- device(ACTUATOR, ACTUATOR_KLASS),
       makesActuationKlass(ACTUATOR_KLASS, ACTUATION_KLASS).

actsOnProperty(actID(ACTUATOR, ACTUATION_KLASS), ACTUATABLE_PROPERTY)
    :- device(ACTUATOR, ACTUATOR_KLASS),
       makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)),
       klassActsOnProperty(ACTUATOR_KLASS, ACTUATABLE_PROPERTY).

hasFeatureOfInterest(ACTUATION, HOST)
    :- device(ACTUATOR, ACTUATOR_KLASS),
       isHostedBy(ACTUATOR, HOST),
       makesActuation(SENSOR, ACTUATION).

hasProperty(FEATURE, ACTUATABLE_PROPERTY)
    :- actsOnProperty(ACTUATION, ACTUATABLE_PROPERTY),
       hasFeatureOfInterest(ACTUATION, FEATURE).

hasResult(actID(ACTUATOR, ACTUATION_KLASS), RESULT)
    :- makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)),
       hasResult(ACTUATION_KLASS, RESULT).

hasSimpleResult(actID(ACTUATOR, ACTUATION_KLASS), RESULT)
    :- makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)),
       hasSimpleResult(ACTUATION_KLASS, RESULT).
