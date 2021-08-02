def product10(a):
	return a * 10

list1 = range(10)
print(type(map(product10, list1)))  #<class 'map'>
print(list(map(product10, list1)))  #[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(list(map((lambda b : b * 10), range(10)))) #[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

print(list(filter((lambda c :  c > 10 ),range(15)))) #[11, 12, 13, 14]

'''
<class 'map'>
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
[11, 12, 13, 14]
[Finished in 0.058s]
'''
