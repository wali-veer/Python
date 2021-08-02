import re

str = "This is a test string to practice subn and split regular expression function"

mObj = re.split(r" ",str)
print(mObj)        #['This', 'is', 'a', 'test', 'string', 'to', 'practice', 'subn', 'and', 'split', 'regular', 'expression', 'function']

mObj = re.split(r"\s",str)
print(mObj)        #['This', 'is', 'a', 'test', 'string', 'to', 'practice', 'subn', 'and', 'split', 'regular', 'expression', 'function']

print(str.split()) #['This', 'is', 'a', 'test', 'string', 'to', 'practice', 'subn', 'and', 'split', 'regular', 'expression', 'function']

mObj = re.split(r"\W(\w{2})\W",str)
print(mObj) #['This', 'is', 'a test string', 'to', 'practice subn and split regular expression function']

mObj = re.subn(r" ","_",str)
print(mObj) #('This_is_a_test_string_to_practice_subn_and_split_regular_expression_function', 12)

mObj = re.subn(r"\sis\s"," was ",str)
print(mObj) #('This was a test string to practice subn and split regular expression function', 1)


print("\n\n\n")
