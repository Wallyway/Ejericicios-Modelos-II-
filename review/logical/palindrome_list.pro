% Palindrome
palindrome([]).
palindrome([_]).
palindrome(List) :- reverse(List, List).

