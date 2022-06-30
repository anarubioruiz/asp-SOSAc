% GENERAL KNOWLEDGE
attribute(occupancy).
x_attr_value_for_y(occupied, occupancy).
x_attr_value_for_y(unoccupied, occupancy).

klass(location).
x_is_attr_of_y(lighting, location).
x_is_attr_of_y(occupancy, location).

klass(device).
x_is_property_of_y(location, device).

klass(sensor).
x_observes_y_of_z(SENSOR, ATTR, LOCATION) :- x_instance_of_type_y(SENSOR, SENSOR_TYPE),
                                             x_observes_y_attr(SENSOR_TYPE, ATTR),
                                             x_propvalue_of_y(LOCATION, location, SENSOR).

x_subcklass_of_y(motion_sensor, sensor).
x_observes_y_attr(motion_sensor, occupancy).
x_observed_when_y_is_z(occupied, motion_sensor, true).

klass(smart_bulb).
x_affects_y(smart_bulb, lighting).
x_effect_when_y_is_z(lit, smart_bulb, on).

% GOALS

goal(1, if, x_is_y(location, occupied)).
goal(1, then, x_mustbe_y(location, lit)).

% instruction(1, if, x_is_y(OBSERVER, STATE)) : x_observes_y_of_z(OBSERVER, ATTR, OBSERVED),
%                                               x_observed_when_y_is_z(ATTR_VALUE, OBSERVER, STATE)
% :- goal(ID, if, x_is_y(OBSERVED, ATTR_VALUE)),
%      x_attr_value_for_y(ATTR_VALUE, ATTR).

% { instruction(1, if, x_is_y(motion_sensor, true)) : x_observes_y(motion_sensor, occupancy),
%                                                     x_observed_when_y_is_z(occupied, motion_sensor, true)
% } :- goal(ID, if, x_is_y(location, occupied)),
%      x_attr_value_for_y(occupied, occupancy).



% TRASH
% x_is_measured_by_y(true, MS) :- atribute_x_has_state_y_to_z(occupancy, occupied, L),
%                                 hasPropertyValue(MS, location, L),
%                                 x_observes_y(MS, occupancy).

% x_is_measured_by_y(true, LS) :- atribute_x_has_state_y_to_z(lighting, lit, L),
%                                 hasPropertyValue(LS, location, L),
%                                 x_observes_y(LS, lighting).




% -----------------------


% klass(sensor)
% x_observes_y_prop(sensor, location)
% x_observes_y_attr(sensor, occupancy)


% x_observes_y(SENSOR, ATTR, LOCATION) :- x_instance_of_y(I, K),
%                                         x_observes_y_prop(K, P),
%                                         x_observes_y_attr(K, A).
