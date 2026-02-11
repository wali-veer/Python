import json

filePath= "C:\\Users\\Veeresh\\Documents\\LinkedInLearning\\Python\\Ex_Files_Using_Python_for_Automation\\Ex_Files_Using_Python_for_Automation\\Exercise Files\\My_Practice\\05.parseData\\groceries.json"

with open(filePath,'r') as fileHandle:
    data=fileHandle.read()

parsedData=json.loads(data)
print(parsedData)

for item, quantity in parsedData.items():
    print(item, " and the quantity is ", str(quantity))

print(parsedData["apples"])