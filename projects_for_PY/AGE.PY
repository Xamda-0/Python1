age = int(input('Enter your age: '))
if age <= 13:
    print('too young')
elif age <= 25:
    print('you are a boy')
elif age <= 50:
    print('you are a man')
else:
    print('you are adult')
