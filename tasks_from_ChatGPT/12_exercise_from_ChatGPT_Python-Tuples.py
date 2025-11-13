#  Start of Exercise 1
# Завдання 1 — Доступ до елементів кортежу
#
# Рівень: легкий
#
# Створи кортеж із назвами трьох улюблених фруктів.
#
# Виведи перший і останній елемент.
#
# Використай цикл for, щоб вивести всі елементи кортежу.
#
# Спробуй отримати елемент за допомогою від’ємного індексу.
#
# Приклад очікуваного результату:
#
# Перший фрукт: apple
# Останній фрукт: mango
# Усі фрукти:
# apple
# banana
# mango

# fruits = ("apple", "banana", "mango")
#
# print(fruits[0], fruits[-1])
#
# print("   ")
#
# for fruit in fruits:
#     print(fruit)
#
# print("   ")
#
# print(fruits[-3])

#  End of exercise 1


#  Start of Exercise 2
# Завдання 2 — Робота з методами count() і index()
#
# Рівень: середній
#
# Є кортеж:
#
# numbers = (4, 7, 2, 7, 9, 7, 1)
#
#
# Дізнайся, скільки разів число 7 зустрічається у кортежі.
#
# Знайди індекс першої появи числа 9.
#
# Виведи обидва результати у зручному форматі, наприклад:
#
# Число 7 зустрічається 3 рази
# Число 9 вперше зустрічається на позиції 4
# numbers = (4, 7, 2, 7, 9, 7, 1)
# print(numbers.count(7))
# print(numbers.index(9))
#
# print("Number '7' to meet", numbers.count(7), "times")
# print("Number '9' to meet at first in index", numbers.index(9))

#  End of exercise 2



#  Start of Exercise 3
# Завдання 3 — Перетворення та об’єднання
#
# Рівень: трохи складніший
#
# Створи два кортежі:
#
# fruits = ("apple", "banana", "cherry")
# vegetables = ("carrot", "potato", "tomato")
#
#
# Об’єднай їх у один новий кортеж.
#
# Перетвори отриманий кортеж у список, додай новий елемент "cucumber".
#
# Знову перетвори список назад у кортеж і виведи результат.

# fruits = ("apple", "banana", "cherry")
# vegetables = ("carrot", "potato", "tomato")
#
# healthyFood = fruits + vegetables
# print (healthyFood)
#
# newHealthyFood = list(healthyFood)
# newHealthyFood.append("cucumber")
# healthyFood = tuple(newHealthyFood)
# print (healthyFood)
#
# # or
# fruits = ("apple", "banana", "cherry")
# vegetables = ("carrot", "potato", "tomato")
#
# healthyFood = tuple(list(fruits + vegetables) + ["cucumber"])
# print(healthyFood)

#  End of exercise 3