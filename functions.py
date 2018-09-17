def bill(first, second):
    print(f'good morning :{first}, {second}, how are you ?')


bill('bill', 'john')
name = 'bill'
print(f'{name}')

x = 'zozo'


def area():
    global x
    x = 'zaza'
    print(x)


area()
print(x)
