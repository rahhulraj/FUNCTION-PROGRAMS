#16. Movie Ticket Collection
#Create a function that accepts any number of ticket prices and calculates the total collection.

n=int(input("ENTER THE NUMBER OF TICKET :"))
def movie(*ticketprice):
    total=0
    for i in ticketprice:
        total=total+i
    print("\nMOVIE TICKET COLLECTION")
    print("TOTAL COLLECTION:",total)
prices=list()
for j in range(n):
    price=int(input("ENTER THE TICKET PRICE :"))
    prices.append(price)
movie(*prices)