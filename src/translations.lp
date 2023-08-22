x_is_the_y_of_z(LOCATION, location, DEVICE)
    :- bot_containsElement(LOCATION, DEVICE), device(DEVICE, _).

x_is_the_y_of_z(HOST, host, DEVICE)
    :- bot_hasSubElement(HOST, DEVICE), device(DEVICE, _).
