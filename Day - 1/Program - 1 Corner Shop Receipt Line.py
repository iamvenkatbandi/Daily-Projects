# Corner Shop Receipt Line

shop_name = "Corner Shop"
currency = "₹"
label_width = 11
rule_width = 26

item_name = input("Enter the item name: ")
item_quantity = int(input("Enter the quantity of item: "))
unit_price = float(input("Enter the Price of One Unit: "))

# Calculating the Subtotal using the multiplication operator
subtotal = item_quantity * unit_price

# Printing the Receipt
print("=" * rule_width)
print(f"{shop_name:<{rule_width}}")
print("=" * rule_width)

print(f"{'Item':<{label_width}}: {item_name}")
print(f"{'Qty':<{label_width}}: {item_quantity}")
print(f"{'Unit Price':<{label_width}}: {unit_price}")

print("-" * rule_width)

print(f"{'Subtoal':<{label_width}}: {currency} {subtotal:.2f}")
print("=" * rule_width)