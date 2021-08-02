print("\n Example 1 ------\n")

a = lambda x , y : x * y
print(a("abc ",3)) #abc abc abc
print(a(20,20)) #400

print("\n Example 2 ------\n")

def nonLabda(argList):
    storeRes = []
    for i in range(5):
        for j in range(5):
            product=i*j
            storeRes.append(product)
    return storeRes + argList
print(nonLabda([200,300,400]))

print("\n")

lamList = lambda myList : [i*j for i in range(5) for j in range(5) ] + myList
print(lamList([200,300,400]))

print("\n\n\n")
