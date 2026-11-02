#3. Employee Salary
# Create a function that accepts an employee's basic salary and calculates:
# - HRA = 20% of basic salary
# - DA = 10% of basic salary
# - Total salary = Basic + HRA + DA

def employeesalary(BS):
        HRA=(BS*20)/100
        DA=(BS*10)/100
        total_salary=BS+HRA+DA
        return total_salary
BS=int(input("ENTER THE BASIC SALARY: "))
result=employeesalary(BS)
print("TOTAL SALARY OF EMPLOYEE IS :",result)