def number_spiral_diagonals(size):
    if size % 2 == 0:
        raise ValueError("Size must be an odd number")

    total = 1
    current_number = 1
    for layer in range(1, (size // 2) + 1):
        # step is the difference between consecutive diagonal numbers in the current layer
        step = layer * 2
        for _ in range(4): # There are always 4 corners in each layer
            current_number += step # move to the next diagonal number
            total += current_number

    return total

size = 1001
result = number_spiral_diagonals(size)
print(f"The sum of the numbers on the diagonals in a {size} by {size} spiral is {result}")