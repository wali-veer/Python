t = ()
print(t)
print(type(t)) #<class 'tuple'>

print("\n")
t=(2)
print(t)
print(type(t)) #<class 'int'>

print("\n")
t=(9,)   #for single element a comma is mandatory to make it touple.
print(t)
print(type(t)) #<class 'tuple'>

print("\n")
t=(1,2,3,4,5,6,7)
print(t)
print(t[1])
print(t[-1])
print(t[-3])
print(t[4])

print("\n")
#tuple are immutable.
#t[3]=4 #TypeError: 'tuple' object does not support item assignment
#del t[3] #TypeError: 'tuple' object doesn't support item deletion.

#Touple packing and unpacking.
t1=("Naveen","Bajaj",30)
(name, lname, age)=t1
print(name+" "+ lname +" "+ str(age))

print("\n")
#Same number of variables.
#(name, lname, age,city)=t1 #ValueError: not enough values to unpack (expected 4, got 3)
#(name, lname)=t1 #ValueError: not enough values to unpack (expected 4, got 3)

print("\n")
(a,b,c) = (100,200,300)
print(a)
print(b)
print(c)

print("\n\n")
