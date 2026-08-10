
a=int(input("enter the first side length : "))
b=int(input("enter the second side length : "))
c=int(input("enter the third side length : "))

if(a==b==c):
    print("triangle is equilateral")

elif(a==b and b!=c):
    print(" triangle is isocelus")

elif(c==a and a!=b):
    print(" triangle is isocelus")

elif(b==c and c!=a):
    print(" triangle is isocelus")

else:
    print("triangle is scalene")
