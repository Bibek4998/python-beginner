age=int(input("Enter your age:"))
if age < 18:
    print("You are too youg to get a driving license...")
elif age >= 18 and age < 60:
    print("You are eligble to get a driving license...")
elif age > 60:
    print("You are too old to get a driving license..")
else:
    print("You entered the wrong data...")