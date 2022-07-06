% 1 location ~ 1 instruction
instanceOf(kitchen, location).
instanceOf(motion_sensor1, motion_sensor).
instanceOf(blind_motor1, blind_motor).

propertyValueOf(location, kitchen, motion_sensor1).
propertyValueOf(location, kitchen, blind_motor1).

#show instruction/3.