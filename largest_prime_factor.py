"""
The prime factors of 13195 are 5, 7, 13, 29.
What is the largest prime factor of the number 600_851_475_143
"""
def largest_prime_factor(num):
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
    if num > 1:
        return num
    
# Find the largest prime factor of 600_851_475_143
number = 600_851_475_143
largest_factor = largest_prime_factor(number)

print("The largest prime factor of", number, "is:", largest_factor)

