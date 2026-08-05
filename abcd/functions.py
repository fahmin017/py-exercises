# def my_function():
#     print("testing how it works 🥱🥱")
# my_function()
# print("   ") 

# #************************************************************************************************************************

# # Temperature convertion Fahrenheit to Celsius

# def convertion(temp):
#     return (temp-32)*5/9

# n=int(input("how many convertions:"))
# for i in range(n):
#     temp1 = float(input("what is the feren_height temp :"))
#     temp2 = convertion(temp1)
#     print(f"celcius degree of farenheit {temp1} is :",temp2," ♨️♨️")
# print(" ")

#************************************************************************************************************************

# def greetings():
#     return " hello mwone 😁😁"
# msg = greetings()
# print(msg)

#************************************************************************************************************************

# def greetings(name):
#     print(name,"ee happy alle mwone 🙌🙌")

# greetings("yamal")
# greetings("rono")

#************************************************************************************************************************

# def greetings(name,job):
#     print(name,"is",job)

# greetings("yamal","unemployed")

#************************************************************************************************************************

# You can assign default values to parameters. If the function is called without an argument, it uses the default value:

# def greetings(country ="india 🥷"):
#     print("im from  🙌🙌",country)

# greetings("brazil")
# greetings()

#************************************************************************************************************************

# def my_function(animal, name):
#   print("I have a", animal)
#   print("My", animal + "'s name is", name)

# my_function(animal = "dog", name = "kutha 🐶")

#************************************************************************************************************************
# def my_function(animal,name):
#     print("i have a ",animal)
#     print("its name is",name)

# my_function("dog","billy")
#************************************************************************************************************************

# def my_function(x):
#     for i in x:
#         print(i)
# x=[1,2,3,4]
# my_function(x)

#************************************************************************************************************************

# Sending a dictionary as an argument:

# def my_function(persons):
#     print("name is :",persons["name"])
#     print("age :",persons["age"])
# d ={"name":"fahmin","age":22,"place":"kinalur"}
# my_function(d)

#************************************************************************************************************************

# def my_functions(x,y):
#     return x+y

# a=int(input("enetr the number"))
# b=int(input("enter thr number"))
# result = my_functions(a,b)
# print(result)

# #************************************************************************************************************************
# def my_function(name, /):
#   print("Hello", name)

# my_function("Emil")
# #************************************************************************************************************************
# def my_function(*, name):
#   print("Hello", name)

# my_function(name = "Emil")

# #************************************************************************************************************************
# def my_function(player):
#     print("The new barca player is :",player[1])

# player=("yamal","pedri","gavi")
# my_function(player)

#************************************************************************************************************************

# Arbitrary Arguments - *args
# If you do not know how many arguments will be passed into your function, add a * before the parameter name.
# This way, the function will receive a tuple of arguments and can access the items accordingly:

# def my_function(*player):
#     print("The new barca player is :",player[2])
# my_function("yamal","pedri","gavi")

# #************************************************************************************************************************
# def my_function(*player):
#     print("type:",type(player))
#     print("The new barca player is :",player[2])
#     print("The old barca player is :",player[0])
#     print("The young barca player is :",player[1])
# my_function("yamal","pedri","gavi")

# #************************************************************************************************************************

# def my_function(greeting,*players):
#     for i in players:
#         print(greeting,players)
# my_function("hello","yamal","messi","rono")
# #************************************************************************************************************************
# def my_function(greeting,*players):
#     for i in players:
#         print(greeting,i)
# my_function("hello","yamal","messi","rono")

#************************************************************************************************************************

# def my_function(*num):
#     total = 0
#     for i in num:
#         total=total+i
#     print("total sum =",total)

# my_function(2,3)
# my_function(2,3,58,41,21,)
# my_function(2,8,9,3)

#************************************************************************************************************************

#*************REVERSING A STRING********************

# def my_function(x):
#     rev = x[::-1]
#     print("reversed srting =",rev)

# a=input("enter a string :")
# my_function(a)

#************************************************************************************************************************

#***************** PALINDROME***********************
# def my_function(x):
#     rev =x[::-1]
#     if x==rev:
#         print("it is a palindrome")
#     else:
#         print("not a palindrome")

# a=input("enter a string :")
# my_function(a)

#************************************************************************************************************************

# def my_function(x,y):
#    return x+y

# a=int(input("enter the first number"))
# b=int(input("enter the second number"))

# sum=my_function(a,b)
# print(sum)
    
#************************************************************************************************************************
# def my_function(x,y):
#     print("swapped number a",y)
#     print("swapped number a",x)

# a=int(input("enter the number a :"))
# b=int(input("enter the number b :"))
# my_function(a,b)
#************************************************************************************************************************


# def my_function(x,y):
#     m = x 
#     n = y
#     print("value of a =",n) 
#     print("value of b =",m)
  

# a=int(input("enter the number a :"))
# b=int(input("enter the number b :"))
# my_function(a,b)

#************************************************************************************************************************

# n=int(input("how many no you want to add : "))
# b=list()
# for i in range(n):
    
#     a=int(input("enter the number : "))
#     b.append(a)
#     s = sum(b)
# print("sum is",s)

#************************************************************************************************************************

# def my_function(x,y):
#     return x+y

# a=list(input("enter the list"))
# b=list(input("enter the list"))
# result = my_function(a,b)
# print("merged list =",result)

#************************************************************************************************************************
# def my_function(x,y):
#     if x==y:
#         print("it is a anagram")
#     else:
#         print("not a anagram")

# a=input("enter the first string :")
# b=input("enter the second string :")

# c=a.lower()
# d=b.lower()

# g=''.join(sorted(c))
# h=''.join(sorted(d))

# my_function(g,h)

# #************************************************************************************************************************

# Exercise 2. Variable Length of Arguments (*args)
# Practice Problem: Create a function func1() such that it can accept a variable number of arguments and print all of them.
# Whether you pass two numbers or five, the function should handle them all without error.

# def my_function(*num):
#     print("the numbers are :",num)

# my_function(10,20,30)
# my_function(20,74)
# my_function(58)

#************************************************************************************************************************

# Exercise 3. Return Multiple Values from a Function
# Practice Problem: Write a function calculation() that accepts two variables and calculates both addition and subtraction.
# The function must return both results in a single return statement.

# def calculation(x,y):
#     n=x+y
#     m=x-y
#     return n,m
# a = int(input("enter the number :"))
# b = int(input("enter the number :"))
# result = calculation(a,b)
# print(result)

#************************************************************************************************************************

# Exercise 4. Function with Default Argument
# Practice Problem: Create a function show_employee() that accepts an employee’s name and salary. 
# If the salary is not provided in the function call, the function should automatically assign a default value of 9000.

# def show_employee(name,salary=9000):
#     print(name,salary)

# show_employee(name="finu",salary=8500)
# show_employee(name="ron")

#************************************************************************************************************************

# Exercise 5. Create an Inner Function
# Practice Problem: Create an outer function that accepts two parameters, a and b.
# Inside, create an inner function that calculates the addition of a and b. 
# The outer function should then add 5 to that sum and return the final result.


#************************************************************************************************************************
