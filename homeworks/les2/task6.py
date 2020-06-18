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
print('\n')
for i in result_list:
    print(i)

analityc={}
name_list=[]
cost_list=[]
numbers_list=[]
metric_list=[]
for i in result_list:
    name_list.append(i[1]["Название"])
    cost_list.append(i[1]["Цена"])
    numbers_list.append(i[1]["Количество"])
    metric_list.append(i[1]["Единица измерения"])
analityc.update({"Название":name_list})
analityc.update({"Цена":cost_list})
analityc.update({"Количество":numbers_list})
analityc.update({"Единица измерения":metric_list})

print('\n')
print(analityc.items())