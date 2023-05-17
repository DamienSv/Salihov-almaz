#Задание 1
#Создайте класс cat и добавьте 3 атрибута (имя, окрас, возраст) и 3 метода класса (мяукнуть, мурлыкать и еще один на ваше усмотрение).
#Создайте 1 экземпляр класса и продемонстрируйте его атрибуты и методы.
class Cat:
  def __init__(self, name, color, age):
    self.name = name
    self.color = color
    self.age = age
  def meow(self):
    print(f"{self.name} мяу!")
  def purr(self):
    print(f"{self.name} мурлыкает...")
  def sleep(self):
    print(f"{self.name} разодрал диван")
my_cat = Cat("Марсик", "серо-черный", 6)
print(f"Кличка кота: {my_cat.name}")
print(f"Окрас кота: {my_cat.color}")
print(f"Возраст кота: {my_cat.age}")
my_cat.meow()
my_cat.purr()
my_cat.sleep()