# # name = "Fahmin"
# # print("Hello, World")
# # print(name)
# # print(2+3)
# # print(2-3)
# # print(5%2)

# # print("------BIO DATA------")
# # print(input("enter your name:"))
# # print(input("enter your age:"))
# # print(input("enter your place:"))

# # list=[1,2,3,4,5]
# # print(list)

# # print(list[1])


# # fruits=["apple","orange","kiwi"]
# # print(fruits[1])
# # fruits.append("pineapple")
# # print(fruits)

# # players=["messi","ronaldo","neymar"]
# # print(players)
# # players.append("yamal")
# # print(players)


# fruits=["apple","orange","kiwi"]
# print(fruits[1])
# fruits.append("pineapple")
# print(fruits)

# fruits.remove("orange")
# print(fruits)

# fruits.extend(["mango","banana","passion fruit","avacado"])
# print(fruits)

# fruits.insert(1,"strawberry")
# print(fruits)


# players=["messi","ronaldo","nmeymar"]
# print(players)

# players.append("olmo")
# print(players)

# players.insert(0,"yamal")
# print(players)

# players.extend(["rodri","martinez"])
# print(players)

# print(len(players))

# for x in players:
#     print(x)


# name = "hello"
# print(name[::-1])  #reversing 

# name = "hello"
# print(name[1:5])     #slicing

# name = "abhinand"
# print(name.upper())

# name1 = "ABHINAND"
# print(name1.lower())

# subject = 'python'
# print(subject.capitalize())

# print(subject.isdigit())

# list1 = ["messi","rono","neymar","hazard"]
# print(list1)

# list1[3]="kevin"
# print(list1)

# list1[1:3]="yamal","coco","cryff"
# print(list1)

# list1.insert(5,"rono")
# print(list1)

# list1.append("marcelo")
# print(list1)

# list2 = ["pedri","gavi","cubarsi"]
# list1.extend(list2)
# print(list1)

# list1.remove("coco")
# print(list1)

# for i in range(len(list1)):
#     print(list1[i])

# list1.sort()
# print(list1)

# list1.sort(reverse=True)    # descending oder
# print(list1)

# list1=[12,15,45,23,16]
# print("third element is : ",list1[2])
# a=len(list1)
# print("length of list :",a)
# if a == 0:
#     print("list is empty")
# else:
#     print("list is not empty")

# #*******************************************************************************************************

# Exercise 2. Perform List Manipulation
# Practice Problem: Take a given list and modify it through five specific actions:

# Change Element: Change the second element of a list to 200 and print the updated list.
# Append Element: Add 600 o the end of a list and print the new list.
# Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
# Remove Element (by value): Remove 600 from the list and print the list.
# Remove Element (by index): Remove the element at index 0 from the list print the list.
# Exercise Purpose: Python lists are mutable, meaning they can be changed after they are created. 
# This exercise demonstrates the various ways to “reshape” your data dynamically during execution.

# Given Input: Initial List: [100, 50, 400, 500]


# list2 =[100,50,400,500]
# print(list2)
# list2[1]=200
# print("updated list",list2)
# list2.append(600)
# print("appended list :",list2)
# list2.insert(2,300)
# print(list2)
# list2.remove(600)
# print("removed list :",list2)
# del list2[0]
# print("removed list =",list2)

#*****************************************************************************************************************************