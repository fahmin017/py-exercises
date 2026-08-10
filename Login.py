
# 12. Login
# Allow only 3 login attempts.

a=input("enter ur user name : ")
b=input("enter your password :")
for i in range(3):
    n=input("confrim your password :")
    if n==b:
        print("login successful")
        break
    
    else:
        print("invalid passworn !!")
print(" no more attemps")