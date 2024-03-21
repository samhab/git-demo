import math

def power(a, b):
    return a ** b

def logarithm(x):
    if x <= 0:
        raise ValueError('Logarithm of x <= is not defined')
    return math.log(x)
