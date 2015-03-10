# -*- coding: utf-8 -*-

__author__ = 'cpn'


def ger_attr(obj):
    """
    1. Как получить список всех атрибутов объекта
    """
    return dir(obj)


def get_public_attr(obj):
    """
    2. Как получить список всех публичных атрибутов объекта
    """
    # return [atr for atr in dir(obj) if not atr.startswith('_')]
    return filter(lambda atr: not atr.startswith('_'), dir(obj))


def get_method(obj):
    """
    3. Как получить список методов объекта
    """
    # return [atr for atr in dir(obj) if callable(getattr(obj, atr))]
    return filter(lambda atr: callable(getattr(obj, atr)), dir(obj))


def get_help(obj):
    """
    4. В какой "магической" переменной хранится содержимое help?

    >>> class test_obj(object):
    ...    '''doc'''
    ...    pass
    >>> get_help(test_obj)
    'doc'

    """

    return obj.__doc__


def concat_tuple(*args):
    """
    5. Есть два кортежа, получить третий как конкатенацию первых двух
    >>> t_1 = (1,2)
    >>> t_2 = (3, 4)
    >>> concat_tuple(t_1, t_2)
    (1, 2, 3, 4)

    """
    t_1 = args[0]
    t_2 = args[1]

    return t_1+t_2


def concat_unic(*args):
    """
    6. Есть два кортежа, получить третий как объединение
    уникальных элементов первых двух кортежей
    """
    set_1 = set(args[0])
    set_2 = set(args[1])

    return tuple(set_1 | set_2)


def clice_list(lst):
    """
    7. Почему если в цикле меняется список, то используется
    for x in lst[:], что означает [:]?

    >>> lst = [1, 2, 3]
    >>> res = clice_list(lst)
    >>> res[1] != res[2]
    True
    """
    if id(lst) != id(lst[:]):
        return (
            'При [:] id объектов не равны:', id(lst), id(lst[:])
        )
    else:
        pass


def two_list_to_dict(list_1, list_2):
    """
    8. Есть два списка одинаковой длины, в одном ключи, в другом значения.
    Составить словарь.

    >>> list_1 = [1, 2, 3]
    >>> list_2 = [11, 12, 13]
    >>> two_list_to_dict(list_1, list_2)
    {1: 11, 2: 12, 3: 13}
    """
    return {key: value for key, value in zip(list_1, list_2)}


def two_list_to_dict_2(list_1, list_2):
    """
    9. Есть два списка разной длины, в одном ключи, в другом значения.
    Составить словарь. Для ключей, для которых нет значений
    использовать None в качестве значения.
    Значения, для которых нет ключей игнорировать.

    >>> list_1 = [1, 2, 3]
    >>> list_2 = [11, 12, 13]
    >>> two_list_to_dict_2(list_1, list_2)
    {1: 11, 2: 12, 3: 13}

    >>> list_3 = [1, 2, 3]
    >>> list_4 = [11]
    >>> two_list_to_dict_2(list_3, list_4)
    {1: 11, 2: None, 3: None}

    >>> list_3 = [1, 2]
    >>> list_4 = [11, 12, 13]
    >>> two_list_to_dict_2(list_3, list_4)
    {1: 11, 2: 12}

    """
    return {key: value for key, value in map(None, list_1, list_2) if key}


def invert_dict(input_dict):
    """
    10. Есть словарь. Инвертировать его. Т.е. пары ключ:
    значение поменять местами — значение: ключ.

    >>> input_dict = {1: 11, 2: 22}
    >>> invert_dict(input_dict)
    {11: 1, 22: 2}
    """
    return {value: key for key, value in input_dict.iteritems()}


def encode_utf_8_end_cp1251(input_unicode):
    """
    11. Есть строка в юникоде, получить 8-битную строку в
    кодировке utf-8 и cp1251

    >>> test_un = u'empty'
    >>> encode_utf_8_end_cp1251(test_un)
    ('empty', 'empty')
    """
    return input_unicode.encode('windows-1251'), input_unicode.encode('utf-8')


def decode_1251_unicode(input_str):
    """
    12. Есть строка в кодировке cp1251, получить юникодную строку

    >>> test_str = u'empty'.encode('windows-1251')
    >>> decode_1251_unicode(test_str)
    u'empty'
    """
    return input_str.decode('windows-1251')

if __name__ == "__main__":
    import doctest
    doctest.testmod()