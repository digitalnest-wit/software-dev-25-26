# ATM Simulator - There are two bugs to find and fix.

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
        balance + amount
        print(f"Deposited ${amount}")
    
    elif choice == "3":
        amount = float(input("Withdrawal amount: $"))
        balance -= amount
        print(f"Withdrew ${amount}")
    
print("Thank you for using our ATM!")
