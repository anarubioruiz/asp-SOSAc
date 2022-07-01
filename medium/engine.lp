% ------ BASIC ENGINE

memberOf(I, K) :- instanceOf(I, K).

memberOf(I, K2) :- memberOf(I, K1),
                   subclassOf(K1, K2).

subclassOf(K1, K3) :- subclassOf(K1, K2),
                      subclassOf(K2, K3).

% ------ RULES ENGINE

antecedentsCount(TRANSITION_ID, COUNT) :-
    transition(TRANSITION_ID),
    #count { A, B : antecedent(TRANSITION_ID, A, B) } = COUNT.

consecuentsCount(TRANSITION_ID, COUNT) :-
    transition(TRANSITION_ID),
    #count { A, B : consecuent(TRANSITION_ID, A, B) } = COUNT.

deviceObserves(DEVICE, TARGET) : memberOf(DEVICE, sensor);
deviceAffects(DEVICE, TARGET) : memberOf(DEVICE, actuator) :-
    targetPropertyOf(_, TARGET_KLASS, DEVICE_KLASS),
    instanceOf(DEVICE, DEVICE_KLASS),
    propertyValueOf(TARGET_KLASS, TARGET, DEVICE).

instruction(ID, if, stateOf(STATE, DEVICE)) :-
    goal(ID, if, stateOf(ATTR_VALUE, TARGET_KLASS)),
    instanceOf(TARGET, TARGET_KLASS),
    deviceObserves(DEVICE, TARGET),
    memberOf(DEVICE, DEVICE_KLASS),
    deviceStateImplies(DEVICE_KLASS, STATE, ATTR_VALUE).

instruction(ID, then, stateOf(STATE, DEVICE)) :-
    goal(ID, then, stateOf(ATTR_VALUE, TARGET_KLASS)),
    instanceOf(TARGET, TARGET_KLASS),
    deviceAffects(DEVICE, TARGET),
    memberOf(DEVICE, DEVICE_KLASS),
    deviceStateImplies(DEVICE_KLASS, STATE, ATTR_VALUE).
