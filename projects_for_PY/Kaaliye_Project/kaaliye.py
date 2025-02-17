# Kaaliye projects
Mynum = 252611223344

pdf_hard = '1. Pdf \n2. Hard'
hubid = '1. Haa \n2. Maya'
pdf = ' Pdf '
hubid2 = '1. Haa \n2. Maya'



# function of appointments
def ballan(itemsDict, leftWidth, rightWidth):
    print('Ballanta'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

Ballanta = {'Place': 'Compass 3', 'room': '4', 'Day': 'Axad', 'Tar': '23/01/2025', 'Time': '11:40 AM'}

# funcion of options if it is pdf or hard 
def hard_pdf():
    nooc_buugga = input('>>> ')
    if nooc_buugga == '1':
        print('Fadlan noogu soo dir', Mynum)
    elif nooc_buugga == '2':
        print('Plese write your information.')
        name = input('>>> Name: ')
        Id = input('>>> ID: ')
        num = input('>>> Number: ')
        Class = input('>>> Class: ')
        if len(num) not in [10,9]:
            print('Please complete your number.')
        
        else:
            print('Ma hubtaa in ay saxan tahay.')
            print(f'Magacaaga waa:{name} \nId-gaaga waa: {Id}  \nNumber-kaaga waa: {num} \nFasalkaaga waa: {Class}')  
            print(hubid)
            hubinta_xogta = input('>>> ')
            if hubinta_xogta == '1':
                ballan(Ballanta, 20, 18)
                print('Mahadsanid')
            else:
                print('Mahadsanid')

# function of scientific subjects
def scientific_subj():
    print("""
1. Math
2. Physics
3. Biology
4. Chemistry
""")
    choice_subj =  input('>>> ')
    if choice_subj in ['1', '2','3','4']:
        print(pdf_hard)
        hard_pdf()
    else:
        print('Something Wrong Please try again!')
# founction of languages
def language_subj():
    subj_list = """1. Somali \n2. Carabi\n3. English"""
    print(subj_list)
    choice_subj =  input('>>> ')
    if choice_subj in ['1', '2','3']:
        print(pdf_hard)
        hard_pdf()
    else:
        print('Something Wrong Please try again!')
# function ii haayso maadddooyinka soo haray.
def Other_subj():

    print("""
1. Conflict resolution
2. A. writing & Critical thinking
3. Islamic
4. Introduction of Computer


""")
    choice_subj =  input('>>> ')
    if choice_subj in ['1', '2','3','4']:
        print(pdf_hard)
        hard_pdf()
    else:
        print('Something Wrong Please try again!')
# main fuction of foundation books
def SNU_FOUND():
    print("""
1. Scientific Subjects
2. Languages
3. Others
""")
    found_dooro_subj = input('>>> ')
    if found_dooro_subj == '1':
        scientific_subj()
    elif found_dooro_subj == '2':
        language_subj()
    elif found_dooro_subj == '3':
        Other_subj()
    else:
        print('Something Wrong Please try again!')

# semester one 'other functions'
def semester_others():
    semester_other_books = """
1. English
2. Calculus
3. Physics
"""
    print(semester_other_books)
    option_other_User = input('>>> ')
    if option_other_User in ['1','2','3']:
        print(pdf_hard)
        hard_pdf()
    else:
        print('Something wrong please try again!')
#  main function of semester 1 
def Semester_One_Books():
    semester_books = """
1. Programming Languages (Python1)
2. Computer Applications
3. Introduction to Computer Science
4. Others
"""
    print(semester_books)
    semester_option_user = input('>>> ')
    if semester_option_user  in ['1','2','3']:
        print(pdf_hard)
        hard_pdf()
    elif semester_option_user == '4':
        semester_others()
    else:
        print('something wrong please try again!')

        
# main function of SNU books
def SNU_BOOKS():
    print("1. Foundation Books \n2. Semester 1 Books")
    found_dooro_subj = input('>>> ')
    if found_dooro_subj == '1':
        SNU_FOUND()
    elif found_dooro_subj == '2':
        Semester_One_Books()
    else:
        print('Something Wrong Please try again!')
    
    
   

# Personal development books
def develop_books():
    dev_options_user = input('>>> ')
    if dev_options_user in ['1', '2','3','4','5','6']:
        print(f'Personal development books are all {pdf}. So did you want?')
        print(hubid2)
        hubis = input('>>> ')
        if hubis == '1':
            print('Plese write your number.')
            num = input('>>> Number: ')
            if len(num) not in [10,9]:
                print('Please complete your number.')
            else:
                print('We will send you ASAP.')
        
        else:
            print('Mahadsanid')
    else:
        print('Something wrong please try again!')
    
# main function of personal development
def Personal_Dev_books():
    dev_books = """
1. Yaa Qaatay burcadkaygii
2. TARBIYAYNTA NAFTA
3. The ART of lazzines
4. Dhambaallada qur'aanka
5. Daawada Murugada
6. Waa Ku Salaamay Saaxiib
"""
    print(dev_books)
    develop_books()

# Random time table 


# Main function of Kaaliye Projects
def allFunction():
    Options = """
1. SNU books
2. Personal Development books
3. Random time table
"""
    print(Options)
    found_dooro_subj = input('>>> ')
    if found_dooro_subj == '1':
        SNU_BOOKS()
    elif found_dooro_subj == '2':
        Personal_Dev_books()
    else:
        print('Something wrong please try again!')
    #   if Options == '1':
    #         pass
allFunction()

