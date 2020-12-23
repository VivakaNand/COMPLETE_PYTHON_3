# multiple inheritance


class A:

    def class_a_method(self):
        return 'I\'m just a class A method'

    def hello(self):
        return 'hello from class A'

class B:
    def class_b_method(self):
        return 'I\'m just a class B method'

    def hello(self):
        return 'hello from class B'

class C(B,A):
    pass

#instance_a = A()
#print(instance_a.class_a_method())
#print(instance_a.hello())

#instance_b = B()
#print(instance_b.class_b_method())
#print(instance_b.hello())

instance_c = C()
print(instance_c.class_a_method())
print(instance_c.class_b_method())
print(instance_c.hello())
print(help(C)) # resulation order check
#print(C.mro())
