instanceOf(bathroom, location).
instanceOf(motion_sensor1, motion_sensor).
instanceOf(smart_bulb1, smart_bulb).

propertyValueOf(location, bathroom, motion_sensor1).
propertyValueOf(location, bathroom, smart_bulb1).

instanceOf(kitchen, location).
instanceOf(motion_sensor2, motion_sensor).
instanceOf(blind_motor1, blind_motor).
instanceOf(smart_bulb2, blind_motor).

propertyValueOf(location, kitchen, motion_sensor2).
propertyValueOf(location, kitchen, blind_motor1).
propertyValueOf(location, kitchen, smart_bulb2).

#show instruction/3.
% #show transitionTriggersCount/2.
% #show transitionChangesCount/2.
#show _transitionTrigger/3.
#show _transitionChange/3.
% #show _transitionCondition/3.