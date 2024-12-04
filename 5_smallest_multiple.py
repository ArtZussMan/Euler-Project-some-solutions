"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any
remainder. What is the smallest positive number that is evenly divisible by all of the numbers
from 1 to 20?
"""
import math

lcm = 1

for number in range(2,100):
    lcm = (lcm * number) // math.gcd(lcm, number)

print(lcm)
