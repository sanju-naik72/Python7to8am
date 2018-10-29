balance = 5000
print("Welcome to ICICI ATM")
pin = input("Enter Pin No : ")
if pin == "5475":
    print("Welcome")
    amt = int(input("Enter Withdraw Amount :"))
    if (amt%100) == 0 :
        if amt <= 20000 :
            if amt <= balance:
                balance = balance-amt
                print("Withdraw is Done")
                print("Available Balance : ",balance)
            else:
                print("No Funds")
        else:
            print("Max Withdraw is 20000/- only")
    else:
        print("Invalid Amount")
else:
    print("Invalid Pin No")
print("Thanks For Using ATM")