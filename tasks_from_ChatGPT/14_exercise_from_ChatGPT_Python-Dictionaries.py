#  Start of Exercise 1
# Завдання 1 — Фільтрація унікальних значень
#
# Створи програму, яка:
#
# Приймає список чисел (із повтореннями).
#
# Перетворює його на множину та повертає тільки унікальні елементи.
#
# Виводить:
#
# початковий список
#
# множину унікальних значень
#
# кількість унікальних елементів
#
# Приклад вводу:
#
# [1, 2, 2, 3, 4, 4, 5]
#
#
# Приклад виводу:
#
# Initial list: [...]
# Unique values: {1, 2, 3, 4, 5}
# Count: 5

# initial_list = input("Enter your random number: ")
#
# unique_values = set(initial_list)
# print(unique_values)
# print(len(unique_values))

#  End of exercise 1


#  Start of Exercise 2
# Завдання 2 — Порівняння множин
#
# У тебе є два набори товарів, що є в магазині:
#
# store1 = {"bread", "milk", "eggs", "coffee"}
# store2 = {"milk", "tea", "chocolate", "bread"}
#
#
# Напиши програму, яка виводить:
#
# Товари, що є в обох магазинах (перетин).
#
# Товари, що є лише в першому магазині.
#
# Товари, що є лише в другому магазині.
#
# Об’єднаний список усіх товарів без повторень.

# store1 = {"bread", "milk", "eggs", "coffee"}
# store2 = {"milk", "tea", "chocolate", "bread"}
# print(store1.intersection(store2))
# print(store1)
# print(store2)
# print(store1 | store2)

#  End of exercise 2



#  Start of Exercise 3
# Завдання 3 — Меню ресторану (динамічне оновлення множини)
#
# Створи множину menu, яка містить страви ресторану, наприклад:
#
# menu = {"pizza", "burger", "salad"}
#
#
# Потім:
#
# Додай у меню дві нові страви add().
#
# Спробуй видалити страву, якої немає у меню, двома способами:
#
# через remove()
#
# через discard()
#
# Поясни на екрані різницю (наприклад, повідомленням).
#
# Виведи оновлене меню.

menu = {"pizza", "burger", "salad"}
menu.add("bread")
menu.add("cake")
print(menu)

try:
    menu.remove("salad")
except KeyError:
    print("remove(): ПОМИЛКА! Такої страви немає у меню.")
print(menu)

menu.discard("pizza")
print(menu)
#  End of exercise 3