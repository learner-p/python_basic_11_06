seconds=input('Введите количество секунд\n')
if seconds.isdigit():
    seconds=int(seconds)
    hh=seconds//3600
    mm=(seconds-hh*3600)//60
    ss=seconds-hh*3600-mm*60
    time=f'{hh}:{mm}:{ss}'
    print(time)