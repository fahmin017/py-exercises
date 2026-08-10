
while(True):
    print("1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.EXIT")
    n=int(input("enter your choice : "))
    if(n==1):
        a=float(input("enter the first number : "))
        b=float(input("enter the second number : "))
        c=a+b
        print(f"Addition of {a} and {b} is :",c)
        print("")       # just for adding space

    elif(n==2):
        d=float(input("enter the first number : "))
        e=float(input("enter the second number : "))
        f=d-e
        print(f"Substraction of {d} and {e} is :",f)
        print("")       # just for adding space


    elif(n==3):
        g=float(input("enter the first number : "))
        h=float(input("enter the second number : "))
        i=g*h
        print(f"multiplication of {g} and {h} is :",i)
        print("")       # just for adding space


    elif(n==4):
        j=float(input("enter the first number : "))
        k=float(input("enter the second number : "))
        l=j/k
        print(f"Division of {j} and {k} is :",l)
        print("")       # just for adding space

    elif(n==5):
        print("exiting")
        break

    else:
        print("invalid input !!")
