class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        def show(self):
            print("A person")
class nurse(person):
    def show(self):
        print("She is a nurse.")
class driver(person):
    def show(self):
        print("He is a driver")

class doctor(person):
    def show(self):
        print("He is a doctor")
nurse1=nurse("Radha",21)
driver1=driver("Ram",23)
doctor1=doctor("D.R. Bishal",32)
for x in (nurse1,driver1,doctor1):
    print(x.name,x.age)