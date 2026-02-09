'''
- Object oriented programming is based on classes, methods and objects.
- class is like a variable of its own type containings - variable attributes and funcations (methods).
- Class is like a blueprint for creating an object.
- Object is an instance of the defined class. The attribute values of a defined object defines the state of that object.
- Class inheritance.

'''

class MyTest(object):
    def __init__ (self, num, str, flot):
        self.num = num
        self.str = str
        self.flot = flot

    def metd (self, dt):
        print("This is a number through method ---> " + str(self.num))
        print("This is a string through method ---> " + self.str)
        print("This is a float through method ---> " + str(self.flot))
        print("The date of expiry through method ---> " +  str(dt))

clssObj = MyTest(100,"test string", 1.34)
clssObj.metd(20210802)
print("\n")

print("This is a number through direct call  ---> " + str(clssObj.num))
print("This is a string through direct call  ---> " + clssObj.str)
print("This is a float through direct call  ---> " + str(clssObj.flot))

print("\n=====================")

clssObj2 = MyTest(10000,"test string of second object", 1.99999999)
clssObj2.metd(20290802)
print("\n")

print("This is a number through direct call  ---> " + str(clssObj2.num))
print("This is a string through direct call  ---> " + clssObj2.str)
print("This is a float through direct call  ---> " + str(clssObj2.flot))

print("\n=====================")

'''
getattr
setattr
hasattr
delattr
'''

print(getattr(clssObj2,"metd")) #<bound method MyTest.metd of <__main__.MyTest object at 0x7ff2eaa54bb0>>
#print(getattr(clssObj2,"metd2")) #AttributeError: 'MyTest' object has no attribute 'metd2'
print(getattr(clssObj,"flot")) #1.34
print(setattr(clssObj,"flot",99.99999))
print(getattr(clssObj,"flot")) #99.99999
print(hasattr(clssObj,"flot")) #True
print(hasattr(clssObj,"flot123")) #False
print(delattr(clssObj,"flot")) #None
print(hasattr(clssObj,"flot")) #False
print(hasattr(clssObj2,"flot")) #True

print("\n=====================")

print(isinstance(clssObj2,MyTest)) #True
print(isinstance(clssObj,MyTest))  #True
#print(isinstance(random,MyTest))  #NameError: name 'random' is not defined

print("\n\n\n")

print("\n========  Class inheritance =============\n")


class ChldClass(MyTest):
    def __init__(self, numC, strC, flotC, modelC):
        MyTest.__init__(self,numC, strC, flotC)
        self.modelC = modelC

    def methC(self, expDateC):
        print("This is from child class method " + str(expDateC) + " ---> " + str(self.modelC) )

objChld = ChldClass(999,"From Child class object",999.999, 10000)

objChld.methC(8888)
objChld.metd(20210804)

print("\n")

print(issubclass(ChldClass,MyTest)) #True
print(issubclass(MyTest,ChldClass)) #False

print("\n\n\n")
