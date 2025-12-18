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
# def discribe_person(**discribe):
#     if discribe:
#         print ("\n--- Information ---")
#         for key, value in discribe.items():
#             print(f"{key}: {value}")
#     else:
#             print ("\nNo information provided.")
#
# discribe_person(name="alisa", age=25, hair_color="blond")
# discribe_person(job="enginer", hobby="running")
#
# discribe_person()


# pynative Func Exercise 12

# global_var = 10
#
# def new_global_var(number):
#     global global_var
#     global_var = number
#     print("Inside function:", global_var)
#
#
# new_global_var(15)
#
# print("Outside function:", global_var)


# pynative Func Exercise 13: Write a recursive function to calculate the factorial

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(3))


# pynative Func Exercise 14: Create a lambda function that squares a given number

# def square(number):
#
#     result = lambda number: number * number
#     print(result(number))
#
#
# square(3)

# pynative Func Exercise 15: Use a lambda with the filter() function to get all even numbers from a list

# def even_number(numbers):
#     even_numbers_list = []
#     for number in numbers:
#         if number % 2 == 0:
#             even_numbers_list.append(number)
#     return even_numbers_list
#
# print("the even number list are: ", even_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
#
# print(even_numbers)


# pynative Func Exercise 16: Use a lambda with the map() function to double each element in a list

# numbers = [1, 2, 3, 4, 5]
# double_numbers = list(map(lambda number: number *2, numbers))
# print(double_numbers)

# pynative Func Exercise 17: Use a lambda with the sorted() function to sort a list of tuples based on the second element

# data = [('apple', 5), ('banana', 2), ('cherry', 8), ('date', 1)]
# sorted_data = sorted(data, key=lambda item: item[1])
# print(sorted_data)


# pynative Func Exercise 18: Create Higher-Order Function

def apply_operation(func, x, y):
    return func(x, y)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

result_add = apply_operation(add, 2, 4)
print("result of add:", result_add)

result_subtract = apply_operation(subtract, 2, 4)
print(result_subtract)

result_multiply = apply_operation(multiply, 2, 4)
print(result_multiply)

result_divide = apply_operation(divide, 2, 4)
print(result_divide)