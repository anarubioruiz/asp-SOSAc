objetive(room01, illuminated, "true").

k_makesActuation(_smartTV_, illuminate).
k_makesActuation(_windowBlindMotor_, illuminate).

time(day) :- not time(night).

% Priorities
% 1 - HIGH
% 2 - MEDIUM
% 3 - LOW
% 4 - VERY LOW

actuation_priority(_smartBulb_, illuminate, 2) :- time(day).
actuation_priority(_smartBulb_, illuminate, 1) :- time(night).

actuation_priority(_windowBlindMotor_, illuminate, 1) :- time(day).
actuation_priority(_windowBlindMotor_, illuminate, 4) :- time(night).

actuation_priority(_smartTV_, illuminate, 3).

{ use(ACTUATOR, ACTUATION) : makesActuation(ACTUATOR, ACTUATION),
                             hasFeatureOfInterest(ACTUATION, ENTITY),
                             actsOnProperty(ACTUATION, PROPERTY),
                             hasSimpleResult(ACTUATION, VALUE) } = 1 :- objetive(ENTITY, PROPERTY, VALUE).

#minimize { X@1 : use(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)),
                  sosac_device(ACTUATOR, ACTUATOR_KLASS),
                  actuation_priority(ACTUATOR_KLASS, ACTUATION_KLASS, X) }.

sosac_device(wb01, _windowBlindMotor_) :- not remove_device(wb01).
bot_containsElement(room01, wb01).

sosac_device(sb01, _smartBulb_) :- not remove_device(sb01).
bot_containsElement(room01, sb01).

sosac_device(tv01, _smartTV_) :- not remove_device(tv01).
bot_containsElement(room01, tv01).

% UTILS:
time(time).
remove_device(remove_device).
use(ACTUATOR) :- use(ACTUATOR, _).

#show use/2.
