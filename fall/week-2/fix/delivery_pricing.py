# Food Delivery Fee Calculator
# Calculates delivery fees based on distance, order size, weather conditions,
# and premium membership status.

import time


print("Delivery Fee Calculator")
print("=" * 23)

# Get user input
restaurant = input("Restaurant name: ")
distance = float(input("Distance to delivery address (miles): "))
order_total = float(input("Order total: $"))
weather = input("Current weather (clear/rain/snow): ").lower().strip()
premium_member = input("Are you a Premium member? (yes/no): ").lower() == 'yes'

# Simulate calculation by sleeping for two seconds
print()
print("Calculating...")
time.sleep(2)
print()

# Initialize fee variables
base_fee = 0
distance_fee = 0
weather_fee = 0
service_fee = 0
total_fees = 0

# Base delivery fee based on distance
if distance <= 2:
    base_fee = 2.99
elif distance <= 5:
    base_fee = 4.99
else:
    base_fee = 6.99

# Distance fee for longer trips
if distance > 5:
    extra_miles = distance - 5
    distance_fee = extra_miles * 0.75

# Weather surcharge
RAIN_SURCHARGE = 1.50
SNOW_SURCHARGE = 2.50

if weather == "rain" or weather == "snow":
    if weather == "rain":
        weather_fee = RAIN_SURCHARGE
    elif weather == "snow":
        weather_fee = SNOW_SURCHARGE

# Service fee based on order size
if order_total < 15:
    service_fee = 2.00
elif order_total < 30:
    service_fee = 1.00

# Calculate total before membership discount
total_fees = base_fee + distance_fee + weather_fee + service_fee

# Premium member benefits
if premium_member:
    if total_fees > 5:
        # Free delivery on orders with high fees
        total_fees = 0
        discount_applied = "Free delivery"
    else:
        # 50% off on smaller fees
        total_fees = total_fees * 0.5
        discount_applied = "50% off"
else:
    discount_applied = "None"

# Display breakdown
print(f'+{"-" * 45}+')
print('Thank You'.upper().center(45))
print(f'+{"-" * 45}+')
print(f'Restaurant:  {restaurant}')
print(f'Distance:    {distance} miles')
print(f'Order Total: ${order_total:.2f}')
print()
print(f'    Base Fee:          ${base_fee:.2f}')
print(f'    Distance Fee:      ${distance_fee:.2f}')
print(f'    Subtotal:          ${base_fee + distance_fee + weather_fee + service_fee:.2f}')
print()

if weather_fee > 0:
    print(f'    Weather Surcharge: ${weather_fee} ({weather})')

if service_fee > 0:
    print(f'    Small Order Fee:   ${service_fee:.2f}')

print(f'    Discount Applied:  {discount_applied}')
print(f'    Delivery Fee:      ${total_fees:.2f}')
print()
print(f'Total: ${order_total + total_fees:.2f}')
print(f'+{"-" * 45}+')
