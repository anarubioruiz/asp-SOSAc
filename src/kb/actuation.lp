% ---- ILLUMINATE
sosakc_actuation(illuminate).
sosakc_hasResult(illuminate, "boolean").
sosakc_hasSimpleResult(illuminate, "true").

sosakc_actsOnProperty(ACTUATOR_KLASS, illuminated)
    :- sosakc_makesActuation(ACTUATOR_KLASS, illuminate).

sosakc_actuation(not_illuminate).
sosakc_hasResult(not_illuminate, "boolean").
sosakc_hasSimpleResult(not_illuminate, "false").

sosakc_actsOnProperty(ACTUATOR_KLASS, illuminated)
    :- sosakc_makesActuation(ACTUATOR_KLASS, not_illuminate).

% ---- OPEN/CLOSE COVER
sosakc_actuation(open_cover).
sosakc_hasResult(open_cover, "boolean").
sosakc_hasSimpleResult(open_cover, "true").

sosakc_actsOnProperty(ACTUATOR_KLASS, open)
    :- sosakc_makesActuation(ACTUATOR_KLASS, open_cover).

sosakc_actuation(close_cover).
sosakc_hasResult(close_cover, "boolean").
sosakc_hasSimpleResult(close_cover, "false").

sosakc_actsOnProperty(ACTUATOR_KLASS, open)
    :- sosakc_makesActuation(ACTUATOR_KLASS, close_cover).

% ---- WARN OF DANGER
sosakc_actuation(warn_of_danger).
sosakc_hasResult(warn_of_danger, "boolean").
sosakc_hasSimpleResult(warn_of_danger, "true").

sosakc_actsOnProperty(ACTUATOR_KLASS, in_alert)
    :- sosakc_makesActuation(ACTUATOR_KLASS, warn_of_danger).
