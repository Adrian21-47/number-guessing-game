def calculate_bill():
    total = 0

    while True:

        try:
            price = float(input("Enter the price of the item (enter 0 to finish): "))

            if price == 0:
                break

            total += price
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        vat = 0.2 * total
        net_amount = total - vat

    print("Total without vat: {:.2f}KES".format(net_amount))
    print("Vat(20%): {:.2f}KES".format(vat))
    print("Total Amount: {:.2f}KES".format(total))

if __name__ == "__main__":
    print("Welcome to the Restaurant Bill Calculator!")
    calculate_bill()
