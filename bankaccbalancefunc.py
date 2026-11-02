#Part 6 – Local and global variables
#22. Bank Account Balance
#Create a global variable balance = 5000.
#Create a function deposit() that accepts an amount and updates the global balance.
#Display the updated balance.

balance=5000
def deposit(amount):
    global balance
    balance=balance+amount
    print("UPDATED BALANCE:",balance)
amount=int(input("ENTER THE DEPOSIT AMOUNT:"))
deposit(amount)

