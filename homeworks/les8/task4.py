'''4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым
для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие
для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.'''

class Stock:
    def __init__(self,mol,firm):
        self.mol=mol
        self.firm=firm
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