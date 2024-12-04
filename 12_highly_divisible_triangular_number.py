# Highly Divisible Triangular Number
from collections import Counter


def prime_factorization(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def count_divisors(n):
    factors = prime_factorization(n)
    count = 1
    for _, exp in Counter(factors).items():
        count *= exp + 1
    return count


target_divisors = 500
triangle_number = 1
increment = 2

while count_divisors(triangle_number) <= target_divisors:
    triangle_number += increment
    increment += 1

print(
    f"The value of the first triangle number to have over {target_divisors} divisors is: {triangle_number}"
)
