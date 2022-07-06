% 2 locations ~ 2 instructions (2 possible consequents/location)
instanceOf(kitchen, location).
instanceOf(motion_sensor1, motion_sensor).
instanceOf(blind_motor1, blind_motor).
instanceOf(blind_motor2, blind_motor).

propertyValueOf(location, kitchen, motion_sensor1).
propertyValueOf(location, kitchen, blind_motor1).
propertyValueOf(location, kitchen, blind_motor2).


instanceOf(bathroom, location).
instanceOf(motion_sensor2, motion_sensor).
instanceOf(blind_motor3, blind_motor).
instanceOf(blind_motor4, blind_motor).


propertyValueOf(location, bathroom, motion_sensor2).
propertyValueOf(location, bathroom, blind_motor3).
propertyValueOf(location, bathroom, blind_motor4).

#show instruction/3.