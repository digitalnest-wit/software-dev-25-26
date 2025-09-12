# ============================================================================
# CODE ALONG 2: Savings Tracker (FIXED VERSION)  
# Expected behavior: Calculate how much more money and time needed to reach goal
# ============================================================================

print("=== Savings Goal Tracker ===")
savings_goal = float(input("What's your savings goal? $"))
current_savings = float(input("How much have you saved so far? $"))
monthly_savings = float(input("How much do you save per month? $"))

money_needed = savings_goal - current_savings
months_needed = money_needed / monthly_savings

print(f"You need ${money_needed:.2f} more to reach your goal.")
print(f"At your current rate, you'll reach your goal in {months_needed:.1f} months.")