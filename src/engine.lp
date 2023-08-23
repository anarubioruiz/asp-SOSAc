%  ---- DEVICE INSTANCES

x_is_the_y_of_z(LOCATION, location, DEVICE)
    :- sosac_device(DEVICE, _),
       x_is_the_y_of_z(HOST, host, DEVICE),
       x_is_the_y_of_z(LOCATION, location, HOST).

x_is_the_y_of_z(LOCATION, location, HOST)
    :- sosac_device(DEVICE, _),
       x_is_the_y_of_z(LOCATION, location, DEVICE),
       x_is_the_y_of_z(HOST, host, DEVICE).

isHostedBy(DEVICE, LOCATION)
    :- sosac_device(DEVICE, _),
       x_is_the_y_of_z(LOCATION, location, DEVICE),
       not x_is_the_y_of_z(_, host, DEVICE).

isHostedBy(DEVICE, SPECIFIED_HOST)
    :- sosac_device(DEVICE, _),
       x_is_the_y_of_z(SPECIFIED_HOST, host, DEVICE).

isHostedBy(DEVICE, SPECIFIED_HOST)
    :- sosac_device(DEVICE, _),
       x_is_the_y_of_z(SPECIFIED_HOST, host, DEVICE).

:- sosac_device(DEVICE, DEVICE_KLASS),
   sosakc_hasFeatureOfInterest((DEVICE_KLASS, _), PROPERTY),
   not x_is_the_y_of_z(_, PROPERTY, DEVICE),
   PROPERTY != home.

% ---- SENSOR INSTANCES

sosac_sensor(SENSOR) :- makesObservation(SENSOR, _).

makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS))
    :- sosac_device(SENSOR, SENSOR_KLASS),
       sosakc_makesObservation(SENSOR_KLASS, OBSERVATION_KLASS).

observedProperty(actID(SENSOR, OBSERVATION_KLASS), OBSERVABLE_PROPERTY)
    :- sosac_device(SENSOR, SENSOR_KLASS),
       makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)),
       sosakc_observesProperty(SENSOR_KLASS, OBSERVABLE_PROPERTY).

observes(SENSOR, OBSERVABLE_PROPERTY)
    :- observedProperty(actID(SENSOR, _), OBSERVABLE_PROPERTY).

hasFeatureOfInterest(actID(SENSOR, OBSERVATION_KLASS), ENTITY)
    :- sosac_device(SENSOR, SENSOR_KLASS),
       makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)),
       x_is_the_interest_of_z(ENTITY, SENSOR).

hasFeatureOfInterest(actID(SENSOR, OBSERVATION_KLASS), home)
    :- sosac_device(SENSOR, SENSOR_KLASS),
       makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)),
       sosakc_hasFeatureOfInterest((SENSOR_KLASS, OBSERVATION_KLASS), home),
       not x_is_the_interest_of_z(_, SENSOR).

hasFeatureOfInterest(actID(SENSOR, OBSERVATION_KLASS), FEATURE)
    :- sosac_device(SENSOR, SENSOR_KLASS),
       makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)),
       sosakc_hasFeatureOfInterest((SENSOR_KLASS, OBSERVATION_KLASS), PROPERTY),
       x_is_the_y_of_z(FEATURE, PROPERTY, SENSOR),
       not x_is_the_interest_of_z(_, SENSOR),
       PROPERTY != home.

hasFeatureOfInterest(actID(SENSOR, OBSERVATION_KLASS), LOCATION)
    :- sosac_device(SENSOR, SENSOR_KLASS),
       makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)),
       not sosakc_hasFeatureOfInterest((SENSOR_KLASS, OBSERVATION_KLASS), _),
       x_is_the_y_of_z(LOCATION, location, SENSOR),
       not x_is_the_interest_of_z(_, SENSOR).

hasProperty(FEATURE, OBSERVABLE_PROPERTY)
    :- observedProperty(OBSERVATION, OBSERVABLE_PROPERTY),
       hasFeatureOfInterest(OBSERVATION, FEATURE).

hasResult(actID(SENSOR, OBSERVATION_KLASS), RESULT)
    :- makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)),
       sosakc_hasResult(OBSERVATION_KLASS, RESULT).

hasSimpleResult(actID(SENSOR, OBSERVATION_KLASS), RESULT)
    :- makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)),
       sosakc_hasSimpleResult(OBSERVATION_KLASS, RESULT).

% ---- ACTUATOR INSTANCES

sosac_actuator(ACTUATOR) :- makesActuation(ACTUATOR, _).

makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS))
    :- sosac_device(ACTUATOR, ACTUATOR_KLASS),
       sosakc_makesActuation(ACTUATOR_KLASS, ACTUATION_KLASS).

actsOnProperty(actID(ACTUATOR, ACTUATION_KLASS), ACTUATABLE_PROPERTY)
    :- sosac_device(ACTUATOR, ACTUATOR_KLASS),
       makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)),
       sosakc_actsOnProperty(ACTUATOR_KLASS, ACTUATABLE_PROPERTY).

hasFeatureOfInterest(actID(ACTUATOR, ACTUATION_KLASS), ENTITY)
    :- sosac_device(ACTUATOR, ACTUATOR_KLASS),
       makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)),
       x_is_the_interest_of_z(ENTITY, ACTUATOR).

hasFeatureOfInterest(actID(ACTUATOR, ACTUATION_KLASS), home)
    :- sosac_device(ACTUATOR, ACTUATOR_KLASS),
       makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)),
       sosakc_hasFeatureOfInterest((ACTUATOR_KLASS, ACTUATION_KLASS), home),
       not x_is_the_interest_of_z(_, ACTUATOR).

hasFeatureOfInterest(actID(ACTUATOR, ACTUATION_KLASS), FEATURE)
    :- sosac_device(ACTUATOR, ACTUATOR_KLASS),
       makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)),
       sosakc_hasFeatureOfInterest((ACTUATOR_KLASS, ACTUATION_KLASS), PROPERTY),
       x_is_the_y_of_z(FEATURE, PROPERTY, ACTUATOR),
       not x_is_the_interest_of_z(_, ACTUATOR),
       PROPERTY != home.

hasFeatureOfInterest(actID(ACTUATOR, ACTUATION_KLASS), LOCATION)
    :- sosac_device(ACTUATOR, ACTUATOR_KLASS),
       makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)),
       not sosakc_hasFeatureOfInterest((ACTUATOR_KLASS, ACTUATION_KLASS), _),
       x_is_the_y_of_z(LOCATION, location, ACTUATOR),
       not x_is_the_interest_of_z(_, ACTUATOR).

hasProperty(FEATURE, ACTUATABLE_PROPERTY)
    :- actsOnProperty(ACTUATION, ACTUATABLE_PROPERTY),
       hasFeatureOfInterest(ACTUATION, FEATURE).

hasResult(actID(ACTUATOR, ACTUATION_KLASS), RESULT)
    :- makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)),
       sosakc_hasResult(ACTUATION_KLASS, RESULT).

hasSimpleResult(actID(ACTUATOR, ACTUATION_KLASS), RESULT)
    :- makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)),
       sosakc_hasSimpleResult(ACTUATION_KLASS, RESULT).
