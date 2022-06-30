x_member_of_y(I, K) :- x_instance_of_y(I, K).

x_member_of_y(I, K2) :- x_member_of_y(I, K1),
                        x_subcklass_of_y(K1, K2).

x_subcklass_of_y(K1, K3) :- x_subcklass_of_y(K1, K2),
                            x_subcklass_of_y(K2, K3).
