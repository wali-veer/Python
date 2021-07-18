#https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

str = "This is a test"

print(len(str))
print(str.count("i"))
print(str.count("test"))
print(str.upper())
print(str.lower())
print(str.startswith("T"))
print(str.startswith("t"))
print(str.endswith("T"))
print(str.endswith("t"))
print(str.index("i"))
#print(str.index("q"))# ValueError: substring not found
print(str.find("is"))
print(str.find("su"))

print("\n")

# strip, split, join, replace

str2 = "  this is to test string   "
print(str2.strip())
print(str2.replace(" ",""))
str3 = "$$$$this is to test string$$$"
print(str3.upper().strip("$"))

print(str3.split(" "))
print("_".join(str3))


print("\n\n")
