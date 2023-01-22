need(room01, illuminated, "true").

klass_makesActuation(_smartTV_, illuminate).
klass_makesActuation(_windowBlind_, illuminate).

time(day) :- not time(night).

actuation_priority(_smartBulb_, illuminate, 2) :- time(day).
actuation_priority(_smartBulb_, illuminate, 1) :- time(night).

actuation_priority(_windowBlind_, illuminate, 1) :- time(day).
actuation_priority(_windowBlind_, illuminate, 11) :- time(night).

actuation_priority(_smartTV_, illuminate, 10).

{ use(ACTUATOR, ACTUATION) : device(ACTUATOR, ACTUATOR_KLASS),
                             makesActuation(ACTUATOR, ACTUATION),
                             hasFeatureOfInterest(ACTUATION, ENTITY),
                             actsOnProperty(ACTUATION, PROPERTY),
                             hasSimpleResult(ACTUATION, VALUE) } = 1 :- need(ENTITY, PROPERTY, VALUE).

#minimize { X@1 : use(ACTUATOR, actID(ACTUATOR, ACTUATION_KLASS)),
                  device(ACTUATOR, ACTUATOR_KLASS),
                  actuation_priority(ACTUATOR_KLASS, ACTUATION_KLASS, X) }.

device(wb01, _windowBlind_) :- not remove_device(wb01).
x_is_the_y_of_z(room01, location, wb01).

device(sb01, _smartBulb_) :- not remove_device(sb01).
x_is_the_y_of_z(room01, location, sb01).

device(tv01, _smartTV_) :- not remove_device(tv01).
x_is_the_y_of_z(room01, location, tv01).

% UTILS:
time(time).
remove_device(remove_device).
use(ACTUATOR) :- use(ACTUATOR, _).

#show use/1.
