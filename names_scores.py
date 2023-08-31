""" Exercise from the website Project Euler """

def calculate_name_score(name):
    """
    calculates the score of each nome
    """
    alphabetical_value = sum(ord(char) - ord('A') + 1 for char in name.upper())
    return alphabetical_value

def calculate_total_score(namees):
    """
    returns the total score of each name
    """
    total_score = 0
    for index, name in enumerate(namees, start=1):
        name_score = calculate_name_score(name)
        total_score += name_score * index
    return total_score

with open('C:/Users/Icarl/Desktop/Python Projects/Project Euler/names.txt',
          mode='r', encoding="UTF-8") as file:
    names = file.read().replace('"', '').split(',')

names.sort()

total_scores = calculate_total_score(names)

print(total_scores)
