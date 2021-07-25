'''
open()
https://docs.python.org/3/library/functions.html#open

Python - Files I/O
https://www.tutorialspoint.com/python/python_files_io.htm
'''

fObj = open("TrankTest.txt","w+")

fObj.write("This is a test for truncate function! \n")
fObj.write("This is a test for truncate function second line! \n")

fObj.close()

fObj1 = open("TrankTest.txt","r+")

print(fObj1.readlines())
print("\n")

fObj1.seek(0)

fObj1.truncate(20)
print(fObj1.readlines())
print("\n")

fObj1.close()
