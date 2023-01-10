%  ---- SENSORS MODELLED

device(motion_sensor01, _motionSensor_).
x_is_the_y_of_z(room02, location, motion_sensor01).

device(broken_window_sensor01, _brokenWindowSensor_).
x_is_the_y_of_z(room01, location, broken_window_sensor01).
x_is_the_y_of_z(window01, host, broken_window_sensor01).

device(door_sensor01, _doorSensor_).
x_is_the_y_of_z(room01, location, door_sensor01).
x_is_the_y_of_z(door01, host, door_sensor01).

device(light_sensor01, _lightSensor_).
x_is_the_y_of_z(room03, location, light_sensor01).

device(temp_sensor01, _temperatureSensor_).
x_is_the_y_of_z(room01, location, temp_sensor01).

% ---- ACTUATORS MODELLED

device(smart_bulb01, _smartBulb_).
x_is_the_y_of_z(room03, location, smart_bulb01).

device(alarm_siren01, _alarmSiren_).
x_is_the_y_of_z(room02, location, alarm_siren01).
