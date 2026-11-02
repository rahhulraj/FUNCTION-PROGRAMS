#20. Product Information
#Create a function that accepts a product ID and any number of additional product details.
#Example: product name, price, brand, quantity and category.

def product(productid,*details):
    print("\nPRODUCT INFORMATION")
    print("PRODUCT ID:",productid)
    for i in details:
        print(i[0],":",i[1])
productid=input("ENTER THE PRODUCT ID:")
n=int(input("ENTER THE NUMBER OF DETAILS:"))
details=list()
for j in range(n):
    key=input("ENTER THE DETAIL NAME:")
    value=input("ENTER THE DETAIL VALUE:")
    details.append((key,value))
product(productid,*details)