filePath= "C:\\Users\\Veeresh\\Documents\\LinkedInLearning\\Python\\Ex_Files_Using_Python_for_Automation\\Ex_Files_Using_Python_for_Automation\\Exercise Files\\My_Practice\\05.parseData\\groceries.txt"

with open(filePath,'r') as fileHandler:
    line=fileHandler.read()
    print(line)
    print('------ Parsing the data -------')
    parsedData=line.split(",")
    print("Parsed Data  ----->", parsedData)

    print("item at index 6 is ", parsedData[6])




