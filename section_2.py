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


if __name__ == "__main__":
    import doctest
    doctest.testmod()