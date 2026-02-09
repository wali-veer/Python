x = True
cnt = 0

while x:

    print ("Yes, it is true !")

    ip = int(input("Enter your choice you want to continue 1=Yes, 0 = No   :   "))

    if ip == 0:
        x = False

    cnt = cnt + 1

    print ("While loop count " + str(cnt))
else:
    print("You have selected 'No' ! Exting while loop")
