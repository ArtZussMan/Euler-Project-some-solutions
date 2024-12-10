from tqdm import tqdm


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    return all(n % i != 0 and n % (i + 2) != 0 for i in range(5, int(n**0.5) + 1, 6))


max_primes = 0
product_ab = 0
cont = 0

for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0
        while True:
            result = n**2 + a * n + b
            cont += 1
            if not is_prime(result):
                break
            n += 1
        if n > max_primes:
            max_primes = n
            product_ab = a * b

print("Product of coefficients a and b:", product_ab)
print("Maximum number of consecutive primes:", max_primes)
