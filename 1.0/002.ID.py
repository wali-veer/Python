
v1 = 100
print(v1)
print("\n")

v2 , v3 , v4 = 200 , 300, 400

print(id(v2))
print(id(200))
print("\n")

print(id(v3))
print(id(300))
print("\n")

print(id(v4))
print(id(400))

print("\n")

v4=v1
print(id(v4))
print(id(v1))
print(id(100))
