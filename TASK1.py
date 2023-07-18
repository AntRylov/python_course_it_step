#Напишите рекурсивную функцию get_list(n: int, lst=[]) -> list, чтобы сгенерировать и вернуть список от 1 до N.
#Аргументом функции является только N.


def get_list(n: int, lst=[]) -> list:
    if len(lst) <= n:
        for i in range(1, n + 1):
            lst.append(i)

    return lst


print(get_list(int(input())))