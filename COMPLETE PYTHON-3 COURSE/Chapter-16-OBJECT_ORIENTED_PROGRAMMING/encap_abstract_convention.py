# Encapsulation # use usefull data and functions at one place in class
# Abstraction # to hide complexity
# Some special naming convention
# Name Mangling, __name (not a convention)

class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        # self.price = price
        # self._price = price # _name is convention for private name
        self.__price = price

    def make_a_call(self, phone_number):
        print(f"calling {phone_number} ...")
    
    def full_name(self):
        return f"{self.brand} {self.model_name}"
    
    def send_message(self):
        pass # twilio

phone1 = Phone('Nokia', '1100', 1000)
# print(phone1.__price)
print(phone1._Phone__price)
phone1._Phone__price = -1000
print(phone1._Phone__price)
#print(phone1.__dict__)

# phone1._price = -1000
# print(phone1._price)
# _name # convention for private name
# __name__ # dunder/magic methods


# l = [3,4,2,1]
# l.sort() # here we are using sort method to sort the list but we don't know the basic algorithm behind it, here complexity is hide 
# print(l)
