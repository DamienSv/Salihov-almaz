#Создайте класс Car, реализуйте в нем 5 атрибутов :
#цвет,
#марку,
#кузов (сидан sedan, грузовик truck),
#скорость,
#тип коробки передач;
#и 6 методов:
#start - заставляет начинать движение
#stop - останавливает машину
#turn - поворачивает машину в какую-либо сторону, и выводит сообщение:" Машина повернула налево"
#speed_up - ускоряет автомобиль
#speed_down - замедляет автомобиль
#beep - сигналит
#Создайте два экземпляра класса truck и car. Продемонстрируйте работу всех методов
class Car:
    def __init__(self, color, brand, body, speed, gearbox):
        self.color = color
        self.brand = brand
        self.body = body
        self.speed = speed
        self.gearbox = gearbox
    def start(self):
        print("Машина начала движение")
    def stop(self):
        print("Машина остановилась")
    def turn(self, direction):
        print("Машина повернула на ", direction)
    def speed_up(self, speed_increase):
        self.speed += speed_increase
        print("Скорость увеличена на ", speed_increase)
    def speed_down(self, speed_decrease):
        self.speed -= speed_decrease
        print("Скорость уменьшена на ", speed_decrease)
    def beep(self):
        print("Бип-бип!")
truck1 = Car("Белый", "Камаз", "грузовик", 60, "механика")
truck2 = Car("Красный", "Mercedes-Benz", "грузовик", 50, "автомат")
car1 = Car("белый", "Ford", "хэтчбек", 100, "автомат")
car2 = Car("синий", "Volkswagen", "седан", 70, "механика")

truck1.start()
truck1.turn("право")
truck1.speed_up(20)
truck1.speed_down(10)
truck1.stop()
truck1.beep()

truck2.start()
truck2.turn("лево")
truck2.speed_up(30)
truck2.speed_down(15)
truck2.stop()
truck2.beep()

car1.start()
car1.turn("лево")
car1.speed_up(50)
car1.speed_down(25)
car1.stop()
car1.beep()

car2.start()
car2.turn("право")
car2.speed_up(10)
car2.speed_down(5)
car2.stop()
car2.beep()