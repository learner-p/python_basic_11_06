my_list = [7, 5, 3, 3, 2]
while True:
    new=input('Ввод натурального числа:')
    if new.isdigit():
        if float(new)>0 and (float(new)%2==0 or (float(new)+1)%2==0):
            new=int(new)
            break
        else:
            print('Некорректный ввод')
    else:
        print('Некорректный ввод')

print(new)
my_list.append(new)
my_list.sort(reverse=True)
print(my_list)
