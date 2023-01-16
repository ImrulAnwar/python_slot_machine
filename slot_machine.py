MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

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

def get_number_of_lines():
    while (True):
        lines = input("Enter the number of lines to bet on? (1-"+str(MAX_LINES)+")? ")
        if (lines.isdigit()):
            lines = int(lines)
            if (1 <= lines <= MAX_LINES):
                break
            else:
                print("Please enter a number whithin range")
        else:
            print("Please enter a valid number")
    return lines

def get_bet():
    while (True): 
        amount = input(f"How much do you want to bet? {MIN_BET} - {MAX_BET} ")
        if (amount.isdigit()):
            amount = int(amount)
            if (MIN_BET <= amount <= MAX_BET):
                break
            else:
                print("Please enter a number within range")
        else:
            print("Please enter a valid number")
    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while (True):
        bet = get_bet()
        total_bet = bet * lines
        if (total_bet <= balance):
            print(f"You're betting {total_bet} for {lines} lines")
            break
        else:
            print("You don't have enough money to bet on that many lines")

main()