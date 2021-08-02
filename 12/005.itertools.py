from itertools import *

l1 = [1,2,3,4,5,"a","b","c"]
l2 = [6,7,8,9,0,"d","e","f"]

print("---------- chain ------------\n")
print(list(chain(l1,l2))) #[1, 2, 3, 4, 5, 'a', 'b', 'c', 6, 7, 8, 9, 0, 'd', 'e', 'f']

print("\n")

for i in (chain(l1,l2)):
    print(i)

print("\n")

'''
----- output ---
[1, 2, 3, 4, 5, 'a', 'b', 'c', 6, 7, 8, 9, 0, 'd', 'e', 'f']


1
2
3
4
5
a
b
c
6
7
8
9
0
d
e
f
'''

print("---------- count ------------\n")

print("\n")

for i in count(10 , 2.5):
    if i <= 50 :
        print (i)
    else:
        break

print("\n")

'''
----- output ---
10
12.5
15.0
17.5
20.0
22.5
25.0
27.5
30.0
32.5
35.0
37.5
40.0
42.5
45.0
47.5
50.0
'''

print("---------- cycle ------------\n")

a = range (15,21)
loopBreakCounter =0
for i in cycle (a):
    print(i)
#without below two "if condictions" cycle will go into indefinite loop
    if i == 20:
        print (str(loopBreakCounter) + "--------")
        loopBreakCounter += 1
    if loopBreakCounter > 20:
        break

'''
15
16
17
18
19
20
0--------
15
16
17
18
19
20
1--------
15
16
17
18
19
20
2--------
15
16
17
18
19
20
3--------
15
16
17
18
19
20
4--------
15
16
17
18
19
20
5--------
15
16
17
18
19
20
6--------
15
16
17
18
19
20
7--------
15
16
17
18
19
20
8--------
15
16
17
18
19
20
9--------
15
16
17
18
19
20
10--------
15
16
17
18
19
20
11--------
15
16
17
18
19
20
12--------
15
16
17
18
19
20
13--------
15
16
17
18
19
20
14--------
15
16
17
18
19
20
15--------
15
16
17
18
19
20
16--------
15
16
17
18
19
20
17--------
15
16
17
18
19
20
18--------
15
16
17
18
19
20
19--------
15
16
17
18
19
20
20--------
'''

print("\n---------- filter ------------\n")

print(list(filter((lambda i : i > 5) ,[1,2,3,4,5,6,7,8,9,10])))  #[6, 7, 8, 9, 10]

print("\n---------- filterfalse ------------\n") 

print(list(filterfalse((lambda i : i > 5) ,[1,2,3,4,5,6,7,8,9,10]))) #[1, 2, 3, 4, 5]


print("\n---------- islice ------------\n")

print(list(range(10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10))[2:10]) #[2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10))[2:10:2]) #[2, 4, 6, 8]
print(list(islice(range(10),2,10))) #[2, 3, 4, 5, 6, 7, 8, 9]
print(list(islice(range(10),2,10,2))) #[2, 4, 6, 8]

print("\n\n\n\n")
