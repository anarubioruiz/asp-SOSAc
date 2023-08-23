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

graph(graph_output).

% % ------------------------------------

node(LOCATION, graph_output)
    :- x_is_the_y_of_z(LOCATION, location, _).
attr(node,LOCATION,label,LOCATION)
    :- x_is_the_y_of_z(LOCATION, location, _).

edge((DEVICE, LOCATION), graph_output)
    :- x_is_the_y_of_z(LOCATION, location, DEVICE),
       not isHostedBy(DEVICE, LOCATION).
attr(edge, (DEVICE, LOCATION), label, "isLocatedIn")
    :- x_is_the_y_of_z(LOCATION, location, DEVICE),
       not isHostedBy(DEVICE, LOCATION).

% % ------------------------------------

node((SENSOR, OBSERVATION_KLASS), graph_output)
    :- makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)).
attr(node, (SENSOR, OBSERVATION_KLASS), label, LABEL)
    :- makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)),
       LABEL = @gen_act_label(SENSOR, OBSERVATION_KLASS).

node(SENSOR, graph_output)
    :- makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)).
attr(node,SENSOR,label,SENSOR)
    :- makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)).

edge((SENSOR, (SENSOR, OBSERVATION_KLASS)), graph_output)
    :- makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)).
attr(edge, (SENSOR, (SENSOR, OBSERVATION_KLASS)), label, "makesObservation")
    :- makesObservation(SENSOR, actID(SENSOR, OBSERVATION_KLASS)).


node((ACTUATOR, ACTUATION_KLASS), graph_output)
    :- makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)).
attr(node, (ACTUATOR, ACTUATION_KLASS), label, LABEL)
    :- makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)),
       LABEL = @gen_act_label(ACTUATOR, ACTUATION_KLASS).

node(ACTUATOR, graph_output)
    :- makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)).
attr(node,ACTUATOR,label,ACTUATOR)
    :- makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)).

edge((ACTUATOR, (ACTUATOR, ACTUATION_KLASS)), graph_output)
    :- makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)).
attr(edge, (ACTUATOR, (ACTUATOR, ACTUATION_KLASS)), label, "makesActuation")
    :- makesActuation(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)).

% % ------------------------------------

node(OBSERVABLE_PROPERTY, graph_output)
    :- observedProperty(actID(SENSOR, OBSERVATION_KLASS), OBSERVABLE_PROPERTY).
attr(node,OBSERVABLE_PROPERTY,label,OBSERVABLE_PROPERTY)
    :- observedProperty(actID(SENSOR, OBSERVATION_KLASS), OBSERVABLE_PROPERTY).

attr(node, (SENSOR, OBSERVATION_KLASS), label, LABEL)
    :- observedProperty(actID(SENSOR, OBSERVATION_KLASS), OBSERVABLE_PROPERTY),
       LABEL = @gen_act_label(SENSOR, OBSERVATION_KLASS).

edge(((SENSOR, OBSERVATION_KLASS), OBSERVABLE_PROPERTY), graph_output)
    :- observedProperty(actID(SENSOR, OBSERVATION_KLASS), OBSERVABLE_PROPERTY).
attr(edge, ((SENSOR, OBSERVATION_KLASS), OBSERVABLE_PROPERTY), label, "observedProperty")
    :- observedProperty(actID(SENSOR, OBSERVATION_KLASS), OBSERVABLE_PROPERTY).


node(ACTUATABLE_PROPERTY, graph_output)
    :- actsOnProperty(actID(ACTUATOR, ACTUATION_KLASS), ACTUATABLE_PROPERTY).
attr(node,ACTUATABLE_PROPERTY,label,ACTUATABLE_PROPERTY)
    :- actsOnProperty(actID(ACTUATOR, ACTUATION_KLASS), ACTUATABLE_PROPERTY).

attr(node, (ACTUATOR, ACTUATION_KLASS), label, LABEL)
    :- actsOnProperty(actID(ACTUATOR, ACTUATION_KLASS), ACTUATABLE_PROPERTY),
       LABEL = @gen_act_label(ACTUATOR, ACTUATION_KLASS).

edge(((ACTUATOR, ACTUATION_KLASS), ACTUATABLE_PROPERTY), graph_output)
    :- actsOnProperty(actID(ACTUATOR, ACTUATION_KLASS), ACTUATABLE_PROPERTY).
attr(edge, ((ACTUATOR, ACTUATION_KLASS), ACTUATABLE_PROPERTY), label, "actsOnProperty")
    :- actsOnProperty(actID(ACTUATOR, ACTUATION_KLASS), ACTUATABLE_PROPERTY).

% % ------------------------------------

edge((SENSOR, OBSERVABLE_PROPERTY), graph_output)
    :- observedProperty(actID(SENSOR, OBSERVATION_KLASS), OBSERVABLE_PROPERTY).
attr(edge, (SENSOR, OBSERVABLE_PROPERTY), label, "sosac_observes")
    :- observedProperty(actID(SENSOR, OBSERVATION_KLASS), OBSERVABLE_PROPERTY).

% % ------------------------------------

node(FEATURE, graph_output)
    :- hasFeatureOfInterest(actID(SENSOR, OBSERVATION_KLASS), FEATURE).
attr(node,FEATURE,label,FEATURE)
    :- hasFeatureOfInterest(actID(SENSOR, OBSERVATION_KLASS), FEATURE).

edge(((SENSOR, OBSERVATION_KLASS), FEATURE), graph_output)
    :- hasFeatureOfInterest(actID(SENSOR, OBSERVATION_KLASS), FEATURE).
attr(edge, ((SENSOR, OBSERVATION_KLASS), FEATURE), label, "hasFeatureOfInterest")
    :- hasFeatureOfInterest(actID(SENSOR, OBSERVATION_KLASS), FEATURE).

% % ------------------------------------

node(PLATFORM, graph_output)
    :- isHostedBy(DEVICE, PLATFORM).
attr(node,PLATFORM,label,PLATFORM)
    :- isHostedBy(DEVICE, PLATFORM).

edge((DEVICE, PLATFORM), graph_output)
    :- isHostedBy(DEVICE, PLATFORM).
attr(edge, (DEVICE, PLATFORM), label, "isHostedBy")
    :- isHostedBy(DEVICE, PLATFORM).

% % ------------------------------------

node((RESULT, (SENSOR, OBSERVATION_KLASS)), graph_output)
    :- hasResult(actID(SENSOR, OBSERVATION_KLASS), RESULT).
attr(node,(RESULT, (SENSOR, OBSERVATION_KLASS)),label,RESULT)
    :- hasResult(actID(SENSOR, OBSERVATION_KLASS), RESULT).
edge(((SENSOR, OBSERVATION_KLASS), (RESULT, (SENSOR, OBSERVATION_KLASS))), graph_output)
    :- hasResult(actID(SENSOR, OBSERVATION_KLASS), RESULT).
attr(edge, ((SENSOR, OBSERVATION_KLASS), (RESULT, (SENSOR, OBSERVATION_KLASS))), label, "hasResult")
    :- hasResult(actID(SENSOR, OBSERVATION_KLASS), RESULT).
