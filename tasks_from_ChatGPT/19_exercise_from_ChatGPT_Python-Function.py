#  Start of Exercise 1
# Завдання 1 — Функція, що перевіряє парність числа
#
# Опис:
# Напиши функцію is_even(n), яка приймає число і повертає True, якщо воно парне, і False, якщо непарне.
# Потім виклич цю функцію в циклі для чисел з 1 до 20.
#
# Приклад очікуваного виводу:
#
# 1 -> False
# 2 -> True
# 3 -> False
# 4 -> True
# ...

# def chek_even(num):
#     for x in range(1, num):
#         print (x, ">> even" if x % 2 == 0 else ">> odd")
#
# list = chek_even(21)
# print (list )

# End of exercise 1

#  Start of Exercise 2
# Завдання 2 — Функція, що рахує кількість голосних у рядку
#
# Опис:
# Створи функцію count_vowels(text), яка рахує кількість голосних літер у рядку (a, e, i, o, u).
# Функція має повертати число.
#
# Потім виклич її на кількох прикладах:
#
# "hello"
# "python"
# "beautiful day"
#
#
# Підказка: використовуй цикл for і оператор in.

#  End of exercise 2

# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     vowels_letter = []
#     for letter in text:
#         if letter in vowels:
#             vowels_letter.append(letter)
#     number_of_vowels = len(vowels_letter)
#     return number_of_vowels
#
# print(count_vowels("hello"))
# print(count_vowels("python"))
# print(count_vowels("beautiful day"))

#  Start of Exercise 3
# Завдання 3 — Функція, що повертає найбільше число зі списку
#
# Опис:
# Реалізуй функцію my_max(numbers), яка не використовує вбудований max(), а сама знаходить найбільший елемент списку.
#
# Функція:
#
# приймає список чисел
#
# проходить його циклом
#
# повертає максимальне значення
#
# Потім протестуй її:
#
# print(my_max([3, 7, 1, 9, 4]))
# print(my_max([-5, -2, -10]))
#
#
# Очікування:
#
# 9
# -2

# def my_max(numbers):
#     return max(numbers)
# print(my_max([3, 7, 1, 9, 4]))
# print(my_max([-5, -2, -10]))

# def my_max(numbers):
#     largest = numbers[0]
#     for number in numbers:
#        if number > largest:
#            largest = number
#     return largest
#
# print(my_max([3, 7, 1, 9, 4]))
# print(my_max([-5, -2, -10]))

def my_max(numbers):
    largest = sorted (numbers)
    print (largest)
    print (largest[-1])

print(my_max([3, 7, 1, 9, 4]))
print(my_max([-5, -2, -10]))
# End of exercise 3