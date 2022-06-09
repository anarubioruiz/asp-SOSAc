instanceOf(kitchen, location).
instanceOf(lamp1, smart_bulb).
instanceOf(window1, window).
hasPropertyValue(window1, location, kitchen).
hasPropertyValue(lamp1, location, kitchen).

instanceOf(bathroom, location).
instanceOf(lamp2, smart_bulb).
hasPropertyValue(lamp2, location, bathroom).

#show is/2.
