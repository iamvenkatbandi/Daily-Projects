currency_symbol = "₹"
border = "="
percentage = 100
label_width = 16
money_width = 8
rule_width = 44

# Collecting Information from the User
customer_name = input("Customer Name: ")
movie_name = input("Movie Name: ")
show_time = input("Show Time: ")
mobile_number = input("Mobile Number: ")

number_of_tickets = int(input("Number of Tickets: "))
ticket_price = float(input("Ticket Price: "))
booking_fee = float(input("Booking Fee per Ticket: "))
gst = float(input("GST: "))

# Cleaning the Customer Name
cleaned_customer_name = customer_name.strip().title()

# Converting the Movie name into Upper Case
movie_title = movie_name.upper()

# Calculating the Total Ticket Price
total_ticket_price = number_of_tickets * ticket_price

# Calculating the Booking Fee Total
total_booking_fee = number_of_tickets * booking_fee

# Calculating the Subtotal
subtotal = total_ticket_price + total_booking_fee

# Calculating the GST Fraction
gst_fraction = gst / percentage

# Calculating the GST Amount
gst_amount = gst_fraction * subtotal

# Calculating the Grand Total
grandtotal = subtotal + gst_amount

# Calculating the Average Amount Per Ticket
average_amount_per_ticket = grandtotal / number_of_tickets

# Building a Booking Reference String
show_key = show_time.replace(":","").replace(" ","")
booking_reference = show_key + "-" + str(number_of_tickets)

# Creating and Formatting the Slip
slip = f"""\
{border * rule_width}
{movie_title:^{rule_width}}
{border * rule_width}
{'Customer':<{label_width}}: {cleaned_customer_name}
{'Phone':<{label_width}}: {mobile_number}
{'Show':<{label_width}}: {show_time}
{'Booking Ref':<{label_width}}: {booking_reference}
{'Tickets':<{label_width}}: {number_of_tickets}
{'Ticket Price':<{label_width}}: {f'{currency_symbol} {ticket_price:,.2f}':>{money_width}}
{'Booking Fee':<{label_width}}: {f'{currency_symbol} {total_booking_fee:,.2f}':>{money_width}}
{'Subtotal':<{label_width}}: {f'{currency_symbol} {subtotal:,.2f}':>{money_width}}
{'GST ({gst:.1f}%)':<{label_width}}: {f'{currency_symbol} {gst_amount:,.2f}':>{money_width}}
{'Grand Total':<{label_width}}: {f'{currency_symbol} {grandtotal:,.2f}':>{money_width}}
{'Per Ticket':<{label_width}}: {f'{currency_symbol} {average_amount_per_ticket:,.2f}':>{money_width}}
{border * rule_width}
{'Booking Confirmed':^{rule_width}}
{border * rule_width}
"""

print(slip)

print(f"[check] tickets -> {type(number_of_tickets)}")
print(f"[check] price   -> {type(ticket_price)}")
print(f"[check] gst     -> {type(gst_fraction)} value {gst_fraction}")