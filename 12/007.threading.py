import threading
import time

def myFunction():
    print("STARTING the function")
    time.sleep(3)
    print("ENDING the function")

trdList=[]

for i in range(5):
    th = threading.Thread(target = myFunction)
    th.start()
    trdList.append(th)

for tr in trdList:
    tr.join()  #join() makes sure the program waits for all threads to terminate

''' ------output
$ python 007.threading.py
STARTING the function
STARTING the function
STARTING the function
STARTING the function
STARTING the function
ENDING the function
ENDING the function
ENDING the function
ENDING the function
ENDING the function
'''

#without threads the function calls will happen in sequential and not parallel

print("\n\n\n")

for i in range(5):
    myFunction()
'''
STARTING the function
ENDING the function
STARTING the function
ENDING the function
STARTING the function
ENDING the function
STARTING the function
ENDING the function
STARTING the function
ENDING the function
'''
