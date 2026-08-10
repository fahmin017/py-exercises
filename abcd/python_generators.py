# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# for i in my_generator():
#     print(i)

#*******************************************************************************************************************************
# Generator that yields numbers:

# def count_num(n):
#     count = 1
#     while count<=n:
#         yield count
#         count = count+1

# for i in count_num(7):
#     print(i)

#*******************************************************************************************************************************
# # mem sav
# def large_sequence(n):
#   for i in range(n):
#     yield i

# # This doesn't create a million numbers in memory
# gen = large_sequence(1000000)
# print(next(gen))
# print(next(gen))
# print(next(gen))

#*******************************************************************************************************************************

# def names():
#   yield "hello"
#   yield "my"
#   yield "boy"

# gen = names()
# print(next(gen))
# print(next(gen))
# print(next(gen))
  
#*******************************************************************************************************************************

# Generator Expressions
# Similar to list comprehensions, you can create generators using generator expressions with parentheses instead of square brackets:

# Example
# List comprehension vs generator expression:

# list_comp = [x*x for x in range(5)]
# print(list_comp)

# gen_exp = (x*x for x in range(8))
# print(gen_exp)
# print(list(gen_exp))
#*******************************************************************************************************************************

# Using a generator expression with sum:
# Calculate sum without creating a list

# total = sum (x+1 for x in range(6))
# print("Total =",total)

#*******************************************************************************************************************************

# Calculate sum without creating a list

# total = sum(x*x for x in range(7))
# print("sum of squares  =",total)

#*******************************************************************************************************************************
# Fibonacci seq in generators

# def fibonacci():
#     a=0
#     b=1
#     while True:
#         yield a
#         a,b = b,a+b

# gen = fibonacci()
# for i in range(10):
#     print(next(gen))

#*******************************************************************************************************************************

# Generator Methods
# Generators have special methods for advanced control:

# send() Method
# The send() method allows you to send a value to the generator:

# def send_generator():
#     while True:
#         rec = yield
#         print("sended =",rec)

# gen = send_generator()
# next(gen)
# gen.send("hello")
# gen.send("entha mwone 🤦‍♂️🤦‍♂️")

#*******************************************************************************************************************************

# def my_generator():
#     try:
#         yield 1
#         yield 2
#         yield 3

#     finally:
#         print("it ends here and now..🔫🔫")

# gen = my_generator()
# print(next(gen))
# print(next(gen))
# gen.close()

#*******************************************************************************************************************************
# squares = (num *num for num in range(10))

# for square in squares:
#     print(square)

#     if square > 10:
#          squares.close()

#*******************************************************************************************************************************

# Cubes Generator

# Write a Python program that creates a generator function that yields cubes of numbers from 1 to n. Accept n from the user.

# def cube_generator(n):
#     for i in range(1,n+1):
#         yield i**3

# n=int(input("enter the number:"))
# gen = cube_generator(n)

# print(f"cubes of numbers 1 to {n}")

# for j in gen:
#     print(j)

#*******************************************************************************************************************************

# Write a Python program that creates a generator function that generates all prime numbers between two given numbers.

# def prime_check(s,e):
#     for i in range(s,e+1):
#         if i<2:
#             continue

#         is_prime = True
#         for j in range(2,i):
#             if i%j==0:
#                 is_prime = False
#                 break
#         if is_prime:
#             yield i

# s=int(input("enter the first number"))
# e=int(input("enter the first number"))

# for n in prime_check(s,e):
#     print(n)

#*******************************************************************************************************************************

# Write a Python program that creates a generator function that generates product of all even numbers between two given numbers.

# def product_even(s,e):
#     product =1
#     for i in range(s,e+1):
#         if i%2==0:
#             product = product*i
#             yield product

# s=int(input("enter the first number"))
# e=int(input("enter the first number"))

# for n in product_even(s,e):
#     print(n)

#*******************************************************************************************************************************

# Write a Python program that creates a generator function that generates product of all odd numbers between two given numbers.

# def odd_product(s,e):
#     product = 1
#     for i in range(s,e+1):
#         if i%2!=0:
#             product = product*i
#             yield product

# s=int(input("first no: "))
# e=int(input("first no: "))

# for n in odd_product(s,e):
#     print(n)

#*******************************************************************************************************************************

# Write a Python program that creates a generator function that generates product of all factors of a given number

# def factors(n):
#     for i in range(1,n+1):
#         if n%i==0:
#             yield i

# n=int(input("enter the nuber"))
# gen=factors(n)
# print(f"factors of {n} is :")
# for j in gen:
#     print(j)

#*******************************************************************************************************************************

# Write a Python program to create a generator function that generates the powers of a number up to a specified exponent

# def power(b,e):
#     result =1
#     for i in range(e+1):
#         yield result
#         result = result*b
# b=int(input("enter the base number :"))
# e=int(input("enter how many exponent u want :"))

# gen=power(b,e)
# print(f"power of {b} to the exponent {e} is :")
# for j in gen:
#     print(j)


#*******************************************************************************************************************************
