

% Avaliable movements.
move(2, 1).
move(1, 4).
move(4, 5).
move(4, 7).
move(5, 6).
move(7, 8).
move(8, 9).
move(6, 3).

% Search if it is solvable.

is_solvable(Start, End) :- move(Start, End).
is_solvable(Start, End) :- move(Start, Z), is_solvable(Z, End).

% This is not provebable.
%f(Start, End) :- move(Start, End).
%f(Start, End) :- f(Start, Z), f(Z, End).

/* Evaluation.
 * is_solvable(2,9) = move(2, Z_0), is_solvable(Z_0=1, 9)
 * is_solvable(1,9) = move(1, Z_2), is_solvable(Z_2=4 , 9)
 * is_solvable(4,9) = move(4, Z_3), is_solvable(Z_3=[5 ; 7], 9)
 *     is_solvable(5,9) = move(5, Z_4), is_solvable(Z_4=6, 9)
 *     is_solvable(6,9) = move(6, Z_5), is_solvable(Z_5=3, 9)
 *     is_solvable(3,9) = move(2, Z_6) -> false ;
 *         is_solvable(7,9) = move(7, Z_4), is_solvable(Z_4=8, 9)
 *         is_solvable(8,9) = move(8, 9) -> true
 * */
