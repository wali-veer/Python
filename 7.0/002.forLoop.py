l = ['Dan','Man','Tan','Ban','Pan']
print(l)

for i in l :
    print (i)
else:
    print("end of FIRST for loop")
print("\n")

for i , v in enumerate (l):
    print(str(i)+" "+ v)
else:
    print("end of SECOND for loop")
print("\n")

for i in range(len(l)):
    print(l[i])
else:
    print("end of THIRD for loop")
print("\n\n")
