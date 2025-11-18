#  Start of Exercise 1
# Завдання 1: Книга контактів
#
# Створи словник contacts, де ключ — ім’я людини, а значення — інший словник з інформацією:
#
# телефон
#
# email
#
# Приклад структури (на твій розсуд):
#
# contacts = {
#     "Ivan": {"phone": "123456", "email": "ivan@example.com"},
#     ...
# }
#
# Твоє завдання:
#
# Вивести всі імена (ключі).
#
# Для кожної людини вивести її телефон та email у форматі:
#
# Ivan - phone: 123456, email: ivan@example.com

# contacts = {
#     "Ivan": {
#         "phone": "123456",
#         "email": "ivan@example.com",
#     },
#     "Ola": {
#         "phone": "654321",
#         "email": "ola@example.com",
#     }
# }
#
# print ( contacts.keys() )
# print (f"Ivan - {contacts['Ivan']['phone']}, {contacts['Ivan']['email']} \nOla - {contacts['Ola']['phone']}, {contacts['Ola']['email']}")
# End of exercise 1


#  Start of Exercise 2
# Завдання 2: Магазин і ціни
#
# Створи словник store, де:
#
# ключ — назва товару
#
# значення — його ціна (число)
#
# Наприклад:
#
# store = {
#     "apple": 20,
#     "banana": 25,
#     "milk": 35
# }
#
# Твоє завдання:
#
# Додай новий товар у словник.
#
# Зміни ціну існуючого товару.
#
# Видали один товар.
#
# Виведи всі товари та їхні ціни у форматі:
#
# apple: 20 грн
# banana: 25 грн
# milk: 35 грн

#  End of exercise 2

# store = {
#     "apple": 20,
#     "banana": 25,
#     "milk": 35
# }
# store["egs"] = 15
# store["apple"] = 10
# store.pop("milk")
#
# print(store.items())
# print(type(store))

#  Start of Exercise 3
# Завдання 3: Статистика учнів
#
# Створи словник students, де:
#
# ключ — ім’я студента
#
# значення — його оцінка (число від 1 до 12)
#
# Наприклад:
#
# students = {
#     "Olena": 11,
#     "Maksym": 9,
#     "Sofia": 12
# }
#
# Твоє завдання:
#
# Знайти і вивести середнє значення оцінок.
#
# Вивести всіх учнів, які мають оцінку 10 і більше.
#
# Вивести учня з найвищою оцінкою (ім’я + оцінка).

students = {
    "Olena": 11,
    "Maksym": 9,
    "Sofia": 12
}

averageGrades = sum(students.values()) / len(students)
print("Average grade:", averageGrades)

print("Students who have a grades of 10 or higher : ")

for keys, value in students.items():
    if value >= 10:
        print(keys)

print ("   ")

max_value = max(students.values())
for keys, value in students.items():
    if value == max_value:
        print("Best student:\n", keys)

# End of exercise 3