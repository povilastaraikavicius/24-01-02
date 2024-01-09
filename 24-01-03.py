# def get_string_lenght(strin_to_check: str) -> int:
#     return -len(strin_to_check)


# animals = ["ferret", "vole", "dog", "gecko"]
# print(sorted(animals, key=get_string_lenght))
# # ['dog', 'ferret', 'gecko', 'vole']


# from typing import Callable


# def add_two_number(first_num: int, second_num: int) -> int:
#     return first_num + second_num


# def add_another_two_nums(number: int, number_func: Callable):
#     return number_func(2, number)


# print(add_another_two_nums(number=4, number_func=add_two_number))


# reverse = lambda s: s[::-1]
# print(reverse("I am a string"))
# # 'gnirts a ma I'


# task1
# Write a Python program to find if a given string starts with a given character using Lambda. Output:True or False
#  Parašykite Python programą, kad sužinotumėte, ar tam tikra eilutė prasideda tam tikru simboliu, naudodami Lambda.
# Išvestis:teisinga arba klaidinga


# text = "Python is hard to learn."

# result = text.startswith("is hard")

# print(result)

# result = text.startswith("Python is ")

# print(result)

# result = text.startswith("Python is hard to learn.")

# print(result)


# Alberto pvz


# my_string = "troleibusas"
# my_char = "T"

# check_first_char = (
#     lambda given_string, given_character: True
#     if given_string[0] == given_character
#     else False
# )

# print(check_first_char(my_string, my_char))


# task2
# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
# also create a lambda function that multiplies argument x with argument y and print the result.


# from typing import Callable


# increase_by_fifteen: Callable[[int], int] = lambda number: number + 15
# multiply: Callable[[int], int] = lambda x, y: x * y
# result = increase_by_fifteen(10)
# result1 = multiply(5, 6)
# print(result)
# print(result1)


# sauliaus pvz:

# from typing import Callable


# increase_by_fifteen: Callable[[int], int] = lambda x: x + 15

# multtiply: Callable[[float, float], float] = lambda x, y: x * y

# print(increase_by_fifteen(20))
# print(multtiply(5.0, 3.0))


# task3
# Write a Python program to square and cube every number in a given list of integers using Lambda

# from typing import Callable

# l = [1, 2, 3, 4]

# square: Callable[[int], int] = lambda x: x**2
# cube: Callable[[float], float] = lambda x: x**3

# print([square(i) for i in l])
# print([cube(i) for i in l])


# l = [1, 2, 3, 4]
# x = [i**2 for i in l]

# print(x)


# task4
# Write a Python program to extract year, month, date and time using Lambda. Sample Output:
# 2020-01-15 09:03:32.744178
# 2020
# 1
# 15
# 09:03:32.744178

# import datetime
# now = datetime.datetime.now()

# print(now)

# year = lambda x: x.year

# month = lambda x: x.month

# day = lambda x: x.day

# t = lambda x: x.time()

# print(year(now))
# print(month(now))
# print(day(now))
# print(t(now))

# alberto PVZ

# from datetime import datetime

# my_date = datetime.now()

# get_formatted_data = (lambda my_date: f"{my_date.year}\n{my_date.month}\n{my_date.day}\n{my_date.time()}\n")

# print(get_formatted_data(my_date=my_date))


# sauliaus PvZ

# import datetime

# current_time = datetime.datetime.now()

# extract_time_in_diferent_formats = lambda current_time: (
#     current_time.year,
#     current_time.month,
#     current_time.day,
#     current_time.time(),
# )

# result = extract_time_in_diferent_formats(current_time)

# for item in result:
#     print(item)
