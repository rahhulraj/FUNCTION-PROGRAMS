#18. Student Profile
#Create a function that accepts a student's name and any number of additional details such as age, course, college, location and phone number.
#Display all the details.

def student(name,*details):
    print("\nSTUDENT PROFILE")
    print("STUDENT NAME:",name)
    for i in details:
        print(i[0],":",i[1])
name=input("ENTER THE STUDENT NAME:")
n=int(input("ENTER THE NUMBER OF DETAILS:"))
details=list()
for j in range(n):
    key=input("ENTER THE DETAIL NAME:")
    value=input("ENTER THE DETAIL VALUE:")
    details.append((key,value))
student(name,*details)