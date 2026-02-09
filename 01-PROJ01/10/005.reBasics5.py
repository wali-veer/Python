import re

str = "This is an another string to test regular expression 7"

mObj = re.search(r"^[A-Z][a-z]{3}\s",str)
print(mObj.group()) #This

mObj = re.search(r"\s\d",str)
print(mObj.group()) #7

mObj = re.search(r"\w{10}\s\d",str)
print(mObj.group()) #expression 7

str1= "I am  zzzzzzzzzz   .....  sleeeeeping"

mObj1=re.search(r"\sz{10}\s",str1)
print(mObj1.group()) # zzzzzzzzzz

mObj1=re.search(r"\sz{1,}\s",str1)
print(mObj1.group()) # zzzzzzzzzz

mObj1=re.search(r"\sz{1,10}\s",str1)
print(mObj1.group()) # zzzzzzzzzz

mObj1=re.search(r"\sz{1,10}?",str1)
print(mObj1.group()) # z

mObj1=re.search(r"\sz{5,10}?",str1)
print(mObj1.group()) # zzzzz

print("\n\n\n")
