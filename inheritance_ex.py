# Inheritance example in python programming.
class person:
    def __init__(self, name,age): # This is the constructor of the class.
        self.name=name
        self.age=age
    def display(self):  # This is the method of the class.
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
    def message(self):  # This is the method of the class.
         print("Welcome to the cursed world of Python programming.")    
x=person("Bibek Joshi",16)  # This is the object of the class.
x.display()     # This is the method calling.
x.message()



# Now we will create another class student which will inherit the properties of the class person.
# The class student will have two additional properties semester and address.
# The class student will have a method show() which will display the properties of the class student.


class student(person):
    def __init__(self, semester,address):
        self.semester=semester
        self.address=address
    def show(self):
            print(f"Semester: {self.semester}")
            print(f"Address: {self.address}")

y=student(5,"Kathmandu")
y.show()
