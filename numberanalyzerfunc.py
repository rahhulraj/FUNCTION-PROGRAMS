#15. Number Analyzer
#Create a function that accepts any number of integers and displays:
#- Largest number
#- Smallest number
#- Sum of all numbers

n=int(input("ENTER THE TOTAL NUMBERS: "))
def number(*num):
    total=0
    for i in num:
        total=total + i
        smallest=min(num)
        largest=max(num)
    print("\nNUMBER ANALYSIS")
    print("LARGEST NUMBER:",largest)
    print("SMALLEST NUMBER:",smallest)
    print("SUM:",total)
numbers=list()
for j in range(n):
    num=int(input("ENTER THE NUMBER: "))
    numbers.append(num)
number(*numbers)