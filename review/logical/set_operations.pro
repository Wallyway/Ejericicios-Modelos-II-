% Union
union(Set, [], Set).
union(Set, [Head|Tail], [Head|NewTail]) :- union(Set, Tail, NewTail).

% Intersection
exist([X|_], X).
exist([_|Tail], X) :- exist(Tail, X).

intersection(_, [], []).
intersection(Set, [Head|Tail], [Head|Result]) :-
        exist(Set, Head),
        intersection(Set, Tail, Result).
intersection(Set, [Head|Tail], Result) :-
        \+ exist(Set, Head),
        intersection(Set, Tail, Result).

% Difference
difference([], _, []).
difference([Head|Tail], Set, [Head|Result]) :-
        \+ exist(Set, Head),
        difference(Tail, Set, Result).
difference([Head|Tail], Set, Result) :-
        exist(Set, Head),
        difference(Tail, Set, Result).
