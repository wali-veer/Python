phoneBook = {'Veer': 12345,'Raj': 67890,'Chin': 9876,'Rup':54321}

print(phoneBook['Veer'])
print(hash('Veer'))

#print(phoneBook['mom'])
phoneBook['mom'] = 34567
print(phoneBook['mom'])

phoneBook['mom'] = 287364283462 #this has overwritten the last entry
print(phoneBook['mom'])

phoneBook['mom'] = ('287364283462','34567') #you can practically use any datatype as value. It can be another dictionary
print(phoneBook['mom'])

print('++++++++++++')

def get_key (value_of_key):
    for key, value in phoneBook.items():
        if value == value_of_key :
            return key
            
print(get_key(12345))
print(get_key(12345122))