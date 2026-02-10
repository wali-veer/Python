import time

hungry = True

while hungry :
    print('\nOpening the door to check if Pizza arrived')
    front_door = open('Ex_Files_Python_EssT\iPracticedPythonFiles\pollingExample.txt', 'r')

    if 'Delivery Person' in front_door:
        print('The pizza has arraived')
        hungry = False
    else:
        print('Still we need to wait for delivery guy to arrive')

    print('Closing the front door')
    front_door.close()
    time.sleep(1)