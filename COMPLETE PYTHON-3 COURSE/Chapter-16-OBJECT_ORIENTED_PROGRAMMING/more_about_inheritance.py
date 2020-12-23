# we can drive more than two classes from base class
# multilevel inheritance
# method resulation order
# method overriding
# isinstance(), issubclass()
# Inheritance 

class Phone: # base class / parent class
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)
    
    def make_a_call(self, phone_number):
        print(f"calling {phone_number} ...")
    
    def full_name(self):
        return f"{self.brand} {self.model_name}"

class Smartphone(Phone): # drived / child class
    def __init__(self, brand,model_name,price,ram,internal_memory,rear_camera):

        # two ways 
        # 1 - by parent class
        # Phone.__init__(self,brand,model_name,price) # uncommon way
        # 2 - by super method
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera
    # method overriding
    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"


class FlagshipPhone(Smartphone):
    def __init__(self, brand,model_name,price,ram,internal_memory,rear_camera,front_camera):
        super().__init__(brand,model_name,price,ram,internal_memory,rear_camera)
        self.front_camera= front_camera


phone = Phone('Nokia', '1100',1000)
# smartphone = Smartphone('onePlus','S',30000,'6 GB','32 GB','30 MP')
# onePlus = FlagshipPhone('onePlus','S',30000,'6 GB','32 GB','30 MP','20 MP')
onePlus5 = Smartphone('onePlus','S',30000,'6 GB','32 GB','30 MP')
onePlus5t = FlagshipPhone('onePlus','S',30000,'6 GB','32 GB','30 MP','20 MP')

# print(phone.full_name())
# print(smartphone.full_name() + f" and price is {smartphone._price}")
# print(onePlus.full_name() + f" and front camera is {onePlus.front_camera}")
# print(onePlus.full_name())
# print(help(FlagshipPhone))

# isinstance() # it check object belongto class or not
# print(isinstance(onePlus5, FlagshipPhone))
# print(isinstance(onePlus5t, Phone))

#issubclass() # it checks subclass of parent classes
print(issubclass(FlagshipPhone,Smartphone))