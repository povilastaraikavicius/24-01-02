# def reverse(s):
#     return s[::-1]


# print(reverse("I am a string"))


# animals = ["cat", "dog", "hedgehog", "gecko"]


# def reverse(s):
#     return s[::-1]


# iterator = map(reverse, animals)
# for i in iterator:
#     print(i)
# # tac
# # god
# # gohegdeh
# # okceg

# iterator = map(reverse, animals)
# print(list(iterator))


# animals = ["cat", "dog", "hedgehog", "gecko"]
# iterator = map(lambda s: s[::-1], animals)
# print(list(iterator))
# ['tac', 'god', 'gohegdeh', 'okceg']
# ------------------------------------------------------------------------------------------------------------------

# task5
# Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# # Sorted the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]


# original_list = [
#     ("English", 88),
#     ("Science", 90),
#     ("Maths", 97),
#     ("Social sciences", 82),
# ]

# sorted_list = sorted(original_list, key=lambda x: x[1])

# print(original_list)

# print(sorted_list)
# ----------------------------------------------------------------------------------------------------------------------------------------
# task6
# Write a Python program to sort a list of dictionaries buy color value using Lambda.
# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color':
# 'Blue'}]

# # Sorted the List of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color':
# 'Gold'}]

# original_list = [
#     {"make": "Nokia", "model": 216, "color": "Black"},
#     {"make": "Mi Max", "model": "2", "color": "Gold"},
#     {"make": "Samsung", "model": 7, "color": "Blue"},
# ]

# sorted_list = sorted(original_list, key=lambda x: x["color"])

# print(original_list)

# print(sorted_list)
# --------------------------------------------------------------------------------------------------------------

# task 7
# Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda.

# # Original Matrix:
# `[[1, 2, 3], [2, 4, 5], [1, 1, 1]]`

# # Sort the said matrix in ascending order according to the sum of its rows
# `[[1, 1, 1], [1, 2, 3], [2, 4, 5]]`

# # Original Matrix:
# `[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]`

# # Sort the said matrix in ascending order according to the sum of its rows
# `[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]`

# original_matrix = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]

# sorted_matrix = sorted(original_matrix, key=lambda x: sum(x))

# print(sorted_matrix)


# original_matrix = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# sorted_matrix1 = sorted(original_matrix, key=lambda x: sum(x))
# print(sorted_matrix1)

# ------------------------------------------------------------------------------------------------------------------


# 1.Write a Python program to triple all numbers of a given list of integers. Use Python map

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# iterator = map(lambda x: x * 3, my_list)

# # print(list(iterator))
# -----------------------------------------------------------------------------------------------------

# 2.Write a Python program to square the elements of a list using map() function.

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# iterator = map(lambda x: pow(x, 2), my_list)

# print(list(iterator))
# ----------------------------------------------------------------------------------------------------

# 3.Write a Python program to add three given lists using Python map and lambda

# def f(a, b, c):
#     return a + b + c

# print(list(map(f, [1, 2, 3], [4, 5, 6], [7, 8, 9])))

# ------------------------------------------------------------------------------------------------

# 5.Write a Python program to convert a given list of integers and a tuple of integers in a list of strings


# list_int = [1, 12, 15, 21, 131]
# list_string = map(str, list_int)
# print(list(list_string))


# integer_tuple = (6, 7, 8, 9, 10)
# integer_tuple = map(str, integer_tuple)
# print(list(integer_tuple))

# -------------------------------------------------------------------------------------------------------


# 6.Write a Python program to filter a list of integers using Lambda

# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Even numbers from the said list:
# [2, 4, 6, 8, 10]

# Odd numbers from the said list:
# [1, 3, 5, 7, 9]

# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(list(filter(lambda x: x % 2 == 0, number)))
# print(list(filter(lambda x: x % 2 != 0, number)))

# ---------------------------------------------------------------------------------------------------


