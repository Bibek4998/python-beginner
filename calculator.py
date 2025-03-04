# This is the python code for calculator...
userInput=int(input("Enter the number: "))
userInput2=int(input("Enter the number: "))
operator=input("Enter the operator: ")
if operator == '+' :
   sum=userInput+userInput2
   print(f"The summation of {userInput} and {userInput2} is:{sum}")
elif operator == '-':
    sub=userInput-userInput2
    print(f"The subtraction of {userInput} and {userInput2} is: {sub}")
elif operator == '*':
    multi=userInput * userInput2
    print(f"The multiplication of {userInput} and {userInput2} is: {multi}")
elif operator == '/':
    divide= userInput/userInput2
    print(f"The division of {userInput} and {userInput2} is: {divide}")
else:
    print("You entered the invalid operator")