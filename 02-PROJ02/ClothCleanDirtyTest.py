from ClothCleanDirty import *

obj1=laundry()
obj2=obj1
print(id(obj1))
print(id(obj2))
print(obj1 is obj2)

obj1.make_dirty()
print(obj2.clean)

obj2.make_clean()
print(obj1.clean)

obj3=laundry()
obj4=laundry()
print(id(obj3))
print(id(obj4))
print(obj3 is obj4)

obj3.make_dirty()
print(obj4.clean)

obj4.make_clean()
print(obj3.clean)
