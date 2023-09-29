# Реализуйте генератор, который будет бесконечно генерировать нечётные числа.


def odd_gen(num):
    if num % 2 != 0:
        while True:
            yield num
            num += 2
    if num % 2 == 0:
        num += 1
        while True:
            yield num
            num += 2


odd = odd_gen(3)
print(next(odd))
print(next(odd))
print(next(odd))
print(next(odd))
print(next(odd))
print(next(odd))
print(next(odd))
print(next(odd))

