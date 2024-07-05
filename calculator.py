import math
def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b ==0:
        raise ValueError('--ZeroDivisionError--')
    return a / b
def power(a, b):
    if b < 0:
        raise ValueError('--not available in basic calculator--')
    return math.pow(a, b)
def sqroot(a):
    if a < 0:
        raise ValueError('--Must be positive')
    return math.sqrt(a)

