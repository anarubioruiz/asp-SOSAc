instanceOf(motion_sensor1, motion_sensor).
instanceOf(smart_bulb1, smart_bulb).
instanceOf(window_sensor1, window_sensor).
instanceOf(alarm_siren1, alarm_siren).

instanceOf(motion_sensor2, motion_sensor).
instanceOf(blind_motor1, blind_motor).
instanceOf(smart_bulb2, blind_motor).

instanceOf(bathroom, location).
instanceOf(kitchen, location).

propertyValueOf(location, bathroom, motion_sensor1).
propertyValueOf(location, bathroom, smart_bulb1).

propertyValueOf(location, kitchen, window_sensor1).
propertyValueOf(location, kitchen, alarm_siren1).
propertyValueOf(location, kitchen, motion_sensor2).
propertyValueOf(location, kitchen, blind_motor1).
propertyValueOf(location, kitchen, smart_bulb2).



#show instruction/3.
% #show transitionTriggersCount/2.
% #show transitionChangesCount/2.
#show _transitionTrigger/3.
#show _transitionChange/3.
% #show _transitionCondition/3.
