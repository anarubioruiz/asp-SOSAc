klass(motionSensor).
observes(MOTION_SENSOR, motion) :- motionSensor(MOTION_SENSOR).

isHostedBy(MOTION_SENSOR, LOCATION)
    :- motionSensor(MOTION_SENSOR),
       locatedAt(MOTION_SENSOR, LOCATION).

hasFeatureOfInterest(OBSERVATION, HOST)
    :- motionSensor(MOTION_SENSOR),
       isHostedBy(MOTION_SENSOR, HOST),
       makesObservation(MOTION_SENSOR, OBSERVATION).


% This must generate a random observation ID and infer that kitchen
% is the feature of interest of ms1
motionSensor(ms1).
locatedAt(ms1, kitchen).
% =
makesObservation(MOTION_SENSOR, ob1)
    :- motionSensor(MOTION_SENSOR),
       isHostedBy(MOTION_SENSOR, HOST).

% TODO:
%  - ObservableProperty of "observed" relation must generate a hasProperty
%    relation when hasFeatureofInterest exists.
%  - Tests
