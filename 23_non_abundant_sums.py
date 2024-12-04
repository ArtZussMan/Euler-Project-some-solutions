total_sum = 0
abundant_numbers = []
max_number = 28123


def sum_of_divisors(n):
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i

    return total


def deficient_or_abundant(n):
    suma = sum_of_divisors(n)
    if suma > n:
        return "Abundant"
    elif suma < n:
        return "Deficient"
    else:
        return "Perfect"


for i in range(1, max_number):
    type_of_number = deficient_or_abundant(i)
    if type_of_number == "Abundant":
        abundant_numbers.append(i)

is_abundant_sum = [False] * max_number

for i in range(len(abundant_numbers)):
    for j in range(i, len(abundant_numbers)):
        abundant_sum = abundant_numbers[i] + abundant_numbers[j]
        if abundant_sum < max_number:
            is_abundant_sum[abundant_sum] = True


# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers
for i in range(1, max_number):
    if not is_abundant_sum[i]:
        total_sum += i
print(total_sum)
