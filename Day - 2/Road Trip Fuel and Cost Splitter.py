# Fixed Values
report_name = "Road Trip Cost Report"
currency = "₹"
distance_unit = "km"
fuel_unit = "litres"
hour = "hours"
minute = "minutes"

divider = "="
line = "-"
rule_width = 45
label_width = 18
money_width = 14

# Collecting Information from the User
route_name = input("Route Name: ")
one_way_distance = float(input("One-Way Distance: "))
vehicle_mileage = float(input("Vehicle Mileage: "))
petrol_price = float(input("Petrol Price: "))
total_toll_charges = float(input("Total Toll Charges: "))
number_of_travellers = int(input("Number of Travellers: "))
average_speed = int(input("Average Speed: "))

# Calculating how much fuel needed
fuel_needed = one_way_distance / vehicle_mileage

# Calculating how much fuel cost
fuel_cost = fuel_needed * petrol_price

# Calculating the Total Trip Cost
total_trip_cost = fuel_cost + total_toll_charges

# Calculating the Share per Person
share_per_person = total_trip_cost / number_of_travellers

# Calculating the Travel Time (Showing in Hours and Minutes)
total_minutes = int(one_way_distance * 60 / average_speed)
hours = total_minutes // 60
minutes = total_minutes % 60

# Formatting the Route Name
formatted_route_name = route_name.capitalize()

# Capitalizing the Report Name
capitalized_report_name = report_name.upper()

# Printing the Road Trip Cost Report
report = f"""
{divider * rule_width}
{capitalized_report_name:^{rule_width}}
{divider * rule_width}
{'Trip':<{label_width}}: {formatted_route_name}
{'Distance':<{label_width}}: {one_way_distance:,.1f} {distance_unit}
{'Travellers':<{label_width}}: {number_of_travellers}
{line * rule_width}
{'Fuel Needed':<{label_width}}: {fuel_needed:,.2f} {fuel_unit}
{'Fuel Cost':<{label_width}}: {currency}{fuel_cost:,.2f}
{'Toll Charges':<{label_width}}: {currency}{total_toll_charges:,.2f}
{'Total Trip Cost':<{label_width}}: {currency}{total_trip_cost:,.2f}
{line * rule_width}
{'Share per Person':<{label_width}}: {currency}{share_per_person:,.2f}
{'Travel Time':<{label_width}}: {hours} {hour} {minutes} {minute}
{divider * rule_width}
"""

print(report)