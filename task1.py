#Реализуйте класс-итератор EvenRange, который принимает начало и конец интервала в качестве
# аргументов __init__ и дает только чётные числа во время итерации. Если пользователь
# пытается итерироваться после того, как он дал все возможные числа, должно быть напечатано
# Out of numbers! Примечание: Не используйте функцию range()


class EvenRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __next__(self):
        if self.start % 2 != 0:
            self.start += 1
            return self.start
        elif self.start % 2 == 0 and self.start < self.end - 1:
            self.start += 2
            result = self.start
            return result
        else:
            raise StopIteration("Out of numbers!")

    def __iter__(self):
        return self


erange = EvenRange(1, 10)
print(next(erange))
print(next(erange))
print(next(erange))
print(next(erange))
print(next(erange))
print(next(erange))

