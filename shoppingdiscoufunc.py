#23. Shopping Discount
#Create a global variable discount = 15.
#Create a function that accepts the product price and calculates the discounted price using the global discount variable.
discount=15
def shopping(price):
    finalprice=price-(price*discount/100)
    print("PRODUCT PRICE:",price)
    print("DISCOUNT:",discount,"%")
    print("FINAL PRICE:",finalprice)
price=int(input("ENTER THE PRODUCT PRICE:"))
shopping(price)