import math


def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 == 0:
        raise ValueError("Denominator cannot be zero. extcode: 1")
    return num1 / num2
def mod(num1, num2):
    if num2 == 0:
        raise ValueError("Denominator cannot be zero. extcode: 1")
    return num1 % num2
def sin(num):
    return math.sin(num)
def cos(num):
    return math.cos(num)
def tan(num):
    return math.tan(num)
def sqrt(num):
    if num < 0:
        raise ValueError("Cannot compute square root of negative number. extcode: 1")
    return math.sqrt(num)
def pow(num1, num2):
    return math.pow(num1, num2)
def log(num, base=math.e):
    if num <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers. extcode: 1")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1. extcode: 1")
    return math.log(num, base)

def exp(num):
    return math.exp(num)
def floor(num):
    return math.floor(num)
def ceil(num):
    return math.ceil(num)
def abs(num):
    return abs(num)
def round(num, ndigits=0):
    return round(num, ndigits)

def factorial(num):
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers. extcode: 1")
    return math.factorial(num)


def gcd(num1, num2):
    return math.gcd(num1, num2)
def lcm(num1, num2):
    def lcm_helper(a, b):
        return abs(a * b) // math.gcd(a, b)
    return lcm_helper(num1, num2)
