# Recursion

# Recursion is when a function calls itself.

# Recursion is a common mathematical and programming concept. 
# It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

# def my_function(n):
#     if n<=0:
#         print("its done bruh 🥱🥱")
#     else:
#         print(n)
#         my_function(n-1)
# my_function(6)

#******************************************************************************************************************************

# def factorial(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))

#******************************************************************************************************************************
# Find the 7th number in the Fibonacci sequence:

# def fib(n):
#     if n<=0:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)

# print(fib(7))
#******************************************************************************************************************************

# Recursion with Lists

# Recursion can be used to process lists by handling one element at a time:
# Calculate the sum of all elements in a list:

# def sum_list(n):
#     if len(n)==0:
#         return "list is empty"
#     else:
#         return n[0]+sum_list(n[1:])
# n=[1,23,5,41,6]
# print(sum_list(n))

#******************************************************************************************************************************

# Find the maximum value in a list:

# def maximum(n):
#     if len(n)==0:
#         return "list is empty"
#     else:
#         max_val = max(n)
#         return max_val
# n=[5,1,7,8,6,12,4,7,6,3,8]
# print(maximum(n))

#******************************************************************************************************************************

# def fib(n):
#     if n<=0:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# a = int(input("enter the number"))
# for i in range(a):
#     print(fib(i),end="")

#******************************************************************************************************************************

# A Python 3 program to emonstrate working of
# recursion
# def printFun(test):

#     if (test < 1):
#         return
#     else:

#         print(test, end=" ")
#         printFun(test-1)  
#         print(test, end=" ")
#         return
    
# test = 3
# printFun(test)

#******************************************************************************************************************************

# def sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum(n - 1)
# n = 10
# print(sum(n))

#******************************************************************************************************************************

# Check if a number is Palindrome

# def palindrome(n):

#     rev = 0
#     temp = abs(n)
#     while temp!=0:
#         rev = (rev*10)+(temp%10)
#         temp = temp//10
#     return (rev==abs(n))

# n=int(input("enter the no :"))
# if palindrome(n)==True:
#     print(" IT IS PALINDROME")
# else:
#     print("IT IS NOT PALINDROME")

#******************************************************************************************************************************

