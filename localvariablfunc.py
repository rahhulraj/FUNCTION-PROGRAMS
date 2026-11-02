#24. Local Variable Practice
#Create a function that declares a variable message = "Welcome to Python".
#Print the message inside the function.
#Try accessing the same variable outside the function. Observe the result.

def message():
    message="Welcome to Python"
    print("INSIDE FUNCTION:",message)
message()
print("OUTSIDE FUNCTION:",message)