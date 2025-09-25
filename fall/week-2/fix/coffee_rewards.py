# Coffee Shop Rewards Program
# Calculates discounts based on loyalty membership and visit frequency

import time


print("☕ Brewjee Coffee Rewards ☕")
print()

# Get user input
name = input("Enter your name: ")
visits = int(input("How many visits this month? "))
member = input("Are you a loyalty member? (yes/no): ").lower() == 'yes'
order_total = float(input("Enter your order total: $"))

# Sleep to simulate work
print()
print(f"Processing rewards for {name}...")
time.sleep(2)
print()

# Initialize discount variables
discount_percent = 0
reward_tier = ""

# Determine discount based on membership and visits
if member:
    if visits >= 15:
        discount_percent = 25
        reward_tier = "Gold Member (25% off)"
    elif visits >= 10:
        discount_percent = 20
        reward_tier = "Silver Member (20% off)"
    elif visits >= 5:
        discount_percent = 15
        reward_tier = "Bronze Member (15% off)"
    else:
        discount_percent = 10
        reward_tier = "New Member (10% off)"
else:
    # Non-members can earn a small discount with frequent visits
    if visits >= 20:
        discount_percent = 10
        reward_tier = "Frequent Customer (10% off)"
    else:
        discount_percent = 0
        reward_tier = "No discount - Join our loyalty program!"

# Calculate savings
discount_amount = order_total * (discount_percent / 100)
final_total = order_total - discount_amount

# Display results
print("=" * 50)
print("REWARDS SUMMARY")
print("=" * 50)
print(f"Customer:          {name}")
print(f"Loyalty Member:    {'Yes' if member else 'No'}")
print(f"Visits This Month: {visits}")
print()
print(f"Order Total: ${order_total:.2f}")
print(f"Reward Tier: {reward_tier}")
print(f"Discount:    {discount_percent}%")
print(f"You Save:    ${discount_amount:.2f}")
print()
print(f"Final Total: ${final_total:.2f}")
print("=" * 50)
print()

# Encouragement messages
if member:
    if visits < 5:
        next_tier = 5 - visits
        print(f"Visit {next_tier} more times to reach Bronze tier!")
    elif visits < 10:
        next_tier = 10 - visits
        print(f"Visit {next_tier} more times to reach Silver tier!")
    elif visits < 15:
        next_tier = 15 - visits
        print(f"Visit {next_tier} more times to reach Gold tier!")
    else:
        print("You've reached our highest tier! Thanks for your loyalty!")
else:
    print("Join our loyalty program to start earning rewards!")

print("Keep it Brewjee ✨")
