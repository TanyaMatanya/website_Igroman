def process_string(input_string: str) -> tuple:
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    sorted_vowels = sorted([char for char in input_string if char in vowels], reverse=True)
    sorted_consonants = sorted([char for char in input_string if char in consonants], reverse=True)

    more_than_three_vowels = len(sorted_vowels) > 3

    return "".join(sorted_vowels), more_than_three_vowels, "".join(sorted_consonants)


# Ввод данных
input_string = input("Введіть рядок: ")
result = process_string(input_string)

# Вывод результата
print(result)