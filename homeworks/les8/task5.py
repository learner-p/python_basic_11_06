'''5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное
подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
любую подходящую структуру, например словарь.'''

class Stock:
    __itemlist=[]
    def __init__(self,mol,firm):
        self.mol=mol
        self.firm=firm
    @classmethod
    def get(cls,object):
        cls.__itemlist.append(object)
    @classmethod
    def check(cls):
        for i in cls.__itemlist:
            print(f'Позиция {i.item}, серийный номер {i.sn}')
class Office:
    def __init__(self,item,sn):
        self.item=item
        self.sn=sn
class Printer(Office):
    def __init__(self,item,sn):
        super().__init__(item,sn)
class Scanner(Office):
    def __init__(self,item,sn):
        super().__init__(item,sn)
class Xerox(Office):
    def __init__(self,item,sn):
        super().__init__(item,sn)
print(1)