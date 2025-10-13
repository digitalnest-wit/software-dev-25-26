# Contact Manager

contacts = []

print("Contact Manager")
print()

# Add contacts
print("Add contacts to your list.")
num_contacts = int(input("How many contacts would you like to add? "))

for i in range(num_contacts):
    name = input(f"Enter contact name {i + 1}: ")
    contacts.append(name)

# Display all contacts
print("\n--- Contacts ---")
for i, contact in enumerate(sorted(contacts)):
    print(f"{i + 1}. {contact}")

# Search for a contact
print()
search_name = input("Search for a contact: ")

if search_name in contacts:
    print(f"Found: {search_name}")
    count = contacts.count(search_name)
    print(f"This name appears {count} time(s) in your contacts.")
else:
    print(f"{search_name} not found in contacts.")

# Display contacts alphabetically
print("\n--- Contacts ---")
contacts.sort()

for i, contact in enumerate(contacts):
    print(f"{i + 1}. {contact}")

# Display summary
print(f"\nTotal contacts: {len(contacts)}")

