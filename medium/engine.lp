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

instruction(@concatenateStr(G_ID, THING, DEVICE), if, stateOf(DEVICE_STATE, DEVICE)) :-
    goal(G_ID, if, stateOf(THING_STATE, THING_KLASS)),
    instanceOf(THING, THING_KLASS),
    memberOf(DEVICE, DEVICE_KLASS),
    propertyValueOf(THING_KLASS, THING, DEVICE),
    transitionTrigger(ID, DEVICE_KLASS, DEVICE_STATE),
    transitionChange(ID, THING_KLASS, THING_STATE).

instruction(ID, then, stateOf(DEVICE_STATE, DEVICE)) :-
    goal(G_ID, then, stateOf(THING_STATE, THING_KLASS)),
    instanceOf(THING, THING_KLASS),
    memberOf(DEVICE, DEVICE_KLASS),
    propertyValueOf(THING_KLASS, THING, DEVICE),
    transitionTrigger(T_ID, DEVICE_KLASS, DEVICE_STATE),
    transitionChange(T_ID, THING_KLASS, THING_STATE),

    instruction(ID, if, stateOf(_, SENSOR)),
    ID = @concatenateStr(G_ID, THING, SENSOR).
