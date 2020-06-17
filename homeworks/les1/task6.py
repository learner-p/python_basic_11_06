while True:
    a = input('км в первый день:')
    b = input('км в целевой день:')
    if not a.isdigit() and not b.isdigit():
        print('Некорректный ввод км')
        continue
    break
a=int(a)
b=int(b)
day=1
while a<b:
    a=a*1.1
    day+=1
print(day)