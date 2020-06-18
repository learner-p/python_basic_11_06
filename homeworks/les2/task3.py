while True:
    month = input('Ввод номера месяца: ')
    if month.isdigit() and 0<int(month)<13:
        month=int(month)
        break
    else:
        print('Некорректный ввод номера месяца')
winter=[12,1,2]
spring=[3,4,5]
summer=[6,7,8]
autumn=[9,10,11]

if month in winter:
    print('Зима')
elif month in spring:
    print('Весна')
elif month in summer:
    print('Лето')
else:
    print('Осень')

times={'Зима':(12,1,2), 'Весна':(3,4,5), 'Лето':(6,7,8), 'Осень':(9,10,11)}
for time,months in times.items():
    for find_month in months:
        if month==find_month:
            print(time)