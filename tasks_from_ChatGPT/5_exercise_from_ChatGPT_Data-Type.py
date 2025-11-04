# # # Start of Exercise 1
# # """
# # Завдання 1: Визнач тип кожної змінної
# #
# # Мета: навчитися використовувати функцію type().
# #
# # Умова:
# # Створи кілька змінних різних типів:
# #
# # a = 10
# # b = 3.14
# # c = "Hello"
# # d = True
# # e = [1, 2, 3]
# #
# #
# # Виведи тип кожної змінної за допомогою type():
# #
# # Тип змінної a: ...
# # Тип змінної b: ...
# # """
# # a = 10
# # b = 3.14
# # c = "Hello"
# # d = True
# # e = [1, 2, 3]
# # print(f" type variable a : {type(a)} ")
# # print(f" type variable b: {type(b)} ")
# # print(f" type variable c: {type(c)} ")
# # print(f" type variable d: {type(d)} ")
# # print(f" type variable e: {type(e)} ")
# # # End of Exercise 1
#
#
# # Start of Exercise 2
# """
# Завдання 2: Визнач тип змінних
#
# Мета: навчитися користуватися функцією type().
#
# Умова:
# Створи три змінні різних типів даних:
#
# name = "Оля"
# age = 15
# height = 1.65
#
#
# Виведи на екран тип кожної змінної, ось так:
#
# Тип змінної name: <class 'str'>
# Тип змінної age: <class 'int'>
# Тип змінної height: <class 'float'>
# """
# name = "Оля"
# age = 15
# height = 1.65
#
# print(f" type variable name : {type(name)} ")
# print(f" type variable age: {type(age)} ")
# print(f" type variable height: {type(height)} ")
#
# # End of Exercise 2

# Start of Exercise 3
"""
Завдання 3: Визнач тип введених даних

Мета: побачити, що все, що вводить користувач через input(), спочатку має тип str.

Умова:

Запитай у користувача його улюблене число.

Виведи тип змінної після введення.

Перетвори введення у число (int) і ще раз виведи тип.

📘 Приклад:

number = input("Введи своє улюблене число: ")
print("Після input:", type(number))

number = int(number)
print("Після перетворення:", type(number))
"""
# Step 1: Ask the user for their favorite number
number = input("Enter your favorite number: ")

# Step 2: Check the type after input()
print("After input:", type(number))

# Step 3: Convert the string to an integer
number = int(number)

# Step 4: Check the type after conversion
print("After conversion:", type(number))


