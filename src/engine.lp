%  ---- DEVICE INSTANCES

x_is_the_y_of_z(LOCATION, location, DEVICE)
    :- device(DEVICE, _),
       x_is_the_y_of_z(HOST, host, DEVICE),
       x_is_the_y_of_z(LOCATION, location, HOST).

x_is_the_y_of_z(LOCATION, location, HOST)
    :- device(DEVICE, _),
       x_is_the_y_of_z(LOCATION, location, DEVICE),
       x_is_the_y_of_z(HOST, host, DEVICE).

isHostedBy(DEVICE, LOCATION)
    :- device(DEVICE, _),
       x_is_the_y_of_z(LOCATION, location, DEVICE),
       not x_is_the_y_of_z(_, host, DEVICE).

isHostedBy(DEVICE, SPECIFIED_HOST)
    :- device(DEVICE, _),
       x_is_the_y_of_z(SPECIFIED_HOST, host, DEVICE).

isHostedBy(DEVICE, SPECIFIED_HOST)
    :- device(DEVICE, _),
       x_is_the_y_of_z(SPECIFIED_HOST, host, DEVICE).

:- device(DEVICE, DEVICE_KLASS),
   klass_hasFeatureOfInterest((DEVICE_KLASS, _), PROPERTY),
   not x_is_the_y_of_z(_, PROPERTY, DEVICE),
   PROPERTY != home.

% ---- SENSOR INSTANCES

sensor(SENSOR) :- makesObservation(SENSOR, _).

makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS))
    :- device(SENSOR, SENSOR_KLASS),
       klass_makesObservation(SENSOR_KLASS, OBSERVATION_KLASS).

observedProperty(actID(SENSOR, OBSERVATION_KLASS), OBSERVABLE_PROPERTY)
    :- device(SENSOR, SENSOR_KLASS),
       makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)),
       klass_observesProperty(SENSOR_KLASS, OBSERVABLE_PROPERTY).

observes(SENSOR, OBSERVABLE_PROPERTY)
    :- observedProperty(actID(SENSOR, _), OBSERVABLE_PROPERTY).

hasFeatureOfInterest(actID(SENSOR, OBSERVATION_KLASS), home)
    :- device(SENSOR, SENSOR_KLASS),
       makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)),
       klass_hasFeatureOfInterest((SENSOR_KLASS, OBSERVATION_KLASS), home).

hasFeatureOfInterest(actID(SENSOR, OBSERVATION_KLASS), FEATURE)
    :- device(SENSOR, SENSOR_KLASS),
       makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)),
       klass_hasFeatureOfInterest((SENSOR_KLASS, OBSERVATION_KLASS), PROPERTY),
       x_is_the_y_of_z(FEATURE, PROPERTY, SENSOR).

hasFeatureOfInterest(actID(SENSOR, OBSERVATION_KLASS), LOCATION)
    :- device(SENSOR, SENSOR_KLASS),
       makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)),
       not klass_hasFeatureOfInterest((SENSOR_KLASS, OBSERVATION_KLASS), _),
       x_is_the_y_of_z(LOCATION, location, SENSOR).

hasProperty(FEATURE, OBSERVABLE_PROPERTY)
    :- observedProperty(OBSERVATION, OBSERVABLE_PROPERTY),
       hasFeatureOfInterest(OBSERVATION, FEATURE).

hasResult(actID(SENSOR, OBSERVATION_KLASS), RESULT)
    :- makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)),
       hasResult(OBSERVATION_KLASS, RESULT).

% ---- ACTUATOR INSTANCES

actuator(ACTUATOR) :- makesActuation(ACTUATOR, _).

makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS))
    :- device(ACTUATOR, ACTUATOR_KLASS),
       klass_makesActuation(ACTUATOR_KLASS, ACTUATION_KLASS).

actsOnProperty(actID(ACTUATOR, ACTUATION_KLASS), ACTUATABLE_PROPERTY)
    :- device(ACTUATOR, ACTUATOR_KLASS),
       makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)),
       klass_actsOnProperty(ACTUATOR_KLASS, ACTUATABLE_PROPERTY).

hasFeatureOfInterest(actID(ACTUATOR, ACTUATION_KLASS), home)
    :- device(ACTUATOR, ACTUATOR_KLASS),
       makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)),
       klass_hasFeatureOfInterest((ACTUATOR_KLASS, ACTUATION_KLASS), home).

hasFeatureOfInterest(actID(ACTUATOR, ACTUATION_KLASS), FEATURE)
    :- device(ACTUATOR, ACTUATOR_KLASS),
       makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)),
       klass_hasFeatureOfInterest((ACTUATOR_KLASS, ACTUATION_KLASS), PROPERTY),
       x_is_the_y_of_z(FEATURE, PROPERTY, ACTUATOR),
       PROPERTY != home.

hasFeatureOfInterest(actID(ACTUATOR, ACTUATION_KLASS), LOCATION)
    :- device(ACTUATOR, ACTUATOR_KLASS),
       makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)),
       not klass_hasFeatureOfInterest((ACTUATOR_KLASS, ACTUATION_KLASS), _),
       x_is_the_y_of_z(LOCATION, location, ACTUATOR).

hasProperty(FEATURE, ACTUATABLE_PROPERTY)
    :- actsOnProperty(ACTUATION, ACTUATABLE_PROPERTY),
       hasFeatureOfInterest(ACTUATION, FEATURE).

hasResult(actID(ACTUATOR, ACTUATION_KLASS), RESULT)
    :- makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)),
       hasResult(ACTUATION_KLASS, RESULT).
