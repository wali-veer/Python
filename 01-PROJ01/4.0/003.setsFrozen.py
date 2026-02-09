list1=(1,2,3,4,5,6)
list2=(4,5,6,7,8,9)

fs1=frozenset(list1)
fs2=frozenset(list2)

print(fs1)
print(fs2)
print(type(fs1)) #<class 'frozenset'>
print(type(fs2)) #<class 'frozenset'>

print("\n")

#frozensets are immutable
#fs1.add(10) #AttributeError: 'frozenset' object has no attribute 'add'
#fs1.remove(2) #AttributeError: 'frozenset' object has no attribute 'remove'
#fs1.pop() #AttributeError: 'frozenset' object has no attribute 'pop'
#fs1.clear() #AttributeError: 'frozenset' object has no attribute 'clear'
print(fs1)

print("\n")

print(fs1.intersection(fs2))
print(fs1.union(fs2))
print(fs1.difference(fs2))


print("\n\n")
