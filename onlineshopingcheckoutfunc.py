#28. Online Shopping Checkout
#Create a function that accepts:
#- Customer name (required)
#- Delivery location (required)
#- Product prices (*args)
#- Additional customer details (**kwargs)
#Calculate the total product cost and display all customer details.

def shopping(name,location,*prices,**details):
    total=0
    for i in prices:
        total=total+i
    print("\nONLINE SHOPPING DETAILS")
    print("CUSTOMER NAME:",name)
    print("DELIVERY LOCATION:",location)
    print("\nPRODUCT DETAILS")
    for key,value in details.items():
        print(key,":",value)
    print("\nTOTAL PRODUCT COST:",total)
name=input("ENTER CUSTOMER NAME:")
location=input("ENTER DELIVERY LOCATION:")
n=int(input("ENTER NUMBER OF PRODUCTS:"))
prices=list()
for i in range(n):
    price=int(input("ENTER PRODUCT PRICE:"))
    prices.append(price)
m=int(input("ENTER NUMBER OF CUSTOMER DETAILS:"))
details=list()
for i in range(m):
    key=input("ENTER DETAIL NAME:")
    value=input("ENTER DETAIL VALUE:")
    details.append((key,value))
shopping(name,location,*prices,**dict(details))