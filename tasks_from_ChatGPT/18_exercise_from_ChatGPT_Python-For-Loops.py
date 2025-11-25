#  Start of Exercise 1
# Завдання 1. Підрахунок голосних у рядку
#
# Опис:
# Користувач вводить рядок. Використай цикл for, щоб підрахувати кількість голосних літер (a, e, i, o, u, українські теж можна додати, якщо хочеш).
#
# Приклад вводу:
#
# Enter text: Hello World
#
#
# Очікуваний вивід:
#
# Number of vowels: 3

# enterText = "Hello World"
# numberOfLetters = 0
#
# for letter in enterText:
#     if letter.lower() in 'aeiou':
#         numberOfLetters += 1
#
# print(numberOfLetters)

# End of exercise 1

#  Start of Exercise 2
# Завдання 2. Сума всіх чисел у списку
#
# Опис:
# Є список чисел. Обчисли суму всіх елементів за допомогою циклу for (не використовуй sum()).
#
# Дані:
#
# numbers = [4, 7, 12, 3, 9, 1]
#
#
# Очікуваний вивід:
#
# Total: 36

# numbers = [4, 7, 12, 3, 9, 1]
# sum = 0
# for number in numbers:
#     sum += number
# print(sum)

#  End of exercise 2


#  Start of Exercise 3

# Завдання 3. Вивести тільки ключі або тільки значення словника
#
# Опис:
# Дано словник.
#
# За допомогою for виведи всі ключі
#
# За допомогою for виведи всі значення
#
# Дані:
#
# person = {
#     "name": "Alex",
#     "age": 25,
#     "city": "Kyiv"
# }
#
#
# Очікуваний вивід:
#
# Keys:
# name
# age
# city
#
# Values:
# Alex
# 25
# Kyiv

person = {
     "name": "Alex",
     "age": 25,
     "city": "Kyiv"
 }

for  keys in person:
    print("Keys: ", keys)

for values in person:
    print ("Values: ", person[values])

# End of exercise 3