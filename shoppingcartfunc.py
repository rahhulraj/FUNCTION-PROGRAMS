#13. Shopping Cart
#Create a function that accepts a customer name and any number of product prices.
#Calculate and display the total shopping amount.

n=int(input("ENTER THE NUMBER OF PRODUCT :"))
def shopping(customername,*prices):
    total=0
    for i in prices:
        total=total+i
    print("\nSHOPPING DETAILS")
    print("CUSTOMER NAME:",customername)
    print("TOTAL SHOPPING AMOUNT:",total)
name=str(input("ENTER THE NAME :"))
prices=list()
for j in range(n):
    price=int(input("ENTER THE PRODUCT PRICE :"))
    prices.append(price)
shopping(name,*prices)