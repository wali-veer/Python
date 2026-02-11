filePath= "<PATH>\groceries.txt"

with open(filePath,'r') as fileHandler:
    line=fileHandler.read()
    print(line)
    print('------ Parsing the data -------')
    parsedData=line.split(",")
    print("Parsed Data  ----->", parsedData)

    print("item at index 6 is ", parsedData[6])




