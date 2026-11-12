import math

def power(c, d):
    return c ** d

def logarithm(a, base):
    if a <= 0:
        raise ValueError('Logarithm of x <= is not defined')
    return math.log(a, base)

def exponential(a):
    return math.exp(a)