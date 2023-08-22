%  ---- SENSORS MODELLED

device(motion_sensor01, _motionSensor_).
bot_containsElement(room02, motion_sensor01).

device(bw_sensor01, _brokenWindowSensor_).
bot_containsElement(room01, bw_sensor01).
bot_hasSubElement(window01, bw_sensor01).

device(door_sensor01, _doorSensor_).
bot_containsElement(room01, door_sensor01).
bot_hasSubElement(door01, door_sensor01).

device(light_sensor01, _lightSensor_).
bot_containsElement(room03, light_sensor01).

device(temp_sensor01, _temperatureSensor_).
bot_containsElement(room01, temp_sensor01).

% ---- ACTUATORS MODELLED

device(smart_bulb01, _smartBulb_).
bot_containsElement(room03, smart_bulb01).

device(alarm_siren01, _alarmSiren_).
bot_containsElement(room02, alarm_siren01).
