instanceOf(kitchen, location).
instanceOf(motion_sensor1, motion_sensor).
instanceOf(blind_motor1, blind_motor).

propertyValueOf(location, kitchen, motion_sensor1).
propertyValueOf(location, kitchen, blind_motor1).

instanceOf(bathroom, location).
instanceOf(motion_sensor2, motion_sensor).
instanceOf(blind_motor2, blind_motor).

propertyValueOf(location, bathroom, motion_sensor2).
propertyValueOf(location, bathroom, blind_motor2).

#show instruction/3.
% #show transitionTriggersCount/2.
% #show transitionChangesCount/2.
#show deviceObserves/2.
#show deviceAffects/2.
