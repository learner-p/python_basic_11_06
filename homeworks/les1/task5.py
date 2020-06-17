while True:
    a=input('Выручка: ')
    b=input('Издержки: ')
    if a.isdigit() and  b.isdigit():
        break
a=int(a)
b=int(b)
if a>b:
    print(f'Фирма отработала в прибыль {a-b}')
elif a<b:
    print('Фирма отработала в убыток')
else:
    print('Фирма отработала в 0')
