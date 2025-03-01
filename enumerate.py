# Example of enumerate function in python....
fruits=["Apple","Banana","Pineapple","Orange","Papaya"]
print("This will print the index and value but from the index 2 because we gave a index 2 in the enumerate()")
for indexes, fru in enumerate(fruits, start=2):#This is the index we provided it will start from the index 2...
    print(indexes,fru) 
print("This will print the index and element from the index 0 (default)")
for index, fruit in enumerate(fruits): #We can pass the two arguments in the enumerate function...
    print(index,fruit)
    
# The enumerate function might not be useful in the data structures like dictionaries and sets as they are unorderd.