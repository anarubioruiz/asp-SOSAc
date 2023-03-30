% ---- ILLUMINATE
k_actuation(illuminate).
k_hasResult(illuminate, "boolean").
k_hasSimpleResult(illuminate, "true").

k_actsOnProperty(ACTUATOR_KLASS, illuminated)
    :- k_makesActuation(ACTUATOR_KLASS, illuminate).

k_actuation(notIlluminate).
k_hasResult(notIlluminate, "boolean").
k_hasSimpleResult(notIlluminate, "false").

k_actsOnProperty(ACTUATOR_KLASS, illuminated)
    :- k_makesActuation(ACTUATOR_KLASS, notIlluminate).

% ---- WARN OF DANGER
k_actuation(warnOfDanger).
k_hasResult(warnOfDanger, "boolean").
k_hasSimpleResult(warnOfDanger, "true").

k_actsOnProperty(ACTUATOR_KLASS, in_alert)
    :- k_makesActuation(ACTUATOR_KLASS, warnOfDanger).
