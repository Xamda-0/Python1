# q1
# def times_Ten(numbers):
#     return numbers ** 10
#     # print(numbers)
# print(times_Ten(2))
# print(times_Ten(4))
# # q4
# def chanfeValue(a, b):
#     a = 2
#     b = 1
#     print(a, b)
# def main():
#     x = 0
#     y = 0.0
#     print(x, y)
#     chanfeValue(x, y)
#     print(x, y)

# main()
# q5
# def my_function(a, b, c):
#     d = (a + c) / b
#     print(d)
# my_function(2, 4, 6)
# q6
# import random
# def my_function():
#     rand = random.randint(1, 100)
#     print(rand)

# my_function()
# q7
# def half(number):
#     number = number / 2
#     print(number)
# half(1.4)
# q8
# def cube(num):
#     result = num ** 2 *num
#     return result
# print(cube(4))
# q10
# def get_first_name(name):
#     return name
# print(get_first_name('John  Doe'))

# programming exercises
# q1
# def converter():
#     Kilometers = int(input('Kilometers: '))
#     Miles = Kilometers * 0.6214
#     return Miles
# print(converter())
# q2
# def dayactir():
#     amount_dayactir = int(input('Dayactir: '))
#     awoodaada = int(input('inta aad heli karto: '))
#     total = amount_dayactir * awoodaada
#     print(total)
# dayactir()
# def natiija():
#     maaddo1 = float(input('maadda 1: '))
#     maaddo2 = float(input('maadda 2: '))
#     maaddo3 = float(input('maadda 3: '))
#     maaddo4 = float(input('maadda 4: '))
#     maaddo5 = float(input('maadda 5: '))
#     average = (maaddo1 + maaddo2 + maaddo3 + maaddo4 + maaddo5 ) /5
#     if average >= 90:
#         print('grade: A')
#         print('score: 90-100')
#     elif average >= 80:
#         print('grade: B')
#         print('score:80-90 ')
#     elif average >= 70:
#         print('grade: C')
#         print('score: 70-80')
#     elif average >= 60:
#         print('grade: D')
#         print('score: 60-70')
#     else:
#         print('grade: F')
#         print('score: VERY BAD')
# natiija()

# q16
import random
def my_function():
    rand = random.randint(1, 100)
    if rand %2 == 0:
        print(rand)
        print('is even number')
    else:
        print(rand)
        print('is odd number')

my_function()