# class in python

class Car:
    def __init__(self, name, model,color,price):
        # instance variables
        print("init method called")
        self.name = name
        self.model = model
        self.color = color
        self.price = price

bmw = Car("BMW", "2020", 'Black',15000000)
cro = Car("Carolla", "2020", 'Blue',13000000)
print(bmw.model)
print(cro.name)