% GENERAL KNOWLEDGE
klass(location).
klass(sensor).

x_subcklass_of_y(motion_sensor, sensor).
x_device_for_y_of_z(motion_sensor, occupancy, location).
x_change_when_y_is_z(occupied, motion_sensor, true).

x_subcklass_of_y(smart_bulb, actuator).
x_device_for_y_of_z(smart_bulb, lighting, location).
x_change_when_y_is_z(lit, smart_bulb, on).

x_observes_y(DEVICE, TARGET) : x_member_of_y(DEVICE, sensor);
x_affects_y(DEVICE, TARGET) : x_member_of_y(DEVICE, actuator)
     :- x_device_for_y_of_z(DEVICE_KLASS, _, TARGET_KLASS),
        x_instance_of_y(DEVICE, DEVICE_KLASS),
        x_propvalue_of_y(TARGET, TARGET_KLASS, DEVICE).

instruction(ID, if, x_is_y(DEVICE, STATE))
     : x_instance_of_y(TARGET, TARGET_KLASS),
       x_observes_y(DEVICE, TARGET),
       x_member_of_y(DEVICE, DEVICE_KLASS),
       x_change_when_y_is_z(ATTR_VALUE, DEVICE_KLASS, STATE)
:- goal(ID, if, x_is_y(TARGET_KLASS, ATTR_VALUE)).

instruction(ID, then, x_must_be_y(DEVICE, STATE))
     : x_instance_of_y(TARGET, TARGET_KLASS),
       x_affects_y(DEVICE, TARGET),
       x_member_of_y(DEVICE, DEVICE_KLASS),
       x_change_when_y_is_z(ATTR_VALUE, DEVICE_KLASS, STATE)
:- goal(ID, then, x_must_be_y(TARGET_KLASS, ATTR_VALUE)).
