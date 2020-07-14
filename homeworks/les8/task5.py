'''5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное
подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
любую подходящую структуру, например словарь.'''
class Stock:
    __itemlist={}
    def __init__(self,mol):
        self.mol=mol
    @classmethod
    def get(cls,thing):
        cls.__itemlist.update({thing:{'наименование':thing.item, 'серийный номер':thing.sn, 'МОЛ':thing.mol}})
    @classmethod
    def move_to_mol(cls,obj):
        cls.__itemlist.pop(obj)
    @classmethod
    def check(cls):
        print(cls.__itemlist)
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