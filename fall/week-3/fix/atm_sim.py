# ATM Simulator - Working Version

balance = 1000.0

print("Welcome to the ATM")

while True:
    print("\n--- Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Quit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        print(f"Your balance: ${balance}")
    
    elif choice == "2":
        amount = float(input("Deposit amount: $"))
        balance += amount
        print(f"Deposited ${amount}")
    
    elif choice == "3":
        amount = float(input("Withdrawal amount: $"))
        if amount > balance:
            print("Insufficient funds!")
        else:
            balance -= amount
            print(f"Withdrew ${amount}")
    
    elif choice == "4":
        print("Thank you for using our ATM!")
        break
    
    else:
        print("Invalid option. Please try again.")