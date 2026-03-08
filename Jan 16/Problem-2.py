menu = { 
    "Espresso": 3.50, 
    "Latte": 4.50, 
    "Gold_Flake_Coffee": 50.00, 
    "Sandwich": 8.00, 
    "Luxury_Truffle": 25.00 
}
print("Original Menu:")
print("-" * 25)
for item, price in menu.items():
    print(f"{item:20} ${price:.2f}")
print("-" * 25)


items_to_remove = []

# for item, price in menu.items():
#     if price > 10.00:
#         items_to_remove.append(item)

# # Now remove the expensive items
# for item in items_to_remove:
#     del menu[item]  


print("\nMenu after removing items over $10:")
print("-" * 25)
for item, price in menu.items():
    if price <= 10.00:
        print(f"{item:20} ${price:.2f}")
print("-" * 25)