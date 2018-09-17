fill = {'name': "hilal", "age": 33, 'array': [1, 3, 4]}
print(fill['array'][0])
print('name' in fill)
print(fill.keys())


a = fill.values()
print(a)
b = list(a)
print(b)

c = fill.keys()
d = list(c)
print(d)

z = dict(v="hello", m='world')
print(z)
print(fill.items())
print(list(fill.items()))

fill.__contains__(fill, 'name', )
