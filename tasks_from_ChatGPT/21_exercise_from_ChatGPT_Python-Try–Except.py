#  Start of Exercise 1
# 🧪 Практичні завдання: Python Try Except
# 1. Безпечне перетворення числа
#
# Запроси у користувача число.
# Якщо введено не число — виведи повідомлення:
#
# Помилка: введено не число
#
#
# 📌 Підказка: int() + ValueError
#
# try:
#     number = int(input("Enter a number: "))
#     print("You entered number : ", number)
# except ValueError:
#     print("You didn't enter a number. Please try again.")
from operator import truediv

# End of exercise 1
#

# Start of Exercise 2
# 2. Ділення без аварії
#
# Запроси два числа і поділи перше на друге.
# Оброби:
#
# ділення на нуль
#
# введення нечислових значень
#
# 📌 Використай: ZeroDivisionError, ValueError
# try:
#     number1 = int(input("Enter a firs number: "))
#     number2 = int(input("Enter a second number: "))
#     division = number1 / number2
#     print(division)
# except ValueError:
#     print("You didn't enter a number. Please try again.")
# except ZeroDivisionError:
#     print("Division by zero didn't work. Please try again.")
# End of exercise 2


# Start of Exercise 3
# 3. Доступ до елемента списку
#
# Є список:
#
# numbers = [10, 20, 30, 40]
#
#
# Запроси індекс у користувача і виведи елемент.
# Якщо індекс неправильний — виведи повідомлення про помилку.
#
# 📌 Підказка: IndexError

# try:
#     numbers = [10, 20, 30, 40]
#     index = int(input("Enter the index of value :"))
#     number_index = numbers[index]
#     print(number_index)
# except IndexError:
#     print("Index out of range, try again")

# End of exercise 3

# Start of Exercise 4
# 4. Пошук ключа у словнику
#
# Є словник:
#
# person = {"name": "Anna", "age": 25}
#
#
# Запроси ключ у користувача та виведи значення.
# Якщо ключа не існує — оброби помилку.
#
# 📌 Підказка: KeyError
#
# try:
#     person = {"name": "Anna", "age": 25}
#     user_key = input("Enter your key: ")
#     user_value = person[user_key]
#     print(user_value)
# except KeyError:
#     print("Key not found")
# End of exercise 4


# Start of Exercise 5

# 5. Перевірка числа на парність
#
# Запроси число і перевір:
#
# якщо це не число → помилка
#
# якщо число є → виведи, парне воно чи ні
#
# 📌 Використай: try / except / else
# try:
#     number = int(input("Enter your number: "))
#     if number % 2 == 0:
#         print(f"{number} is even")
#     else:
#         print(f"{number} is odd")
# except ValueError:
#     print ("Please enter a number")
# End of exercise 5


# Start of exercise 6
# 6. Калькулятор (мінімальний)
#
# Запроси:
#
# два числа
#
# операцію (+, -, *, /)
#
# Оброби:
#
# неправильне число ValueError
#
# ділення на нуль ZeroDivisionError
#
# невідому операцію
#
# 📌 Використай: if / elif, try except
# try:
#     number1 = float(input("Enter first number: "))
#     number2 = float(input("Enter another number: "))
#     operation = input("Enter operation (+, -, *, /): ")
#     if operation == "+":
#         print(number1 + number2)
#     elif operation == "-":
#         print(number1 - number2)
#     elif operation == "*":
#         print(number1 * number2)
#     elif operation == "/":
#         print(number1 / number2)
#     else:
#         print("Unknown operation")
# except ValueError:
#     print("You didn't enter a number")
# except ZeroDivisionError:
#     print("Division by zero")

# End of exercise 6


# Start of exercise 7

# 7. Обробка списку чисел
#
# Є список:
#
# values = ["10", "20", "abc", "30"]
#
# Спробуй перетворити всі значення у int.
# Якщо виникає помилка — пропусти елемент і виведи повідомлення.
#
# 📌 Підказка: цикл for + ValueError


# values = ["10", "20", "abc", "30"]
#
# for value in values:
#     try:
#         print(int(value))
#     except ValueError:
#         print("invalid literal for int")

# End of exercise 7


# Start of exercise 8
# 8. Перевірка довжини рядка
#
# Запроси у користувача рядок.
# Якщо він вводить не рядок (імітуй через int()), оброби помилку.
# Інакше — виведи довжину рядка.
#
# 📌 Використай: len(), try except else
# try:
#     user_str = input("Enter your string: ")
#     int(user_str)
# except ValueError:
#     print("Lenght :", len(user_str))
# else:
#     print("You didn't enter a string")
# End of exercise 8

# Start of exercise 9
# 9. Вгадай число (з помилками)
#
# Програма загадує число від 1 до 5.
# Користувач вводить відповідь.
#
# якщо введено не число → помилка
#
# якщо число не в діапазоні → повідомлення
#
# 📌 Використай: if, try except
# import random
# program_number = random.randint(1, 5)
#
# try:
#     user_number = int(input("Enter your number from 1 to 5: "))
# except ValueError:
#     print("You didn't enter a number.")
# else:
#     if user_number < 1 or user_number > 5 :
#         print("You didn't enter a number from 1 to 5")
#
#     if program_number == user_number:
#         print("Your number is correct")
#     else:
#         print("Your number is incorrect")
#
#     print("Your number :", user_number)
# print("Program number :", program_number)

# End of exercise 9

# Start of exercise 10
# 10. Власне повідомлення про помилку
#
# Запроси число.
#
# якщо воно менше 0 — штучно виклич помилку
#
# і оброби її через except
#
# 📌 Підказка: raise ValueError
#
# 🔥 Додаткове завдання (челендж)
#
# Зроби меню:
#
# 1 - додавання
# 2 - віднімання
# 0 - вихід
#
#
# Програма працює у while і не падає при будь-якому неправильному вводі.

while True:
    try:
        choice = int(input(
            " \nMenu:\n"
            "1 - addition \n"
            "2 - subtraction \n"
            "0 - Exit \n"
            "Chosee option:"))

        if choice == 0:
            print("bye")
            break

        elif choice not in (1, 2):
            raise ValueError("Invalid menu option")

        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if choice == 1:
            print("Result:", a + b)

        elif choice == 2:
            print("Result :", a - b)

    except ValueError as e:
        print("Error:", e)


## End of exercise 10


