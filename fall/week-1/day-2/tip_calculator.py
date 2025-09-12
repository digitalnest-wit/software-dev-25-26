# ============================================================================
# CODE ALONG: Tip Calculator
# Expected behavior: Calculate the total amount to pay given a total a tip
# percentage.
# ============================================================================

total_cost = float(input('Enter total amount: $'))
tip_percentage = float(input('Enter desired tip percentage: %'))

tip_amount = total_cost * (tip_percentage / 100)
total_plus_tip = total_cost + tip_amount

print(f'Total amount with tip: ${total_plus_tip}')
