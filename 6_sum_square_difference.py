# The sum of the squares of the first n natural numbers is:

n = int(input("Input a value: "))
sum_squares = 0

for i in range(1,n+1):
    quad = i**2
    sum_squares += quad

print(f"The sum of the squares of the first {n} natural numbers is {sum_squares}")
# The square of the sum of the first n natural numbers is:
square_sum = 0
for j in range(1,n+1):
    square_sum += j
    
print(f"The square of the sum of the first {n} natural numbers is {square_sum**2}")

print(f"""The difference between square of the sum and the 
      sum of the squares is {square_sum**2 - sum_squares}""")