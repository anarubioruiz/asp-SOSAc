%  --- KITCHEN

sosac_Device(m006, motionSensor).
bot_containsElement(kitchen, m006).
sosac_Device(ls006, lightSensor).
bot_containsElement(kitchen, ls006).

sosac_Device(m007, motionSensor).
bot_containsElement(kitchen, m007).
sosac_Device(ls007, lightSensor).
bot_containsElement(kitchen, ls007).

sosac_Device(m002, motionSensor).
bot_containsElement(kitchen, m002).
sosac_Device(ls002, lightSensor).
bot_containsElement(kitchen, ls002).

sosac_Device(m003, motionSensor).
bot_containsElement(kitchen, m003).
sosac_Device(ls003, lightSensor).
bot_containsElement(kitchen, ls003).

sosac_Device(ma016, motionSensor).
bot_containsElement(kitchen, ma016).  % IN AREA
sosac_Device(ls016, lightSensor).
bot_containsElement(kitchen, ls016).

%  --- DINING ROOM

sosac_Device(m004, motionSensor).
bot_containsElement(dining_room, m004).
sosac_Device(ls004, lightSensor).
bot_containsElement(dining_room, ls004).

%  --- LIVING ROOM

sosac_Device(m008, motionSensor).
bot_containsElement(living_room, m008).
sosac_Device(ls008, lightSensor).
bot_containsElement(living_room, ls008).

sosac_Device(m005, motionSensor).
bot_containsElement(living_room, m005).
sosac_Device(ls005, lightSensor).
bot_containsElement(living_room, ls005).

sosac_Device(ma013, motionSensor).
bot_containsElement(living_room, ma013).  % IN AREA
sosac_Device(ls013, lightSensor).
bot_containsElement(living_room, ls013).

sosac_Device(t104, temperatureSensor).
bot_containsElement(living_room, t104).
sosac_Device(t105, temperatureSensor).
bot_containsElement(living_room, t105).

sosac_Device(t101, temperatureSensor).
bot_containsElement(living_room, t101).
sosac_Device(d001, doorSensor).
bot_containsElement(living_room, d001).
bot_hasSubElement(cabinet_door, d001).

%  --- HALL

sosac_Device(m010, motionSensor).
bot_containsElement(hall, m010).
sosac_Device(ls010, lightSensor).
bot_containsElement(hall, ls010).

sosac_Device(m001, motionSensor).
bot_containsElement(hall, m001).
sosac_Device(ls001, lightSensor).
bot_containsElement(hall, ls001).

sosac_Device(t102, temperatureSensor).
bot_containsElement(hall, t102).
sosac_Device(d002, doorSensor).
bot_containsElement(hall, d002).
bot_hasSubElement(entrance_door, d002).

%  --- BATHROOM

sosac_Device(ma015, motionSensor).
bot_containsElement(bathroom, ma015).  % IN AREA
sosac_Device(ls015, lightSensor).
bot_containsElement(bathroom, ls015).

sosac_Device(t103, temperatureSensor).
bot_containsElement(bathroom, t103).
sosac_Device(d003, doorSensor).
bot_containsElement(bathroom, d003).
bot_hasSubElement(bathroom_door, d003).

%  --- BEDROOM

sosac_Device(m011, motionSensor).
bot_containsElement(bedroom, m011).
sosac_Device(ls011, lightSensor).
bot_containsElement(bedroom, ls011).

sosac_Device(m009, motionSensor).
bot_containsElement(bedroom, m009).
sosac_Device(ls009, lightSensor).
bot_containsElement(bedroom, ls009).

sosac_Device(m012, motionSensor).
bot_containsElement(bedroom, m012).
sosac_Device(ls012, lightSensor).
bot_containsElement(bedroom, ls012).

sosac_Device(ma014, motionSensor).
bot_containsElement(bedroom, ma014).  % IN AREA
sosac_Device(ls014, lightSensor).
bot_containsElement(bedroom, ls014).
