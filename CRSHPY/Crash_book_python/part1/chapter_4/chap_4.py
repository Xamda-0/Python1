#  lists
# items = ['xamda', 'yamda','deeqa', 'cali', 'kaafiya', 'kalsoon','faarax']
# print('hello ' +items[0])
# animal = ['elephant', 'lion', 'ham', 'sheep','goats','cat', 'dog']
# print(f'the {animal[0]} is bigger than the {animal[1]}')
# print(f'the {animal[-2]} is scary the {animal[1]}')
# print(animal[4:-2])
# print(len(animal))
# animal[2] = 'mouce'
# print(animal)
# nasted list
# items = [[1,2,3,4,5,6,],['xamda','deeqa','kaafiya']]
# print(items[0][2])
# concatination
# animal = ['elephant', 'lion', 'ham', 'sheep','goats','cat', 'dog']
# animal = animal + [1,2,3,4,]
# del animal[2]
# print(animal)

# text = ['a','v','r','g']*2
# del text[1]
# print(text)
# numText =  [1, 2, 3] + ['A', 'B', 'C']
# print(numText)
# catNames = []
# while True:
#     print('Enter the name of cat ' + str(len(catNames) + 1) + 
#       ' (Or enter nothing to stop.):')
#     name = input()
#     if name == '':
#         break
#     catNames = catNames + [name]  # list concatenation
# print('The cat names are:')
# for name in catNames:
    #   print('  ' + name)
# supplies = ['pen','fish', 'mic']
# print(supplies[-3])   
# for i in range(len(supplies)):
    # print(f'index {str(i)} in supplies is {supplies[i]}')
# supplies = ['pens', 'ink', 'fish' ,'grid', 'food']
# for i in range(len(supplies)):
#     print(f'index {str(i)} in supplies is {supplies[i]}')
# in and not in
# supplies = ['pens', 'ink', 'fish' ,'grid', 'food']
# print('cat' not in supplies)
# print('ink'  in supplies)
# names = ['xamda', 'khadra', 'kaafia' ,'deeqa', 'caasha']
# print('enter your name.')
# name = input()
# if name in names:
#     print(name +' is my name.')
# else:
#     print('i don\'t have your name ' + name +'.')
# names = ['fat', 'black','dress', 'cat']
# size, clour, cloth, pets = names
# print(pets)
# names = ['fat', 'black','dress', 'cat']
# print(names.index('dress'))
# names = ['fat', 'black','dress','fat', 'cat']
# names.append('kaafia')
# print(names)
# names.insert(0,'xamda')
# print(names)
# names.remove('cat')
# print(names)
# names.remove('fat')
# print(names)
# names = ['fat', 'black','dress','find', 'cat']
# names.sort()
# print(names)
# names.sort(reverse= True)
# print(names)
# num = [1,2,3,-4,6,3,-1,-10]
# num.sort()
# print(num)
# alpha = ['H', 'b','A', 'T', 'o','C']
# alpha.sort(key = str.lower)
# print(alpha)
# import random
# messages = ['It is certain',
#     'It is decidedly so',
#     'Yes definitely',
#     'Reply hazy try again',
#     'Ask again later',
#     'Concentrate and ask again',
#     'My reply is no',
#     'Outlook not so good',
#     'Very doubtful']
# print(messages[random.randint(0, len(messages) - 1)])
# alpha = ['H', 'b','A', 'T', 'o','C']
# print(alpha[random.randint(0,len(alpha) -1)])
# name = 'Xamda'
# # print(name[0:4])
# for i in name:
#     print(f'***** {i } *****')
# name = 'my cat name are ken'
# Newname = name[0:12] + 'is' + name[15: 19]
# print(Newname)
# eggs = [1,2,4,5,3]
# del eggs[2]
# del eggs[3]
# del eggs[0]
# del eggs[1]
# eggs.append(0)
# eggs.append(7)
# eggs.append(9)
# eggs.append(8)
# print(eggs)
# tuple
# eggs = (4,5,2,6)
# print(eggs)
# text = (type('hello',))
# print(text)
# print(type('hello'))
# text = (1, 2, 3)
# num = 'hello'
# text = num
# print(text)
# print(num)
# def eggs(someParameter):
#     someParameter.append('Hello')
# spam = ['Xamda']
# eggs(spam)
# print(spam)
# import copy
# eggs = ['A','V','R','Y']
# bar = copy.copy(eggs)
# bar[1] = 23
# print(bar)
# def listValue(list):
#     return list 
# print(listValue('gas','fed','hud'))
# def format_list(items):
#     if not items:  # Handle empty list
#         return ""
#     elif len(items) == 1:  # Handle single-item list
#         return str(items[0])
#     else:
#         return ", ".join(map(str, items[:-1])) + " and " + str(items[-1])

# # Example usage:
# example_list = ["apples", "bananas","kens", "cherries"]
# result = format_list(example_list)
# print(result)  # Output: "apples, bananas and cherries

# triangle(5)
# n=5
# while n>=1:
#     print(' '*(5-n),'* '*n)
#     n-=1