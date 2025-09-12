# Tip Calculator
# Run here: https://www.programiz.com/online-compiler/3kBTIeTfCAtU2

total_cost = float(input('Enter total amount: '))
tip_percentage = float(input('Enter tip percentage: '))

tip_amount = total_cost * (tip_percentage / 100)
total_plus_tip = total_cost + tip_amount

print(f'Total: ${total_plus_tip}')
