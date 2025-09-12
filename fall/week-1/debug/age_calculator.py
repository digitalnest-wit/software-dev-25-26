# ============================================================================
# CHALLENGE: Age Calculator (BUGGY VERSION)
# Expected behavior: Convert age in years to months, days, hours, and minutes
# ============================================================================

print("=== Age Calculator ===")
age_years = input("Enter your age in years: ")

age_months = age_years * 12
age_days = age_years * 365
age_hours = age_days * 24
age_minutes = age_hours * 60

print(f"You are approximately:")
print(f"{age_months} months old")
print(f"{age_days} days old") 
print(f"{age_hours} hours old")
print(f"{age_minutes} minutes old")

# BUGS TO FIND:
# 1. input() returns string, need: age_years = int(input("Enter your age in years: "))
# 2. All calculations will fail because you can't multiply string by number
