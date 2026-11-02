#9. Product Discount
# Create a function that accepts product name, price and discount percentage. Set the default discount percentage to 10%.
# Calculate the final price after discount.

def product_discount(productname,price,discount=10):
    discount_amount=(price*discount)/100
    final_price=price-discount_amount
    print("\nPRODUCT DETAILS")
    print("PRODUCT NAME:",productname)
    print("ORIGINAL PRICE: ₹",price)
    print("DISCOUNT:",discount,"%")
    print("DISCOUNT AMOUNT: ₹",discount_amount)
    print("FINAL PRICE: ₹",final_price)
productname=input("ENTER PRODUCT NAME: ")
price=float(input("ENTER PRODUCT PRICE: "))
product_discount(productname, price)