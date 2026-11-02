#11. Course Registration
#Create a function that accepts:
#- Student name
#- Course name
#- Duration
#- Fee
#Call the function by passing only keyword arguments.

def course(studentname, coursename, duration, fee):
    print("\nCOURSE DETAILS")
    print("STUDENT NAME:",studentname)
    print("COURSE NAME:",coursename)
    print("DURATION:",duration)
    print("FEE:",fee)
course(studentname="Rahul Raj", coursename="Data Analytics", duration="6 Months", fee=55000)
