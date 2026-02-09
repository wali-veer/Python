'''
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions
'''
print("----- LIST -------")
print("----- 1 -------")
list1 = []
for i in range(10):
    res = i ** 2
    list1.append(res)
print(type(list1))
print(list1)

print("----- 2 -------")
list2 = [x ** 2 for x in range(10)]
print(type(list2))
print(list2)

print("----- 3 -------")
list3 = [x ** 2 for x in range(10) if x%2 == 0]
print(type(list3))
print(list3)

print("\n----- SET -------")
print("----- 1 -------")
set1 = {x ** 3 for x in range(10)}
print(type(set1))
print(set1)

print("\n----- SET -------")
print("----- 1 -------")
dict1 = {x:x ** 3 for x in range(10)}
print(type(dict1))
print(dict1)


print("\n\n\n")


'''
----- LIST -------
----- 1 -------
<class 'list'>
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
----- 2 -------
<class 'list'>
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
----- 3 -------
<class 'list'>
[0, 4, 16, 36, 64]

----- SET -------
----- 1 -------
<class 'set'>
{0, 1, 64, 512, 8, 343, 216, 729, 27, 125}

----- SET -------
----- 1 -------
<class 'dict'>
{0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}

'''
