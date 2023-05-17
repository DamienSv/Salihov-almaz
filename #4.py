#Задание 4
#Добавьте ограничение скорости в класс Car из предыдущего задания: для грузовика(truck) 60 км/ч, а для легкового(car) - 80 км/ч. 
#При превышении пусть на экран выводится предупреждение: "Скорость превышена! Разрешенная скорость 60 км/ч"
class Car:
    def __init__(self, color, brand, model, body_type, speed, number, price):
        self.color = color
        self.brand = brand
        self.model = model
        self.body_type = body_type
        self.speed = speed
        self.number = number
        self.price = price
    def check_speed(self):
        if self.body_type == 'truck':
            if self.speed > 60:
                print(f"Скорость грузовика {self.brand} {self.model} с номером {self.number} превышена! Разрешенная скорость 60 км/ч. штраф: {self.price}")
        else:
            if self.speed > 80:
                print(f"Скорость автомобиля {self.brand} {self.model} с номером {self.number} превышена! Разрешенная скорость 80 км/ч. штраф: {self.price}")
truck = Car('Красный', 'Mercedes-Benz', 'Actros', 'truck', 70, 'р770мк716', '500')
truck.check_speed() 
car = Car('Белый', 'Ford', 'Focus', 'Седан', 180, 'м236км716', '2500')
car.check_speed()