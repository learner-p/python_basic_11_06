while True:
    a = input('Ввод числа: ')
    if a.isdigit():
        break
    print('Некорректный ввод')
a=int(a)

result=0
diff=9
while diff >= 0:
    b = a
    while b > 0:
        if (b-diff)%10==0:
            result=diff
            break
        b=b//10
    diff -= 1
    if result>diff:
        break

print(result)