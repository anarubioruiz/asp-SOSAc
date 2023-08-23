%  ---- SENSORS MODELLED

sosac_device(motion_sensor01, _motionSensor_).
bot_containsElement(room02, motion_sensor01).

sosac_device(bw_sensor01, _brokenWindowSensor_).
bot_containsElement(room01, bw_sensor01).
bot_hasSubElement(window01, bw_sensor01).

sosac_device(door_sensor01, _doorSensor_).
bot_containsElement(room01, door_sensor01).
bot_hasSubElement(door01, door_sensor01).

sosac_device(light_sensor01, _lightSensor_).
bot_containsElement(room03, light_sensor01).

sosac_device(temp_sensor01, _temperatureSensor_).
bot_containsElement(room01, temp_sensor01).

% ---- ACTUATORS MODELLED

sosac_device(smart_bulb01, _smartBulb_).
bot_containsElement(room03, smart_bulb01).

sosac_device(alarm_siren01, _alarmSiren_).
bot_containsElement(room02, alarm_siren01).
