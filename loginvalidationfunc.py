#5. Login Validation
#Create a function that accepts a username and password. Display "Login Successful" 
# if both match the predefined credentials; otherwise display "Invalid Login".

def login(username, password):
    correct_username = "unknown"
    correct_password = "12345678"
    if username==correct_username and password==correct_password:
        print("Login Successful")
    else:
        print("Invalid Login")
username=input("ENTER USERNAME HERE: ")
password=input("ENTER PASSWORD HERE : ")
login(username, password)