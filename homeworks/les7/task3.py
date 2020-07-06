class Organic:
    def __init__(self,number):
        self.number=number
    def __add__(self, other):
        return Organic(self.number+other.number)
    def __sub__(self, other):
        return Organic(self.number-other.number) if self.number>other.number else print('Ошибка разности')
    def __mul__(self, other):
        return Organic(self.number*other.number)
    def __truediv__(self,other):
        return Organic(self.number//other.number)
    def make_order(self,cells):
        for i in range(self.number//cells):
            print('*'*cells)
        print('*'*(self.number-(self.number//cells)*cells))
a=Organic(15)
b=Organic(11)
c=a-b
if c:
    print(c.number)
a.make_order(6)