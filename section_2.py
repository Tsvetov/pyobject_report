# -*- coding: utf-8 -*-

__author__ = 'cpn'


def func_sum(*args):
    """
    Написать функцию, которой можно передавать аргументы либо списком/кортежем,
    либо по одному. Функция производит суммирование всех аргументов.

    >>> func_sum(1, 2, 3)
    6
    >>> func_sum([1, 2, 3])
    6
    >>> func_sum((3, 5, 6))
    14
    >>> func_sum(3, (5, 6))
    14
    """
    def __merge(lst):
        for i in lst:
            if isinstance(i, (list, tuple)):
                for i in __merge(i):
                    yield i
            else:
                yield i

    return sum(__merge(args))


def addition_usual(number):
    """
    2. Написать функцию-фабрику, которая будет возвращать
    функцию сложения с аргументом.

    # функция addition возвращает функцию сложения с 5
    >>> add5 = addition_usual(5)
    >>> add5(3) # вернет 3 + 5 = 8
    8
    >>> add5(8) # вернет 8 + 5 = 13
    13
    >>> add8 = addition_usual(8)
    >>> add8(2) # вернет 2 + 8 = 10
    10
    >>> add8(4) # вернет 4 + 8 = 12
    12

    Написать варианты с обычной "внутренней" и анонимной lambda-функцией.
    """

    def add(num_2):
        return num_2 + number

    add_l = lambda num_2: number+num_2
    return add


if __name__ == "__main__":
    import doctest
    doctest.testmod()