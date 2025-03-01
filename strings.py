# String example>>>>>
name="Bibek Raj Joshi"
age=19
address="Dadeldhura"
print(name)
print(age)
print(address)

txt="  Python is a programming Language! "
# python indexing>>>>>>>>>>>
print(f"The character in the index is: {txt[1]}")

# Python slicing>>>>>
print(f"The slicing characters are: {txt[2:5]}")

# Modifying the string>>>>>
# Changind the characters into upper case>>>>>
upper=txt.upper()
print(upper)

# Changing the characters into lower case character>>>>>
lower=txt.lower()
print(lower)
print(len(txt))

# Removing the whitespace in the text>>>>>>
whitespace=txt.strip()
print(whitespace)
print(len(whitespace))

# Replacing the strings >>>>>
replaced=txt.replace("P","C")
print(replaced)

# Spliting the string >>>>>
splited=txt.split(" ")
print(splited)

# Cocatinating the strings in different way>>>>
a= "Hello"
b="World"
c=a +" "+ b 
print(c)

# Escape characters in python.>>>>>
print("They are the  so-called \"Vikings\" from the north.")



