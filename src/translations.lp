device(DEVICE, TYPE)
    :- sosac_device(DEVICE, TYPE).

x_is_the_y_of_z(LOCATION, location, DEVICE)
    :- bot_containsElement(LOCATION, DEVICE), device(DEVICE, _).

x_is_the_y_of_z(HOST, host, DEVICE)
    :- bot_hasSubElement(HOST, DEVICE), device(DEVICE, _).

sosac_hasFeatureOfInterest(ACTIVITY, FEATURE)
    :- hasFeatureOfInterest(ACTIVITY, FEATURE).

sosac_hasResult(ACTIVITY, RESULT)
    :- hasResult(ACTIVITY, RESULT).

sosac_observedProperty(ACTIVITY, PROPERTY)
    :- observedProperty(ACTIVITY, PROPERTY).

sosac_actsOnProperty(ACTIVITY, PROPERTY)
    :- actsOnProperty(ACTIVITY, PROPERTY).

sosac_makesObservation(DEVICE, OBSERVATION)
    :- makesObservation(DEVICE, OBSERVATION).

sosac_makesActuation(DEVICE, ACTUATION)
    :- makesActuation(DEVICE, ACTUATION).

sosac_hosts(PLATFORM, DEVICE)
    :- hosts(PLATFORM, DEVICE).

sosac_hasProperty(ENTITY, PROPERTY)
    :- hasProperty(ENTITY, PROPERTY).

sosac_hasSimpleResult(ACTIVITY, RESULT)
    :- hasSimpleResult(ACTIVITY, RESULT).

sosac_observes(DEVICE, PROPERTY)
    :- observes(DEVICE, PROPERTY).


#show sosac_device/2.
#show bot_containsElement/2.
#show bot_hasSubElement/2.
#show sosac_hasFeatureOfInterest/2.
#show sosac_hasResult/2.
#show sosac_observedProperty/2.
#show sosac_actsOnProperty/2.
#show sosac_makesObservation/2.
#show sosac_makesActuation/2.
#show sosac_hosts/2.
#show sosac_hasProperty/2.
#show sosac_hasSimpleResult/2.
#show sosac_observes/2.
