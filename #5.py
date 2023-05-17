#Задание 5
#Создайте класс светофор (trafficlight). Реализуйте в нем метод, который будет переключать цвета (red, green, yellow) 
#по определенному времени: red = 1 сек, green 2 сек, yellow = 0.5 сек.
#Подсказка:
#Воспользуйтесь модулем time. В нем есть функция sleep
import time

class TrafficLight:
    def __init__(self):
        self.__color = 'red' 
    def running(self):
        while True:
            if self.__color == 'red':
                print('red') 
                time.sleep(1) 
                self.__color = 'green' 
            elif self.__color == 'green':
                print('green') 
                time.sleep(2) 
                self.__color = 'yellow' 
            else:
                print('yellow') 
                time.sleep(0.5) 
                self.__color = 'red' 
traffic_light = TrafficLight()
traffic_light.running()