% ------ BASIC ENGINE

memberOf(INSTANCE, KLASS) :- instanceOf(INSTANCE, KLASS).

memberOf(INSTANCE, KLASS_2) :- memberOf(INSTANCE, KLASS_1),
                               subclassOf(KLASS_1, KLASS_2).

subclassOf(KLASS_1, KLASS_3) :- subclassOf(KLASS_1, KLASS_2),
                                subclassOf(KLASS_2, KLASS_3).

instanceOf(VALUE, PROPERTY) :- propertyValueOf(PROPERTY, VALUE, _).


% ------ RULES ENGINE

% transitionTriggersCount(TRANSITION_ID, COUNT) :-
%     transition(TRANSITION_ID),
%     #count { A, B : transitionTrigger(TRANSITION_ID, A, B) } = COUNT.

% transitionChangesCount(TRANSITION_ID, COUNT) :-
%     transition(TRANSITION_ID),
%     #count { A, B : transitionChange(TRANSITION_ID, A, B) } = COUNT.

instanceOf(_context, context).

_transitionTrigger(ID, DEVICE, DEVICE_STATE) :- transitionTrigger(ID, DEVICE_KLASS, DEVICE_STATE),
                                                 memberOf(DEVICE, DEVICE_KLASS).

_transitionChange(ID, TARGET, TARGET_STATE) :- transitionChange(ID, TARGET_KLASS, TARGET_STATE),
                                                memberOf(TARGET, TARGET_KLASS),
                                                _transitionTrigger(ID, DEVICE, _),
                                                propertyValueOf(TARGET_KLASS, TARGET, DEVICE).

_transitionCondition(ID, THING, STATE) :- transitionCondition(ID, THING_KLASS, STATE),
                                          memberOf(THING, THING_KLASS),
                                          _transitionTrigger(ID, _, _).

% NUEVA VERSION: INSTANCIAS DE TRANSITIONS
instruction(ID, if, stateOf(DEVICE_STATE, DEVICE)) :-
    goal(G_ID, if, stateOf(TARGET_STATE, TARGET_KLASS)),
    _transitionTrigger(T_ID, DEVICE, DEVICE_STATE),
    _transitionChange(T_ID, TARGET, TARGET_STATE),
    propertyValueOf(TARGET_KLASS, TARGET, DEVICE),
    ID = instructionId(G_ID, DEVICE, none).

instruction(ID, then, stateOf(DEVICE_STATE, DEVICE)) :-
    goal(G_ID, then, stateOf(TARGET_STATE, TARGET_KLASS)),
    _transitionTrigger(T_ID, DEVICE, DEVICE_STATE),
    _transitionChange(T_ID, TARGET, TARGET_STATE),
    propertyValueOf(TARGET_KLASS, TARGET, DEVICE),
    propertyValueOf(TARGET_KLASS, TARGET, TRIGGER_DEVICE),
    instruction(instructionId(G_ID, TRIGGER_DEVICE, none), if, stateOf(_, _)),
    ID = instructionId(G_ID, TRIGGER_DEVICE, DEVICE).


instruction(ID, when, stateOf(THING_STATE, THING)) :-
    instruction(ID, _, stateOf(DEVICE_STATE, DEVICE)),
    _transitionCondition(T_ID, THING, THING_STATE),
    _transitionTrigger(T_ID, DEVICE, DEVICE_STATE).

    