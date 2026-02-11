import csv

filePath= "<PATH>\groceries.csv"

with open(filePath,"r") as fileHandle:
    csvReader=csv.reader(fileHandle)
    headerIgnored=next(csvReader)

    for row in csvReader:
 #       row[1]=int(row[1])
        print(row[0],"quantity --->",str(row[1]))