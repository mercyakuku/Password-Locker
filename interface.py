#/usr/bin/env python3.6
from passcode import User, Credentials


def create_new_user(username,password):
    
    # Function to create a new user with a username and password
    
    new_user = User(username,password)
    return new_user

def save_user(user):
    
    # Function to save a new user
    
    user.save_user()

def display_user():
    
    # Function to display existing user
    
    return User.display_user()

def login_user(username,password):
    
    # Function that checks whether a user exists and then login the user in.
    
    check_user = Credentials.verify_user(username,password)
    return check_user

def create_new_credential(account,userName,password):
    
    # Function that creates new credentials for a given user account
    
    new_credential = Credentials(account,userName,password)
    return new_credential

def save_credentials(credentials):
    
    # Function to save Credentials to the credentials list
    
    credentials. save_details()

def display_accounts_details():
    
    # Function that displays all the saved credentials.

    return Credentials.display_credentials()

def delete_credential(credentials):
    
    # Function to delete Credentials from credentials list

    credentials.delete_credentials()

def find_credential(account):
    
    # Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    
    return Credentials.find_credential(account)

def check_credendtials(account):
    
    # Function that check if Credentials exists with that account name and return true or false

    return Credentials.if_credential_exist(account)

def generate_Password():
    
    # Function that generates a random password for the user.

    auto_password=Credentials.generatePassword()
    return auto_password

def copy_password(account):
    
    # Function that copies the password using the pyperclip framework;
    # We import the framework then declare a function that copies the emails.

    return Credentials.copy_password(account)


def passwordlocker():
    print("Hello Welcome to your Password Locker Account. \n Please enter one of the following to proceed.\n CNA - For (Create a New Account)  \n HAN - For (Having An Account?)  \n")
    short_code=input("").lower().strip()
    if short_code == "cna":
        print("Sign Up")
        print('*' * 50)
        username = input("User_name: ")
        while True:
            print(" TOP - Type your own pasword:\n GRP - Generate random Password")
            password_Choice = input().lower().strip()
            if password_Choice == 'top':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'grp':
                password = generate_Password()
                break
            else:
                print("Invalid password please try again")
        save_user(create_new_user(username,password))
        print("*"*85)
        print(f"Hello {username}, Your account has been succesfully created! Here is your Password: {password}")
        print("*"*85)
    elif short_code == "han":
        print("*"*50)
        print("Enter your Username and your Password to log in:")
        print('*' * 50)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username}.Welcome To PassWord Locker Manager")  
            print('\n')
    while True:
        print("Use these short codes to proceed:\n CNC - For (Create a New Credential) \n DC - For (Display Credentials) \n FAC - For (Find A Credential) \n GRP - For (Generate a Randomn Password) \n DC - For (Delete Credential) \n EX - For (Exit Application) \n")
        short_code = input().lower().strip()
        if short_code == "cnc":
            print("Create New Credential")
            print("."*20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(" TOP - To type your own pasword if you already have an account:\n GRP - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'top':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice == 'grp':
                    password = generate_Password()
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_new_credential(account,userName,password))
            print('\n')
            print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully")
            print('\n')
        elif short_code == "dc":
            if display_accounts_details():
                print("Here is your list of accounts: ")
                 
                print('*' * 30)
                print('_'* 30)
                for account in display_accounts_details():
                    print(f" Account:{account.account} \n UserName:{username}\n Password:{password}")
                    print('_'* 30)
                print('*' * 30)
            else:
                print("You don't have any credentials saved yet.")
        elif short_code == "fac":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 50)
                print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
                print('-' * 50)
            else:
                print("This Credential does not exist")
                print('\n')
        elif short_code == "dc":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account} has been successfully deleted!")
                print('\n')
            else:
                print("The Credential you want to delete does not exist in your account yet")

        elif short_code == 'grp':

            password = generate_Password()
            print(f" {password} Your password has been generated succesfully. You can proceed to use it in your account")
        elif short_code == 'ex':
            print("Thanks for using PassWord Locker Manager. Welcome again and see you more often!!!!")
            break
        else:
            print("Wrong entry... Check your entry again and let it match those in the menu")


if __name__ == '__main__':
    passwordlocker()