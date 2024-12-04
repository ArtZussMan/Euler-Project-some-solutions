import math 

with open('Project Euler/largest_product.txt', 'r') as file:
    files = file.read()
    # files = int(files)

interval_lenght = 13
max_product = 1
max_product_substring = ""

for i in range(len(files) - interval_lenght + 1):
    interval = files[i:i+interval_lenght]
    product = 1
    for digit in interval:
        if digit.isdigit(): 
            product *= int(digit)
    if product > max_product:
        max_product = product
        max_product_substring = interval

print(f"The maximum product of {interval_lenght} adjacent digits is: {max_product}")
print(f"The corresponding substring is: {max_product_substring}")
        