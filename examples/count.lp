x_related_with_y(a,b).
x_related_with_y(a,c).
x_related_with_y(b,c).

count(X) :- #count { A : x_related_with_y(a,A) } = X.

#show count/1.
