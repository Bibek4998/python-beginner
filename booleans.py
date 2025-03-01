# Booleans examples>>>>>
a=True
b=False
print(f"The value of variable a is: {a}")
print(f"The value of variable b is:{b}")

# Using the bool function to evaluate the string and integer>>>>
print(bool("Hello, How are you?"))
print(bool(123))

print("Below statement will return the false value beacause these statements are either empty or 0 values.")
print(bool()) #This will return the false value beacause it is an empty.
print(bool([])) #This will also returns the false value.
print(bool("")) #This will also returns the false value beacause it is an empty string..
print(bool(0)) #The value is 0 and it will return the false value

# Using function >>>>
def myfunction():
    return False
if myfunction()==True:
    print("Today is my birthday")
else:
    print("Its not my birth-date")

# Using boolean function to check whether the given object is an integer or not.>>>>
a="This is the string"
b=300
print(isinstance(a,int))
print(isinstance(b,int))