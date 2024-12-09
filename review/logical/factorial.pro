% Factorial
factorial(0,1).
factorial(1,1).
factorial(X, R) :-
        X > 1,
        X1 is X-1,
        factorial(X1, R1),
        R is X*R1.
