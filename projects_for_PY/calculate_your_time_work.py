
empolyees = 0
mult = 1

while empolyees < 3:
     money = int(input( ' enter the money: '))
     time = int(input( ' enter the time: '))
     empolyees += 1
     mult = money * time
     print( " empolyers", empolyees, "gets $", mult)
     again = 'y'
     again = input(' markale ma ubaahan tahay? ')
