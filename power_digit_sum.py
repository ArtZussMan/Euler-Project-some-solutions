"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26
What is the sums of the digits of the number 2^1000?
"""

power = int(input("Input a value: "))
result = 2 ** power
result = str(result)
suma = 0

for i in result:
    suma += int(i)

print(suma)