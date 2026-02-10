#List test

sink = ['Plate','Bowl','Spoon']
print (f'The list sink contain following dishes : {sink}')
for item in sink:
    print(f'Put the {item} into washer')
    sink.remove(item)
print(f'\n There are {len(sink)} dishes in the sink : {sink} \n')

#--------------------------------------------------------------------

sink2 = ['Bogona','Kadia','chamach']
print (f'The list sink contain following dishes : {sink2}')
for item in list(sink2):
    print(f'Put the {item} into washer')
    sink2.remove(item)
print(f'\n There are {len(sink2)} dishes in the sink : {sink2} \n')


