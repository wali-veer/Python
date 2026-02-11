import csv

filePath= "C:\\Users\\Veeresh\\Documents\\LinkedInLearning\\Python\\Ex_Files_Using_Python_for_Automation\\Ex_Files_Using_Python_for_Automation\\Exercise Files\\My_Practice\\05.parseData\\groceries.csv"

with open(filePath,"r") as fileHandle:
    csvReader=csv.reader(fileHandle)
    headerIgnored=next(csvReader)

    for row in csvReader:
 #       row[1]=int(row[1])
        print(row[0],"quantity --->",str(row[1]))