# Gym Membership Eligibility Checker
# Determines gym membership eligibility based on age, permissions, and medical clearance

import time


print("💪 Gym Membership Eligibility 💪")
print()

# Get user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Assume the user will be an adult, who does not need guardian permission nor a
# medical clearance check.
has_guardian = True
medical_clearance = True

if age < 18:
    # Underage users will need guardian permission and, possibly, medical clearance.
    has_guardian = input("Do you have guardian permission? (yes/no): ").lower() == 'yes'
    medical_clearance = input("Do you have medical clearance? (yes/no): ").lower() == 'yes'

# Sleep to simulate work..
print()
print(f"Checking eligibility for {name}...")
print()
time.sleep(1)

# Determine eligibility based on age and requirements
if age >= 18:
    print("✅ Approved")
    print("Membership Level: Full Access")
    print("Reason: Age 18 or older")

elif age >= 16:
    if has_guardian:
        print("✅ Approved")
        print("Membership Level: Teen Access")
        print("Reason: Age 16-17 with guardian permission")
    else:
        print("⛔️ Rejected")
        print("Reason: Guardian permission required for ages 16-17")

elif age >= 14:
    if has_guardian and medical_clearance:
        print("✅ Approved")
        print("Membership Level: Youth Supervised")
        print("Reason: Age 14-15 with guardian permission and medical clearance")
    else:
        print("⛔️ Rejected")
        if not has_guardian:
            print("Missing: Guardian permission required")
        if not medical_clearance:
            print("Missing: Medical clearance required")

else:
    print("⛔️ Rejected")
    print("Reason: Must be at least 14 years old")
