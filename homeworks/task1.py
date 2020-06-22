'''1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.'''

def division(a,b):
    try:
        a=float(a)
        b=float(b)
        print(a/b)
    except ValueError as error:
        print('Некорректный ввод чисел')
    except ZeroDivisionError as error:
        print('Деление на ноль!')

division(input('Ввод первого числа: '),input('Ввод второго числа: '))
