
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        ## raise ValueError("Denominator cannot be zero.")
        return None 
    return x / y

def power(x, y):
    return math.pow(x, y)

def sqrt(x):
    if x < 0:
        raise ValueError("Input must be a non-negative number.")
    return math.sqrt(x)

def factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def mod(x, y):
    if y == 0:
        raise ValueError("Denominator cannot be zero.")
    return x % y

def abs(x):
    if x > 0:
        return x
    else:
        return -x

