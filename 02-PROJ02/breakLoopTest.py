import random

items = ['item-01','item-02','item-03','item-04','item-05',
         'item-06','item-07','item-08','item-09','item-10',
         'item-11','item-12','item-13','item-14','item-15',
         'item-16','item-17','item-18','item-19','item-20']
print('\n')

for dish in list(items):
    if not random.randint(0, 19):
        print('The cabinate is full...\n\n')
        break
    else:
        print(f'Item -- {dish} -- has been placed into cabinate')
        items.remove(dish)




    
    
