fileObj=open("FileWriteMore.txt","w")
fileObj.write("this is a test line ! \n")
fileObj.write("this is SECOND line ! ")

print(fileObj.mode)

fileObj.close()

fileObj1=open("FileWriteMore.txt","r")
print ( fileObj1.readlines())  # This will return the "list of lines"
print(fileObj1.mode)


fileObj2=open("FileWriteMore.txt","a")
print(fileObj1.closed)
fileObj2.writelines("\nThis is another line ! ")
fileObj2.close()

print(fileObj2.mode)

fileObj1.seek(0)
print(fileObj1.read())
fileObj1.close()
print(fileObj1.closed)

print("\n ======================")

with open("FileWriteMode2.txt","w") as fWrite:
    fWrite.writelines("This is first line \n")
    fWrite.writelines("This is second line \n")
    fWrite.writelines("This is third line \n")

print(fWrite.closed)

print("\n\n")
