l1 = [0,1,2,3,4]
l2 = [5,6,7,8,9]

for i in l1:
    for j in l2:
        if j >= 6:
            break
        print(str(i) + " * " + str(j) + " = " + str(i*j))
'''
output
0 * 5 = 0
1 * 5 = 5
2 * 5 = 10
3 * 5 = 15
4 * 5 = 20
'''




print ("\n")

for i in l1:
    for j in l2:
        if j >= 6 and j < 9:
            continue
        print(str(i) + " * " + str(j) + " = " + str(i*j))

print ("\n")

'''
output
0 * 5 = 0
0 * 9 = 0
1 * 5 = 5
1 * 9 = 9
2 * 5 = 10
2 * 9 = 18
3 * 5 = 15
3 * 9 = 27
4 * 5 = 20
4 * 9 = 36
'''



for i in l1:
    pass
'''
output

<pass does not execute anything
Its a place holder.
Nothing will be displayed in the output

'''
