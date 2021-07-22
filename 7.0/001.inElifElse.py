var = input("Enter a number of your choice which is integer : ")

if int(var) < 0 :
    print ("you have entered a NEGATIVE number and which is : " + str(var))
elif int(var) > 0 :
    print ("you have entered a POSITIVE number and which is : " + str(var))
else:
    print ("you have entered a ZERO : " + str(var))
