seconds=input()
seconds=int(seconds)
hh=seconds//3600
mm=(seconds-hh*3600)//60
ss=seconds-hh*3600-mm*60
time=str(hh)+':'+str(mm)+':'+str(ss)
print(time)