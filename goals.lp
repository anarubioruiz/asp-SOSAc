% OCCUPIED LOCATIONS MUST BE LIT -------------------------
is(L, lit) :- instanceOf(L, location), is(L, occupied).

% ...avoiding artificial lighting when no people presence
:- lighting_a(L), not is(L, occupied).

% ...prioritising natural light
:- lighting_n(L), lighting_a(L), instanceOf(L, location).
:- not lighting_n(L),
   is(context, daylighted),
   propertyValueOf(L, location, W), instanceOf(W, window).
