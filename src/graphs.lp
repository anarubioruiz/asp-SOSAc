% clingo graphs.lp output.lp 0 --outf=2 | clingraph --out=render --type=digraph

#script (python)

import clingo
from uuid import uuid4
import base64

def gen_act_label(*params):
    params = list(params)
    label = str(params.pop(0))

    for param in params:
        label = label + ' ' + str(param)

    return label

#end.

% ------------------------------------

graph((SENSOR, OBSERVATION_KLASS)) :- makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)).

node((SENSOR, OBSERVATION_KLASS), (SENSOR, OBSERVATION_KLASS))
    :- makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)).
attr(node, (SENSOR, OBSERVATION_KLASS), label, LABEL)
    :- makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)),
       LABEL = @gen_act_label(SENSOR, OBSERVATION_KLASS, ob).

node(SENSOR, (SENSOR, OBSERVATION_KLASS))
    :- makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)).
attr(node,SENSOR,label,SENSOR)
    :- makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)).

edge((SENSOR, (SENSOR, OBSERVATION_KLASS)), (SENSOR, OBSERVATION_KLASS))
    :- makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)).
attr(edge, (SENSOR, (SENSOR, OBSERVATION_KLASS)), label, "makesObservation")
    :- makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)).

% ------------------------------------

node((SENSOR, OBSERVATION_KLASS), (SENSOR, OBSERVATION_KLASS))
    :- makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)).
attr(node, (SENSOR, OBSERVATION_KLASS), label, LABEL)
    :- observedProperty(actID(SENSOR, OBSERVATION_KLASS), OBSERVABLE_PROPERTY),
       LABEL = @gen_act_label(SENSOR, OBSERVATION_KLASS, ob).

node(OBSERVABLE_PROPERTY, (SENSOR, OBSERVATION_KLASS))
    :- observedProperty(actID(SENSOR, OBSERVATION_KLASS), OBSERVABLE_PROPERTY).
attr(node,OBSERVABLE_PROPERTY,label,OBSERVABLE_PROPERTY)
    :- observedProperty(actID(SENSOR, OBSERVATION_KLASS), OBSERVABLE_PROPERTY).

edge(((SENSOR, OBSERVATION_KLASS), OBSERVABLE_PROPERTY), (SENSOR, OBSERVATION_KLASS))
    :- observedProperty(actID(SENSOR, OBSERVATION_KLASS), OBSERVABLE_PROPERTY).
attr(edge, ((SENSOR, OBSERVATION_KLASS), OBSERVABLE_PROPERTY), label, "observedProperty")
    :- observedProperty(actID(SENSOR, OBSERVATION_KLASS), OBSERVABLE_PROPERTY).

% ------------------------------------

edge((SENSOR, OBSERVABLE_PROPERTY), (SENSOR, OBSERVATION_KLASS))
    :- observedProperty(actID(SENSOR, OBSERVATION_KLASS), OBSERVABLE_PROPERTY).
attr(edge, (SENSOR, OBSERVABLE_PROPERTY), label, "observes")
    :- observedProperty(actID(SENSOR, OBSERVATION_KLASS), OBSERVABLE_PROPERTY).

% ------------------------------------

node(FEATURE, (SENSOR, OBSERVATION_KLASS))
    :- hasFeatureOfInterest(actID(SENSOR, OBSERVATION_KLASS), FEATURE).
attr(node,FEATURE,label,FEATURE)
    :- hasFeatureOfInterest(actID(SENSOR, OBSERVATION_KLASS), FEATURE).

edge(((SENSOR, OBSERVATION_KLASS), FEATURE), (SENSOR, OBSERVATION_KLASS))
    :- hasFeatureOfInterest(actID(SENSOR, OBSERVATION_KLASS), FEATURE).
attr(edge, ((SENSOR, OBSERVATION_KLASS), FEATURE), label, "hasFeatureOfInterest")
    :- hasFeatureOfInterest(actID(SENSOR, OBSERVATION_KLASS), FEATURE).








klass_makesObservation(_motionSensor_,movement).
klass_makesObservation(_brokenWindowSensor_,isBroken).
klass_observesProperty(_motionSensor_,motion).
klass_observesProperty(_brokenWindowSensor_,integrity).
klass_makesActuation(_smartBulb_,illuminate).
klass_makesActuation(_alarmSiren_,warnOfDanger).
klass_actsOnProperty(_smartBulb_,illumination).
klass_actsOnProperty(_alarmSiren_,security).
x_is_the_y_of_z(kitchen,location,ms1).
isHostedBy(ms1,kitchen).
makesObservation(ms1,actID(ms1,movement)).
sensor(ms1).
device(ms1,_motionSensor_).
observedProperty(actID(ms1,movement),motion).
observes(ms1,motion).
hasFeatureOfInterest(actID(ms1,movement),kitchen).
hasProperty(kitchen,motion).
hasResult(movement,"there's movement").
hasResult(noMovement,"there's no movement").
hasResult(isBroken,"is broken").
hasResult(illuminate,"illuminating").
hasResult(notIlluminate,"not illuminating").
hasResult(warnOfDanger,"danger alert").
hasResult(actID(ms1,movement),"there's movement").
hasSimpleResult(movement,"true").
hasSimpleResult(noMovement,"false").
hasSimpleResult(isBroken,"true").
hasSimpleResult(illuminate,"on").
hasSimpleResult(notIlluminate,"off").
hasSimpleResult(warnOfDanger,"on").
hasSimpleResult(actID(ms1,movement),"true").
klass_hasFeatureOfInterest(_alarmSiren_,home).
featureOfInterest(kitchen).
isFeatureOfInterestOf(kitchen,actID(ms1,movement)).
result("there's movement").
result("there's no movement").
result("is broken").
result("illuminating").
result("not illuminating").
result("danger alert").
isResultOf("danger alert",warnOfDanger).
isResultOf("not illuminating",notIlluminate).
isResultOf("illuminating",illuminate).
isResultOf("is broken",isBroken).
isResultOf("there's no movement",noMovement).
isResultOf("there's movement",movement).
isResultOf("there's movement",actID(ms1,movement)).
act(movement).
act(noMovement).
act(isBroken).
act(illuminate).
act(notIlluminate).
act(warnOfDanger).
act(actID(ms1,movement)).
observableProperty(motion).
observation(movement).
observation(noMovement).
observation(isBroken).
observation(actID(ms1,movement)).
isObservedBy(motion,ms1).
madeBySensor(actID(ms1,movement),ms1).
actuation(illuminate).
actuation(notIlluminate).
actuation(warnOfDanger).
platform(kitchen).
hosts(kitchen,ms1).
klass(_motionSensor_).
klass(_brokenWindowSensor_).
klass(_smartBulb_).
klass(_alarmSiren_).
