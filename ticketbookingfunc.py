# 6. Ticket Booking
# Create a function book_ticket() that accepts:
# - Passenger name (required)
# - Destination (required)
# - Number of tickets (default value: 1)
#   Display the booking details.

n = int(input("ENTER THE NUMBER OF PASSENGER: "))
def ticketbooking(passname,destination,numofticket=1):
    print("\nPASSENGER",i,"DETAILS ARE:")
    print("NAME:",passname)
    print("DESTINATION :",destination)
    print("NUMBER OF TICKET HOLD :",numofticket)
for i in range(1,n+1):
    print("\nPASSENGER",i,"DETAILS")
    passname=input("ENTER THE NAME OF PASSENGER : ")
    destination=input("ENTER THE DESTINATION OF PASSENGER : ")
    ticketbooking(passname,destination)