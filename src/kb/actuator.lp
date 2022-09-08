klass(_smartBulb_).
klass_makesActuation(_smartBulb_, illuminate).

klass(_alarmSiren_).
klass_makesActuation(_alarmSiren_, warnOfDanger).
klass_hasFeatureOfInterest(_alarmSiren_, home).
