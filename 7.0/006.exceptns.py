#https://docs.python.org/3/tutorial/errors.html
#https://docs.python.org/3/library/exceptions.html
print("\n\n\n")
v1 = int(input("enter a number ! :  "))
v2 = int(input("and should be devided into ! :  "))

try:
    print(int(v1/v2))
except ZeroDivisionError as e :
    print ("cannot be devided by Zero : " , e)
else:
    print("Success")
finally:
    print("I am shameless and will execute anyway")
print("---- outside -----")

print("\n\n")

l1 = [1,2,3,4]

try:
    print(l1[10])
except IndexError as e :
    print ("index error : " , e)
else:
    print("Success")
finally:
    print("STILL, I am shameless and will execute anyway")
print("---- 2nd time outside -----")



print("\n\n\n")
