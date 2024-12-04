def find_repeating_decimal(numerator, denominator):
    # Handle the case when there's no repeating decimal (terminating decimal)
    remainder = numerator % denominator
    seen_remainders = {}
    decimal_places = []

    while remainder != 0:
        if remainder in seen_remainders:
            start_index = seen_remainders[remainder]
            repeating_cycle = decimal_places[start_index:]
            non_repeating = decimal_places[:start_index]
            return f"0.{''.join(map(str, non_repeating))}({''.join(map(str, repeating_cycle))})"

        seen_remainders[remainder] = len(decimal_places)
        remainder *= 10
        decimal_places.append(remainder // denominator)
        remainder %= denominator

    # If no repeating decimal, return the terminating decimal part
    return f"0.{''.join(map(str, decimal_places))}"


results = []
for d in range(1, 1000):
    result = find_repeating_decimal(1, denominator=d)
    results.append(result)

# Find the longest recurring cycle, and its corresponding denominator (d)
longest_cycle = max(results, key=len)
longest_cycle_length = len(
    longest_cycle.split("(")[-1].split(")")[0]
)  # Get length of repeating part
corresponding_d = results.index(longest_cycle) + 1

print(f"The value of d that contains the longest recurring cycle is: {corresponding_d}")
print(f"The length of the longest recurring cycle is: {longest_cycle_length}")
