# 🐍 Python Strings — Complete Reference Guide

This document contains practical examples of common Python string operations, including indexing, slicing, formatting, joining, and built-in methods.

It can be used as:

-  Learning notes  
-  Revision cheat-sheet  
-  GitHub documentation  
-  Quick experimentation guide  

---

##  Defining Multi-Line Strings

Using triple quotes and the line-continuation character (`\`):

```python
my_string = '''this\
is\
my\
first\
string'''
```

---

##  String Indexing

```python
a = "Cisco Switch"

a.index("i")
```

---

##  Character Count

```python
a = "Cisco Switch"

a.count("i")
```

---

##  Finding a Substring

```python
a = "Cisco Switch"

a.find("sco")
```

---

##  Converting Case

```python
a = "Cisco Switch"

a.lower()   # lowercase
a.upper()   # uppercase
```

---

##  Starts With / Ends With

```python
a = "Cisco Switch"

a.startswith("C")
a.endswith("h")
```

---

##  Removing Characters From Start / End

```python
a = "   Cisco Switch   "
a.strip()          # remove whitespaces

b = "$$$Cisco Switch$$$"
b.strip("$")       # remove specific character
```

---

##  Removing All Occurrences of a Character

```python
a = "   Cisco Switch   "

a.replace(" ", "")
```

---

##  Splitting a String

Splitting by delimiter returns a list:

```python
a = "Cisco,Juniper,HP,Avaya,Nortel"

a.split(",")
```

---

##  Joining Characters Using a Delimiter

```python
a = "Cisco Switch"

"_".join(a)
```

---

##  Additional Useful String Methods

```python
capitalize()   # Capitalizes first letter
lstrip()       # Removes leading whitespace
rstrip()       # Removes trailing whitespace
swapcase()     # Inverts letter case
title()        # Converts to title case

isalnum()      # Alphanumeric check
isalpha()      # Alphabetic check
isdigit()      # Digits only
islower()      # Lowercase check
isnumeric()    # Numeric unicode check
isspace()      # Whitespace check
istitle()      # Title case check
isupper()      # Uppercase check
```

---

##  Concatenating Strings

```python
a = "Cisco"
b = "2691"

a + b
```

---

##  Repeating / Multiplying Strings

```python
a = "Cisco"

a * 3
```

---

##  Membership Testing

```python
a = "Cisco"

"o" in a
"b" not in a
```

---

##  String Formatting — Old Style (`%`)

```python
"Cisco model: %s, %d WAN slots, IOS %f" % ("2600XM", 2, 12.4)
"Cisco model: %s, %d WAN slots, IOS %.f" % ("2600XM", 2, 12.4)
"Cisco model: %s, %d WAN slots, IOS %.1f" % ("2600XM", 2, 12.4)
"Cisco model: %s, %d WAN slots, IOS %.2f" % ("2600XM", 2, 12.4)
```

---

##  String Formatting — `format()`

```python
"Cisco model: {}, {} WAN slots, IOS {}".format("2600XM", 2, 12.4)

"Cisco model: {0}, {1} WAN slots, IOS {2}".format("2600XM", 2, 12.4)
```

---

##  String Slicing Examples

```python
string1 = "O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2"

string1[5:15]     # from index 5 to 14
string1[5:]       # index 5 to end
string1[:10]      # start to index 9
string1[:]        # entire string

string1[-1]       # last character
string1[-2]       # second-to-last
string1[-9:-1]    # substring using negative indexes
string1[-5:]      # last 5 characters
string1[:-5]      # string without last 5 characters

string1[::2]      # skip every second character
string1[::-1]     # reverse string
```

---

##  Important Notes

- `index()` raises an error if the substring is not found.  
- `find()` returns `-1` when the substring does not exist.  
- Slicing is widely used in parsing logs, networking output, and NLP pipelines.

---

 **Happy Coding!**
