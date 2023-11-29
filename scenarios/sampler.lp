%  ---- SENSORS MODELLED

sosac_Device(motion_sensor01, motionSensor).
bot_containsElement(room02, motion_sensor01).

sosac_Device(bw_sensor01, brokenWindowSensor).
bot_containsElement(room01, bw_sensor01).
bot_hasSubElement(window01, bw_sensor01).

sosac_Device(door_sensor01, doorSensor).
bot_containsElement(room01, door_sensor01).
bot_hasSubElement(door01, door_sensor01).

sosac_Device(light_sensor01, lightSensor).
bot_containsElement(room03, light_sensor01).

sosac_Device(temp_sensor01, temperatureSensor).
bot_containsElement(room01, temp_sensor01).

% ---- ACTUATORS MODELLED

sosac_Device(smart_bulb01, smartLight).
bot_containsElement(room03, smart_bulb01).

sosac_Device(alarm_siren01, alarmSiren).
bot_containsElement(room02, alarm_siren01).
