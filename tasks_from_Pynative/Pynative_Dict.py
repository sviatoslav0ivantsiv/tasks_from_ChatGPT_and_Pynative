# pynative Dict Exercise 1
from os import write

# my_dict = {
#     'name': 'Alice',
#     'age': 35,
#     'city': 'New York'
# }
#
# my_dict["profession"]="Doctor"
# my_dict.update({"profession":"Doctor"})
#
# my_dict["age"] = 40
#
# print(my_dict)
# print(f" City : {my_dict['city']}")


# pynative Dict Exercise 2
# my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
#
# my_dict.pop("profession")
# print(f" Del profession, {my_dict}")
#
# for key, value in my_dict.items():
#     print(key, ":", value)
#
# if "profession" in my_dict:
#     print(True)
# else:
#     print(False)

# pynative Dict Exercise 3

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# # Variant 1
# # numbers_dict = {}
# #
# # for index in range(len(keys)):
# #     numbers_dict.update({keys[index] : values[index]})
# #
# # print(numbers_dict)
#
# # variant 2
#
# numbers_dict = dict(zip(keys, values))
# print(numbers_dict)

# pynative Dict Exercise 4
# my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
#
# my_dict.clear()
#
# print(my_dict)

# pynative Dict Exercise 5
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# #
# # # variant 1
# # marged_dict = dict1.copy()
# # marged_dict.update(dict2)
# #
# # print(marged_dict)
#
# # variant 2
# marged_dict = dict1 | dict2
# print(marged_dict)

# pynative Dict Exercise 6
# variant 1
# string1 = 'Jessa'
# letters_dict = {}
# for letter in string1:
#     letters_dict[letter] = letters_dict.get(letter, 0) + 1
#
# print(letters_dict)
#
# # Variant 2
# from collections import Counter
#
# cnt = Counter(string1)
# print(cnt)

# pynative Dict Exercise 7
data = {'person': {'name': 'Alice', 'age': 30}}
print(f" {data.get("person",{}).get("name")}'s age is  {data.get("person",{}).get("age")} ")

# print(f" da")