# # CALCULATOR
operations = input( 'Enter any operator (+ - * /) ')
num1 = float(input( 'Enter the 1st number: '))
num2 = float(input( 'Enter the 2nd number: '))
if operations == '+':
    result = num1 + num2
    print(round(result, 3))
elif operations == '-':
    result = num1 - num2
    print(round(result, 3))
elif operations == '*':
    result = num1 * num2
    print(round(result, 3))
elif operations == '/':
    result = num1 / num2
    print(round(result, 3))
else:
    print(f'{operations} is not a valid operator')