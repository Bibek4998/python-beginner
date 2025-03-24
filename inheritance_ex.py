# Example of the inheritance in Python Programming.
class students:
    def __init__(self,name,address): #This is the constructor of the class.
        self.name=name
        self.address=address
    def show(self): #This method is used to display the information of the students.
        print(f"Name: {self.name}")
        print(f"Address:{self.address}")
display=students("Bibek","Dhangadhi") #This is the object of the class students.
display.show() #This will display the information of the students.