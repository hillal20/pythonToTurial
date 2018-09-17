pots = ['hil', 'bill', 'tom']
for pot in pots:
    print(pot)


for pot in pots[0:2]:
    if pot == 'hil':
        print(f'{pot} -is crazy')
        break
    else:
        print(f'{pot}- not crazy')


age = 10
num = 0
while num < age:
    print(num)
    num += 1
    if num == 5:
        continue
    print('hello')

fill = [1, 2, 3, 4, 5]

for n in range(2, 5):
    print(n)
    print('===>', len(fill))


for n in range(len(fill)-1, -1, -1):
    print(fill[n])
    print('===>', len(fill))
