% ------ BASIC ENGINE

memberOf(I, K) :- instanceOf(I, K).

memberOf(I, K2) :- memberOf(I, K1),
                   subclassOf(K1, K2).

subclassOf(K1, K3) :- subclassOf(K1, K2),
                      subclassOf(K2, K3).

% ------ RULES ENGINE

% transitionTriggersCount(TRANSITION_ID, COUNT) :-
%     transition(TRANSITION_ID),
%     #count { A, B : transitionTrigger(TRANSITION_ID, A, B) } = COUNT.

% transitionChangesCount(TRANSITION_ID, COUNT) :-
%     transition(TRANSITION_ID),
%     #count { A, B : transitionChange(TRANSITION_ID, A, B) } = COUNT.

% deviceObserves(DEVICE, TARGET) :-
%     memberOf(DEVICE, sensor),
%     instanceOf(DEVICE, DEVICE_KLASS),
%     propertyValueOf(TARGET_CLASS, TARGET, DEVICE),
%     transitionTrigger(T_ID, DEVICE_KLASS, _),
%     transitionChange(T_ID, DEVICE_KLASS, TARGET_CLASS, _).

% deviceAffects(DEVICE, TARGET) :-
%     memberOf(DEVICE, actuator),
%     instanceOf(DEVICE, DEVICE_KLASS),
%     propertyValueOf(TARGET_CLASS, TARGET, DEVICE),
%     transitionTrigger(T_ID, DEVICE_KLASS, _),
%     transitionChange(T_ID, DEVICE_KLASS, TARGET_CLASS, _).

instruction(@concatenateStr(G_ID, THING, DEVICE), if, stateOf(DEVICE_STATE, DEVICE)) :-
    goal(G_ID, if, stateOf(THING_STATE, THING_KLASS)),
    instanceOf(THING, THING_KLASS),
    memberOf(DEVICE, DEVICE_KLASS),
    transitionTrigger(ID, DEVICE_KLASS, DEVICE_STATE),
    transitionChange(ID, THING_KLASS, THING_STATE).

instruction(@concatenateStr(G_ID, THING, DEVICE), then, stateOf(DEVICE_STATE, DEVICE)) :-
    goal(G_ID, then, stateOf(THING_STATE, THING_KLASS)),
    instanceOf(THING, THING_KLASS),
    memberOf(DEVICE, DEVICE_KLASS),
    propertyValueOf(THING_KLASS, THING, DEVICE),
    transitionTrigger(T_ID, DEVICE_KLASS, DEVICE_STATE),
    transitionChange(T_ID, THING_KLASS, THING_STATE).



% instruction(ID, if, stateOf(STATE, DEVICE)) :-
%     goal(ID, if, stateOf(THING, THING_KLASS)),
%     instanceOf(TARGET, THING_KLASS),
%     deviceObserves(DEVICE, TARGET),
%     memberOf(DEVICE, DEVICE_KLASS),
%     deviceStateImplies(DEVICE_KLASS, STATE, THING).

% instruction(ID, then, stateOf(STATE, DEVICE)) :-
%     goal(ID, then, stateOf(THING, THING_KLASS)),
%     instanceOf(TARGET, THING_KLASS),
%     deviceAffects(DEVICE, TARGET),
%     memberOf(DEVICE, DEVICE_KLASS),
%     deviceStateImplies(DEVICE_KLASS, STATE, THING).

% deviceObserves(DEVICE, TARGET) : memberOf(DEVICE, sensor) :-
%     targetPropertyOf(_, THING_KLASS, DEVICE_KLASS),
%     instanceOf(DEVICE, DEVICE_KLASS),
%     propertyValueOf(THING_KLASS, TARGET, DEVICE).


% deviceAffects(DEVICE, TARGET) : memberOf(DEVICE, actuator) :-
%     targetPropertyOf(_, THING_KLASS, DEVICE_KLASS),
%     instanceOf(DEVICE, DEVICE_KLASS),
%     propertyValueOf(THING_KLASS, TARGET, DEVICE).

