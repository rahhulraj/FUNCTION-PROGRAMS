#29. Library Fine Calculator
#Create a global variable fine_per_day = 5.
#Create a function that accepts:
#- Student name
#- Number of late days (required)
#- Membership type (default: Normal)
#Calculate the fine. If the membership type is Premium, apply a 50% discount to the fine.

fine_per_day=5
def library(name,days,membership="Normal"):
    global fine_per_day
    fine=days*fine_per_day
    if membership=="Premium":
        fine=fine-(fine*50/100)
    print("\nLIBRARY FINE DETAILS")
    print("STUDENT NAME:",name)
    print("LATE DAYS:",days)
    print("MEMBERSHIP:",membership)
    print("FINE PER DAY:",fine_per_day)
    print("TOTAL FINE:",fine)
name=input("ENTER STUDENT NAME:")
days=int(input("ENTER NUMBER OF LATE DAYS:"))
membership=input("ENTER MEMBERSHIP (PRESS ENTER FOR NORMAL):")
if membership=="":
    library(name,days)
else:
    library(name,days,membership)