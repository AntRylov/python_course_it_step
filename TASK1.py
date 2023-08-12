def do_twice(func):
    def wrapper(*args):
        res = func(*args)
        print(res)
        print(res)
    return wrapper


@do_twice
def good_night(name):
    return f'Good night, {name}'


@do_twice
def good_morning(name):
    return f'Good morning, {name}'


good_night("Peter")
good_morning("Anton")
