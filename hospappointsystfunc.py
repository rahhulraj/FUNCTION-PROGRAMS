#30. Hospital Appointment System
#Create a function that accepts:
#- Patient name (required)
#- Doctor name (required)
#- Consultation fee (default: 500)
#- Any number of additional patient details (**kwargs)
#Display the appointment information and calculate the consultation fee.

def hospital(patient,doctor,fee=500,**details):
    print("\nHOSPITAL APPOINTMENT DETAILS")
    print("PATIENT NAME:",patient)
    print("DOCTOR NAME:",doctor)
    print("CONSULTATION FEE:",fee)
    print("\nPATIENT ADDITIONAL DETAILS")
    for key,value in details.items():
        print(key,":",value)
patient=input("ENTER PATIENT NAME:")
doctor=input("ENTER DOCTOR NAME:")
fee=int(input("ENTER CONSULTATION FEE (PRESS ENTER FOR 500):") or 500)
n=int(input("ENTER NUMBER OF ADDITIONAL DETAILS:"))
details=list()
for i in range(n):
    key=input("ENTER DETAIL NAME:")
    value=input("ENTER DETAIL VALUE:")
    details.append((key,value))
hospital(patient,doctor,fee,**dict(details))