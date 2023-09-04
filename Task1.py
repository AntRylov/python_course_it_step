#Написать класс Cat, создать ему атрибуты size, color, cat_type.
#1.1. При создании объекта класса передавать в конструктор color и cat_type, которые
#записываются в соответсвующие атрибуты.
#1.2. Сделать метод set_size, в котором если self.cat_type это indoor,
#то self.size =  ‘small’ иначе self.size=’undefined’. Протестируйте разные варианты.
#1.3. Сделать класс Tiger, унаследованный от класса Cat.
#1.4. Переопределить метод set_size таким образом чтобы если
# self.cat_type это ‘wild’, то self.size = ‘big’ иначе self.size=’undefined’

class Cat:
    def __init__(self, size, color, cat_type):
        self.size = size
        self.color = color
        self.cat_type = cat_type

    def set_size(self):
        if self.cat_type == "indoor":
            self.size = "small"
            return self.size
        else:
            self.size = "undefined"
            return self.size


class Tiger(Cat):
    def __init__(self, size, color, cat_type):
        super().__init__(size, color, cat_type)

    def set_size(self):
        if self.cat_type == "wild":
            self.size = "big"
            return self.size
        else:
            self.size = "undefined"
            return self.size


cat = Cat("Big", "Grey", "indoor")
tiger = Tiger("Big", "orange", "wild")
print(cat.set_size())
print(tiger.set_size())




