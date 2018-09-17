num1 = 12.466666
num2 = 3.56666
print('num1:', num1, 'num2:', num2)


print('num1==> {0:.3f} ,  num2 ==>{1:.3f}'.format(num1, num2))
print('num1==> {0:.3} ,  num2 ==>{1:.3}'.format(num1, num2))

person = {'name': 'bill', 'age': 23}  # an object in python
person2 = ['bill', 23]  # a list in python
print(person['name'])

sentence = 'i am {0}, i have {1} years'.format(person['name'], person['age'])
print(sentence)
sentence2 = 'i am ===> {0[name]}, i have ===> {0[age]} years'.format(person)
print(sentence2)

sentence3 = 'i am ===> {0[0]}, i have ===> {0[1]} years'.format(person2)
print(sentence3)
