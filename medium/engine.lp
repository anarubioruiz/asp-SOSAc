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

instruction(ID, if, stateOf(DEVICE_STATE, DEVICE)) :-
    goal(ID, if, stateOf(THING_STATE, THING_KLASS)),
    instanceOf(THING, THING_KLASS),
    memberOf(DEVICE, DEVICE_KLASS),
    transitionTrigger(ID, DEVICE_KLASS, DEVICE_STATE),
    transitionChange(ID, THING_KLASS, THING_STATE).

% instruction(ID, then, stateOf(THING_STATE, THING)) :-
%     goal(ID, then, stateOf(THING_STATE, THING_KLASS)),
%     instanceOf(THING, THING_KLASS),
%     memberOf(DEVICE, DEVICE_KLASS),
%     transitionTrigger(ID, DEVICE_KLASS, DEVICE_STATE),
%     transitionChange(ID, THING_KLASS, THING_STATE).

% instruction(ID, then, stateOf(up, blind_motor1)) :-
%     goal(ID, then, stateOf(lit, location)),
%     instanceOf(kitchen, location),
%     transitionChange(ID, location, lit),
%     transitionTrigger(ID, blind_motor, up),
%     memberOf(blind_motor1, blind_motor).

instruction(THING, then, stateOf(DEVICE_STATE, DEVICE)) :-
    goal(_, then, stateOf(THING_STATE, THING_KLASS)),
    instanceOf(THING, THING_KLASS),
    memberOf(DEVICE, DEVICE_KLASS),
    propertyValueOf(THING_KLASS, THING, DEVICE),
    transitionTrigger(T_ID, DEVICE_KLASS, DEVICE_STATE),
    transitionChange(T_ID, THING_KLASS, THING_STATE).

    % instruction(G_ID, if, stateOf(D_S, D)),
    % propertyValueOf(THING_KLASS, THING, D).



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




% instruction(1, if, stateOf(true, motion_sensor1))
% instruction(1, then, stateOf(up, blind_motor1))

% instruction(1, if, stateOf(true, motion_sensor1))
% instruction(1, then, stateOf(up, blind_motor2))

% instruction(1, if, stateOf(true, motion_sensor1))
% instruction(1, then, stateOf(up, smart_bulb1))
