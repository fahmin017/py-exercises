# Write a single-line list comprehension that takes a list of strings, 
# filters out strings shorter than 4 characters, and converts the remaining strings to uppercase.

# l=["apple","banana","kiwi","anar","strawberry"]
# a= [i.upper() for i in l if len(i)>4]
# print(a)

#********************************************************************************************************************************

# Write a function that merges two dictionaries. If a key exists in both dictionaries, sum their values.
# If a key exists in only one, include it as is.

# def merging_dict(d1,d2):
#     result = d1.copy()

#     for key, value in d2.items():
#         result[key] = result.get(key,0)+value

#     return result
# dict1={"finu":243,"sanu":452}
# dict2={"sanu":321,"aaro":213}

# merged_dict = merging_dict(dict1,dict2)
# print("merged dictionary is :",merged_dict)
    
#********************************************************************************************************************************

# Given a sentence, reverse each individual word within the string while maintaining the original word order.

# def reverse(a):
#     b=a.split()
#     rev = [w[::-1]for w in b]
#     return " ".join(rev)

# n=input("enter a string :")
# m=reverse(n)
# print("reversed string :",m)

#********************************************************************************************************************************

# write a function to check if a full sentence is a palindrome. You must ignore case, spaces, and all punctuation marks.

# def palindrome(s):
#     sentance = [x.lower()for x in s if x.isalnum()]
#     clean_str = " ".join(sentance)
#     return clean_str == clean_str[::-1]

# text = "a man,a plan,a canal:panama"
# print("is palindrome?",palindrome(text))

#********************************************************************************************************************************

# Given a list of strings, use a single list comprehension to extract strings that meet two criteria: 
# they must be longer than 5 characters AND they must start with a vowel (a, e, i, o, u).

# l=["apple","education","ice","ocean","python","umbrella"]
# a=[i for i in l if len(i)>5 and i[0].lower() in 'a''e''i''o''u']
# print(a)

#********************************************************************************************************************************

# 1. Grade Calculator
# Write a program that accepts a student's marks (0-100). Using if-elif-else, display grade A (90-100),
# B (80-89), C (70-79), D (60-69), or F (below 60). Display 'Invalid Marks' for values outside 0-100.

# marks = int(input("enter the mark :"))

# if(marks<0 or marks>100):
#     print("invalid input")

# elif(marks>=90):
#     print(" your grade is : A")

# elif(marks >=80):
#     print(" your grade is : B")

# elif(marks >=70):
#     print(" your grade is : C")

# elif(marks >=60):
#     print(" your grade is : D")

# else:
#     print(" your grade : F")

#********************************************************************************************************************************

# 2. Electricity Bill
# Input units consumed. First 100 units cost ■5/unit, next 100 cost ■7/unit and remaining cost
# ■10/unit. Print the final bill.


# a=int(input("enter the units of electricity consumed :"))

# if(a<0):
#     print("invalid")
# elif(a>=0 or a<=100):
#     b=a*5
#     print("electricity bill : ",b)

# elif(a>100 or a<=200):
#     c=a*7
#     print("electricity bill : ",c)

# elif(a>200):
#     d=a*10
#     print("electricity bill : ",d)

# else:
#     print("invalid input")

#********************************************************************************************************************************
# 3. Leap Year
# Input a year and determine whether it is a leap year.

# a=int(input("enter the year :"))
# if(a%4==0 and a%100!=0 or a%400==0):
#     print("it is a leap year")
# else:
#     print("not a leap year")

#********************************************************************************************************************************

# a=int(input("enter the first side length : "))
# b=int(input("enter the second side length : "))
# c=int(input("enter the third side length : "))

# if(a==b==c):
#     print("triangle is equilateral")

# elif(a==b and b!=c):
#     print(" triangle is isocelus")

# elif(c==a and a!=b):
#     print(" triangle is isocelus")

# elif(b==c and c!=a):
#     print(" triangle is isocelus")

# else:
#     print("triangle is scalene")

#********************************************************************************************************************************

# 5. ATM Simulation
# Balance starts at ■10000. Menu: Deposit, Withdraw, Check Balance, Exit. Prevent over-withdrawal.
# def atm_simulation():
#     bal=10000
    
#     while(True):
#         print(" 1. DEPOSIT \n 2.WITHDRAW \n 3.CHECK BALANCE \n 4.EXIT")
#         n=int(input("enter your cohice : "))

