#14. Student Marks
#Create a function that accepts a student's name and marks in any number of subjects.
#Calculate and display:
#- Total marks
#- Number of subjects
#- Average marks
n=int(input("ENTER THE NUMBER SUBJECT :"))
def student(name,*marks):
    total=0
    for i in marks:
        total=total+i
    average=total/n
    print("\nSTUDENT DETAILS")
    print("NAME:",name)
    print("TOTAL MARKS:",total)
    print("NUMBER OF SUBJECTS:",n)
    print("AVERAGE MARKS:",average)

name=str(input("ENTER THE STUDENT NAME :"))
marks=list()
for j in range(n):
    mark=int(input("ENTER THE MARK :"))
    marks.append(mark)
student(name,*marks)