# dictionaries
# myCat = {'color':'gray','size':'chuppy','name':'kalia'}
# print(myCat['name'])
# print(f'my cat name is {myCat["name"]}')
# spam = {1234: 'luggage',42: 'is a answer'}
# print(spam[42])
# lists vs dictionary
# myList = ['name:', 'xamda','age:','20','job:','student']
# myList2 = ['age:','20','job:','student','name:', 'xamda'] # false
# mydict = {'name': 'xamda','age':'20','job':'student'}
# mydict2 = {'age':'20','job':'student','name': 'xamda'} #true
# print(myList == myList2)
# print(mydict == mydict2)
# # birthday project
# birthdays = {'Xamda': 'march 1', 'Deeqa': 'may 4', 'Iqro': 'dec 30'}
# while True:
#     print('enter your name (blank to quit)')
#     name = input()
#     if name == '':
#      break
#     if name in birthdays:
#      print(f'{birthdays[name]} is the birthday of {name}')
#     else:
#      print('idon\'t birthday iformation of '+ name)
#      print('what\'s their birthday')
#      bday = input()
#      birthdays == bday
#      print('birthdays database updated.')
# tusaale = {'name': 'xamda', 'age': 20}
# for k in tusaale.keys():
#     print(k)
# for v in tusaale.values():
#     print(v)
# for i in tusaale.items():
#     print(i)
# tusaale = {'name': 'xamda', 'age': 20}
# print(tusaale.keys())
# print(list(tusaale.keys()))
# for k,v in tusaale.items():
#     print(f'keys is: {k} and value is: {str(v)} ')
# checking keys if is exists or not
# print('nam' in tusaale.keys())
# print('name' in tusaale.keys())
# get() method
# picnicItems = {'apple': 3,'icecream':20, 'sanbuusa': 25}
# print('i\'m bringing ' +str(picnicItems.get('apple', 0)) + ' apples')
# print('i\'m bringing ' +str(picnicItems.get('mango juice',15 )) + ' mango juice')
# spam = {'name': 'Pooka', 'age': 5}
# if 'color' not in spam:
#     spam['color'] = 'black'
#     print(spam)
# print(spam.setdefault('color','black')) #if it's not exists it will add
# print(spam.setdefault('color','blue')) # if exists do n't changed
# import pprint
# message = 'It was a bright cold day in April.'
# count = {}
# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
# # pprint.pprint(count)
# print(pprint.pformat(count))

 # inventory.py
# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# def displayInventory(inventory):
#     print("Inventory:")
#     item_total = 0
#     for k, v in inventory.items():
#         print(str(v) + ' ' + k)
#         item_total += v
#     print("Total number of items: " + str(item_total))
# displayInventory(stuff)
# def addToInventory(inventory, addedItems):
#     # your code goes here
#     inv = {'gold coin': 42, 'rope': 1}
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# inv = addToInventory(inv, dragonLoot)
# displayInventory(inv)