result_list=[]
number=1
while True:
    name=input(f'Название товара №{str(number)}: ')
    cost=input(f'Цена товара №{str(number)}: ')
    numbers=input(f'Количество товара №{str(number)}: ')
    metric=input(f'Единица измерения товара №{str(number)}: ')
    desc={"Название":name, "Цена":cost,"Количество":numbers,"Единица измерения":metric}
    result_list.append((number,desc))
    if input("Ввод следующего? ")=='нет':
        break
    number += 1
for i in result_list:
    print(i)