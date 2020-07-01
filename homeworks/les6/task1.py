'''1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера,
создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.'''

import time
class TrafficLight:
        __color='red'
        def running(self):
            assert TrafficLight.__color=='red', 'Неправильный цвет'
            print(TrafficLight.__color)
            time.sleep(7)
            TrafficLight.__color='yellow'
            assert TrafficLight.__color=='yellow', 'Неправильный цвет'
            print(TrafficLight.__color)
            time.sleep(2)
            TrafficLight.__color='green'
            assert TrafficLight.__color=='green', 'Неправильный цвет'
            print(TrafficLight.__color)
            time.sleep(5)
            TrafficLight.__color='red'
s = TrafficLight()
while True:
    s.running()