isHostedBy(DEVICE, LOCATION)
    :- device(DEVICE, _),
       locatedAt(DEVICE, LOCATION).

sensor(SENSOR) :- makesObservation(SENSOR, _).

observes(SENSOR, OBSERVABLE_PROPERTY)
    :- device(SENSOR, SENSOR_KLASS),
       klassObserves(SENSOR_KLASS, OBSERVABLE_PROPERTY).

makesObservation(SENSOR, actID(SENSOR, OBSERVATION))
    :- device(SENSOR, SENSOR_KLASS),
       makesObservationType(SENSOR_KLASS, OBSERVATION).

observedProperty(actID(SENSOR, OBSERVATION), OBSERVABLE_PROPERTY)
    :- observes(SENSOR, OBSERVABLE_PROPERTY),
       makesObservation(SENSOR, actID(SENSOR, OBSERVATION)).

hasFeatureOfInterest(OBSERVATION, HOST)
    :- device(SENSOR, SENSOR_KLASS),
       isHostedBy(SENSOR, HOST),
       makesObservation(SENSOR, OBSERVATION).

hasProperty(FEATURE, OBSERVABLE_PROPERTY)
    :- observedProperty(OBSERVATION, OBSERVABLE_PROPERTY),
       hasFeatureOfInterest(OBSERVATION, FEATURE).

hasResult(actID(SENSOR, OBSERVATION_TYPE), RESULT)
    :- device(SENSOR, SENSOR_KLASS),
       makesObservation(SENSOR, actID(SENSOR, OBSERVATION_TYPE)),
       hasResult(OBSERVATION_TYPE, RESULT).

hasSimpleResult(actID(SENSOR, OBSERVATION_TYPE), RESULT)
    :- device(SENSOR, SENSOR_KLASS),
       makesObservation(SENSOR, actID(SENSOR, OBSERVATION_TYPE)),
       hasSimpleResult(OBSERVATION_TYPE, RESULT).
