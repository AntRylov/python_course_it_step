#Написать класс, который описывает пользователя (class User), сделать ему приватный атрибут
# age, который передается в конструктор, публичный атрибут name, который так же передается
# в конструктор.

#1 Написать getter и setter для атрибута age.

#2 Добавить в setter проверку на валидный возраст (не отрицательное, целое число)


class User:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0 or type(age) != int:
            raise ValueError("Возраст указан не верно")
        else:
            self.__age = age


user = User("Антон", 30)
print(user.age)
#user.age = -35
#user.age = 4.7
print(user.age)
