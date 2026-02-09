list1 = [1,2,3,5,6,7,8,2,3,4,6,7]
print(sorted(list1))
print("\n")

set1=set(list1)
print(set1)
print(type(set1)) #<class 'list'>
print("\n")

set2=set([11,11,12,12,13,13,14,14])
print(set2)
print("\n")

print(len(set1))
print(len(set2))
print("\n")

#set are mutable

print(11 in set2)
print(100 in set2)
print(100 not in set2)
print("\n")

print(set1)
set1.add(100)
print(set1)

set1.add(2)
print(set1)

set1.remove(100)
print(set1)


print("\n\n")
