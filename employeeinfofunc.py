#19. Employee Information
#Create a function that accepts an employee ID and any number of keyword details.
#Example details:
#- Name
#- Department
#- Salary
#- Experience
#- Designation
#Display all the information.

def employee(empid,*details):
    print("\nEMPLOYEE INFORMATION")
    print("EMPLOYEE ID:",empid)
    for i in details:
        print(i[0],":",i[1])
empid=input("ENTER THE EMPLOYEE ID:")
n=int(input("ENTER THE NUMBER OF DETAILS:"))
details=list()
for j in range(n):
    key=input("ENTER THE DETAIL NAME:")
    value=input("ENTER THE DETAIL VALUE:")
    details.append((key,value))
employee(empid,*details)