str = "0123456789"

print(str[0])
print(str[3])
print(str[9])
print("\n")
print(str[-1])
print(str[-2])
print("\n")
print(len(str))
print("\n")

#IndexError: string index out of range
print(str[len(str)])
