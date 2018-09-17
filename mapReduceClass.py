import functools
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return 'Point(x=%s, y=%s)' % (self.x, self.y)


# p = Point(1, 2)
# print(p)


# name = 'marcog'
# number = 42
# print('%s %d' % (name, number))


# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return "<Human: %s, %d>" % (self.name, self.age)


# b = Human("hilal", 33)
# print(b)
# print(b.__repr__())


# s = 'Hello, Geeks.'
# print(repr(s))
# print(repr(2.0/11.0))
# print(str(s))
# print(str(2.0/11.0))

# list = [1, 3, 4, 5, 6, 6]
# l = list.__len__()
# print(l)
# d = list.__repr__()
# print(d)


# class Foo():
#     def __init__(self):
#         self.l = 4


# foo = Foo()
# repr(foo.__init__)
# # print(foo)
# mx = lambda x, y = 9: x if x > y else y
# print(mx(15, 9))

array = [1, 2, 3, 4]


def double(x):
    return x*2


def largest(x):

    return x > 2


def total(x, y):
    return x+y


x = map(double, array)
y = filter(largest, array)
z = functools.reduce(total, array)


print(list(x))
print(list(y))
print(z)
