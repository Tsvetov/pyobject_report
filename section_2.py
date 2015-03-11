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


def addition_range(start=0, count=5):
    """
    Написать фабрику, аналогичную п.2, но возвращающей список таких функций

    # список из функций сложения от 0 до 5 включительно
    # т.е. аналогичное [add0, add1, add2, add3, add4, add5]
    >>> additionals = addition_range(0, 5)
    >>> res = []
    >>> for i in additionals:
    ...     res.append(i(2))
    >>> res
    [2, 3, 4, 5, 6, 7]
    """
    res = []
    for i in xrange(start, count+1):
        res.append(lambda x, i=i: x+i)
    return res


def mymap(*args):
    """
    Написать аналог map:

    первым аргументом идет либо функция, либо список функций
    вторым аргументом — список аргументов, которые будут переданы функциям
    полагается, что эти функции — функции одного аргумента
    в данном случае "развернутая" запись будет:
    [
        (add0(1), add0(2), add0(3)),
        (add1(1), add1(2), add1(3)),
        (add2(1), add2(2), add2(3))
    ]
    >>> mymap(addition_range(0, 2), [1, 2, 3])
    [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
    """
    func, lst = args
    if isinstance(func, list):
        return [tuple(map(i, lst)) for i in func]
    else:
        return tuple(map(func, lst))


if __name__ == "__main__":
    import doctest
    doctest.testmod()