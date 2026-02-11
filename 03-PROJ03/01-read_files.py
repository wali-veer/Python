fileInput = open("My_Practice\InputData.txt", "r")
print(fileInput.read())
fileInput.close() 

fileInput = open("My_Practice\InputData.txt", "r")
for line in fileInput:
    select_col=line.split()
    if select_col [2] == "Pass":
        print(select_col[0] + " " + select_col[1] +" year old is passed")
    else:
        print(select_col[0] + " " + select_col[1] +" year old is failed")
fileInput.close()