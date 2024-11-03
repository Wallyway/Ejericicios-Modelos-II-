father_of('Juan', 'María').
father_of('Pablo', 'Juan').
father_of('Pablo', 'Marcela').
father_of('Carlos', 'Debora').

merried_with('Juan', 'Debora').

son_of(A, B) :- father(B,A).
grandparent_of(A, B) :- father_of(A, Z), father_of(Z, B).
cousin_of(A, B) :- grandparent_of(Z, A), grandparent_of(Z, B).
fil_of(A, B) :- merried_with(Z, B), father_of(A, Z).
brother_of(X, Y) :- father_of(Z, X), father_of(Z, Y).
