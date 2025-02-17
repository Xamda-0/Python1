from Table_of_Stock import StockTable
from Customer_information import Customer_Diwaan
import Users_Info
import pandas as pd

def Users_gelid():
    # print('Which user you are? \n1. User1 \n2. User2')
    # optionUser = input(">> ")
    # if optionUser :
        print('>> Enter your Password and Username')
        username = input(">> Username ")
        password = input(">> Password ")
        file_path = 'User_Info.csv'
        data = pd.read_csv(file_path)

        # Filter out the user with the given username and password
        user = data[(data['Username'] == username) & (data['Password'] == password)]
        if not user.empty:
            print(f"Soo dhawow {username}!")
            Customer_Diwaan()
        else:
            print("Username ama password waa khalad! Fadlan isku day mar kale.")
    # else:
    #     print("something wrong please try again!")

# Users_gelid()

def ManagerFun():
    password = 'Ma4321'
    print("Enter your password")
    ManPass = input(">> ")
    if ManPass != password:
        print("Password-ka waa qalad!")
        return False
    optionsManager = print("""
    1. Table of users
    2. Table of Stock
    3. Customer Information
    """)
    choiceMan = input(">> ")
    if choiceMan == '1':
        print("1. Add user \n2. Remove user")
        choiceUser = input(">> ")
        if choiceUser == '1':
            Users_Info.UsersAdd()
        elif choiceUser == '2':
            Users_Info.RemoveUser()
        else:
            print("something wrong please try again!")
    elif choiceMan == '2':
        StockTable()
    elif choiceMan == '3':
        print("1. Xogta bukaanka. \n2. Diwaangelinta Bukaanka ")
        choiceXogta = input(">> ")
        if choiceXogta == '1':
            filname = "CustomerInformation.csv"
            data =pd.read_csv(filname)
            print(data)
        elif choiceXogta == '2':
            Customer_Diwaan()
        else:
            print("something wrong please try again!")
    elif choiceMan == '4':
        pass
    else:
        print('Something wrong please try again!')

def Main():
    print("Welcome to the Group 3 Pharmacy.")
    print("Who are you?")
    optionSystem = """
    1. Manager
    2. Users
    3. Exit
    """
    print(optionSystem)
    optionMain = input(">> ")
    if optionMain == '1':
        ManagerFun()
    elif optionMain == '2':
        Users_gelid()
    elif optionMain == '3':
        exit()
    else:
        print('Something wrong please try again!')

Main()