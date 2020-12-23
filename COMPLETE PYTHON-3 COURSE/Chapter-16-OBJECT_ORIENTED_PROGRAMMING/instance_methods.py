# instance methods

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
        return self.age>18

p1 = Person('Vivek', 'Vishan', 25)
p2 = Person('Aneel', 'Vishan', 30)

print(p2.full_name())
print(p2.is_above_18())

l = [1,2,3]
# clear , pop
#l.clear()
#print(l)
#list.clear(l)
#print(l)
#l.append(10)
#print(l)
list.append(l,10)
print(l)