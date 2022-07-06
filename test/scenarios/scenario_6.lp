% 2 locations ~ 2 instructions (2 possible antecents/location)
instanceOf(kitchen, location).
instanceOf(motion_sensor1, motion_sensor).
instanceOf(motion_sensor2, motion_sensor).
instanceOf(blind_motor1, blind_motor).

propertyValueOf(location, kitchen, motion_sensor1).
propertyValueOf(location, kitchen, motion_sensor2).
propertyValueOf(location, kitchen, blind_motor1).


instanceOf(bathroom, location).
instanceOf(motion_sensor3, motion_sensor).
instanceOf(motion_sensor4, motion_sensor).
instanceOf(blind_motor2, blind_motor).

propertyValueOf(location, bathroom, motion_sensor3).
propertyValueOf(location, bathroom, motion_sensor4).
propertyValueOf(location, bathroom, blind_motor2).

#show instruction/3.