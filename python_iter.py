 # Python iterables.
# An iterable is an object that can be iterated upon and string is an iterable object.

name="Bibek Raj Joshi"
nameIter=iter(name)
a=next(nameIter)
b=next(nameIter)
c=next(nameIter)
d=next(nameIter)
e=next(nameIter)
f=next(nameIter)


print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
 # Now we will iterate the list .

print("List iteration using the next() function.")


names=["Bibek","Sudip","Aayush","Ankit","Khadga"]
listIter=iter(names)
g=next(listIter)
h=next(listIter)
i=next(listIter)
j=next(listIter)
k=next(listIter)
print(g)
print(h)
print(i)
print(j)
print(k)
