# Lambda Functions
# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# a = int(input("enter the no : "))
# x=lambda b:b+10     #ADDING 10 TO THE GIVEN INPUT
# print(x(a))

#******************************************************************************************************************************

# a = int(input("enter the no : "))
# c= int(input("enter the 2 no : "))
# x=lambda n,m:n*m     #ADDING 10 TO THE GIVEN INPUT
# print(x(a,c))

#******************************************************************************************************************************

# function definition to make a function that always doubles the number you send in:

# def my_function(n):
#     return lambda a: a * n

# double = my_function(2)

# print(double(10))

#******************************************************************************************************************************

# function definition to make a function that always triple the number you send in:

# def my_function(n):
#     return lambda a: a * n

# double = my_function(3)

# print(double(10))

#******************************************************************************************************************************

# Lambda with Built-in Functions
# Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().

# Using Lambda with map()

# Double all numbers in a list:

# a=[1,5,7,1,6]
# b=list(map(lambda a:a*2,a))
# print("doubled list =",b)


#******************************************************************************************************************************

# Using Lambda with filter()
# The filter() function creates a list of items for which a function returns True:

# Filter out odd and even numbers from a list:

# n=[4,5,7,1,6,9,2]
# odd = list(filter(lambda a:a % 2!=0,n))
# even = list(filter(lambda x:x % 2==0,n))

# print("odd numbers are :",odd)
# print("odd numbers are :",even)

#******************************************************************************************************************************

# Using Lambda with sorted()
# The sorted() function can use a lambda as a key for custom sorting:

# Example
# Sort a list of tuples by the second element:

# t=[("finu",25),("sanu",20),("aaro",17)]
# sort = sorted(t,key=lambda a:a[0])
# print(sort)

#******************************************************************************************************************************

# t=[("finu",25,33),("sanu",20,90),("aaro",17,123)]
# sort = sorted(t,key=lambda a:a[2])
# print(sort)

#******************************************************************************************************************************

# l=["messi","rono","yamal","neyney"]
# sort = sorted(l,key=lambda a:len(a))
# print(sort)

#******************************************************************************************************************************
#  # LARGEST OF 2 NO
# a=int(input("enter the number"))
# b=int(input("enter the number"))
# larger = lambda x,m:x if x>m else m
# print(larger(a,b))

#******************************************************************************************************************************

# Write a lambda function that returns the addition of two numbers.

# a=int(input("enter the 1 number"))
# b=int(input("enter the 2 number"))
# multiply = lambda x,m:x+m
# print(multiply(a,b))

#******************************************************************************************************************************

# a=[]
# s = sum(filter(lambda x:x%2==0,a))
# print(s)

#******************************************************************************************************************************