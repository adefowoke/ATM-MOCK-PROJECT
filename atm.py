from datetime import datetime
import getpass
import random

User_Database = {}


def date_time():
    """ function will print the current date in your timezone """
    now = datetime.now().strftime("%B %d %Y, %H:%M:%S")
    print(now)


def generate_account_number():
    """ function will generate 9 random numbers between 1 and 9 """
    return random.randint(111111111, 999999999)


def check_account_balance(user_account_number):
    """
    function will check if the user has made any previous deposit
    if there has been previous deposit, then the length of the user_database
    is extended by 1, so the amount will be at index 5, and return the value
    if nil previous deposit, there is no index 5, so it returns the error.

    """
    try:
        value = User_Database.get(int(user_account_number))[5]
        print(value)
    except IndexError:
        print("You have zero account balance")


def complaint():
    print("Please enter your complaint and we will surely get back to you")


def close_account(user_account_number):
    """
    this gives the user the option of deleting account from the database, if it does
    exist, if not it returns the error message.
    :param user_account_number: the dictionary key to access the user information
    :return:
    """
    user_input = int(input("Are you sure you want to close your account, if yes, please enter 1"))
    if user_input == 1:
        try:
            del User_Database[int(user_account_number)]
            print("We are sorry to see you go")
        except KeyError:
            print("User does not exist")
    else:
        exit()


def withdraw(user_account_number):
    amount = int(input("Enter the amount you want to withdraw"))
    try:
        value = User_Database.get(int(user_account_number))[5]
        sub_value = value - amount
        print(sub_value)
    except IndexError:
        print("You have insufficient funds")


def deposit(account_number):
    amount = int(input("How much would you like to deposit"))
    User_Database[int(account_number)].append(amount)
    print(f"Your current balance is {User_Database[int(account_number)][5]} Naira")


def register():
    """
    registers new user by taking user input and forming a dictionary with the account
    number as key and a list of other information as value.
    :return: the user information as inputed except the account number which is randomly
    generated.

    The bank_transaction then runs giving the user the option to choose from.

    """
    print("Welcome to Zuri Bank, \nkindly follow the instructions to create an account with us")
    first_name = input("\nWhat is your first name? \n").title()
    last_name = input("\nWhat is your last name? \n").title()
    gender = input("Male or Female")
    email_address = input("\nPlease enter your email address")
    password = input("\nPlease enter your password")
    account_number = generate_account_number()
    User_Database[account_number] = [first_name, last_name, email_address, password, gender]
    for key, value in User_Database.items():
        print(f"\nHere are your bank details \naccount number : {key} \nfull name : {value[0]} {value[1]} "
              f"\nemail address : {value[2]} \ngender : {value[4]} \npassword : {value[3]}\n")

    bank_transaction()


def bank_transaction():
    user_account_number = input("Enter account number")
    user_password = getpass.getpass("Enter your password")
    password_len = len(user_password)
    print("*" * password_len)

    if int(user_account_number) in User_Database and user_password == User_Database[int(user_account_number)][3]:
        print("""These are the available options:
                              1. Withdraw
                              2. Cash Deposit
                              3. Complaint
                              4. check account balance
                              5. Close my account 
                              6. Exit""")
        try:
            user_input = int(input("\nselect option"))

            if user_input == 1:
                withdraw(user_account_number)
            elif user_input == 2:
                deposit(user_account_number)
            elif user_input == 3:
                complaint()
            elif user_input == 4:
                check_account_balance(user_account_number)
            elif user_input == 5:
                close_account(user_account_number)
            elif user_input == 6:
                exit()

            else:
                print("Please select the options listed")
        except ValueError:
            print("Please enter a valid number")
            bank_transaction()

    else:
        print("Kindly enter your valid bank details")


def login():
    date_time()
    print("\nWelcome to Zuri Bank \nAre you a registered user, if yes enter 1 , if no enter 2")
    try:
        user_input = int(input())
        if user_input == 1:
            bank_transaction()
        elif user_input == 2:
            register()
        else:
            print("Please enter a valid option")
            login()
    except ValueError:
        print("Please enter a valid number")
        login()


login()
