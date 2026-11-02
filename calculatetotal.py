# Q)Calculate Total Create a function calculate_total() that accepts two numbers and displays their sum, difference,
#  product and division.

def calculate_total(a,b):
        sum=a+b
        return sum
a=int(input("ENTER THE NUMBER 1: "))
b=int(input("ENTER THE NUMBER 2: "))
result=calculate_total(a,b)
print("SUM OF TWO NUMBER IS :",result)