class Student:
    def __init__(self, _name, _roll_no, _marks):
        self._name = _name
        self._roll_no = _roll_no
        self._marks = _marks

    # getter for name 
    def get_name(self):
        return self._name
    
    # setter for name
    def set_name(self, name):
        if name.strip() != "":
            self._name = name
        else:
            print("Name cannot be empty")

    # getter for roll no
    def get_roll_no(self):
        return self._roll_no
    
    # setter for roll no
    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100:
            self._roll_no = roll_no
        else:
            print("Roll no has to be between 1 and 100")

    # getter for marks
    def get_marks(self):
        return self._marks
    
    # setter for marks
    def set_marks(self, marks):
        if marks >= 0:
            self._marks = marks
        else:
            print("Marks should not be negative")

s1 = Student("Sara", 1, 49)

print(s1.get_name())
print(s1.get_roll_no())
print(s1.get_marks())

s1.set_name("Saara")
s1.set_roll_no(2)
s1.set_marks(50)

print(s1.get_name())
print(s1.get_roll_no())
print(s1.get_marks())
