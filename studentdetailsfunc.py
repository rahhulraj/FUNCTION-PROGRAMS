n = int(input("ENTER THE NUMBER OF STUDENTS: "))
def student_details():
    for i in range(1,n+1):
        print("\nSTUDENT",i,"DETAILS")
        name=input("ENTER THE NAME OF STUDENT: ")
        age=input("ENTER THE AGE OF STUDENT: ")
        course=input("ENTER THE COURSE OF STUDENT: ")

        print("\nSTUDENT",i,"DETAILS ARE:")
        print("NAME:",name)
        print("AGE:",age)
        print("COURSE:",course)

student_details()