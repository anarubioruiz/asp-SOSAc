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

sosac_sensor(SENSOR) :- sosac_makesObservation(SENSOR, _).

sosac_makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS))
    :- sosac_device(SENSOR, SENSOR_KLASS),
       sosakc_makesObservation(SENSOR_KLASS, OBSERVATION_KLASS).

sosac_observedProperty(actID(SENSOR, OBSERVATION_KLASS), OBSERVABLE_PROPERTY)
    :- sosac_device(SENSOR, SENSOR_KLASS),
       sosac_makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)),
       sosakc_observesProperty(SENSOR_KLASS, OBSERVABLE_PROPERTY).

sosac_observes(SENSOR, OBSERVABLE_PROPERTY)
    :- sosac_observedProperty(actID(SENSOR, _), OBSERVABLE_PROPERTY).

sosac_hasFeatureOfInterest(actID(SENSOR, OBSERVATION_KLASS), ENTITY)
    :- sosac_device(SENSOR, SENSOR_KLASS),
       sosac_makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)),
       x_is_the_interest_of_z(ENTITY, SENSOR).

sosac_hasFeatureOfInterest(actID(SENSOR, OBSERVATION_KLASS), home)
    :- sosac_device(SENSOR, SENSOR_KLASS),
       sosac_makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)),
       sosakc_hasFeatureOfInterest((SENSOR_KLASS, OBSERVATION_KLASS), home),
       not x_is_the_interest_of_z(_, SENSOR).

sosac_hasFeatureOfInterest(actID(SENSOR, OBSERVATION_KLASS), FEATURE)
    :- sosac_device(SENSOR, SENSOR_KLASS),
       sosac_makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)),
       sosakc_hasFeatureOfInterest((SENSOR_KLASS, OBSERVATION_KLASS), PROPERTY),
       x_is_the_y_of_z(FEATURE, PROPERTY, SENSOR),
       not x_is_the_interest_of_z(_, SENSOR),
       PROPERTY != home.

sosac_hasFeatureOfInterest(actID(SENSOR, OBSERVATION_KLASS), LOCATION)
    :- sosac_device(SENSOR, SENSOR_KLASS),
       sosac_makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)),
       not sosakc_hasFeatureOfInterest((SENSOR_KLASS, OBSERVATION_KLASS), _),
       x_is_the_y_of_z(LOCATION, location, SENSOR),
       not x_is_the_interest_of_z(_, SENSOR).

hasProperty(FEATURE, OBSERVABLE_PROPERTY)
    :- sosac_observedProperty(OBSERVATION, OBSERVABLE_PROPERTY),
       sosac_hasFeatureOfInterest(OBSERVATION, FEATURE).

sosac_hasResult(actID(SENSOR, OBSERVATION_KLASS), RESULT)
    :- sosac_makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)),
       sosakc_hasResult(OBSERVATION_KLASS, RESULT).

sosac_hasSimpleResult(actID(SENSOR, OBSERVATION_KLASS), RESULT)
    :- sosac_makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)),
       sosakc_hasSimpleResult(OBSERVATION_KLASS, RESULT).

% ---- ACTUATOR INSTANCES

sosac_actuator(ACTUATOR) :- sosac_makesActuation(ACTUATOR, _).

sosac_makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS))
    :- sosac_device(ACTUATOR, ACTUATOR_KLASS),
       sosakc_makesActuation(ACTUATOR_KLASS, ACTUATION_KLASS).

sosac_actsOnProperty(actID(ACTUATOR, ACTUATION_KLASS), ACTUATABLE_PROPERTY)
    :- sosac_device(ACTUATOR, ACTUATOR_KLASS),
       sosac_makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)),
       sosakc_actsOnProperty(ACTUATOR_KLASS, ACTUATABLE_PROPERTY).

sosac_hasFeatureOfInterest(actID(ACTUATOR, ACTUATION_KLASS), ENTITY)
    :- sosac_device(ACTUATOR, ACTUATOR_KLASS),
       sosac_makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)),
       x_is_the_interest_of_z(ENTITY, ACTUATOR).

sosac_hasFeatureOfInterest(actID(ACTUATOR, ACTUATION_KLASS), home)
    :- sosac_device(ACTUATOR, ACTUATOR_KLASS),
       sosac_makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)),
       sosakc_hasFeatureOfInterest((ACTUATOR_KLASS, ACTUATION_KLASS), home),
       not x_is_the_interest_of_z(_, ACTUATOR).

sosac_hasFeatureOfInterest(actID(ACTUATOR, ACTUATION_KLASS), FEATURE)
    :- sosac_device(ACTUATOR, ACTUATOR_KLASS),
       sosac_makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)),
       sosakc_hasFeatureOfInterest((ACTUATOR_KLASS, ACTUATION_KLASS), PROPERTY),
       x_is_the_y_of_z(FEATURE, PROPERTY, ACTUATOR),
       not x_is_the_interest_of_z(_, ACTUATOR),
       PROPERTY != home.

sosac_hasFeatureOfInterest(actID(ACTUATOR, ACTUATION_KLASS), LOCATION)
    :- sosac_device(ACTUATOR, ACTUATOR_KLASS),
       sosac_makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)),
       not sosakc_hasFeatureOfInterest((ACTUATOR_KLASS, ACTUATION_KLASS), _),
       x_is_the_y_of_z(LOCATION, location, ACTUATOR),
       not x_is_the_interest_of_z(_, ACTUATOR).

hasProperty(FEATURE, ACTUATABLE_PROPERTY)
    :- sosac_actsOnProperty(ACTUATION, ACTUATABLE_PROPERTY),
       sosac_hasFeatureOfInterest(ACTUATION, FEATURE).

sosac_hasResult(actID(ACTUATOR, ACTUATION_KLASS), RESULT)
    :- sosac_makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)),
       sosakc_hasResult(ACTUATION_KLASS, RESULT).

sosac_hasSimpleResult(actID(ACTUATOR, ACTUATION_KLASS), RESULT)
    :- sosac_makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)),
       sosakc_hasSimpleResult(ACTUATION_KLASS, RESULT).
