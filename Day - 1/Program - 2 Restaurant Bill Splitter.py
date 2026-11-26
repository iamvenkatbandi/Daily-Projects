<<<<<<< HEAD
# Restaurant Bill Splitter

currency = "₹"
percentage = 100
label_width = 11
rule_width = 26

# Collecting Information from the User
restaurant_name = input("Enter the Restaurant Name: ")
bill_amount = float(input("Enter the bill amount: "))
gst = float(input("Enter the GST Percentage: "))
tip = float(input("Enter the Tip Percentage: "))
number_of_people = int(input("Enter the Number of People Splitting: "))

# Calculating the GST and Tip rate
gst_rate = gst / percentage
tip_rate = tip / percentage

# Calculating the GST and Tip amount
gst_amount = gst_rate * bill_amount
tip_amount = tip_rate * bill_amount

# Calculating the Total Amount
total_bill = bill_amount + gst_amount + tip_amount

# Calculating the Per Person Share
per_person_share = total_bill/number_of_people

# Pre-built labels
gst_label = f"GST ({gst_rate:.1%})"
tip_label = f"Tip ({tip_rate:.1%})"

# Printing the Bill
print(f"{restaurant_name:<{rule_width}}")
print("=" * rule_width)

print(f"{'Food Amount':<{label_width}}: {currency} {bill_amount}")
print(f"{gst_label:<{label_width}}: {currency} {gst_amount:.2f}")
print(f"{tip_label:<{label_width}}: {currency} {tip_amount:.2f}")

print("-" * rule_width)

print(f"{'Grand Total':<{label_width}}: {currency} {total_bill:.2f}")
print(f"{'Per Person Share':<{label_width}}: {currency} {per_person_share:.2f}")

print("=" * rule_width)

print(f"Each of {number_of_people} pay {per_person_share:.2f}")

=======
# Restaurant Bill Splitter

currency = "₹"
percentage = 100
label_width = 11
rule_width = 26

# Collecting Information from the User
restaurant_name = input("Enter the Restaurant Name: ")
bill_amount = float(input("Enter the bill amount: "))
gst = float(input("Enter the GST Percentage: "))
tip = float(input("Enter the Tip Percentage: "))
number_of_people = int(input("Enter the Number of People Splitting: "))

# Calculating the GST and Tip rate
gst_rate = gst / percentage
tip_rate = tip / percentage

# Calculating the GST and Tip amount
gst_amount = gst_rate * bill_amount
tip_amount = tip_rate * bill_amount

# Calculating the Total Amount
total_bill = bill_amount + gst_amount + tip_amount

# Calculating the Per Person Share
per_person_share = total_bill/number_of_people

# Pre-built labels
gst_label = f"GST ({gst_rate:.1%})"
tip_label = f"Tip ({tip_rate:.1%})"

# Printing the Bill
print(f"{restaurant_name:<{rule_width}}")
print("=" * rule_width)

print(f"{'Food Amount':<{label_width}}: {currency} {bill_amount}")
print(f"{gst_label:<{label_width}}: {currency} {gst_amount:.2f}")
print(f"{tip_label:<{label_width}}: {currency} {tip_amount:.2f}")

print("-" * rule_width)

print(f"{'Grand Total':<{label_width}}: {currency} {total_bill:.2f}")
print(f"{'Per Person Share':<{label_width}}: {currency} {per_person_share:.2f}")

print("=" * rule_width)

print(f"Each of {number_of_people} pay {per_person_share:.2f}")

>>>>>>> 12737d9a0827c40a6c997d188586d96246f5171f
print("=" * rule_width)