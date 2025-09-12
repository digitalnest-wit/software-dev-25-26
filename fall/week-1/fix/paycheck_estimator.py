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
take_home_pay = gross_pay - taxes

print(f"Gross pay: ${gross_pay:.2f}")
print(f"Taxes (20%): ${taxes:.2f}")
print(f"Take-home pay: ${take_home_pay:.2f}")
