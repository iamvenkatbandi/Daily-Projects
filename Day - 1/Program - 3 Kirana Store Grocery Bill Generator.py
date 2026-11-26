# Fixed Information
divider = "="
line_divider = '-'

kilogram = "kg"
litre = "L"

multiplication = "x"
equal_to = "="

currency = "₹"

rule_width = 40
line_width = 40
label_width = 12
percentage = 100

store_name = "Sri Lakshmi Kirana Store"
gst_percentage = 5
gst_fraction = gst_percentage / percentage

# Collecting Information from User
customers_name = input("Customer Name: ")
rice_quantity = float(input("Rice Quantity (KG): "))
rice_price_per_kg = float(input("Price of Rice (KG): "))
dal_quantity = float(input("Dal Quantity (KG): "))
dal_price_per_kg = float(input("Price of Dal (KG): "))
sunflower_oil_quantity = float(input("Sunflower Oil Quantity (Ltr): "))
sunflower_oil_price_per_ltr = float(input("Price of Sunflower Oil (Ltr): "))

# Capitalizing the Store Name
cleaned_store_name = store_name.upper()

# Calculating the Amount
rice_amount = rice_quantity * rice_price_per_kg
dal_amount = dal_quantity * dal_price_per_kg
sunflower_oil_amount = sunflower_oil_quantity * sunflower_oil_price_per_ltr

# Calculating the subtotal
subtotal = rice_amount + dal_amount + sunflower_oil_amount

# Adding GST to Subtotal
grand_total = subtotal + gst_fraction

# Pre-built Labels
gst_label = f"GST ({gst_fraction:.1%})"

bill = f"""
{divider * rule_width}
{cleaned_store_name:^{rule_width}}
{divider * rule_width}
{'Customer':<{label_width}}: {customers_name}
{line_divider * line_width}
{'Rice':<{label_width}}: {rice_quantity} {kilogram} {multiplication} {currency} {rice_price_per_kg} {equal_to} {currency} {rice_amount}
{'Toor Dal':<{label_width}}: {dal_quantity} {litre} {multiplication} {currency} {dal_price_per_kg} {equal_to} {currency} {dal_amount}
{'Oil':<{label_width}}: {sunflower_oil_quantity} {multiplication} {currency} {sunflower_oil_price_per_ltr} {equal_to} {currency} {sunflower_oil_amount}
{line_divider * line_width}
{'Subtotal':<{label_width}}: {currency} {subtotal:.2f}
{gst_label:<{label_width}}: {currency} {gst_fraction:.2f}
{'Total':<{label_width}}: {currency} {grand_total:.2f}
{divider * rule_width}
{f'Thank You, {customers_name}! Visit Again.'}
"""

print(bill)