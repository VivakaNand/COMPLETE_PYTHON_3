class laptop:
    count_instance = 0
    def __init__(self, brand, model, price):
        laptop.count_instance += 1
        self.brand = brand
        self.model = model
        self.price = price
        self.name = brand + ' ' + model

laptop1 = laptop('IBM', '102', 20000)
laptop2 = laptop('HP', '121', 30000)
laptop3 = laptop('HP', '121', 30000)
laptop4 = laptop('HP', '121', 30000)

print(laptop.count_instance)