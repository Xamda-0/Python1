
accountDict = {'111111': 'Faarax Somali', '222222': 'Farhia Somali' , '333333': 'Xaliima Somali'}
def SalaamBank():
    print("1. Ka Wareeji EVCPlus")
    wareeji = input(">>> ")
    if wareeji == '1':
        print('Fadlan dooro xisaabta Bangiga')
        print("""
            1. SALAAM SOMALI BANK
            2. Salaam Sch
            3. Bank Beeraha
            4. Darasalaam Bank
            5. MyBank LTD
            """)
        BankOption = input('>>> ')
        if BankOption == '1':
            print(" Fadlan Geli Account-ka")
            account = input('>>> ')
            if account not in accountDict.keys():
                print("please try again")
                print(" Fadlan Geli Macluumaad")
                maclumad = input('>>> ')
        else:
            print(" Something is wrong please try again")

# SalaamBank()