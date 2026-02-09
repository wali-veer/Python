set1 = {1,2,3,4,5,6}
set2 = {5,6,7,8,9,0}

print(set1.intersection(set2)) #{5, 6}
print(set2.intersection(set1)) #{5, 6}
print("\n")
print(set1.difference(set2)) #{1, 2, 3, 4}
print(set2.difference(set1)) #{0, 8, 9, 7}
print("\n")
print(set1.union(set2)) #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set2.union(set1)) #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print("\n")
print(set1.pop()) #1
print(set1.pop()) #2
print("\n")
print(set1.clear()) #None
