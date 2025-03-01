# The operators in the python are as follows>>>
# Arithmetic Operators(+,-,*,/,%)
# Assignment Operators(+=,-=,*=,/=)
# Bitwise Operators(&,|,~)
# Comparison Operators(==,!=,<,>,<=,>=)
# Logical Operators(and,or,not)
# Identity Operators(is, is not)
# Membership Operators (in, not in)

# Arithmetic example >>>>>
a=10
b=20
c=a+b #You can assign the other operators also (-,*,/)
print(c)

# Assignment example
x=90
x *= 50
print(x)

# Comparison example
x=10
if x>=20:
    print("The value of x is equal to 10")
elif x > 10:
    print("The value of x is greater than the 10 ")
elif x<10:
    print("The value is less than 10")    
elif x==10:
    print("The value is equal to 10")
else:
    print("The value of x is not equal.")

# Biwise Operator example>>>>
a=20
b=20
c=10
if a & b | c ==a==b==c:
    print("They are qual to each other.")
else:
    print("Theya are not equal to each other.")

# Logical example>>>>
a=40
b=550
c=665
if a and b > c:
    print(f"{a},{b} are greater than {c}.")
elif  a or b < c:
    print(f"{a} or {b} are smaller than {c}")
else:
    print(f"{a},{b} are not greater than {c}. ")

# Indentity example>>>>>
x = ["Bibek", "Aayush"]
y = ["Bibek", "Aayush"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# Membership example
a=["Bibek","Aayush","Ankit","Subhman"]
print("Bibek" in a) #This will return the true beacause it has the value Bibek in it.
print("Sujan" in a) #This will return the false value beacause there is no Sujan in the variable a.