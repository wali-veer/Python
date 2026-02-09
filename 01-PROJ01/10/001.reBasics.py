"""
https://www.tutorialspoint.com/python3/python_reg_expressions.htm
"""




import re

str = "This is a sample string to test regular expression"

matchObj = re.match("This",str)
print(matchObj)
print(type(matchObj))
print(matchObj.group())
print("\n")
'''
:output:
<re.Match object; span=(0, 4), match='This'>
<class 're.Match'>
This
'''

matchObj2 = re.match("abcd",str)
print(matchObj2)
print(type(matchObj2))
#print(matchObj2.group())
print("\n")
'''
:output:
None
<class 'NoneType'>
'''

matchObj3 = re.match("this",str,re.I)
print(matchObj3)
print(type(matchObj3))
print(matchObj3.group())
'''
::output::
<re.Match object; span=(0, 4), match='This'>
<class 're.Match'>
This
'''
print("\n")

str2 = "22.22.22.1     0    b4:a9:5a:ff:c8:45 VLAN#222      L"
matchObj4 = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*",str2)

'''result is '22.22.22.1'; 'r' means the pattern should be treated like a raw string;
any pair of parentheses indicates the start and the end of a group;
if a match is found for the pattern inside the parentheses,
then the contents of that group can be extracted with the group() method applied to the match object;
in regex syntax, a dot represents any character, except a new line character;
the plus sign means that the previous expression, which in our case is just a dot, may repeat one or more times;
the question mark matching as few characters as possible
'''

print(matchObj4.group(1) + " ----->   group 1" )
print(len(matchObj4.group(1)))

print(matchObj4.group(2)  + " ----->   group 2" )
print(len(matchObj4.group(2))  )

print(matchObj4.group(3) + " ----->   group 3" )
print(len(matchObj4.group(3))   )

print(matchObj4.group(4)  + " ----->   group 4" )
print(len(matchObj4.group(4)) )

print(matchObj4.groups())

print(matchObj4.group())
print(len(matchObj4.group()))

print("\n\n")

str3 = "22.22.22.1     0    b4:a9:5a:ff:c8:45 VLAN#222      L"

matchObj5 = re.findall(r"(\d\d)\.(\d{2})\.([0-9][0-9])\.([0-9]{1,3})",str3)
print(matchObj5)  #[('22', '22', '22', '1')]

matchObj6 = re.findall(r"\d\d\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}",str3)
print(matchObj6) #['22.22.22.1']

str4 = "22.22.22.1     0    b4:a9:5a:ff:c8:45 VLAN#222      L   11.22.33.4"
matchObj7 = re.findall(r"\d\d\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}",str4)
print(matchObj7)  #['22.22.22.1', '11.22.33.4']

str5 = "22.22.22.1     0    b4:a9:5a:ff:c8:45 VLAN#222      L   11.22.33.4"
str6=re.sub("\d","0",str5)
print(str6)  #00.00.00.0     0    b0:a0:0a:ff:c0:00 VLAN#000      L   00.00.00.0


print("\n\n\n")
