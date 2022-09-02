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
