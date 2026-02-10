ml=[
        [
            [1,1,1],[11,11,11]
            ],
        [
            [2,2,2],[22,22,22]
            ],
        [
            [3,3,3],[33,33,33]
            ]
        ]
level3=0
level2=0
level1=0
for l3 in ml:
    level2=0
    for l2 in l3:
        level1=0
        for l1 in l2:
            print(f'[{level3}][{level2}][{level1}] -- {l1}')
            level1=level1+1    
        level2=level2+1
    level3=level3+1
