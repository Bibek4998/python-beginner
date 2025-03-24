# This is the example of string representation in Python programming.
class stringExample:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old."
student=stringExample("Bibek", 16)
print(student)