# 10. Employee Registration
# Create a function that accepts employee name, age, department and salary.
# Call the function using keyword arguments in a different order.
def employee(name,age,department,salary):
    print("\nEMPLOYEE DETAILS")
    print("NAME:",name)
    print("AGE:",age)
    print("DEPARTMENT:",department)
    print("SALARY:",salary)
employee(salary=25000,department="IT",name="Rahul Raj",age=22)