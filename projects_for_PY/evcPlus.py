# # EVCPLUS PROJECT
myMoney = 10
print('EVCPlus Project')
EvcNum = input()
if EvcNum == '*770#':
    print('Fadlan geli PIN-kaaga(Enter PIN)')
    Pin = input()
    if Pin == '1234':
        print("""
1. Itus Haraaga
2. Kaarka hadalka
3. Bixi Biil
4. U wareeji EVCPlus
5. Warbixin kooban
6. Salaam bank
7. Maareynta
8. Bill Payment
""")
    if Pin != '1234':
         print('PIN-ku waa qalad, Fadlan ku celi markale')
         Pin = input()
    itus = input()
    if itus == '1':
        print(f'Haraagaagu waa ${myMoney}.')
    wareejin = input()
    if wareejin == '4':
            print('Fadlan geli Mobile-ka')
            mobile = input()
            NumHormuud = '611112233'
            if mobile == NumHormuud:
                print('Fadlan geli Lacagta')
                lacag = int(input())
                print(f'Ma hubtaa inaad ${lacag} u warejisid {mobile}')
                print("""
1. Haa
2. Maya
""")
                haa = input()
                if haa == '1':
                    tar = '12/8/2024 4:40:13 PM'
                    haraa = myMoney - lacag
                    print(f'<-EVCPlus-> ${lacag} ayaad u wareejisay {mobile}, Tar: {tar}, Haraagaagu waa ${haraa}')
                else:
                    print('Mahadsanid!')
else:
    print('Something is wrong try again!')
                    

    