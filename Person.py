class Person:
    def __init__(self, name, surname, skill=1):
        self.name = name
        self.surname = surname
        self.skill = skill

    def info(self):
        return f'Мy name is {self.name} {self.surname} my qualification =  {self.skill}'

    def __del__(self):
        print(f'Good bye,mister {self.name} {self.surname}')


person1 = Person('Steven', 'Gerrard', 8)
person2 = Person('Frank', 'Lampard', 12)
person3 = Person('Jordan', 'Henderson', 14)


print(person1.info())
print(person2.info())
print(person3.info())
del person1
print(input())





