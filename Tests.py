# здесь объявляйте функцию-декоратор
def integer_params_decorated(func):
    def wrapper(*args, **kwargs):
        if not all([type(i) == int for i in args[1:]]):
            raise TypeError("аргументы должны быть целыми числами")
        else:
            return func(*args, **kwargs)
    return wrapper    




def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls


@integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value