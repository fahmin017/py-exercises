# x = int(input("enter the no:"))

# if(x % 2 == 0):
#     print("even no")

# else:
#     print("odd no")


###########################################
# y=int(input("enter the no :"))

# if(y>0):
#     print("positive")

# else:
#     print("negative")


##############################################

# x = int(input("enter your age :"))

# if(x>= 18):
#     print("can vote")
# else:
#     print("cant vote")







##############################################





# # x = int(input("enter the number"))

# # if (x>0):
# #     print("positive no")

# # elif(x==0):
# #     print("zero")

# # else:
# #     print("negative")


# x = int(input("enter the mark"))

# if (x>90):
#     print("Grade A")

# elif(x>80):
#     print("Grade B")

# elif(x>70):
#     print("Grade C")

# elif(x>60):
#     print("Grade D")
# else:
#     print("failed")

###################################################

################ TASK #####################

# vowel checker

# x=input("enter a letter")

# if(x=="a"):
#     print("it is a vowel")

# elif(x=="e"):
#     print("it is a vowel")

# elif(x=="i"):
#     print("it is a vowel")

# elif(x=="o"):
#     print("it is a vowel")

# elif(x=="u"):
#     print("it is a vowel")

# else:
#     print("it is not a vowel")

##################################################################

# Triangle Type: Accept the lengths of three sides and determine if the triangle is Equilateral (all sides equal),
# #  Isosceles (two sides equal), or Scalene (no sides equal).

# x=int(input("enter the length"))
# y=int(input("enter the length"))
# z=int(input("enter the length"))

# if(x==y==z):
#     print("it is a equilateral triangle")

# elif(x==y and y!=z):
#     print("it is a isosceles triangle")

# elif(y==z and z!=x):
#     print("it is a isosceles triangle")

# elif(z==x and z!=y):
#     print("it is a isosceles triangle")

# else:
#     print("it is a scalene triangle")

########################################################################

# Electricity Bill: Calculate the bill based on units consumed:
# First 100 units: Free.
# Next 200 units: Rs. 2 per unit.
# Above 300 units: Rs. 5 per unit.
        #  ****************

x = int(input("enter the number of unit consumed"))

if(x<=100):
    print("electricity bill = 0")

elif(x<=300 and x>100):
    n = x*2
    print("electric charge =",n)

else:
    y = x*5
    print("electric charge =",y)