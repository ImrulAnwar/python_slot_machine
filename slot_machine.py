def deposit():
    while (True):
        amount = input("How much do you want to deposit? ")
        if (amount.isdigit()):
            amount = int(amount)
            if (amount > 0):
                break
            else:
                print("Please enter a positive number")
        else:
            print("Please enter a valid number")
    return amount

deposit()
