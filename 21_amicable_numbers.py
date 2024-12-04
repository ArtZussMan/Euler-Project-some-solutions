def sum_of_divisors(n):
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i

    return total


amicable_nums = []

for a in range(2, 10000):
    b = sum_of_divisors(a)
    if b > a and sum_of_divisors(b) == a:
        amicable_nums.append(a)
        amicable_nums.append(b)


print(sum(amicable_nums))
# print(total_sum)
