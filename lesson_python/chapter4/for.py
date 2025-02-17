# for num in range(100, 0, -1):
#     print(num)
# start = int(input(' start: '))
# end = int(input(' end: '))
# step = int(input(' step: '))
# for user in range(start, end, step):
#     print(user)
start = int(input(' start: '))
end = int(input(' end: '))
total = 0
for user in range(start, end):
    total = total + user
    print(user)
print(total)