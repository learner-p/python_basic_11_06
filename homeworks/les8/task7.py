'''7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.'''
import traceback
class Complex:
    def __init__(self,numeric):
        self.numeric=numeric
        try:
            if not 'i' in numeric:
                self.a=numeric
            else:
                if '+' in numeric:
                    self.a=numeric.split('+')[0]
                elif not '-' in numeric:
                    self.a='0'
                elif len(numeric.split('-'))==2:
                    self.a='0' if numeric[0]=='-' else numeric.split('-')[0]
                else:
                    self.a='-'+numeric.split('-')[1]

            if not 'i' in numeric:
                self.b='0'
            else:
                if self.a=='0':
                    self.b=numeric[:-1]
                else:
                    self.b=numeric.split(self.a)[1][:-1] if '-' in numeric.split(self.a)[1] else numeric.split(self.a)[1][1:-1]
            self.a=float(self.a)
            self.b=float(self.b)
        except:
            print('Неуспешная обработка комплексного числа\n',traceback.format_exc())

    def __add__(self, other):
        return Complex((str(self.a+other.a) if self.a+other.a!=0 else '')+(('+'+str(self.b+other.b)+'i') if self.b+other.b>0 else (str(self.b+other.b)+'i') if self.b+other.b<0 else ''))
    def __mul__(self, other):
        return Complex((str(self.a*other.a-self.b*other.b) if self.a*other.a-self.b*other.b!=0 else '')+(('+'+str(self.a*other.b+self.b*other.a)+'i') if self.a*other.b+self.b*other.a>0 else (str(self.a*other.b+self.b*other.a)+'i') if self.a*other.b+self.b*other.a<0 else ''))

    "(a + bi) · (c + di) = (ac – bd) + (ad + bc)i"

first=Complex('5-4i')
second=Complex('-9+3i')
third=Complex('-4.5-2i')
fourth=Complex('-3i')
fifth=Complex('5')
print(1)
for i in [first,second,third,fourth,fifth]:
    print('=' * 20)
    print(i.numeric)
    print(i.a,i.b)

for i in [second,third,fourth,fifth]:
    print('*'*20)
    print((first+i).numeric)
    print((first*i).numeric)