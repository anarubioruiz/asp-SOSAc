time(1..lasttime).

follows(b, a).
follows(c, b).
follows(d, c).

target(d).
init(b).
at(I, 1) :- init(I).

{ at(NEXT, T) : follows(NEXT,CURRENT), at(CURRENT,T-1) } :- time(T).
finish :- at(CURRENT, T), target(CURRENT).
:- not finish.

#show at/2.
