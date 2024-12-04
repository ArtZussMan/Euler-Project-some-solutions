# Summation of Primes
prume = []


def is_prime(n):
    """
    Print's if any given number is prime or not
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


for num in range(1, 2_000_000):
    if is_prime(num):
        prume.append(num)

print(sum(prume))
