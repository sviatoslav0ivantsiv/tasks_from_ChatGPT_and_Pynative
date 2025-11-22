#  Start of Exercise 1
# Завдання 1: Лічильник чисел
#
# Опис:
# Користувач вводить число N.
# Твоя програма має вивести всі числа від 1 до N включно за допомогою while loop.
#
# Приклад роботи:
#
# Enter N: 5
# 1
# 2
# 3
# 4
# 5
# Done!
#
#
# Підказка:
# Використай i = 1, а потім while i <= N:.

# num = int(input("Enter a number: "))
# i = 1
# while i <= num:
#     print (i)
#     i = i + 1

# End of exercise 1


#  Start of Exercise 2
# Завдання 2: Поки користувач не введе "stop"
#
# Опис:
# Створи програму, яка питає користувача текст у циклі while.
# Цикл має зупинитися лише тоді, коли користувач введе слово stop.
#
# В кінці програму має вивести:
#
# Program stopped.
#
#
# Приклад роботи:
#
# Enter text: hi
# Enter text: hello
# Enter text: python
# Enter text: stop
# Program stopped.
#
#
# Підказка:
# Порівнюй рядок: if text == "stop":.

# word = input("Enter your word (if you enter 'stop', the program will stop):")
#
# while word != 'stop':
#     print(word)
#     word = input("Enter your word (if you enter 'stop', the program will stop):")
# else:
#     print("Program stopped")

#  End of exercise 2





#  Start of Exercise 3
# Завдання
# 3: Підрахунок суми списку вручну
#
# Опис: Є список чисел:
# numbers = [3, 7, 2, 9, 4]
#
# Потрібно за допомогою while обчислити суму всіх елементів списку. Не використовуй sum().
#
# Очікуваний результат:
#
# The
# total
# sum is 25
#
# Підказка:
# Використай:
#
# індекс
# i = 0
#
# while i < len(numbers):
#
# змінну
# total = 0

numbers = [3, 7, 2, 9, 4]

i = 0
total = 0

while i < len(numbers):
    total += numbers[i]
    i += 1

print("Total:", total)

# End of exercise 3