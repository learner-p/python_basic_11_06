n=input('Ввод числа\n')
if n.isdigit():
    result = int(n) + int(str(n*2)) + int(str(n*3))
    print(int(result))