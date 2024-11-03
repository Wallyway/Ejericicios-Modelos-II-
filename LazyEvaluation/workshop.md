Lazy Evaluation Workshop
========================

I. "multiply sum 4 3 subtract 6 2"
----------------------------------

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
---------------------------------

Abrevations:
- factorial as fac
- fibonacci as fib

Note:
Para este caso se tomará en cuenta la definción clásica del fibonacci (0, 1, 1, 2...),
lo que quiere decir que el cuarto número de la suceción es 2. Lo que quiere decir que "fibonacci 4" es igual a 2.

En pseudocódigo: 

    if n is 1 fibonacci is 0
    else if n is 2 or 3 fibonacci of n is 1
    else fibonacci of n is fibonacci of n-1 + fibonacci of n-2

Evaluation:

    1. fac fib sum 3 1
    2. (fib sum 3 1)*fac((fib sum 3 1)-1)... <-- "factorial"
    3. (fib(sum 3 1 -1)+fib(sum 3 1 -2)*((fib sum 3 1)-1) <-- "fibonacci"
    4. (fib(3+1 -1)+fib(sum 3 1 -2))*(fib(3+1 -1)+fib(sum 3 1 -2)-1) <-- "sum"

some sum steps later...

    (fib(3+1 -1)+fib(3+1 -2))*(fib(3+1 -1)+fib(sum 3 1 -2)-1)
    (fib(4 -1)+fib(3+1 -2))*(fib(4 -1)+fib(3+1 -2) - 1) <-- "+"

some pluses steps later...

    (fib(4 -1)+fib(4 -2))*(fib(4 -1)+fib(4 -2) - 1)
    (fib(3)+fib(4-2))*(fib(4-1)+fib(4-2) -1) <-- "-"

some subtract operations later...

    (fib(3)+fib(2))*(fib(3)+fib(2) -1)
    (1 + fib(2))*(fib(3)+fib(2) -1) <-- "fibonacci"

some fibonacci steps later...

    (1 + 1)*(1 + 1 -1)
    (2)*(2-1) <-- "+"
    2*(1) <-- "-"
    2 <-- "*"

El resultado es 2.

III. "power product 3 sumList [1...5] 2"
----------------------------------------

Abbreviations:
- power as pow
- product as prod
- sumList as sml

Evaluacition:

	1. pow prod 3 sml [1..5] 2
	2. (prod 3 sml [1..5])*(prod 3 sml [1..5]) <-- "power"
	3. (3 * sml [1..5])*(prod 3 sml [1..5]) <-- "product"
	4. (3 * sml [1..5]) * (3 * sml [1..5]) <-- "product"
	5. (3 * sml [1,2,3,4,5])*(3 * sml [1..5]) <-- ".."
	6. (3 * sml [1,2,3,4,5])*(3 * sml [1,2,3,4,5]) <-- ".."
  7. (3 * (1+ sml [2,3,4,5]) * (3 * (sml [1,2,3,4,5]) <-- "sumList"

some sumList steps later...

	(3 * (1+2+3+4+5+0)) * (3 * (1+2+3+4+5+0))
	(3 * 15) * (3 * (1 + 2 + 3 + 4 + 5 + 0)) <-- "+"
	(3 * 15) * (3 * 15) <-- "+"
	45 * (3 *1 5) <-- "*"
	45 * 45 <-- "*"
	2025 <-- "*"

El resultado es 2025.
