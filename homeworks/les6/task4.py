'''4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать
текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.'''

class Car:
    def __init__(self,speed,color,name,is_police=False):
        self.speed=speed
        self.color=color
        self.name=name
        self.is_police=is_police
    def go(self):
        print(f'Машина поехала')
    def stop(self):
        print(f'Машина остановилась')
    def turn(self,direction):
        print(f'Машина повернула {direction.lower()}')
    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed>60:
            print(f'Превышение скорости на {self.speed-60}')
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed>40:
            print(f'Превышение скорости на {self.speed-40}')
class PoliceCar(Car):
    pass

t=TownCar(65,'silver','solaris')
print(t.speed)
print(t.is_police)
t.go()
t.turn('Направо')
t.show_speed()
print()
s=SportCar(120,'black','ferrari')
s.show_speed()
s.stop()
print(s.is_police)
print()
p=PoliceCar(70,'white','skoda',True)
print(p.is_police)
p.turn('направо')