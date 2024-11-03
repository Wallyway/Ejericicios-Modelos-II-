% Avaliable movements.

move(2,4)
move(1,3)
move(5,4)

% Finds a path.

is_solvable(START, END, PATH) :- move(START, END)
is_solvable(START, END, PATH) :- move(START, Z), move(Z, END)

