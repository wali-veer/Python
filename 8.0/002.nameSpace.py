# ---- NAME SPACES ------
#  1) Built-in namespace
#  2) Global namespace
#  3) Local namespace

var1 = 100

def func(a,b,c,d, *args):
    global var1
    var1 = 3
    var2 = 0
    print (a*b*c*d)
    print(args)
    print(type(args))

func(1,2,3,4,5,6,7,8,9)

print(var1)
#print(var2) #NameError: name 'var2' is not defined

print ("\n")


def func2(a=10,b=20,c=30):
    return(a*b*c)

print(func2())  #Output 6000
print(func2(0))  #Output 0
print(func2(1,2))  #Output  60

print ("\n\n\n")

'''
#output
24
(5, 6, 7, 8, 9)
<class 'tuple'>
3


6000
0
60
'''
