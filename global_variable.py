# This the example of global variable in Python programming.
name="Bibek"
def myfunction():
    print("Hello, my name is " + name)
myfunction()

# The above code will print "Hello, my name is Bibek" because the variable name is defined outside of the function and is accessible within the function.

# We will look for another global variable example in Python programming.
a=10
def sum():
    a=21
    print(f"The number is {a}")
sum()
# The above code will print "The number is 21" because the variable a is defined inside the function and is local to that function. The global variable a is not accessible within the function.