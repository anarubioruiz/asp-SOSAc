%  --- KITCHEN

device(m006, _motionSensor_).
bot_containsElement(kitchen, m006).
device(ls006, _lightSensor_).
bot_containsElement(kitchen, ls006).

device(m007, _motionSensor_).
bot_containsElement(kitchen, m007).
device(ls007, _lightSensor_).
bot_containsElement(kitchen, ls007).

device(m002, _motionSensor_).
bot_containsElement(kitchen, m002).
device(ls002, _lightSensor_).
bot_containsElement(kitchen, ls002).

device(m003, _motionSensor_).
bot_containsElement(kitchen, m003).
device(ls003, _lightSensor_).
bot_containsElement(kitchen, ls003).

device(ma016, _motionSensor_).
bot_containsElement(kitchen, ma016).  % IN AREA
device(ls016, _lightSensor_).
bot_containsElement(kitchen, ls016).

%  --- DINING ROOM

device(m004, _motionSensor_).
bot_containsElement(dining_room, m004).
device(ls004, _lightSensor_).
bot_containsElement(dining_room, ls004).

%  --- LIVING ROOM

device(m008, _motionSensor_).
bot_containsElement(living_room, m008).
device(ls008, _lightSensor_).
bot_containsElement(living_room, ls008).

device(m005, _motionSensor_).
bot_containsElement(living_room, m005).
device(ls005, _lightSensor_).
bot_containsElement(living_room, ls005).

device(ma013, _motionSensor_).
bot_containsElement(living_room, ma013).  % IN AREA
device(ls013, _lightSensor_).
bot_containsElement(living_room, ls013).

device(t104, _temperatureSensor_).
bot_containsElement(living_room, t104).
device(t105, _temperatureSensor_).
bot_containsElement(living_room, t105).

device(t101, _temperatureSensor_).
bot_containsElement(living_room, t101).
device(d001, _doorSensor_).
bot_containsElement(living_room, d001).
bot_hasSubElement(cabinet_door, d001).

%  --- HALL

device(m010, _motionSensor_).
bot_containsElement(hall, m010).
device(ls010, _lightSensor_).
bot_containsElement(hall, ls010).

device(m001, _motionSensor_).
bot_containsElement(hall, m001).
device(ls001, _lightSensor_).
bot_containsElement(hall, ls001).

device(t102, _temperatureSensor_).
bot_containsElement(hall, t102).
device(d002, _doorSensor_).
bot_containsElement(hall, d002).
bot_hasSubElement(entrance_door, d002).

%  --- BATHROOM

device(ma015, _motionSensor_).
bot_containsElement(bathroom, ma015).  % IN AREA
device(ls015, _lightSensor_).
bot_containsElement(bathroom, ls015).

device(t103, _temperatureSensor_).
bot_containsElement(bathroom, t103).
device(d003, _doorSensor_).
bot_containsElement(bathroom, d003).
bot_hasSubElement(bathroom_door, d003).

%  --- BEDROOM

device(m011, _motionSensor_).
bot_containsElement(bedroom, m011).
device(ls011, _lightSensor_).
bot_containsElement(bedroom, ls011).

device(m009, _motionSensor_).
bot_containsElement(bedroom, m009).
device(ls009, _lightSensor_).
bot_containsElement(bedroom, ls009).

device(m012, _motionSensor_).
bot_containsElement(bedroom, m012).
device(ls012, _lightSensor_).
bot_containsElement(bedroom, ls012).

device(ma014, _motionSensor_).
bot_containsElement(bedroom, ma014).  % IN AREA
device(ls014, _lightSensor_).
bot_containsElement(bedroom, ls014).
