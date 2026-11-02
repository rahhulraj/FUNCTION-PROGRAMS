#Mobile Recharge
# Create a function that accepts a mobile number and recharge amount. Set the default recharge amount to ₹199.
# Call the function in three different ways:
# - Pass both arguments.
# - Pass only the mobile number.
# - Pass the arguments using keyword arguments.

def mobile_recharge(mobileno,amount=199):
    print("--------MOBILE RECHARGE DETAILS IS-------")
    print("MOBILE NUMBER :",mobileno)
    print("RECHARGE AMOUNT: ",amount)
mobnum=int(input("ENTER THE PHONE NUMBER :"))
rechamount=int(input("ENTER THE RECHRGE AMMOUNT :"))
mobile_recharge(mobnum,rechamount)
print("\t")
mobnum=int(input("ENTER THE PHONE NUMBER :"))
mobile_recharge(mobnum)
print("\t")
mobile_recharge(mobileno=8078162799,amount=399)