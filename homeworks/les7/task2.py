'''2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы
для основных классов проекта, проверить на практике работу декоратора @property.'''

class Clothes:
    bad_list=[]
    def __init__(self,name,size):
        self.name=name
        self.size=size
        if self.name=='coat':
            self.V=size
        elif self.name=='suit':
            self.H=size
        else:
            print(f'Некорректный тип одежды объекта {self.name}')
            Clothes.bad_list.append(self)
    @property
    def calc(self):
        if self.name=='coat' or self.name=='suit':
            return (f'Расход ткани на объект {self.name}, {self.size} составляет {(self.V/6.5 + 0.5) if self.name=="coat" else (self.H*2 + 0.3)}')
        else:
            return f'Ошибка расчета для объекта {self.name}'
    @calc.setter
    def calc(self,size):
        if size>190:
            self.H=1.2*self.H
    def __add__(self, other):
        return self.calc+other.calc

a=Clothes('coat',46)
b=Clothes('suit',175)
c=Clothes('suit',191)
d=Clothes('jacket',48)
print(a.calc)
print(b.calc)
print(c.calc)
if d:
    print(d.calc)
print(Clothes.bad_list)
print(d)
del d
print(Clothes.bad_list)
print(d)