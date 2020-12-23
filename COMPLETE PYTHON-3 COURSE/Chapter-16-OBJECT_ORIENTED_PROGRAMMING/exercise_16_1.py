# create a laptop class with attributes like name, model, price
# create two objects/instance of your laptop class

class laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.name = brand + ' ' + model

laptop1 = laptop('IBM', '102', 20000)
laptop2 = laptop('HP', '121', 30000)

print(laptop1.name)
print(laptop2.model)