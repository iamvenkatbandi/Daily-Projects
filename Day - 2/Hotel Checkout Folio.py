currency = "₹"
percentage = 100
border = "="
divider = "-"
folio_width = 52
label_width = 13
money_label_width = 28
money_width = 12


# Collecting Information from Users
guest_name = input("Guest Name: ")
room_number = input("Room Number: ")
number_of_nights = int(input("Number of Nights: "))
room_rate_per_night = float(input("Room Rate per Night: "))
number_of_extra_beds = int(input("Number of Extra Beds: "))
extra_bed_rate_per_night = int(input("Rate of Extra Bed per Night: "))
food_and_beverage_charges = float(input("Food & Beverage Charges: "))
minibar_charges = float(input("Total Minibar Charges: "))
service_charge_percentage = float(input("Service Charge: "))
gst_percentage = float(input("GST: "))
loyalty_discount_percentage = float(input("Loyalty Discount: "))

# Cleaning the Guest name
cleaned_guest_name = guest_name.strip().title()

# Storing all percentages in Whole numbers and Fractions
service_charge_fraction = service_charge_percentage / percentage
gst_fraction = gst_percentage / percentage
loyalty_discount_fraction = loyalty_discount_percentage / percentage

# Calculating the Room Charge
room_charges = number_of_nights * room_rate_per_night

# Calculating the Extra Bed Charge
extra_bed_charge = number_of_extra_beds * extra_bed_rate_per_night

# Calculating the Subtotal
subtotal = room_charges + extra_bed_charge + food_and_beverage_charges + minibar_charges

# Calculating the Loyalty Discount
loyalty_discount = loyalty_discount_fraction * room_charges

# Calculating Amount After Discount
amount_after_discount = subtotal - loyalty_discount

# Calculating the Service Charge
service_charge = service_charge_fraction * amount_after_discount

# Calculating the GST
gst = gst_fraction * (amount_after_discount + service_charge)

# Calculating the Grand Total
grand_total = amount_after_discount
grand_total += service_charge
grand_total += gst

# Splitting the Grand Total into Rupees and Paise
whole_rupees = grand_total // 1
paise_fraction = grand_total % 1
paise = paise_fraction * 100

# Calculating the Average Amount Per Night
average_amount_per_night = grand_total / number_of_nights

# Calculating the Extra Charges
extra_charges = service_charge + gst / subtotal

# Creating the Folio
folio = f"""
{border}
{'The Palm Grove':^{folio_width}}
{'Hotel Checkout Folio':^{folio_width}}
{border}
{'Guest':<{label_width}}: {cleaned_guest_name}
{'Room Number':<{label_width}}: {room_number}
{'Nights':<{label_width}}: {number_of_nights}
{divider}
{'+ Room Charges':<{money_label_width}}{currency}{room_charges:>{money_width},.2f}
{'+ Extra Bed Charges':<{money_label_width}}{currency}{extra_bed_charge:>{money_width},.2f}
{'+ Food & Beverages':<{money_label_width}}{currency}{food_and_beverage_charges:>{money_width},.2f}
{'+ Minibar':<{money_label_width}}{currency}{minibar_charges:>{money_width},.2f}
{'Charges Subtotal':<{money_label_width}}{currency}{subtotal:>{money_width},.2f}

"""