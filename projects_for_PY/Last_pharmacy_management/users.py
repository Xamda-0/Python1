import openpyxl
import pandas as pd
# Shaqaalaha lagu diwaan gelinaa
def diiwanka_shaqale():
    workbook = openpyxl.load_workbook('that.xlsx')
    sheet = workbook['workers']
    while True:
        df = pd.read_excel('that.xlsx', sheet_name='workers')
        name = input('>>> Name:- ')
        if name in df['Name'].values:
            print("shaqaalahaan horay ayaa loo diwaan geliyay.")
            break
        else:
            age = int(input('>>> age:-'))
            certificate = input(">>> What kind of certificate you've? :-")
            number = input('>>> your Number:-')
            if len(number) != 9:
                print('sorry this number does not exist.(check it.)')
                exit()
            else:
                pass
            Refrence = input('>>> Refrence:-')
            Refrence_number = input('>>> Refrence number:-')
            if len(Refrence_number) != 9:
                print('sorry this number does not exist.(check it.)')
                exit()
            else:
                pass
            print('your code is zma23')
            sheet.append([name, age, certificate, number, Refrence, Refrence_number,])
            workbook.save('that.xlsx')    
                
            second_around = input('this worker is saved. would U like to do another? \n Yes or No\n:-').lower()
            if second_around != 'Yes':
                print('Job done successfully.')
                exit()
            True
# diiwanka_shaqale()
#  main function ka managerka
def Qeybta_Maamulaha():
    sirta = '1010'
    name = '>> Dr. Xamda Cumar Cali'
    password = input('Fadlan lambarka sirta:- ')
    if password == sirta:
        print(f'Mudane{name}.Soo dhawoow.')
        print("""
    >>> welcome: 
        --> WHAT IS THE JOB TODAY?:

    1. Daawo Ku darid.
    2. Hubin_guud.
    3. diiwanka_shaqale.
    4. waxba...(exit)
    
    """)
    else:
        print('Lama yaqaano cidda aad tahay!')
        exit()
            


# this waa qeybta lagu diiwan gelinayay Bukaanka
def Bukaan_diwan_gelin():
    while True:
        workbook = openpyxl.load_workbook('that.xlsx')
        sheet = workbook['bixiyaha']
        user = input('-->Employee whom saved this info:-')
        code_name = input('-->What is the code?:- ')
        if code_name == 'zma23':
            print('you allowed to fill the form...')
        else:
            print('identify yourself.')
            break
        print('--ask the info of the customer about--')
        name = input('>>>Cus.name:- ')
        age = int(input(">>>Cus.age:- "))
        state = input('>>>Cus.state for male (1), for female(2):- ')
        if state == '1':
            pass
        elif state == '2':
            uur = input('Sister are pregnant... (yes or No) :- ')
            if uur == 'yes':
                print('Sister we recommondan you to see a real Doctor.')
                exit()
            else:
                pass
        else:
            exit()

        his_her_pain = input('>>> you suffering from:- ')
        print('--> his/her medicine is:- ')
        tablet_kind = input('')
        how_many = input('how many tablets:- ')
        sheet.append([user, code_name, name, age, state, his_her_pain, tablet_kind, how_many])
        workbook.save('that.xlsx')
        again = input("-->>Job done successfully. Would U do it agian.\n Haa \n Maya\n:-").lower()

        if again !='Haa':
            print('Mahadsanid')
            break
        True

#  manager ka nas ayaa arki karo xogtaan
def hubin_guud():
    print('''
        1. whole Medicines  
        2. Workers list
        3. what been paid.
        4. Customers been saved.
        ''')
    qeybta = input('which sectin you want to insure:-')
    if qeybta == '1':
        df = pd.read_excel('that.xlsx',sheet_name='medicine')
        print(df)
    elif qeybta == '2':
        df = pd.read_excel('that.xlsx',sheet_name='workers')
        print(df)
    elif qeybta == '3':
        df = pd.read_excel('that.xlsx',sheet_name='bixiyaha')
        print(df)
    elif qeybta == '4':
        df = pd.read_excel('that.xlsx',sheet_name='price')
        print(df)
    else:
        print(f'{qeybta}is not allowed.')

def employee():
    print('welcome to the employee section... ')
    df = pd.read_excel('that.xlsx', sheet_name='workers')
    Name = input('>>> ')
    if Name in df['Name'].values:
        print('Soo dhawoow', Name)
    else:
        print("Laguuma ogola employee section.")
        exit()
# employee()