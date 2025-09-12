# ============================================================================
# CODE ALONG 3: Paycheck Estimator (BUGGY VERSION)
# Expected behavior: Calculate take-home pay after 20% tax deduction
# ============================================================================

print("=== Paycheck Estimator ===")
hourly_wage = float(input("Enter your hourly wage: $"))
hours_worked = float(input("Enter hours worked this week: "))

gross_pay = hourly_wage * hours_worked
tax_rate = 0.20
taxes = gross_pay * tax_rate
take_home_pay = gross_pay + taxes

print(f"Gross pay: ${gross_pay}")
print(f"Taxes (20%): ${taxes}")
print(f"Take-home pay: ${take_home_pay}")

# BUGS TO FIND:
# 1. take_home_pay calculation adds taxes instead of subtracting
# 2. Should be: take_home_pay = gross_pay - taxes
# 3. This makes it look like you earn MORE money after taxes!
