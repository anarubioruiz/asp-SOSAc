% OCCUPIED LOCATIONS MUST BE LIT -------------------------
is(L, lit) :- instanceOf(L, location), is(L, occupied).

% ...avoiding artificial lighting when no people presence
:- lighting_a(L), not is(L, occupied).

% ...prioritising natural light
:- lighting_n(L), lighting_a(L), instanceOf(L, location).
:- not lighting_n(L),
   is(context, daylighted),
   propertyValueOf(L, location, W), instanceOf(W, window).
% Falta modelar el estado de la ventana



% TESTING -------------------------------------------------

g1_trigger(L) :- instanceOf(L, location), is(L, occupied).
goal(is(L, lit)) :- g1_trigger(L).

instruction(W,G) :- transition(W, then(G)), goal(G).
% We need a method to determine what complex facts derive the simple fact to achieve
% simple(lamp, on) -> complex(lighting_a(lamp.location)) -> means(lighting_a(lamp.location), is(lamp.location, lit))
