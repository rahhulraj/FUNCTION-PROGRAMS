#27. Employee Payroll System
#Create a function that accepts employee name, basic salary and any number of additional allowances using **kwargs.
#Calculate the total salary by adding all allowances to the basic salary.

def employee(name,basic,**allowances):
    total=basic
    print("\nEMPLOYEE PAYROLL")
    print("EMPLOYEE NAME:",name)
    print("BASIC SALARY:",basic)
    for key,value in allowances.items():
        print(key,":",value)
        total=total+value
    print("TOTAL SALARY:",total)
name=input("ENTER EMPLOYEE NAME:")
basic=int(input("ENTER BASIC SALARY:"))
n=int(input("ENTER NUMBER OF ALLOWANCES:"))
allowances=list()
for i in range(n):
    key=input("ENTER ALLOWANCE NAME:")
    value=int(input("ENTER ALLOWANCE AMOUNT:"))
    allowances.append((key,value))
employee(name,basic,**dict(allowances))