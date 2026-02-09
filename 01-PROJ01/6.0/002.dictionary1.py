d = {"name": "naam", "age":12, "city":"bangalore"}
print(d)
print(type(d)) #<class 'dict'>
print("\n")

print(d.keys())
print(list(d.keys()))
print(type(d.keys())) #<class 'dict_keys'>
print("\n")

print(d.values())
print(list(d.values()))
print(type(d.values())) #<class 'dict_values'>
print("\n")

print(d.items())
print(list(d.items()))
print(type(d.items())) #<class 'dict_items'>
print("\n")

print(d["name"])

d["college"]="Mysore"
print(d)


print("\n")
print("\n")
