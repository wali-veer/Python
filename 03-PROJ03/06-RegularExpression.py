import re

exampleText = "My phone number is 918472-224455 and 918473-999999"

phoneRegEx=re.compile(r"\d\d\d\d\d\d-\d\d\d\d\d\d")
result=phoneRegEx.search(exampleText)

if result:
    print(result.group())
    print("The area code is ", result.group()[0:6])

print("-------------")
matches = re.findall(r"\d\d\d\d\d\d-\d\d\d\d\d\d",exampleText)
if matches:
    for item in matches:
        seperated=item.split("-")
        print("Area code " , seperated[1])
        print("Phone number is " , seperated[0])
        print("-------------")
