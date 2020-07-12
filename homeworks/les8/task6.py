'''6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества
принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.'''
class Stock:
    __itemlist={}
    def __init__(self,mol):
        self.mol=mol
    @classmethod
    def get(cls,thing):
        cls.__itemlist.update({thing:{'наименование':thing.item, 'серийный номер':thing.sn, 'МОЛ':thing.mol}})
        print(f'Позиция {thing.item} {thing.sn} перемещена на склад')
    @classmethod
    def move_to_mol(cls,obj):
        try:
            cls.__itemlist.pop(obj)
            print(f'Позиция {obj.item} {obj.sn} перемещен со склада')
        except KeyError:
            print(f'Ошибка: позиция {obj.item} {obj.sn} отсутствует на складе')
    @classmethod
    def check(cls):
        print(f'Проверка объектов склада {cls.__name__}')
        return([i for i in cls.__itemlist.values()])
class Office:
    def __init__(self,item,sn,mol):
        self.item=item
        self.sn=sn
        self.mol=mol
    def move_to_stock(self):
        Stock.get(self)
class Printer(Office):
    def __init__(self,item,sn,mol):
        super().__init__(item,sn,mol)
class Scanner(Office):
    def __init__(self,item,sn,mol):
        super().__init__(item,sn,mol)
class Xerox(Office):
    def __init__(self,item,sn,mol):
        super().__init__(item,sn,mol)

a=Printer('hp3230','444334j34534j','hr')
b=Xerox('lg509','2kljwek23','security')
c=Scanner('dell','2lkj23lsdl','management')
if __name__ == '__main__':
    print(Stock.check())
    a.move_to_stock()
    c.move_to_stock()
    print(Stock.check())
    b.move_to_stock()
    print(Stock.check())
    Stock.move_to_mol(c)
    print(Stock.check())
    Stock.move_to_mol(c)