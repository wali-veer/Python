fileObject = open("Test.txt","r")

#reads entire file.
print(fileObject.read())

fileObject.seek(0)

print (fileObject.readline())
print("\n")
print(fileObject.tell())
print("\n")
print (fileObject.read(10))
print("\n")
print(fileObject.tell())
print("\n")
print (fileObject.read(10))
print("\n")
print(fileObject.tell())

#fileObject = open("Test.txt","x")  #FileExistsError: [Errno 17] File exists:


'''
Pune
Bangalore
Gulbarga
Hyderabad
Noida
Madras
Delhi

Pune

5
Bangalore

15
Gulbarga
H
25
'''
