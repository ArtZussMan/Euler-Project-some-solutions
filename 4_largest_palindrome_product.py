"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two
2-digit numbers is 9009 = 91 x 99
Find the largest palindrome made from the product of two 3-digit numbers.
"""

largest_palindrome = 0

# Iterate through all possible combinations of two 2-digit numbers
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j

        # Check if the product is a palindrome
        if str(product) == str(product)[::-1]:
            # Update the largest palindrome if necessary
            if product > largest_palindrome:
                largest_palindrome = product

print("The largest palindrome made from the product of two 3-digit numbers is:", largest_palindrome)
