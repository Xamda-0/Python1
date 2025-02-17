import users
import openpyxl
import pandas as pd

# file='that.xlsx'
print("................................................................")
print("-Welcome to the Pharmacy Managment System-")
print("................................................................")
print('this system helps manage medicine, tracks sales, and handle information\n')

Options ='''
    --> WHAT IS THE JOB TODAY?:

    1. Diwaan gelin Bukaan.
    2. daawo la bixiyey iyo qiimaheeda.
    3. Daawo Raadin.
    '''
# daawo ayaa lagu daraa
def Add_daawo():
    while True:
        df = pd.read_excel('that.xlsx')
        Daawo = input('Medicine name:- ')
        if Daawo in df['Medicine Name'].values:
            print('Waa ay taal, daawadaan.')
            break
        else:
            workbook = openpyxl.load_workbook('that.xlsx')
            sheet = workbook['medicine']
            Nooca = input('Type of the medicine:- ')
            Qiimaha_dawada = float(input('price USD $ '))
            how_many = int(input('How many:- '))
            sheet.append([Daawo, Nooca, Qiimaha_dawada, how_many])
            workbook.save('that.xlsx')
            again = input('Dawadan waa la diiwaan geliyey.\n Dawo kale miyaa la diwaan gilinaa? (Haa ama Maya):- ')

            if again=='Haa':
                True
            else:
                print('Mahadsanid')
                break

#  qeybta bilawga ......
def mainFunction():
    isticmale = input('>>> Who are you?\n >>> I am :-\n 1. Manager\n \
2. Employee \n(use Numbers plz):-')
    if isticmale == '1':
        users.Qeybta_Maamulaha()
        select = input('(use numbers):-')
        #  daawo ku darid
        if select == '1':
                Add_daawo()

        #  in aad arki kartid inta daawo taaalo oo idil.
        elif select == '2':
            users.hubin_guud()
        # In Shaqaale lagusoo daro
        elif select == '3':
                users.diiwanka_shaqale()
            
            # waa ka bixid
        elif select == '4':
            print('Waad mahadsantahay. (Here we are always if you need us.)')
            exit()
        else:
            print('This section does not identify yet.')
    #  shaqaalaha ayaa bukaanka diwaan gelinaayo
    elif isticmale == '2':
        users.employee()
        print(Options)
        
        #  diiwan gilinta Bukaan
        dooro = input('choose the job:- ')
        if dooro == '1':
            users.Bukaan_diwan_gelin()

    # daawo labixiyey  iyo qiimaha lagu iibiyey.
        elif dooro == '2':
            while True:
                workbook = openpyxl.load_workbook('that.xlsx')
                sheet = workbook['price']
                tablet_name = input('-->Daawada la iibiye magaceda:- ')
                immisa = int(input('--> Immisa xabo:- '))
                price = float(input('-->  Qiimaha :- '))
                multi = immisa*price
                print(multi)
                sheet.append([tablet_name, price, multi])
                workbook.save('that.xlsx')
                again = input('-->Dawadaani waa la qoray, mid kale miyaa la qoraa? (Haa ama Maya) :-').lower()
                if again != 'Haa':
                    print('---------')
                    print('Mahadsanid')
                    print('---------')
                    break
                True

        #  daawo ayaa lagu raaadiye hadii ay talo ama in ay dhamty
        elif dooro == '3':
            df = pd.read_excel('that.xlsx')
            raadi_daawo = input('>>> ')
            if raadi_daawo in df['Medicine Name'].values:
                print('Wey taaala.')
            else:
                print("Wey go'day.")
        else:
            print('This section does not identify yet.')
    else:
        print('This section is not accessed Thank you!')
mainFunction()