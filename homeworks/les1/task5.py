while True:
    a=input('Выручка: ')
    b=input('Издержки: ')
    if a.isdigit() and  b.isdigit():
        break
    print('Некорректный ввод')
a=int(a)
b=int(b)
if a>b:
    print(f'Фирма отработала в прибыль {a-b}')
    while True:
        c=input('Количество сотрудников: ')
        if c.isdigit():
            break
    c = int(c)
    print(f'Прибыль из расчета на сотрудника составила {(a-b)/c}')
elif a<b:
    print('Фирма отработала в убыток')
else:
    print('Фирма отработала в 0')
