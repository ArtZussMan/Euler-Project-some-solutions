limit = 10000
fibonacci_list = [1, 1]

for i in range(2, limit):
    fibonacci = fibonacci_list[-1] + fibonacci_list[-2]  # Access last two elements
    fibonacci_list.append(fibonacci)

    if len(str(fibonacci)) >= 1000:
        print(i)
        break

print(len(str(fibonacci_list[4781])))
