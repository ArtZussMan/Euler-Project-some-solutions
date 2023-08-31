
unique_powers = set() # Convert iterable to sequence of iterable with different elements

for a in range(2,101):
    for b in range(2,101):
        power = a ** b
        unique_powers.add(power)


print(len(unique_powers))
