# This is the file example in which we will store the user details in the file.
# We will take the user input then store those information in the file..
name=str(input("Enter your name: "))
age= int(input("Enter your age: "))
address=str(input("Enter your address: "))
details=open("userDetail.txt",'w')
details.write(f"The name is:{name}, age is: {age} address is: {address}")
print(name,age,address)
details.close()
