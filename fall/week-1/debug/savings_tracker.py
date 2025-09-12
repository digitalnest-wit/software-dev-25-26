# ============================================================================
# CODE ALONG 2: Savings Tracker (BUGGY VERSION)  
# Expected behavior: Calculate how much more money and time needed to reach goal
# ============================================================================

print("=== Savings Goal Tracker ===")
savings_goal = float(input("What's your savings goal? $"))
current_savings = float(input("How much have you saved so far? $"))
monthly_savings = float(input("How much do you save per month? $"))

money_needed = current_savings - savings_goal
months_needed = money_needed / monthly_savings

print(f"You need ${money_needed} more to reach your goal.")
print(f"At your current rate, you'll reach your goal in {months_needed} months.")

# BUGS TO FIND:
# 1. money_needed calculation is backwards
# 2. Should be: money_needed = savings_goal - current_savings
# 3. This will cause negative numbers and wrong calculations
