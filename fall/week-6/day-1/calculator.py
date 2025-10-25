def add(a, b):
    result = a + b
    print(f"\n{a} + {b} = {result}")

def subtract(a, b):
    result =  a - b
    print(f"\n{a} - {b} = {result}")

def multiply(a, b):
    result =  a * b
    print(f"\n{a} * {b} = {result}")

def divide(a, b):
    result =  a / b
    print(f"\n{a} / {b} = {result}")


print("\n=== Calculator Program ===")

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

print("\nOperations:")
print("  1. Add")
print("  2. Subtract")
print("  3. Multiply")
print("  4. Divide")

choice = input("\nChoose an operation (1-4): ").strip()

if choice == "1":
    add(first_number, second_number)
elif choice == "2":
    subtract(first_number, second_number)
elif choice == "3":
    multiply(first_number, second_number)
elif choice == "4":
    divide(first_number, second_number)
else:
    print("\nInvalid choice")
