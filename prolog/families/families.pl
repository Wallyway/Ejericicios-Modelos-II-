% Family relationships
parentof('david', 'alexander').
parentof('david', 'brayan').
parentof('david', 'carolina').
parentof('david', 'diego').
parentof('david', 'emilia').
parentof('david', 'fernanda').
parentof('sofia', 'alexander').
parentof('sofia', 'brayan').
parentof('sofia', 'carolina').
parentof('sofia', 'diego').
parentof('sofia', 'emilia').
parentof('sofia', 'fernanda').
parentof('alexander', 'gabriel').
parentof('alexander', 'hugo').
parentof('maria', 'gabriel').
parentof('maria', 'hugo').
parentof('carolina', 'isabella').
parentof('carolina', 'juliana').
parentof('juan', 'isabella').
parentof('juan', 'juliana').

% Gender information
male('david').
male('alexander').
male('brayan').
male('diego').
male('gabriel').
male('hugo').
male('juan').

female('sofia').
female('carolina').
female('emilia').
female('fernanda').
female('maria').
female('isabella').
female('juliana').

% Rules for family relationships
childof(A, B) :- parentof(B, A).
fatherof(A, B) :- parentof(A, B), male(A).
motherof(A, B) :- parentof(A, B), female(A).
grandparentof(A, B) :- parentof(A, C), parentof(C, B).
siblingof(A, B) :- parentof(C, A), parentof(C, B), A \== B.
uncleof(A, B) :- parentof(C, B), siblingof(A, C), male(A).
auntof(A, B) :- parentof(C, B), siblingof(A, C), female(A).
father_in_law(A, B) :- parentof(A, C), partner(B, C), male(A).
brotherof(A, B) :- siblingof(A, B), male(A).
brother_in_lawof(A, B) :- siblingof(C, B), partner(A, C), male(A).
cousinof(A, B) :- grandparentof(C, A), grandparentof(C, B), \+ siblingof(A, B).

% Additional predicates
partner(A, B) :- parentof(A, C), parentof(B, C), A \== B.
happy(X) :- partner(X, _).

% Predicate to find all parents of a person
all_parents(R, M) :- findall(Y, parentof(Y, R), M).
