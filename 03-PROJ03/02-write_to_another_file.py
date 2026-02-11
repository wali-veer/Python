fileHandle = open("My_Practice\InputData.txt", "r")
passedMemebers = open("My_Practice\passedMemebers.txt", "w")
failedMemebers = open("My_Practice\\failedMemebers.txt", "w")

for line in fileHandle:
    pass_or_fail = line.split()
    if pass_or_fail[2] == "Pass":
        passedMemebers.write(line)
    else:
        failedMemebers.write(line)

fileHandle.close()

passedMemebers.close()

failedMemebers.close()
