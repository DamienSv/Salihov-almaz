#Задание 2
#Создайте класс Good, который будет вычислять значения стоимости товаров. В качестве атрибутов пусть будут:
#name (имя товара),
#price(цена за 1 кг),
#cost (стоимость),
#weight(масса);
#в качестве методов:
#calc - вычисляющий стоимость товара.
#Реализуйте два экземпляра класса Good:
#Яблоки apple('apple', price = 100, weight = 1.5)
#Груши pear('pear', price = 120, weight = 0.8)
#Выведите их стоимость

class Good:
    def __init__(self, name, price, weight):
        self.name = name 
        self.price = price 
        self.weight = weight  
    def calc(self):
        self.cost = self.price * self.weight 
apple = Good('apple', 100, 1.5)
pear = Good('pear', 120, 0.8)
apple.calc()
pear.calc()
print('Стоимость яблок:', apple.cost)
print('Стоимость груш:', pear.cost)