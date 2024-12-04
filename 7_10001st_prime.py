# 10001st Prime

def is_prime(n):
    '''
    Print's if any given number is prime or not
    '''
    if n <= 1:
        return False
    for i in range(2, int( n ** 0.5 ) + 1):
        if n % i == 0:
            return False
    return True


primes = []

for num in range(1, 500_000):
    if is_prime(num):
        primes.append(num)
    
print(f"The 10001st prime number is {primes[10001]}")
        