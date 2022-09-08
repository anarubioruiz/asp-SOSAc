% ---- ILLUMINATE
actuation(illuminate).
hasResult(illuminate, "illuminating").
hasSimpleResult(illuminate, "on").

klassActsOnProperty(ACTUATOR_KLASS, illumination)
    :- makesActuationKlass(ACTUATOR_KLASS, illuminate).

actuation(notIlluminate).
hasResult(notIlluminate, "not illuminating").
hasSimpleResult(notIlluminate, "off").

klassActsOnProperty(ACTUATOR_KLASS, illumination)
    :- makesActuationKlass(ACTUATOR_KLASS, notIlluminate).

% ---- WARN OF DANGER
actuation(warnOfDanger).
hasResult(warnOfDanger, "danger alert").
hasSimpleResult(warnOfDanger, "on").

klassActsOnProperty(ACTUATOR_KLASS, security)
    :- makesActuationKlass(ACTUATOR_KLASS, warnOfDanger).
