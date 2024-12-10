"""
1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
The sum of these numbers is 1634 + 8208 + 9474 = 19316
Find the sums of all the numbers that can be written as the sum of fifth powers of their digits
"""


def digit_power(n, power):
    digits = [int(digit) for digit in str(n)]
    result = sum(digit**power for digit in digits)
    return result

for i in range()

power = 4
print(digit_power(1634, power=power))
