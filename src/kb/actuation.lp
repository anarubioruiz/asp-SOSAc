% ---- ILLUMINATE
actuation(illuminate).
hasResult(illuminate, "true").

klass_actsOnProperty(ACTUATOR_KLASS, illuminated)
    :- klass_makesActuation(ACTUATOR_KLASS, illuminate).

actuation(notIlluminate).
hasResult(notIlluminate, "false").

klass_actsOnProperty(ACTUATOR_KLASS, illuminated)
    :- klass_makesActuation(ACTUATOR_KLASS, notIlluminate).

% ---- WARN OF DANGER
actuation(warnOfDanger).
hasResult(warnOfDanger, "true").

klass_actsOnProperty(ACTUATOR_KLASS, in_alert)
    :- klass_makesActuation(ACTUATOR_KLASS, warnOfDanger).
