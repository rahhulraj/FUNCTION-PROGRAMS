#17. Attendance Percentage
#Create a function that accepts a student name and attendance values for any number of working days (1 for present and 0 for absent).
#Calculate the attendance percentage


n=int(input("ENTER THE NUMBER OF DAYS :"))
def attendance(name,*days):
    present=0
    total=0
    for i in days:
        if i==1:
            present=present+1
        total=total+1
    percentage=(present/total)*100
    print("\nATTENDANCE DETAILS")
    print("STUDENT NAME:",name)
    print("TOTAL WORKING DAYS:",total)
    print("PRESENT DAYS:",present)
    print("ATTENDANCE PERCENTAGE:",percentage,"%")

name=str(input("ENTER THE NAME :"))
days=list()
for j in range(n):
    day=int(input("ENTER THE STATUS :"))
    days.append(day)
attendance(name,*days)