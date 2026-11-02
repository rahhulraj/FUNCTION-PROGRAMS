#25. Global and Local Variables
#Create a global variable x = 100.
#Inside a function, create another variable named x = 50.
#Print the value of x inside and outside the function.
#Explain why the values are different.

x=100
def sample():
    x=50
    print("INSIDE FUNCTION:",x)
sample()
print("OUTSIDE FUNCTION:",x)