#         if(n==1):
#             a=int(input("enter the amount you want to deposit :"))
#             bal=bal+a
#             print("Deposited sucessfully \nYour current balance is :",bal)

#         elif(n==2):
#             d=int(input("enter the amount you want to withdraw :"))
#             bal=bal-d
#             print("withraw sucessfull \nYour current balance is :",bal)

#         elif(n==3):
#             print("Your current balance is :",bal)

#         elif(n==4):
#             print("Exiting :")

#             break 

#         else:
#             print("invalid")

# atm_simulation()

#********************************************************************************************************************************

# 6. Multiplication Tables
# Print multiplication tables from 1 to 10.

# def multiplication_table(a):
#     for i in range(1,11):
#         b=i*a
#         print(f"multiplication of : {x} * {i} : ",b)
# x=int(input("enter the number :" ))
# multiplication_table(x)

#********************************************************************************************************************************

# 7. Prime Numbers
# Print all prime numbers from 1 to 100.

# for num in range(2, 101):

#     count = 0

#     for i in range(1, num + 1):
#         if num % i == 0:
#             count = count+1

#     if count == 2:
#             print(num)

#********************************************************************************************************************************

# 8. Fibonacci
# Print first N Fibonacci numbers using a for loop.
# a=0
# b=1
# n=int(input("enter the number : "))
# for i in range(n):
#     print(a)
#     a,b=b,a+b

#********************************************************************************************************************************

# 9. Pattern
# Print: 1 / 22 / 333 / 4444 / 55555.

# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end="")
#     print()

#********************************************************************************************************************************

# 10. Character Counter
# Count uppercase, lowercase, digits and special characters.

# a=input("enter the character : ")
# upper_c =0
# lower_c =0
# digits_c =0
# special_c =0

# for i in a:
#     if i.isupper():
#         upper_c=upper_c+1

#     elif i.islower():
#         lower_c=lower_c+1

#     elif i.isdigit():
#         digits_c=digits_c+1

#     else:
#         special_c=special_c+1

# print(f"upper case : {upper_c}\nlowercse : {lower_c}\ndigits : {digits_c}\nspecial : {special_c}")
#********************************************************************************************************************************

# 11. Guess Number
# Secret number=25. Repeat until correct.


# #********************************************************************************************************************************

# 12. Login
# Allow only 3 login attempts.

# a=input("enter ur user name : ")
# b=input("enter your password :")
# for i in range(3):
#     n=input("confrim your password :")
#     if n==b:
#         print("login successful")
#         break
    
#     else:
#         print("invalid passworn !!")
# print(" no more attemps")
#********************************************************************************************************************************

# 13. Calculator
# Run calculator repeatedly until Exit.

# while(True):
#     print("1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.EXIT")
#     n=int(input("enter your choice : "))
#     if(n==1):
#         a=float(input("enter the first number : "))
#         b=float(input("enter the second number : "))
#         c=a+b
#         print(f"Addition of {a} and {b} is :",c)
#         print("")       # just for adding space

#     elif(n==2):
#         d=float(input("enter the first number : "))
#         e=float(input("enter the second number : "))
#         f=d-e
#         print(f"Substraction of {d} and {e} is :",f)
#         print("")       # just for adding space


#     elif(n==3):
#         g=float(input("enter the first number : "))
#         h=float(input("enter the second number : "))
#         i=g*h
#         print(f"multiplication of {g} and {h} is :",i)
#         print("")       # just for adding space


#     elif(n==4):
#         j=float(input("enter the first number : "))
#         k=float(input("enter the second number : "))
#         l=j/k
#         print(f"Division of {j} and {k} is :",l)
#         print("")       # just for adding space

#     elif(n==5):
#         print("exiting")
#         break

#     else:
#         print("invalid input !!")

#********************************************************************************************************************************

# 14. Reverse Number
# Reverse an integer using while.
# def reversing_int(x):
#     rev=0
#     while(x>0):
#         last_digit = x%10
#         rev = (rev * 10)+last_digit
#         x=x//10
#     return rev

# n=int(input("enter the intiger :"))
# print(reversing_int(n))

# *******************************************************************************************************************************

# 15. Sum of Digits
# Find digit sum using while.

# s=0
# n=int(input("enter the number"))
# while(n>0):
#     last_digit = n%10
#     s=s+last_digit
#     n=n//10
# print("sum =",s)

#********************************************************************************************************************************

# 16. Calculator Functions
# Implement add, subtract, multiply, divide.

#********************************************************************************************************************************