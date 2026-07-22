def calculate_energy_charge(units):
    energy_charge = 0

    if units <= 30:
        energy_charge = units * 1.90
    elif units <= 75:
        energy_charge = (
            (30 * 1.90) +
            ((units - 30) * 3.00)
        )
    elif units <= 125:
        energy_charge = (
            (30 * 1.90) +
            (45 * 3.00) +
            ((units - 75) * 4.50)
        )
    elif units <= 225:
        energy_charge = (
            (30 * 1.90) +
            (45 * 3.00) +
            (50 * 4.50) +
            ((units - 125) * 6.00)
        )
    elif units <= 400:
        energy_charge = (
            (30 * 1.90) +
            (45 * 3.00) +
            (50 * 4.50) +
            (100 * 6.00) +
            ((units - 225) * 8.75)
        )
    else:
        energy_charge = (
            (30 * 1.90) +
            (45 * 3.00) +
            (50 * 4.50) +
            (100 * 6.00) +
            (175 * 8.75) +
            ((units - 400) * 9.75)
        )

    return energy_charge

def calculate_fixed_charge():
    return 10

def main():
    print("Welcome to Electrcity Bill Calculator")

    try:
        units = float(input("Enter Number of Units Consumed: "))

        if units < 0:
            print("Units can't be Negative.")
            return

        energy_charge = calculate_energy_charge(units)
        fixed_charge = calculate_fixed_charge()

        total_bill = energy_charge + fixed_charge

        print("\n----------- BILL DETAILS ----------")
        print(f"Units Consumed: {units}")
        print(f"Entergy Charge: ₹{energy_charge:.2f}")
        print(f"Fixed Charge: ₹{fixed_charge:.2f}")
        print("-----------------------------------")
        print(f"Total Bill: ₹{total_bill:.2f}")
        print("-----------------------------------")
    except ValueError:
        print("Invalid Input! Please enter Numeric Values only.")

main()