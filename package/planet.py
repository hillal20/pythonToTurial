class Planet:
    lang = 'arabic'

    def __init__(self, name, age, nationality, married):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.married = married

    def console(self):
        print(f'self name ===> {self.name}')

    @classmethod
    def bill(cls):
        print(f'langCls ===>{cls.lang}')

    @staticmethod
    def fill(color='red'):
        print(f'color ==> {color}')
