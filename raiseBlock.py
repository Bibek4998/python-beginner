age=int(input("Enter your age:"))
if age<0:
        raise Exception("Age can not be 0..")
elif age<18:
        print("You are not eligible to vote..")
else:
        print("You are eligible for voting.")