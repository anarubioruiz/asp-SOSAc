% ---- ILLUMINATE
sosakc_actuation(illuminate).
sosakc_hasResult(illuminate, "boolean").
sosakc_hasSimpleResult(illuminate, "true").

sosakc_actsOnProperty(ACTUATOR_KLASS, illuminated)
    :- sosakc_makesActuation(ACTUATOR_KLASS, illuminate).

sosakc_actuation(notIlluminate).
sosakc_hasResult(notIlluminate, "boolean").
sosakc_hasSimpleResult(notIlluminate, "false").

sosakc_actsOnProperty(ACTUATOR_KLASS, illuminated)
    :- sosakc_makesActuation(ACTUATOR_KLASS, notIlluminate).

% ---- WARN OF DANGER
sosakc_actuation(warnOfDanger).
sosakc_hasResult(warnOfDanger, "boolean").
sosakc_hasSimpleResult(warnOfDanger, "true").

sosakc_actsOnProperty(ACTUATOR_KLASS, in_alert)
    :- sosakc_makesActuation(ACTUATOR_KLASS, warnOfDanger).
