'''3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.'''

def my_func(a,b,c):
    my_list=[a,b,c]
    max1=max(my_list)
    my_list.remove(max1)
    max1=float(max1)
    max2=max(my_list)
    max2=float(max2)
    return (max1+max2)

result=my_func(input('1: '),input('2: '),input('3: '))
print((result))