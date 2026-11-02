# 8. Electricity Bill
#   Create a function that accepts the number of units consumed. Set the price per unit to ₹8 by default.
#   Calculate and display the electricity bill.


def electricity_bill(units,price=8):
    bill=units*price
    print("\n----------ELECTRICITY BILL DETAILS----------")
    print("UNITS CONSUMED:",units)
    print("PRICE PER UNIT: ₹",price)
    print("TOTAL ELECTRICITY BILL: ",bill)
units=int(input("ENTER THE NUMBER OF UNITS CONSUMED: "))
electricity_bill(units)

