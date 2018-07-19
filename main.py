__author__ = 'Nick Terskikh. Designed by NAT Studio'
# -*- coding: utf-8 -*-
# 12.07.2018

import sys

# функция, показывающая размер объектов
def show_sizeof(x, level=0):
    print ("\t" * level, x.__class__, sys.getsizeof(x), x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_sizeof(xx, level + 1)
        else:
            for xx in x:
                show_sizeof(xx, level + 1)


digit_my = int(input('Введите число: '))
print('Введённое вами число занимает в байтах')
show_sizeof(digit_my)
input('Для завершения и выхода из программы нажмите Enter')
