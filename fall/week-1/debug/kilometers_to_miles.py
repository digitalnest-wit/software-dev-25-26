# ============================================================================
# CODE ALONG 1: Kilometers to Miles (BUGGY VERSION)
# Expected behavior: Convert kilometers to miles (1 km = 0.621371 miles)
# ============================================================================

print("=== Kilometers to Miles Converter ===")
kilometers = input("Enter distance in kilometers: ")
miles = kilometers * 0.621371
print(f"{kilometers} kilometers equals {miles} miles")

# BUGS TO FIND:
# 1. input() returns a string, need to convert to float
# 2. Should be: kilometers = float(input("Enter distance in kilometers: "))
