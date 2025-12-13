# pynative Funkc Exercise 2
# def func1(*numbers):
#     print("Printing numbers: ")
#     for number in numbers:
#         print (number)
# func1(20, 40 , 60)
#
# func1(80, 100)

# pynative Func Exercise 3
# def calculation(num1, num2):
#     return num1 + num2, num1 - num2
#
# print(calculation(40,10))

# pynative Func Exercise 4
# def showEmployee ( name, salary = 9000):
#     print(f"Name:, {name}, salary: {salary}")
#
# showEmployee("Ben", 12000)
# showEmployee("Jessa")


# pynative Func Exercise 5

# def two_numbers(a, b):
#     def sum_two_numbers (a, b):
#         return a + b
#     number1 = int(sum_two_numbers(a, b))
#     return number1 + 5
#
# print(two_numbers(4, 3))



# pynative Func Exercise 6

# Цикл
# def sum1 (numbers):
#     numbers_sum = 0
#     for number in numbers:
#         if number == 11:
#             print ("Done")
#         else:
#             numbers_sum += number
#
#     print(numbers_sum)
#
# sum1(range(11))

# Рекурсія pynative Func Exercise 6

# def addition(num):
#     if num:
#         return num + addition(num - 1)
# #     викликати ту саму функцію, зменшивши число на 1
#     else:
#         return 0
#
# print(addition(10))




# pynative Func Exercise 7 Variant 1
# def display_student(name, age):
#     print(name, age)
#
# display_student("Emma", 26)
#
# def show_student(name, age):
#     data = display_student(name, age)
#     return data

# pynative Func Exercise 7 Variant 2
# def display_student(name, age):
#     print(name, age)
#
# display_student("Emma", 26)
#
# show_student = display_student


# pynative Func Exercise 8
# def list():
#     for number in range(4, 30, 2):
#         print(number)


# pynative Func Exercise 8
# list()
#
# def list_numbers():
#     numbers = list(range(4, 30, 2))
#     print(numbers)
#
# list_numbers()

# pynative Func Exercise 9
# def largest_number(number, *numbers):
#     sorted_numbers = sorted(numbers)
#     reverse_sorted_numbers = list(reversed(sorted_numbers))
#     print(reverse_sorted_numbers[0])
#
# largest_number(4, 6, 8, 24, 12, 2)


# pynative Func Exercise 10
# def describe_pet(animal, name):
#     print(f"I have {animal} named {name}.")
#
# # Calling the function using positional arguments
# describe_pet('dog', 'Spike')
# describe_pet('cat', 'Mysja')
#
# # Calling the function using keyword arguments
# describe_pet(animal='dog', name='Spike')
# describe_pet(animal='cat', name='Mysja')

# pynative Func Exercise 11
# name="Alice", age=30
def discribe_person(**discribe):
    print("Name: ", discribe["name"], ", age: ", discribe["age"])

discribe_person(name="Alice", age=30)
# Didnot end