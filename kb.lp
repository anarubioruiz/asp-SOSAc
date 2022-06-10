% state axis
attribute(lightable).
hasState(lightable, lit).
hasState(lightable, unlit).

is(L, unlit) :- not lighting_n(L), not lighting_a(L),
                instanceOf(L, location).

% % lighting complex facts derive simple facts:
is(L, lit) :- { lighting_n(L);lighting_a(L) } = 1,
              instanceOf(L, location).

attribute(switchable).
hasState(switchable, on).
hasState(switchable, off).

attribute(openable).
hasState(openable, open).
hasState(openable, closed).

atribute(daylightable).
hasState(daylightable, daylighted).
hasState(daylightable, undaylighted).

atribute(occupiable).
hasState(occupiable, occupied).
hasState(occupiable, unoccupied).

% klasses
klass(location).
hasAttribute(location, lightable).
hasAttribute(location, occupiable).

klass(device).
hasAttribute(device, switchable).
hasProperty(device, location).

klass(smart_bulb).
subclass(smart_bulb, device).

klass(window).
hasAttribute(window, openable).

instance(context).
hasAttribute(context, daylightable).

% transitions
% Turned on bulbs lit (with Artificial light) their location
t1_trigger(SB, L) :- instanceOf(SB, smart_bulb),
              is(SB, on),
              propertyValueOf(L, location, SB).

transition(
    when(is(SB, on)),
    then(lighting_a(L))
) :- t1_trigger(SB, L).

lighting_a(L) :- t1_trigger(SB, L).

% % Open windows lit (with Natural light) their location
t2_trigger(W, L) :- instanceOf(W, window),
                 is(W, open),
                 propertyValueOf(L, location, W),
                 is(context, daylighted).

transition(
    when(is(W, open), is(context, daylighted)),
    then(lighting_n(L))
) :- t2_trigger(W, L).

lighting_n(L) :- t2_trigger(W, L).
