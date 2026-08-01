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

list1 = ["messi","rono","neymar","hazard"]
print(list1)

list1[3]="kevin"
print(list1)

list1[1:3]="yamal","coco","cryff"
print(list1)

list1.insert(5,"rono")
print(list1)

list1.append("marcelo")
print(list1)

list2 = ["pedri","gavi","cubarsi"]
list1.extend(list2)
print(list1)

list1.remove("coco")
print(list1)

for i in range(len(list1)):
    print(list1[i])

list1.sort()
print(list1)

list1.sort(reverse=True)    # descending oder
print(list1)
