# TUPLES

t1=(23,12,45,56,34)

print(t1)
print(len(t1))
print(min(t1))
print(max(t1))
print(t1+(1,2,3,4,5))
print(t1*2) #(23, 12, 45, 56, 34, 23, 12, 45, 56, 34)
print(t1[2:4])
print(t1[-1])
print(t1[-4:-2]) #(12, 45)
print(t1[::-1]) #(34, 56, 45, 12, 23)
print(t1[::2]) #(23, 45, 34)

print(t1[-2:]) #(56, 34)
print(t1[-1::-1]) #(34, 56, 45, 12, 23)

print("\n")
print(3 in t1)
print(56 in t1)
print(56 not in t1)

print(t1)
del t1
#print(t1) #NameError: name 't1' is not defined

print("\n\n")
