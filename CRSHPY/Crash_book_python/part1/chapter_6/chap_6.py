#  MANIPULATING strings 
# raw string ignores all escape characters
# print(r'That is Carol\'s cat.')
#  Multiline Strings with triple Quotes
# print('''Dear Alice,
#  Eve's cat has been arrested for catnapping, cat burglary, and extortion.
#  Sincerely,
#  Bob''')
#  Multiline Comments
# def spam():
#     """This is a multiline comment to help
#     explain what the spam() function does."""
#     print('Hello!')
# spam()
# The upper(), lower(), isupper(), and islower() String Methods
# spam = 'Hello world!'
# spam = spam.upper()
# print(spam)
# spam = spam.lower()
# print(spam)
# print('How are you?')
# feeling = input()
# if feeling.lower() == 'great':
#     print('I feel great too.')
# else:
#     print('I hope the rest of your day is good.')
# print( '12345'.isupper())
# print( 'abc12345'.islower())
# The isX String Methods
# print('This Is Title Case'.istitle())
# print( 'hello'.isalpha())
# print('hello123'.isalpha())
# while True:
#     print('Enter your age:')
#     age = input()
#     if age.isdecimal():
#         break
#     print('Please enter a number for your age.')
# while True:
#     print('Select a new password (letters and numbers only):')
#     password = input()
#     if password.isalnum():
#         break
#     print('Passwords can only have letters and numbers.')
# The startswith() and endswith() String Methods
# print('Hello world!'.startswith('Hello'))
# print('Hello world!'.endswith('hello'))
#  The join() and split() String Methods
# print( '; '.join(['cats', 'rats', 'bats']))
# print( 'My name is Simon'.split())
#  Justifying Text with rjust(), ljust(), and center()
# print( 'Hello'.rjust(20, '*'))
# print( 'Hello'.ljust(20, '-'))
# # print('Hello'.center(20, '='))

#  Removing Whitespace with strip(), rstrip(), and lstrip()
# spam = '    Hello World '
# print( spam.strip())
# print( spam.rstrip())
# import pyperclip
# pyperclip.copy('Hello world!')
# pyperclip.paste()