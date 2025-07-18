#BANKING PROGRAM

def check_balance(balance):
    print(f"Your balance is ₹{balance: .2f}")

def deposit():
    amount = float(input("Enter the amount to deposit : ₹"))
    if amount <= 0:
        print("Invalid amount. Please try again")
        return 0
    else:
        print("Your amount has been deposited.")
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw : ₹"))
    if amount <= 0:
        print("Amount can't be zero or less than zero.")
        return 0
    elif amount > balance:
        print("Insufficient balance.")
        return 0
    else:
        print("Your amount has been withdrawn. Check your balance.")
        return amount

def main():
    balance = 0
    is_running = True

    print("BANKING PROGRAM")
    print()
    while is_running:
        print("1. Check Balance.")
        print("2. Deposit.")
        print("3. Withdraw.")
        print("4. Exit.")
        input_data = input("Enter your Choice (1 - 4) : ")

        if input_data == "1":
            check_balance(balance)  # ✅ pass balance
        elif input_data == "2":
            balance += deposit()
        elif input_data == "3":
            balance -= withdraw(balance)  # ✅ pass balance
        elif input_data == "4":
            is_running = False
            print("Thank You!")
        else:
            print("Invalid input. Please try again.")
            print()

if __name__ == '__main__':
    main()
