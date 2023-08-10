# Напишите следующие функции:
# ○Нахождение корней квадратного уравнения
# ○Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○Декоратор, запускающий функцию нахождения корней квадратного уравнения
# с каждой тройкой чисел из csv файла.
# ○Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.


import csv
import json
import math
from typing import Callable
from random import uniform, randint


def var_from_csv(func: Callable):
    def wrapper(name):
        func(name)
        with open(name, 'r', newline='') as f:
            file = csv.reader(f)
            for i, line in enumerate(file):
                if i != 0:
                    print(line)
                    find_the_root(line)


    return wrapper



def to_json(func: Callable):
    def wrapper(args):
        with open('new_JSON.json', 'a', encoding='UTF-8') as f:
            json.dump({str(args):str(func(args))}, f, indent=2, ensure_ascii=False)

    return wrapper



@var_from_csv
def create_csv(name):
    with open(name, 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.DictWriter(f, fieldnames=['a', 'b', 'c'],
                                   dialect='excel', quoting=csv.QUOTE_ALL)
        csv_write.writeheader()
        result = []
        for i in range(randint(100, 1000)):
            result.append({'a': round(uniform(1, 100), 2),
                           'b': round(uniform(1, 100), 2),
                           'c': round(uniform(1, 100), 2)})
        csv_write.writerows(result)


@to_json
def find_the_root(args):
    a = float(args[0])
    b = float(args[1])
    c = float(args[2])
    print(f"{a}x^2 + {b}x + {c} = 0")
    discriminant = b ** 2 - 4 * a * c
    print(discriminant)
    if discriminant == 0:
        x1 = -b / (2 * a)
        return (x1)
    else:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        return (x1, x2)


create_csv('new.csv')