# -*- coding: utf-8 -*-

__author__ = 'cpn'



def cycle(it):
    """
    1. Написать функцию-генератор cycle которая бы возвращала
    циклический итератор.

    >>> i = iter([1, 2, 3])
    >>> c = cycle(i)
    >>> c.next()
    1
    >>> c.next()
    2
    >>> c.next()
    3
    >>> c.next()
    1
    """
    it_lst = list(it)
    while True:
        for i in it_lst:
            yield(i)


def chain(*args):
    """
    Написать функцию-генератор chain, которая последовательно итерирует
    переданные объекты (произвольное количество)

    >>> i1 = iter([1, 2, 3])
    >>> i2 = iter([4, 5])
    >>> c = chain(i1, i2)
    >>> c.next()
    1
    >>> c.next()
    2
    >>> c.next()
    3
    >>> c.next()
    4
    >>> c.next()
    5
    >>> c.next()
    Traceback (most recent call last):
      ...
    StopIteration
    """
    for arg in args:
        for i in arg:
            yield i


if __name__ == "__main__":
    import doctest
    doctest.testmod()
