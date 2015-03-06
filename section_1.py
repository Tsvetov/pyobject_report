# -*- coding: utf-8 -*-

__author__ = 'cpn'


def get_help(obj):
    """
    4. В какой "магической" переменной хранится содержимое help?
    """
    return obj.__doc__


def two_list_to_dict(list_1, list_2):
    """
    8. Есть два списка одинаковой длины, в одном ключи, в другом значения.
    Составить словарь.
    """
    return {key: value for key, value in zip(list_1, list_2)}


def two_list_to_dict_2(list_1, list_2):
    """
    9. Есть два списка разной длины, в одном ключи, в другом значения.
    Составить словарь. Для ключей, для которых нет значений
    использовать None в качестве значения.
    Значения, для которых нет ключей игнорировать.
    """
    return {key: value for key, value in map(None, list_1, list_2) if key}


def invert_dict(input_dict):
    """
    10. Есть словарь. Инвертировать его. Т.е. пары ключ:
    значение поменять местами — значение: ключ.
    """
    return {value: key for key, value in input_dict.iteritems()}


def encode_utf_8_end_cp1251(input_unicode):
    """
    11. Есть строка в юникоде, получить 8-битную строку в
    кодировке utf-8 и cp1251
    """
    return input_unicode.decode('windows-1251'), input_unicode.decode('utf-8')


def decode_1251_unicode(input_str):
    """
    12. Есть строка в кодировке cp1251, получить юникодную строку
    """
    return input_str.encode('windows-1251')