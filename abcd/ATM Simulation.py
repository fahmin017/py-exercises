
# 5. ATM Simulation
# Balance starts at ■10000. Menu: Deposit, Withdraw, Check Balance, Exit. Prevent over-withdrawal.
def atm_simulation():
    bal=10000
    
    while(True):
        print(" 1. DEPOSIT \n 2.WITHDRAW \n 3.CHECK BALANCE \n 4.EXIT")
        n=int(input("enter your cohice : "))

        if(n==1):
            a=int(input("enter the amount you want to deposit :"))
            bal=bal+a
            print("Deposited sucessfully \nYour current balance is :",bal)

        elif(n==2):
            d=int(input("enter the amount you want to withdraw :"))
            bal=bal-d
            print("withraw sucessfull \nYour current balance is :",bal)

        elif(n==3):
            print("Your current balance is :",bal)

        elif(n==4):
            print("Exiting :")

            break 

        else:
            print("invalid")

atm_simulation()
