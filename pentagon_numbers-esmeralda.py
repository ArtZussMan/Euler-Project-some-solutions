def generate_pentagonal_numbers(n):
    pentagonal_numbers = []
    for i in range(1, n+1):
        pentagonal_number = i * (3*i - 1) // 2
        pentagonal_numbers.append(pentagonal_number)
    return pentagonal_numbers

def find_minimum_difference():
    pentagonal_numbers = generate_pentagonal_numbers(10000)  # Generate the first 10000 pentagonal numbers

    min_difference = float('inf')
    for i in range(len(pentagonal_numbers)):
        for j in range(i+1, len(pentagonal_numbers)):
            sum_pentagonal = pentagonal_numbers[i] + pentagonal_numbers[j]
            diff_pentagonal = abs(pentagonal_numbers[i] - pentagonal_numbers[j])

            if sum_pentagonal in pentagonal_numbers and diff_pentagonal in pentagonal_numbers:
                if diff_pentagonal < min_difference:
                    min_difference = diff_pentagonal

    return min_difference

# Find the minimum difference
minimum_difference = find_minimum_difference()
print("The minimum difference D is:", minimum_difference)