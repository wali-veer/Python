import pyinputplus as pyip

print("------- Example - 1 -------")
result=pyip.inputInt("Enter a number of your choice", min=0)
print("You have entered ", result)

print("------- Example - 2 -------")
result=pyip.inputMenu(["RED","BLUE","ORANGE"],lettered=False, numbered=True)
print("Greate choice ", result)

print("------- Example - 3 -------")
result=pyip.inputEmail("Your email ID please")
print("you have entered your email as ", result)