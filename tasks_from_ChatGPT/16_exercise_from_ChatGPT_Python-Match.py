#  Start of Exercise 1
# Завдання 1 — Календарний помічник
# Опис:
#
# Користувач вводить номер місяця (1–12).
# Використовуючи match, виведи:
#
# назву місяця
#
# кількість днів у ньому
#
# чи це зимовий/весняний/літній/осінній сезон
#
# Приклад:
# Введіть номер місяця: 3
# Місяць: Березень
# Днів: 31
# Сезон: Весна

# month = int(input(" Enter your month: "))
#
# match month:
#     case 1 :
#         print( {
#             "month": "January",
#             "days": 31,
#             "season": "winter"
#         })
#     case 2 :
#         print( {
#             "month": "February",
#             "days": 28,
#             "season": "winter"
#         })
#     case 3 :
#         print( {
#             "month": "March",
#             "days": 31,
#             "season": "spring"
#         })
#     case 4 :
#         print ( {
#             "month": "April",
#             "days": 31,
#             "season": "spring"
#         })

# End of exercise 1


#  Start of Exercise 2
# Завдання 2 — Калькулятор простих операцій
# Опис:
#
# Створи програму-калькулятор.
# Користувач вводить:
#
# перше число
#
# оператор (+, -, *, /)
#
# друге число
#
# Використай match для виконання відповідної операції.
#
# Приклад:
# Введіть перше число: 4
# Введіть оператор: *
# Введіть друге число: 6
# Результат: 24
#  End of exercise 2

# number1 = int(input("Enter your first number: "))
# operators = input("Enter your operators: (+, -, *, /) ")
# number2 = int(input("Enter your second number: "))
#
# match operators:
#     case "+":
#         print("Your resuls: ", number1 + number2)
#     case "*":
#         print("Your resuls: ", number1 * number2)
#     case "/":
#         if number2 == 0:
#             print("Error: Division by zero  ")
#         else:
#             print("Your resuls: ", number1 / number2)
#     case "-":
#         print("Your resuls: ", number1 - number2)
#     case _:
#         print("Unknown operator!")



#  Start of Exercise 3
# Завдання 3 — Класифікація дня тижня
# Опис:
#
# Користувач вводить число від 1 до 7.
# Використовуючи match:
#
# 1–5 → робочий день
#
# 6–7 → вихідний
#
# інші числа → помилка
#
# Приклад:
# Введіть номер дня тижня: 6
# Це вихідний день.

day = int(input("Enter number of the day of the week: "))
match day:
    case 1 | 2 | 3 | 4 | 5 :
        print ( "weekday")
    case 6 | 7 :
        print ( "weekend")
    case _ :
        print ( "Error")

# End of exercise 3