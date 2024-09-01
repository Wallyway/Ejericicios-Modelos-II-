def recdivide(dividend, divider):
    if dividend  == 0:
        return 0
    return 1 + recdivide(dividend-divider, divider)

def secdivide(dividend, divider):
    result = 0
    while dividend > 0:
        result += 1
        dividend -= divider
    return result

def recmultiply(factor_a, factor_b):
    if factor_a == 0:
        return 0
    return factor_b + recmultiply(factor_a-1, factor_b)

def secmultiply(factor_a, factor_b):
    result = 0
    for i in range(abs(factor_a)):
        result += factor_b
    return result

def recpower(base, exp):
    if exp == 0:
        return 1
    return base*recpower(base, exp-1)

def secpower(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result

def recfibonacci(nth):
    if nth == 1:
        return 0
    elif nth < 4:
        return 1
    return recfibonacci(nth-1)+recfibonacci(nth-2)

def secfibonacci(nth):
    if nth == 1:
        return 0
    elif nth < 4:
        return 1

    result = 0
    nth1 = 0
    nth2 = 1
    
    for i in range(nth-2):
        result = nth1 + nth2
        nth1 = nth2
        nth2 = result
    return result

a = 25
b = 5
print("División recursiva:", recdivide(a,b),"| secuencial:",secdivide(a,b))
print("Multiplicación resursiva:",recmultiply(a,b),"| secuencial:",secmultiply(a,b))
print("Fibonacci recursivo:", recfibonacci(b),"| secuencial:",secfibonacci(b))
print("Potencia al cuadrado recursiva:",recpower(a,b),"| secuencial:",secpower(a,b))
