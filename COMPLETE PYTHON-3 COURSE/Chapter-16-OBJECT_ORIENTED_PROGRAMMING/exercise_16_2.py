class laptop:
    discount_percent = 10 # class variable
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.name = brand + ' ' + model
    
    def apply_discount(self):
        # when use class variable use 'class'
        # return f"After applying {laptop.discount_percent}% discount. Now you have to pay only {(self.price -(self.price*laptop.discount_percent)/100)}"
        
        # when use method variable use 'self'
        return f"After applying {self.discount_percent}% discount. Now you have to pay only {(self.price - (self.price*self.discount_percent)/100)}"

# laptop.discount_percent = 0 # can change discount values
laptop1 = laptop('IBM', '102', 20000)
laptop2 = laptop('HP', '121', 30000)
laptop2.discount_percent = 50 # discount for a perticualr laptop

print(laptop1.apply_discount())
print(laptop2.apply_discount())
#print(laptop1.__dict__) # display instance variables of class