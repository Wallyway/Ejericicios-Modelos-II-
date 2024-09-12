Lazy Evaluation Workshop
=======================

I. "multiply sum 4 3 subtract 6 2"
---------------------------------

Abreviations:
- multiply as mlp
- subtract as sub

Evaluation:

    1. mlp sum 4 3 sub 6 2
    2. (sum 4 3)*(sub 6 2) <- "muliply"
    3. (4 + 3)*(sub 6 2) <- "sum"
    4. (4 + 3)*(6 - 2) <- "subtract"
    5. 7*(6 - 2) <- "+"
    6. 7*4 <- "-"
    7. 28 <- "*"

El resutlatdo es 28.


II. "factorial fibonacci sum 3 1"
--------------------------------

Abrevations:
- factorial as fac
- fibonacci as fib

Note:
Para este caso se tomará en cuenta la definción clásica del fibonacci (0, 1, 1, 2...),
lo que quiere decir que el cuarto número de la suceción es 2. Lo que quiere decir que "fibonacci 4" es igual a 2.

En pseudocódigo: 

    if n is 1 fibonacci is 0
    else if n is 2 or 3 fibonacci of n is 1
    else fibonacci of n is fibonacci n-1 + fibonacci n-2

Evaluation:

    1. fac fib sum 3 1
    2. (fib sum 3 1)*fac((fib sum 3 1)-1)... <-- "factorial"
    3. (fib(sum 3 1 -1)+fib(sum 3 1 -2)*((fib sum 3 1)-1) <-- "fibonacci"
    4. (fib(3+1 -1)+fib(sum 3 1 -2))*(fib(3+1 -1)+fib(sum 3 1 -2)-1) <-- "sum"

some steps later...

    (fib(3+1 -1)+fib(3+1 -2))*(fib(3+1 -1)+fib(sum 3 1 -2)-1)
    (fib(4 -1)+fib(3+1 -2))*(fib(4 -1)+fib(3+1 -2) - 1) <-- "+"

some steps later...

    (fib(4 -1)+fib(4 -2))*(fib(4 -1)+fib(4 -2) - 1)
    (fib(3)+fib(4-2))*(fib(4-1)+fib(4-2) -1) <-- "-"

some steps later...

    (fib(3)+fib(2))*(fib(3)+fib(2) -1)
    (1 + fib(2))*(fib(3)+fib(2) -1) <-- "fibonacci"

some steps later...

    (1 + 1)*(1 + 1 -1)
    (2)*(2-1) <-- "+"
    2*(1) <-- "-"
    2 <-- "*"

El resultado es 2.

III. something
--------------