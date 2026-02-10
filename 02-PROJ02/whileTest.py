import random

dirty = True
cleanCount = 0

while dirty:
    cleanCount += 1
    print(f' Scrubbed the dish {cleanCount} times!')
    print('Rinse to check if the dish is clean... \n')
    
    if not random.randint(0,10):
        print('Dish is clean now..')
        dirty=False
    else:
        print('Still dish is dirty')
    