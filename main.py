# Programmer Name: Oreoluwa Adebusoye
# Program Name: Shipment Weight and Cost Calculation Program
# What program does: This program calculates the shipping costs of items

# Purpose output
print("Hi there! This program helps you to determine your total shipping cost based on the weight and number of the items being shipped.\n")

# Prompt the user to enter the total number of items they are planning to ship
num_items = int(input("Enter the number of items being shipped: "))

# Ask the user to provide the weight of each individual item in pounds
item_weight = float(input("Enter the weight of each item (in lbs): "))

# Request the user to input the shipping cost per kilogram or pounds
shipping_cost_per_unit = float(input("Enter the shipping cost per lb: "))

# Calculate total weight
total_weight = num_items * item_weight

# Calculate total shipping cost
total_shipping_cost = total_weight * shipping_cost_per_unit

# Output the results
print(f"\nNumber of Items: {num_items}")
print(f"Weight of Each Item: {item_weight:.2f} lbs")
print(f"Total Weight of Shipment: {total_weight:.2f} lbs")
print(f"Total Shipping Cost: ${total_shipping_cost:.2f}")