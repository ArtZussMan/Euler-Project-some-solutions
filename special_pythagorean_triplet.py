"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a²+b² = c²
For example, 3² + 4² = 9 + 16 = 25 = 5²
There exists exactly one Pythagorean triplet for which a + b + c = 1000
Find the product abc
"""
found_solution = False

for i in range(1,1000):
    for j in range(1,1000):
        for k in range(1,1000):
            
            if i**2 + j**2 == k**2 and i+j+k == 1000:
                print(f""" 
                        There is a solution:
                        i = {i}
                        j = {j}
                        k = {k}
                        And the solution for a*b*c is
                        {i*j*k}
                        """)
                found_solution = True
                break
        if found_solution:
            break
    if found_solution:
        break    
                    
if not found_solution:
    print("No solution found.")

'''  
A different approach that giver directly the result, without taking too long:
It uses the "Pythagorean Triplet Formula." The Pythagorean Triplet Formula states 
that for any two positive integers m and n where m > n, a Pythagorean triplet can be 
generated using the following formulas:
a = m^2 - n^2
b = 2 * m * n
c = m^2 + n^2

for m in range(2, 1000):
    for n in range(1, m):
        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2

        if a + b + c == 1000:
            product = a * b * c
            print(f"The product of the Pythagorean triplet where a + b + c = 1000 is: {product}")
            break
    else:
        continue
    break
'''