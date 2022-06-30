subclass(C1,C2) :- subclass(C1,C3),
                   subclass(C3,C2).

% isA implies the entity E is a member of the klass K
memberOf(E,K) :- isA(E,K).

% an entity is member of parent klasses of its klass
memberOf(E,K1) :- isA(E,K2),
                  subclass(K2,K1).

%instances
instance(E) :- instanceOf(E,K).
isA(E,K) :- instanceOf(E,K).

% A klass can not be an instance
:- instanceOf(E,_), klass(E).

% properties
property(P) :- hasProperty(_,P).
propertyOf(P,E) :- hasProperty(E,P).
hasProperty(E,P) :- propertyOf(P,E).

% If a klass has a property, every member of that klass has that property
hasProperty(E,P) :- memberOf(E,K),
                    hasProperty(K,P).

% Property values for instances
propertyValueOf(V,P,I) :- hasPropertyValue(I,P,V).
hasPropertyValue(I,P,V) :- propertyValueOf(V,P,I).

% Only instances can have a property value
:- hasPropertyValue(E,_,_), klass(E).
% :- hasPropertyValue(E,_,_), not instance(E).

% states
state(S) :- hasState(_,S).
stateOf(S,E) :- hasState(E,S).
hasState(E,S) :- stateOf(S,E).
% NOTE: no se indica quién puede tener estados. ¿Sería necesario?

% hasAttribute implies A is a attribute
attribute(A) :- hasAttribute(_,A).
attributeOf(A,E) :- hasAttribute(E,A).
hasAttribute(E,A) :- attributeOf(A,E).
% NOTE: no se indica quién puede tener atributos. ¿Sería necesario?

% If a klass has an attribute, every member of that klass has that attribute
hasAttribute(E,A) :- memberOf(E,K),
                     hasAttribute(K,A).

% A state only can be part of one attribute
:- 2 { hasState(A,S) : attribute(A) }, state(S).

% When an entity has an attribute, the entity can be characterized by any state of that attribute
canBe(E,S) :- hasAttribute(E,A),
              hasState(A,S).

% An instance (not klass) only can be in one state of the same attribute
1 { is(I,S) : hasState(A,S) } 1 :- hasAttribute(I,A),
                                   instance(I).

% Klasses don't have states
:- is(K,_), klass(K).
% :- is(I,_) not instance(I). --> solo las sintancias tienen estados.
