% 1 location / 2 instructions (2 possible antecedents + 2 possible consequents)
instanceOf(kitchen, location).
instanceOf(motion_sensor1, motion_sensor).
instanceOf(motion_sensor2, motion_sensor).
instanceOf(blind_motor1, blind_motor).
instanceOf(smart_bulb1, smart_bulb).

propertyValueOf(location, kitchen, motion_sensor1).
propertyValueOf(location, kitchen, motion_sensor2).
propertyValueOf(location, kitchen, blind_motor1).
propertyValueOf(location, kitchen, smart_bulb1).

#show instruction/3.