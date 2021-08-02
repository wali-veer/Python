import re

Str = "This is a String 2 b3 used for testing the Reg Expre33io9"

mObj = re.findall(r"[a-z]",Str)
print(mObj) #['h', 'i', 's', 'i', 's', 'a', 't', 'r', 'i', 'n', 'g', 'b', 'u', 's', 'e', 'd', 'f', 'o', 'r', 't', 'e', 's', 't', 'i', 'n', 'g', 't', 'h', 'e', 'e', 'g', 'x', 'p', 'r', 'e', 'i', 'o']

mObj = re.findall(r"[A-Z]",Str)
print(mObj) #['T', 'S', 'R', 'E']

mObj = re.findall(r"[0-9]",Str)
print(mObj) #['2', '3', '3', '3', '9']

mObj = re.findall(r"[a-e]",Str)
print(mObj) #['a', 'b', 'e', 'd', 'e', 'e', 'e', 'e']

mObj = re.findall(r"[aigr]",Str)
print(mObj) #['i', 'i', 'a', 'r', 'i', 'g', 'r', 'i', 'g', 'g', 'r', 'i']

mObj = re.findall(r"[^aigr]",Str)
print(mObj) #['T', 'h', 's', ' ', 's', ' ', ' ', 'S', 't', 'n', ' ', '2', ' ', 'b', '3', ' ', 'u', 's', 'e', 'd', ' ', 'f', 'o', ' ', 't', 'e', 's', 't', 'n', ' ', 't', 'h', 'e', ' ', 'R', 'e', ' ', 'E', 'x', 'p', 'e', '3', '3', 'o', '9']

mObj = re.findall(r"[0-2]",Str)
print(mObj) #['2']

mObj = re.findall(r"[0-5]",Str)
print(mObj) #['2', '3', '3', '3']

mObj = re.findall(r"[^a-z,^A-Z,^\s,^3]",Str)
print(mObj) #['2', '9']


Str2 = "I am enjoying learning a programming language such as Java 8"
mObj2 = re.search(r"\W(\w{2}\W)",Str2)
print(mObj2.group(1)) #am
mObj3 = re.search(r"\W(\w{5}\W)|([A-Z]\w{3})\s\d",Str2)
print(mObj3.group(2)) #Java
mObj4 = re.search(r"([a-z]\w{10})",Str2)
print(mObj4.group(1)) #programming


print("\n\n\n")
