rule_ID(1).

antecedent(1, context, daylighted).
antecedent(1, motor_blind, up).
consecuent(1, location, lit).

antecedents_count(C) :- #count { A, B : antecedent(RULE_ID, A, B) } = C.
consecuents_count(C) :- #count { A, B : consecuent(RULE_ID, A, B) } = C.

{ rule_antecedent(RULE_ID, x_is_y(THING, STATE)) : antecedent(RULE_ID, THING, STATE) } = C
    :- rule_ID(RULE_ID),
       #count { A, B : antecedent(RULE_ID, A, B) } = C.

{ rule_consecuent(RULE_ID, x_is_y(THING, STATE)) : consecuent(RULE_ID, THING, STATE) } = C
    :- rule_ID(RULE_ID),
       #count { A, B : consecuent(RULE_ID, A, B) } = C.

% #show antecedents_count/1.
% #show consecuents_count/1.
#show rule_antecedent/2.
#show rule_consecuent/2.
