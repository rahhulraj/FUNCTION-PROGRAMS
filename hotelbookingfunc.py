#12. Hotel Booking
#Create a function that accepts customer name, room type, number of days and number of guests.
#Call the function using a combination of positional and keyword arguments.\

def hotel(customername, roomtype, days, guests):
    print("\nHOTEL BOOKING DETAILS")
    print("CUSTOMER NAME:",customername)
    print("ROOM TYPE:",roomtype)
    print("NUMBER OF DAYS:",days)
    print("NUMBER OF GUESTS:",guests)
hotel("Rahul Raj","SHARING",days=3,guests=2)