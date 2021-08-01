"""
\D --> Inverse of \d
\S --> Inverse of \s
\W --> Inverse of \w
\A --> Starts with Example : \AV , starts with V
\Z --> Ends with Example : Q\Z, ends with Z
"""

import re

str = "This is a sample text 2 test a Regular Expression in Python 3"

mObj1 = re.search(r"\D+", str) #This is a sample text
print(mObj1.group())

mObj2 = re.search(r"\S+", str)  #This
print(mObj2.group())

mObj3 = re.search(r"\AT", str)  #T
print(mObj3.group())

mObj4 = re.search(r"3\Z", str)  #3
print(mObj4.group())

print("\n\n\n")
