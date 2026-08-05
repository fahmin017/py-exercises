# def classroom(x):
#     def student():
#         x()
#         return "class have 30 std"
#     return student
# @classroom
# def my_function():
#     print(" I am in this class ") 
# my_function()

#****************************************************************************************************************************

# def change_case(func):
#     def inner():
#         return func().upper()
#     return inner

# @change_case
# def my_function():
#     return "hello mwone 😁😁"
# print(my_function())

#****************************************************************************************************************************

# def change_case(func):
#     def inner():
#         return func().upper()
#     return inner

# @change_case
# def my_function():
#     return "hello mwone 😁😁"

# @change_case
# def function():
#     return " entha meone 🥱🥱"

# print(my_function())
# print(function())


#****************************************************************************************************************************
# def change_case(func):
    
#     def inner(x):
        
#         return func(x).upper()
#     return inner

# @change_case
# def my_function(name):
#     return "hello mwone 😁😁"+ name
# print(my_function("fahmin"))

#****************************************************************************************************************************

# Decorator With Arguments
# Decorators can accept their own arguments by adding another wrapper level.

# def change_case(n):
#     def change_case(func):
#         def my_inner():
#             if n%2==0:
#                 a=func().upper()
#             else:
#                 a=func().lower()
#             return a
#         return my_inner
#     return change_case

# @change_case(2)
# def my_function():
#     return " suGalle 😁😁"
# print(my_function())

#****************************************************************************************************************************


