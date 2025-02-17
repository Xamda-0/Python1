import os
import csv
import pandas as pd

def UsersAdd():
    fileNameUser = 'User_Info.csv'
    file_exists = os.path.isfile(fileNameUser)

    # Ku fur faylka habka "append mode" oo ku dar header haddii aanu jirin
    with open(fileNameUser, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Haddii faylku aanu jirin, qor header-ka si loo kala hago
        if not file_exists:
            writer.writerow([
                "Full_Name",
                'Number',
                'Username',
                'Password',
                'User_Numbers',
            ])

        # Gelinta xogta isticmaalaha
        while True:
            print('Please write his/her name.')
            Full_name = input(">> Full name: ").strip()
            Number = input(">> Number: ").strip()
            Username = input(">> Username: ").strip()
            Password = input(">> Password: ").strip()
            Users = input(">> User_Number: ").strip()

            if len(Number) in [9, 10] and len(Password) == 8 and Password.isalnum():
                print(f"Welcome to the team {Username}")
                writer.writerow([Full_name, Number, Username, Password, Users])
                print('Data has been saved successfully!.')
                jawaab = input("Ma rabtaa inaad xog kale geliso? (Haa/Haa ma ahan): ").lower()
                if jawaab != 'haa':
                    print("Faylka waa la xiray. Mahadsanid!")
                    break
            else:
                print("Please complete User's information!")

# UsersAdd()
def RemoveUser():
    Username = input(">> Username: ")
    Password = input(">> Password: ")
    print(f"Ma hubtaa in aad delete gareeyso {Username} \n1. Haa \n2. Maya")
    choiceRem = input(">> ")
    if choiceRem == '1':
        file_path = "User_Info.csv" 
        data = pd.read_csv(file_path)
        
        # Filter out the user with the given username
        data = data[data['Username'] != Username]
        data = data[data['Password'] != Password]
        
        print('You deleted successfully!')
        data.to_csv("User_Info.csv", index=False)
        print("Safka waa la saaray, xogta cusub waa la keydiyey.")
    elif choiceRem == '2':
        print('Mahadsanid')
    else:
        print('something wrong please try again!')

# RemoveUser()