# Personal Budget Tracker
# Run here: https://www.programiz.com/online-compiler/0moVyq6i5z5GM

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

print("Income and Expenses")
print("===================")
print()
print(f'Monthly income: ${monthly_income:.2f}')
print(f'Cost of rent:   ${rent_cost:.2f}')
print(f'Available:      ${money_available:.2f}')
print()
print("Budgets")
print("=======")
print()
print(f'Food:           ${food_budget:.2f}')
print(f'Entertainment:  ${entertainment_budget:.2f}')
print(f'Video Games:    ${videogames_budget:.2f}')
print(f'Subscriptions:  ${subscriptions_budget:.2f}')
print()
print(f'Total budgets:          ${total_budget:.2f}')
print(f'Available after budget: ${money_available - total_budget:.2f}')
print("=" * 20)
