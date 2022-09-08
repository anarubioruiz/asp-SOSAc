% ---- ILLUMINATE
actuation(illuminate).
hasResult(illuminate, "illuminating").
hasSimpleResult(illuminate, "on").

klass_actsOnProperty(ACTUATOR_KLASS, illumination)
    :- klass_makesActuation(ACTUATOR_KLASS, illuminate).

actuation(notIlluminate).
hasResult(notIlluminate, "not illuminating").
hasSimpleResult(notIlluminate, "off").

klass_actsOnProperty(ACTUATOR_KLASS, illumination)
    :- klass_makesActuation(ACTUATOR_KLASS, notIlluminate).

% ---- WARN OF DANGER
actuation(warnOfDanger).
hasResult(warnOfDanger, "danger alert").
hasSimpleResult(warnOfDanger, "on").

klass_actsOnProperty(ACTUATOR_KLASS, security)
    :- klass_makesActuation(ACTUATOR_KLASS, warnOfDanger).
