#Part 7 – Combined practical challenges
#These questions combine multiple concepts.
#26. Restaurant Billing System
#Create a function that accepts:
#- Customer name (required)
#- Table number (required)
#- Any number of food item prices (*args)
#- Payment method (default: Cash)
#Calculate the total bill and display the details.

def restaurant(name,table,*prices,payment="Cash"):
    total=0
    for i in prices:
        total=total+i
    print("\nRESTAURANT BILL")
    print("CUSTOMER NAME:",name)
    print("TABLE NUMBER:",table)
    print("TOTAL BILL:",total)
    print("PAYMENT METHOD:",payment)
name=input("ENTER CUSTOMER NAME:")
table=int(input("ENTER TABLE NUMBER:"))
n=int(input("ENTER NUMBER OF FOOD ITEMS:"))
prices=list()
for i in range(n):
    price=int(input("ENTER FOOD ITEM PRICE:"))
    prices.append(price)
payment=input("ENTER PAYMENT METHOD (PRESS ENTER FOR CASH):")
if payment=="":
    restaurant(name,table,*prices)
else:
    restaurant(name,table,*prices,payment=payment)