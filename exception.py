try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a / b
    print("Division:", c)
except ZeroDivisionError:
    print("Divide by zero error...")
except ValueError:
    print("Invalid input! Please enter integers only.")
else:
    print("Program executed successfully")
finally:
    print("Always executed")
