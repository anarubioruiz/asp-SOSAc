observes(MOTION_SENSOR, motion) :- motionSensor(MOTION_SENSOR).

isHostedBy(MOTION_SENSOR, LOCATION)
    :- motionSensor(MOTION_SENSOR),
       locatedAt(MOTION_SENSOR, LOCATION).

makesObservation(MOTION_SENSOR, MOTION_SENSOR)  % replace 2nd with @gen_id()
    :- motionSensor(MOTION_SENSOR),
       isHostedBy(MOTION_SENSOR, HOST).

hasFeatureOfInterest(OBSERVATION, HOST)
    :- motionSensor(MOTION_SENSOR),
       isHostedBy(MOTION_SENSOR, HOST),
       makesObservation(MOTION_SENSOR, OBSERVATION).
