#  Start of Exercise 1
# Завдання 1: Перевірка віку для доступу
#
# Опис:
# Користувач вводить свій вік.
# Ти маєш визначити:
#
# якщо вік <=0 → вивести: "Invalid age"
#
# якщо вік < 18 → "Access denied"
#
# якщо вік ≥ 18 → "Access granted"
#
# Підказка: використай input() та умовні оператори.


# age = int(input("Enter your age:"))
#
# if age <= 0:
#     print ("Invalid age")
# elif age < 18:
#     print ("Access denied")
# else:
#     print ("Access granted")

# End of exercise 1


#  Start of Exercise 2
# Завдання 2: Магазин знижок
#
# Є ціна товару та статус клієнта:
#
# price = 1200
# status = "vip"   # може бути "vip", "regular" або "new"
#
#
# Правила:
#
# якщо статус "vip" → знижка 20%
#
# якщо "regular" → знижка 10%
#
# якщо "new" → без знижки
#
# Завдання:
# Обчисли фінальну ціну товару та виведи:
#
# Final price: X

# price = 1200
#
# status = input("Enter your status: ")
#
# if status == "vip":
#     print ( "Final price:", price*0.8 )
# elif status == "regular":
#     print ( "Final price:", price*0.9 )
# else:
#     print( "Final price:", price )

#  End of exercise 2

#  Start of Exercise 3
# Завдання 3: Оцінка студента
#
# Є словник з оцінкою:
#
# student = {
#     "name": "Oleh",
#     "grade": 73
# }
#
#
# Напиши програму, яка:
#
# якщо оцінка ≥ 90 → "Excellent"
#
# якщо 75–89 → "Good"
#
# якщо 60–74 → "Satisfactory"
#
# якщо < 60 → "Fail"
#
# Виведи:
#
# Student Oleh: Good

student = {
        "name": "Oleh",
        "grade": 73
}
student["grade"] = 55

if student["grade"] >= 90 :
    print( "Student Oleh: Excellent")
elif student["grade"] >= 75 and student["grade"] <= 89 :
    print( "Student Oleh: Good")
elif student["grade"] >= 60 and student["grade"] <= 74:
    print("Student Oleh: Satisfactory")
elif student["grade"] < 60:
    print( "Student Oleh: Fail")

# score = int(input("Enter your score: "))
# End of exercise 3