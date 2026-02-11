import xml.etree.ElementTree as ET

filePath= "<PATH>\groceries.xml"

tree=ET.parse(filePath)

root=tree.getroot()

itemsOverSix=[]

for item in root.findall("grocery_item"):
    name=item.find("name").text
    price=item.find("price").text
    print("Item name is", name, "price -->", price)

    if float(price) > 6:
        itemsOverSix.append(name)

print("---- The list of items priced over six ----")
for ios in itemsOverSix:
    print(ios)
