% ---- ILLUMINATE
actuation(illuminate).
hasResult(illuminate, boolean).
hasSimpleResult(illuminate, "true").

klass_actsOnProperty(ACTUATOR_KLASS, illuminated)
    :- klass_makesActuation(ACTUATOR_KLASS, illuminate).

actuation(notIlluminate).
hasResult(notIlluminate, boolean).
hasSimpleResult(notIlluminate, "false").

klass_actsOnProperty(ACTUATOR_KLASS, illuminated)
    :- klass_makesActuation(ACTUATOR_KLASS, notIlluminate).

% ---- WARN OF DANGER
actuation(warnOfDanger).
hasResult(warnOfDanger, boolean).
hasSimpleResult(warnOfDanger, "true").

klass_actsOnProperty(ACTUATOR_KLASS, in_alert)
    :- klass_makesActuation(ACTUATOR_KLASS, warnOfDanger).
