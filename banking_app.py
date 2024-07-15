# This is my python banking app
import datetime

# Set a date variable for posting transactions 
today = str(datetime.datetime.now())

class Bank:
    
    ##########################################
    ##########################################
    #### Define functions for calculation ####
    ##########################################
    ##########################################

    # Define initial balance amount
    def __init__(self, initial_amount = 0.00):
        self.balance = initial_amount
        
    # Define withdraw calculation to subtract amount entered from the current balance
    def withdraw(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        self.balance = self.balance - amount
        self.log_transaction(f"-Withdrew ${amount}")
    
    # Define deposit calculation to add amount entered to the current balance
    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        self.balance = self.balance + amount
        self.log_transaction(f"+Deposited ${amount}")
        
    def log_transaction(self, transaction_str):
        with open('transactions.txt', 'a') as file:
            file.write(f"On {today} \n {transaction_str} \t\t\t\t Current balance: ${self.balance}\n")
        
    ###############################
    ###############################
    #### End defined functions ####
    ###############################
    ###############################

# Activate class
account = Bank()    
    
while True:
    try:
        # Initial greeting
        print("Welcome! \nPlease select one of the following options:")

        # Create a list of options to choose from
        list_options = ["1-Check balance","2-Deposit","3-Withdraw"]

        # Show each option
        for o in list_options:
            print(o)
            
        # User must make a selection
        choose = int(input("Please choose a number that corresponds with the action you want to take: "))

        cb = 0 # check balance
        d = 0 # deposit
        w = 0 # withdraw
    except KeyboardInterrupt:
        print("Leaving ATM")
        break
            
        ###############################################
        ##### Add logic based on user choice input ####
        ###############################################

    # If user choses to view current balance, show current balance
    if choose == 1:
            cb = str(account.balance)
            print("You're current balance is $" + cb)


    # If user choses to deposit, call the deposit function and print transaction to txt file
    # and update current balance in the account_balance txt file
    elif choose == 2:
            d = int(input("Please enter the amount you wish to deposit: $"))
            account.deposit(d)
            print("Successfully deposited $" + str(d) + "\nYour current balance is $" + str(account.balance) +"\n")
            
    # If user choses to withdraw, call the withdraw function and print transaction to txt file
    # and update current balance in the account_balance txt file
    elif choose == 3:
        w = int(input("Please enter the amount you wish to withdraw: $"))
        account.withdraw(w)
        if account.balance < w:
            print("You do not have sufficient funds to process this transaction. Please enter a different amount")
            w
        else:
            print("$" + str(w) + " has been withdrawn from your account. Your current balance is $" + str(account.balance))
    
    else:
        print("That is not a valid action")
    ##############################################
    ################ End logic  ##################
    ##############################################    