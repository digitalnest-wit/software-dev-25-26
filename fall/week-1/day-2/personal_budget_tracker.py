# ============================================================================
# CHALLENGE: Personal Budget Tracker
# Expected behavior: Calculate money available and display a summary given
# monthly expenses and budget goals.
# ============================================================================

print("Personal Budget Tracker")
print()

monthly_income = float(input('Monthly income: $'))
rent_cost = float(input('Cost of rent: $'))
print()

prompt = 'How much would you like to spend on'

food_budget = float(input(f'{prompt} food monthly? $'))
entertainment_budget = float(input(f'{prompt} entertainment monthly? $'))
videogames_budget = float(input(f'{prompt} video games monthly? $'))
subscriptions_budget = float(input(f'{prompt} subscriptions monthly? $'))
print()

total_budget = food_budget + entertainment_budget + videogames_budget + subscriptions_budget
money_available = monthly_income - rent_cost

summary = f'''
Income and Expenses
===================

Monthly income: ${monthly_income:.2f}
Cost of rent:   ${rent_cost:.2f}
Available:      ${money_available:.2f}

Budgets
=======

Food:           ${food_budget:.2f}
Entertainment:  ${entertainment_budget:.2f}
Video Games:    ${videogames_budget:.2f}
Subscriptions:  ${subscriptions_budget:.2f}

Total budgets:          ${total_budget:.2f}
Available after budget: ${money_available - total_budget:.2f}
{"=" * 20}
'''

print(summary)
