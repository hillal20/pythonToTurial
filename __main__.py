class Foo:
    bill = 'hill'
    print('hello word')

    def __init__(self):
        self.a = 10
        print('this is __init__')

    def friend(self):
        print('friend', self.bill)

    print('last')

    def __del__(self):
        print('this is __del__')
        print('goodby')

    def build(self):
        print('buil')


boo = Foo()
print(boo.bill)
print(boo.a)
print(boo)
print(dir(boo))
