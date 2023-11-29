% Workaround for not changing the engine, that uses
% x_is_the_y_of_z for both 'location' and 'host'.
% If the engine rules are changed later to consider
% bot_containsElement and bot_hasSubElement, this
% don't need to be loaded.

x_is_the_y_of_z(LOCATION, location, DEVICE)
    :- bot_containsElement(LOCATION, DEVICE), sosac_Device(DEVICE, _).

x_is_the_y_of_z(HOST, host, DEVICE)
    :- bot_hasSubElement(HOST, DEVICE), sosac_Device(DEVICE, _).
