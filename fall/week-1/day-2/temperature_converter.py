# ============================================================================
# CHALLENGE: Temperature Converter
# Expected behavior: Calculate the total amount to pay given a total a tip
# percentage.
# ============================================================================

temp_fahrenheit = float(input('Enter a temperature: ºF '))
temp_celsius = (temp_fahrenheit - 32) * (5 / 9)

print(f'=> {temp_celsius:.2f}ºC')
