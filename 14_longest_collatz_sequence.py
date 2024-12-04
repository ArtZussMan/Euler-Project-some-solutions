# Longest Collatz Sequence
def collatz_sequence_length(n):
    count = 1
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count


max_length = 0
number_with_longest_sequence = 0

for number in range(1, 1000000):
    length = collatz_sequence_length(number)
    if length > max_length:
        max_length = length
        number_with_longest_sequence = number

print("Number with the longest Collatz sequence:", number_with_longest_sequence)
print("Length of the longest Collatz sequence:", max_length)
