x = [1,2,3]
y = [10,20,30,40,50]

for i in x:
    for j in y:
        print(i*j)
    print("\n")

var = int(input("Enter a number :  "))
if var > 0:
    print("The number if positive number ! ")
    if var > 10:
        print("the number is higher that 10 ! ")
elif var < 0:
    print("Number is negative ! ")
    if var < -10:
        print("the number is lower that -10 ! ")
else:
    print("Number is ZERO ! ")
