try:
    number=int(input("Enter a number of your choice"))
    result = 10 / number
    print ("The result is ", result)
except ValueError:
    print ("Only numbers are allowed")
except ZeroDivisionError:
    print("You have caused zero division error")