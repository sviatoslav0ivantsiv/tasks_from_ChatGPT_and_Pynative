#  Start of Exercise 1
# ✅ Завдання 1: Створи свій модуль і імпортуй його
#
# Опис:
# Створи файл mymath.py, у якому буде 3 функції:
#
# add(a, b) → повертає суму
#
# subtract(a, b) → повертає різницю
#
# multiply(a, b) → повертає добуток
#
# У іншому файлі main.py:
#
# Імпортуй модуль mymath
#
# Використай всі три функції
#
# Виведи результат кожної
#
# Ціль: практика зі створення власного модуля та його імпорту.

# import mymath
# print (mymath.add(5, 6))
# print (mymath.sub(8, 3))
# print (mymath.mul(2, 9))

# End of exercise 1

#  Start of Exercise 2
# Завдання 2: Імпорт тільки окремих функцій
#
# Створи файл converter.py з функціями:
#
# km_to_miles(km)
#
# celsius_to_fahrenheit(c)
#
# У файлі main.py:
#
# Імпортуй лише одну функцію з модуля:
#
# from converter import km_to_miles
#
#
# Виклич її
#
# Спробуй викликати другу функцію й подивись, яка виникне помилка (для розуміння, як працює імпорт)
#
# Ціль: навчитися імпортувати тільки потрібні елементи.
#

# from converter import convert_distance
# convert_distance(100)
#
# from converter import convert_temp
# convert_temp(100)

# End of exercise 2



#  Start of Exercise 3
# Завдання 3: Використай вбудований модуль та свій власний
#
# Створи файл tools.py із функцією:
#
# random_greeting() — повертає випадкове привітання зі списку, наприклад:
#
# ["Hello", "Hi", "Welcome", "Good day"]
#
#
# У файлі main.py:
#
# Імпортуй модуль random (вбудований модуль Python)
#
# Імпортуй свій модуль tools
#
# Зроби так, щоб:
#
# випадкове привітання з tools.random_greeting()
#
# доповнювалося випадковим числом від 1 до 100 (модуль random)
#
# Виведи результат, наприклад:
#
# Hello 42
#
#
# Ціль: навчитися комбінувати власні модулі та стандартні модулі Python.

import random

import tools

print(random.randint(1, 100))

# End of exercise 3