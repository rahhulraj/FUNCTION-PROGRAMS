#21. Event Registration
#Create a function that accepts an event name and any number of participant details using keyword arguments.
#Display all registered details.

def event(eventname,**details):
    print("\nEVENT REGISTRATION")
    print("EVENT NAME:",eventname)
    for key,value in details.items():
        print(key,":",value)
eventname=input("ENTER THE EVENT NAME:")
n=int(input("ENTER THE NUMBER OF DETAILS:"))
details=list()
for i in range(n):
    key=input("ENTER THE DETAIL NAME:")
    value=input("ENTER THE DETAIL VALUE:")
    details.append((key,value))
event(eventname,**dict(details))