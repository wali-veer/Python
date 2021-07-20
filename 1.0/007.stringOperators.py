s1 = "Hello "
s2 = "World!"
print(s1+s2)
print("\n")

s3 = " Hello Hi"
print(s3*3)

print("\n")
print("ll" in s3)
print("ih" not in s3)

print("\n")

print("My name is %s, I am %d year old and I have %f floating things  " % ("veeresh", 30,1000.909))
print("My name is %s, I am %d year old and I have %.2f floating things  " % ("veeresh", 30,1000.909))
print("My name is %s, I am %d year old and I have %.f floating things  " % ("veeresh", 30,1000.909))

print("\n")

print("My name is {}, I am {} year old and I have {} numbers".format("veeresh",29,1000000.0909))
print("My name is {0}, I am {1} year old and I have {2} numbers".format("veeresh",27,0.0909))
print("My name is {2}, I am {1} year old and I have {2} numbers".format("veeresh",27,0.0909)) #My name is 0.0909, I am 27 year old and I have 0.0909 numbers
print("This is index {1}, although it should have been index {0}".format(0,1)) #This is index 1, although it should have been index 0




print("\n\n")
