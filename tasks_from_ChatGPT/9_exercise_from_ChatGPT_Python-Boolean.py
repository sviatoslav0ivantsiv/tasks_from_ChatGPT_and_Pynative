# Start of Exercise 1

# Завдання 1: Перевірка віку користувача
#
# Опис:
# Напиши програму, яка запитує у користувача його вік і перевіряє, чи є він повнолітнім (18 років і більше).
# Використай булеві змінні для збереження результату перевірки

# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are adult")
# else:
#     print("You are not 18 yars old")

# Variant 2
# age = int(input("Enter your age: "))
# is_adult = age >= 18
# print ("Adult:", is_adult )

# End of exercise 1


# Start of Exercise 2

# Створи просту перевірку входу.
# У тебе є правильне ім’я користувача "admin" і пароль "1234".
# Запитай у користувача його ім’я та пароль, і за допомогою булевих значень визнач,
# чи можна йому увійти.

# username = input(" Enter your username: ")
# password = input("Enter your password: ")
#
# is_username_correct = username == "admin"
# is_password_correct = password == "1234"
#
# can_login = is_password_correct and is_username_correct
# # print("Access is allowed:", can_login)
# if can_login:
#     print("Access is allowed")
# else:
#     print("Access is denied, check your username and password")

# End of exercise 2


# Start of Exercise 3

# Завдання 3: Число парне чи непарне
#
# Опис:
# Запитай у користувача число і визнач, чи є воно парним.
# Використай оператор % і булеву змінну для збереження результату.
#

number = int(input("Enter a number: "))

if number % 2 == 0:
    print ("The number is even")
else:
    print ("The number is odd")

# End of exercise 2