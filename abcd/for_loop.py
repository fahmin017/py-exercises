# fruits=["apple","orange","kiwi"]

# for i in fruits:
#     print(i)

# for i in range(1,6):
#     print(i)

# for i in range(1,10,2):
#     print(i)                        #odd numbers using for loop

# for i in range(0,10,2):
#     print(i)                        #even numbers using for loop


# for i in range (0, 100, 5):
#     print(i)


# for i in range(5):
#     print(i,end=" ")


# for i in range(5):
#     for j in range(6):
#         print(i, end=" ")
#     print()

#*********************************************************************************************************

# n=5                                                                 
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# out: 

# *
# **
# ***
# ****
# *****


#************************************************************************************************************

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

# out :

# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

#*****************************************************************************************************************

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")

#     for j in range(i+1):
#         print("*", end=" ")
#     print()  



#           * 
#         * * 
#       * * * 
#     * * * * 
#   * * * * * 


#*****************************************************************************************************************************

# for i in range(6):
#     for j in range(1,i+1):
#         print(j,end="  ")
#     print()


#**************************************************************************************************************************

# for i in range(6,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()



    

#*****************************************************************************************************************************

# for i in range(5):
#     for j in range(5):
#         print("#",end="  ")
#     print()




# for i in range(5):
#     for j in range(5):
#         print("$",end="  ")
#     print()




# for i in range(5):
#     for j in range(5):
#         print("&",end="  ")
#     print()


#***********************************************************************************************************************


# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")

#     for j in range(i+1):
#         print("*", end=" ")

#     for j in range(i):
#             print("*", end=" ")

#     print()  

#**************************************************************************************************************************

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")

#     for j in range(i+1):
#         print("*", end=" ")

#     for j in range(i):
#             print("*", end=" ")

#     print()  

# for a in range(n):
#     for b in range(a+2):
#         print(" ",end=" ")

#     for b in range(a,n-1):
#          print("*",end=" ")

#     for b in range(a+2,n):
#          print("*",end=" ")
         
#     print()


# OUTPUT

#           * 
#         * * * 
#       * * * * * 
#     * * * * * * * 
#   * * * * * * * * * 
#     * * * * * * * 
#       * * * * * 
#         * * * 
#           * 
            

#*********************************************************************************************************************
# n=5

# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+j), end=" ")
#     print()


# n=5
# for i in range(n,0,-1):
#     for j in range(i+1):
#         print(chr(65+j),end=" ")
#     print()

# OUTPUT

# A B C D E F 
# A B C D E 
# A B C D 
# A B C 
# A B 


#*********************************************************************************************************************


# n=5
# for i in range(n):

#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print(chr(65+j),end=" ")
#     print()

    #*****************************************************************************************************************

# BUTTERFLY PATTERN
# n=5
# for i in range(n-1):
#     for j in range(i+1):
#         print("*",end=" ")

#     print()

# for a in range(n):
#     for b in range(a,n):
#         print("*",end=" ")
#     print()


#OUTPUT

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 


#*************************************************************************************************************************

# n=7
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


# OUTPUT

        # 1234567
        # 123456
        # 12345
        # 1234
        # 123
        # 12
        # 1


#**********************************************************************************************************************

# n=7
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# for a in range(2,n+1):
#     for b in range(1,a+1):
#         print(b,end=" ")
#     print()


#OUTPUT

    # 1 2 3 4 5 6 7 
    # 1 2 3 4 5 6 
    # 1 2 3 4 5 
    # 1 2 3 4 
    # 1 2 3 
    # 1 2 
    # 1 
    # 1 2 
    # 1 2 3 
    # 1 2 3 4 
    # 1 2 3 4 5 
    # 1 2 3 4 5 6 
    # 1 2 3 4 5 6 7 

#***********************************************************************************************************************

# n= int(input("enter the number"))
# s=0
# for i in range(1,n+1):
#     s=s+i
#     print("sum =",s)


#***********************************************************************************************************************


# TO CALCULATE THE CUBE OF ALL NO: FROM 1 TO GIVEN NUMBE

# a= int(input("enter the number"))
# for i in range(1,a+1,+1):
#     a=i*i*i
#     print(f"cube of {i} =",a)



# OUTPUT:
#     cube of 1 = 1
#     cube of 2 = 8
#     cube of 3 = 27
#     cube of 4 = 64

#***********************************************************************************************************************

# Count occurrences of a specific element in a list
    
# n= list((input("enter the list")))
# print("your list =",n)
# a=input("enter the number you want to count")
# count =0
# for i in n:
#     if i == a:
#         count = count+1
# print(f"occurance of the number {a} in the list is: ",count)


# n= list((input("enter the list")))
# print("your list =",n)
# a=input("enter the number you want to count")
# count = n.count(a)
# print(f"occurance of{a}=",count)


#**********************************************************************************************************************

# Reverse a string using a for loop (no slicing)

# a = input("enter the string :")
# reversed_str = ""

# for i in a:
#     reversed_str = i + reversed_str
# print("Reversed string =",reversed_str)


# b = input("Enter  string :")
# reversed_str = b[::-1]
# print("reversed string is =",reversed_str)

#**********************************************************************************************************************


a = input("enter the string :")
reversed_str = ""

for i in a:
    reversed_str = i + reversed_str
print("reversed=",reversed_str)
if reversed_str == a:
    print("palindrome")
else:
    print("not palindrome")
