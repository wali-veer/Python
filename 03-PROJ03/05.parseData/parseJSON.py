import json

filePath= "<PATH>\groceries.json"

with open(filePath,'r') as fileHandle:
    data=fileHandle.read()

parsedData=json.loads(data)
print(parsedData)

for item, quantity in parsedData.items():
    print(item, " and the quantity is ", str(quantity))

print(parsedData["apples"])