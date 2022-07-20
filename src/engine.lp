% ----------------------
% ---- OBSERVATIONS ----

% ---- observes, observedBy

observes(SENSOR, OBSERVABLE_PROPERTY) :- isObservedBy(OBSERVABLE_PROPERTY, SENSOR).
isObservedBy(OBSERVABLE_PROPERTY, SENSOR) :- observes(SENSOR, OBSERVABLE_PROPERTY).

% sosa:isObservedBy ONLY sosa:Sensor
% sosa:observes ONLY sosa:ObservableProperty
{sensor(SENSOR); observableProperty(OBSERVABLE_PROPERTY)} = 2 :- observes(SENSOR, OBSERVABLE_PROPERTY).

% ---- makesObservation, madeBySensor

makesObservation(SENSOR, OBSERVATION) :- madeBySensor(OBSERVATION, SENSOR).
madeBySensor(OBSERVATION, SENSOR) :- makesObservation(SENSOR, OBSERVATION).

% sosa:madeObservation ONLY sosa:Observation
% sosa:madeBySensor ONLY sosa:Sensor
{sensor(SENSOR); observation(OBSERVATION)} = 2 :- makesObservation(SENSOR, OBSERVATION).
