class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display_details(self):
        print("Name: ", self.name)

        if self.age is not None:
            print("Age: ", self.age)
        
        if self.address is not None:
            print("Address: ", self.address)

p1 = Person("Sara")
p2 = Person("Sara", 21)
p3 = Person("Sara", 21, "Mumbai")

print(p1.display_details())
print(p2.display_details())
print(p3.display_details())
