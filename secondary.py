"""
Вспомогательные функции
"""


import os


def check_valid_input(somevalue):
    if not somevalue.isdigit():
        print('Ошибка. Должно быть натуральным числом\n')
        return None
    elif (int(somevalue) <= 0) or (int(somevalue) != float(somevalue)):
        print('Ошибка. Должно быть натуральным числом\n')
        return None
    else:
        return int(somevalue)


def open_helper():
    with open('RULES', 'r') as helper:
        print(helper.read())


def check_saving():
    """
    Проверка наоичия сохраненной игры
    """
    if os.stat('dumps/data.pickle').st_size == 0:
        return 0
    else:
        return 1
