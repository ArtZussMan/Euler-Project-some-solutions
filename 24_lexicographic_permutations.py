import math


def find_lexicographic_permutation(n):
    digits = list(range(10))
    result = []

    n -= 1  # Adjust for 0-based indexing
    for i in range(9, -1, -1):
        index = n // math.factorial(i)
        result.append(digits[index])
        digits.pop(index)
        n %= math.factorial(i)

    return "".join(map(str, result))


millionth_permutation = find_lexicographic_permutation(1000000)
print(millionth_permutation)
