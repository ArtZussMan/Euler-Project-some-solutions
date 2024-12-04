# Counting number letters


def convert_to_word(number):
    # Define word representations for numbers up to 20
    num_words = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
    }

    # Define word representations for tens
    tens_words = {
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
    }

    if number == 1000:
        return "one thousand"
    elif number < 20:
        return num_words[number]
    elif number < 100:
        tens = number // 10
        ones = number % 10
        return (
            tens_words[tens] + " " + num_words[ones] if ones != 0 else tens_words[tens]
        )
    else:
        hundreds = number // 100
        remainder = number % 100
        if remainder != 0:
            return num_words[hundreds] + " hundred and " + convert_to_word(remainder)
        else:
            return num_words[hundreds] + " hundred"


def count_letters(word):
    # Remove spaces and hyphens from the word
    word = word.replace(" ", "").replace("-", "")
    return len(word)


total_letters = 0

for number in range(1, 1001):
    word = convert_to_word(number)
    letter_count = count_letters(word)
    total_letters += letter_count

print(total_letters)
