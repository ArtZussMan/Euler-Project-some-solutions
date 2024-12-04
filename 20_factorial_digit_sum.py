# 20 - Factorial Digit Sum
from math import factorial

factor = factorial(100)
soma = sum(int(char) for char in str(factor))
print(soma)
