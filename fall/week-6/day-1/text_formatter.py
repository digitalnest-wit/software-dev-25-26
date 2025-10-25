def to_uppercase(text):
    result = text.upper()
    print(f"\nUppercase: {result}")

def to_lowercase(text):
    result = text.lower()
    print(f"\nLowercase: {result}")

def to_title_case(text):
    result = text.title()
    print(f"\nTitle Case: {result}")

def reverse_text(text):
    result = text[::-1]
    print(f"\nReversed: {result}")

def count_words(text):
    words = text.split()
    result = len(words)
    
    print(f"\nWord Count: {result}")


print("\n=== Text Formatter ===")

user_text = input("Enter text to format: ")

print("\nFormatting Options:")
print("  1. Uppercase")
print("  2. Lowercase")
print("  3. Title Case")
print("  4. Reverse")
print("  5. Count Words")

choice = input("\nChoose option (1-5): ").strip()

if choice == "1":
    to_uppercase(user_text)
elif choice == "2":
    to_lowercase(user_text)
elif choice == "3":
    to_title_case(user_text)
elif choice == "4":
    reverse_text(user_text)
elif choice == "5":
    count_words(user_text)
else:
    print("\nInvalid choice")
